import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from .models import Transactions
from .serializer import TransactionSerializer
from orders.models import Order

ZARINPAL_MERCHANT = '6ee44d95-85fd-4a15-bbca-0b3ea934591e'
ZARINPAL_REQUEST_URL = 'https://sandbox.zarinpal.com/pg/v4/payment/request.json'
ZARINPAL_VERIFY_URL = 'https://sandbox.zarinpal.com/pg/v4/payment/verify.json'
ZARINPAL_STARTPAY_URL = 'https://sandbox.zarinpal.com/pg/StartPay/'

class CreateTransactionView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            order = get_object_or_404(Order, id=serializer.validated_data['order'].id)

            if not order.paying_amount or int(order.paying_amount) < 1000:
                return Response({"error": "مبلغ پرداخت باید حداقل ۱۰۰۰ ریال باشد."}, status=400)

            headers = {
                "accept": "application/json",
                "content-type": "application/json",
            }

            data = {
                "merchant_id": ZARINPAL_MERCHANT,
                "amount": int(order.paying_amount),
                "callback_url": "http://localhost:8000/api/transactions/verify/",
                "description": f"سفارش شماره {order.id}"
            }

            response = requests.post(ZARINPAL_REQUEST_URL, json=data, headers=headers)

            try:
                res_data = response.json()
            except Exception:
                return Response({"error": "پاسخ زرین پال قابل تبدیل به JSON نیست."}, status=500)

            if res_data.get("data") and res_data["data"].get("code") == 100:
                authority = res_data["data"]["authority"]
                transaction = serializer.save(
                    amount=order.paying_amount,
                    token=authority,
                    status="init",
                    order=order
                )
                pay_url = f"{ZARINPAL_STARTPAY_URL}{authority}"
                return Response({
                    "pay_url": pay_url,
                    "transaction_id": transaction.id
                }, status=200)

            return Response({
                "error": "درخواست ناموفق از زرین پال",
                "zarinpal_response": res_data
            }, status=400)

        return Response(serializer.errors, status=400)


class VerifyTransactionView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        authority = request.query_params.get('Authority')
        status_param = request.query_params.get('Status')

        transaction = get_object_or_404(Transactions, token=authority)

        if status_param != 'OK':
            transaction.status = 'failed'
            transaction.save()

            order = transaction.order
            order.payment_status = 'failed'
            order.save()

            return Response({"messages": "پرداخت ناموفق"}, status=400)

        data = {
            "merchant_id": ZARINPAL_MERCHANT,
            "amount": int(transaction.amount),
            "authority": authority
        }

        response = requests.post(ZARINPAL_VERIFY_URL, json=data)
        try:
            res_data = response.json()
        except Exception:
            return Response({"error": "پاسخ زرین پال قابل تبدیل به JSON نیست."}, status=500)

        if res_data.get('data') and res_data['data'].get('code') == 100:
            transaction.status = 'success'
            transaction.trans_id = res_data['data'].get('ref_id')
            transaction.save()

            order = transaction.order
            order.payment_status = 'paid'
            order.save()

            return Response({
                "messages": "پرداخت موفق",
                "ref_id": res_data['data'].get('ref_id')
            })

        else:
            transaction.status = 'failed'
            transaction.save()

            order = transaction.order
            order.payment_status = 'failed'
            order.save()

            return Response({
                "messages": "پرداخت ناموفق",
                "zarinpal_response": res_data  # اضافه کردم برای اینکه ببینی خطا چیه
            }, status=400)
