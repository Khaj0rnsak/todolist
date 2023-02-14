from rest_framework import viewsets
from .serializers import RapperSerializer
from .models import Rapper
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from django.conf import settings
from django.core.mail import send_mail

def count_trailing_zeros(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count

def factorial_trailing_zeros(n):
    count = count_trailing_zeros(n)
    return count

class MaxintArr(generics.ListAPIView):
    def get(self, request):
        array = [1,2,1,3,5,6,4]
        max_value = array[0]
        max_index = 0
        for i in range(len(array)):
            if array[i] > max_value:
                max_value = array[i]
                max_index = i
        return Response({'index ของตัวเลขที่มีค่ามากที่สุด' : max_index})

class Factorial(generics.ListAPIView):
    def get(self, request):
        countresult = factorial_trailing_zeros(10)
        return Response({'จำนวนเลข 0' : countresult})

class EmailAPI(APIView):
    def post(self, request):
        subject = self.request.GET.get('subject')
        txt_ = self.request.GET.get('text')
        html_ = self.request.GET.get('html')
        recipient_list = self.request.GET.get('recipient_list')
        from_email = settings.DEFAULT_FROM_EMAIL

        if subject is None and txt_ is None and html_ is None and recipient_list is None:
            return Response({'msg': 'There must be a subject, a recipient list, and either HTML or Text.'}, status=200)
        elif html_ is not None and txt_ is not None:
            return Response({'msg': 'You can either use HTML or Text.'}, status=200)
        elif html_ is None and txt_ is None:
            return Response({'msg': 'Either HTML or Text is required.'}, status=200)
        elif recipient_list is None:
            return Response({'msg': 'Recipient List required.'}, status=200)
        elif subject is None:
            return Response({'msg': 'Subject required.'}, status=200)
        else:
            sent_mail = send_mail(
                subject,
                txt_,
                from_email,
                recipient_list.split(','),
                html_message=html_,
                fail_silently=False,
            )
            return Response({'msg': sent_mail}, status=200)