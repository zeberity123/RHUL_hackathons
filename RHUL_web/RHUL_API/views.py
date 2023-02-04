from django.shortcuts import render

from rest_framework.views import APIView
from django.views.generic import DetailView
from .models import Account_Holder, CompanyInfo
from .serializers import Account_Holder_serializers
from django.http import HttpResponse
from rest_framework.response import Response
import datetime

# Create your views here.


def Dashboard(request):
    return render(request, 'RHUL_Home.html', {'title': 'Dashboard'})


class AccountHolderAPIView(APIView):
    def get(self, request):
        modeldata = Account_Holder.objects.all()
        serializer = Account_Holder_serializers(modeldata, many=True)
        return Response(serializer.data)
        # customers = self.get_object(id)
        # serializer = CustomerSerializer(customers)
        # return Response(serializer.data)

class CompanyAPIView(APIView):
    def get(self, request):
        model = CompanyInfo.objects.all()
        return Response(model)
        # customers = self.get_object(id)
        # serializer = CustomerSerializer(customers)
        # return Response(serializer.data)
