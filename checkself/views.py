import datetime
from django.http import HttpRequest, Http404
from django.contrib.auth import login

from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response

from .models import Buyer


@api_view(['POST'])
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

    # response jwt token
    return Response(data={
            "result" : "user created"
    })
