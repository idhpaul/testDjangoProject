import base64
import datetime
from django.http import HttpRequest, Http404
from django.contrib.auth import login
from django.contrib.auth.models import update_last_login

from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

from testDjangoProject.my_settings import MY_SECRET

from .models import Buyer

from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
@api_view(['GET'])
@permission_classes([])
def wake(request:HttpRequest):
    # client send email address
    data = request.data
    print(data)
    
    with open('./testDjangoProject/rsa_2048.pub', mode='rb') as file: # b is important -> binary
        fileContent = file.read()
    
    print(fileContent)

    # response jwt token
    return Response(data={
            "result" : fileContent,
    })
    
@api_view(['POST'])
@permission_classes([])
def auth(request:HttpRequest):
    # client send email address
    data = request.data['data']
    print(data)
    
    chipertext = base64.urlsafe_b64decode(data)
    print(chipertext)
    
    with open("./testDjangoProject/rsa_2048.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=bytes(MY_SECRET['SECRET_KEY'],'utf-8'),
        )
    
    plaintext = private_key.decrypt(
        chipertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    print(plaintext)


    # response jwt token
    return Response(data={
            "result" : "",
    })


@api_view(['POST'])
@permission_classes([])
def self(request:HttpRequest):
    # client send email address
    data = request.data
    print(data)
    
    # Check if buyer data exists.
    # 현재 방식은 Django 방식으로 처리되고 있음
    # Django Rest Framework Serializer 를 이용하면 코드 간결해짐
    try:
        buyer, created = Buyer.objects.get_or_create(
                email=request.data['email'],
                )
        if created:
            print("first buyer")
        else:
            print("exist buyer")
    except KeyError as key_error:
        raise ValidationError({
                "type" : f'{key_error.__class__.__name__}',
                "detail" : f'Please enter a valid \'{key_error}\' '
                })
    except Exception as uncatched_error:
        raise NotFound({
                "type" : f'{uncatched_error.__class__.__name__}',
                "detail" : f'{uncatched_error}'
                })

    # make jwt token
    token = get_tokens_for_user(buyer)

    update_last_login(None, buyer)

    # response jwt token
    return Response(data={
            "result" : "user created",
            "token" : token
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def foo(request:HttpRequest):

    # Need Header Informaion
    # key :     Authorization 
    # value :   Bearer <access-key> 

    # client send email address
    data = request.data
    print(data)
    

    # response jwt token
    return Response(data={
            "result" : "token auth"
    })
