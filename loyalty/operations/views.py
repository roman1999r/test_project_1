from rest_framework import status
from rest_framework.generics import CreateAPIView

from .models import User, Transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import services
from .serializers import UserRegistrSerializer
from operations.tasks import count_balance, check_balance

# Create your views here.

@api_view(["POST"])
def add_balance_view(request):
    if request.method == "POST":
        transaction = services.add_balance(id=request.user.pk, data=request.data)
        check_balance.delay(id=request.user.id)
        return Response(transaction)

@api_view(["GET"])
def get_balance_view(request):
    if request.method == "GET":
        balance = services.get_balance(id=request.user.pk)
        return Response(balance)


@api_view(["POST"])
def sub_balance_view(request):
    if request.method == "POST":
        transaction = services.sub_balance(id=request.user.pk, data=request.data)
        check_balance.delay(id=request.user.id)
        return Response(transaction)

@api_view(["GET"])
def get_overall_balance_view(request):
    if request.method == "GET":
        users = services.get_overall_balance(data=request.data)
        count_balance.delay()
        return Response(users)


@api_view(["GET"])
def get_0_users_view(request):
    if request.method == "GET":
        users = services.get_0_users()
        return Response(users)



@api_view(["GET"])
def get_1000_users_view(request):
    if request.method == "GET":
        users = services.get_1000_users()
        return Response(users)


class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

