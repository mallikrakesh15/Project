from django.shortcuts import render,redirect
from .models import EmployeeRegister
from django.contrib import messages

from rest_framework.generics import ListCreateAPIView
from .serializer import CalenderSerializer,CalenderModel

# Create your views here.
def index(request):
    return render(request,'index.html')


def loginCheck(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        data = EmployeeRegister.objects.get(email=email,password=password)
        return render(request,'home.html',{'data':data})
    except EmployeeRegister.DoesNotExist:
        messages.error(request,'Invalid User')
        return redirect('main')


class UserAppointment(ListCreateAPIView):
    queryset = CalenderModel.objects.all()
    serializer_class = CalenderSerializer
