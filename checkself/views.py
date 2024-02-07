import datetime
from django.http import HttpRequest
from django.contrib.auth import login

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Buyer


@api_view(['POST'])
def self(request:HttpRequest):
    # client send email address
    data = request.data
    print(data)
    
    # Check if buyer data exists.
    try:
        buyer, created = Buyer.objects.get_or_create(
                email=request.data['email'],
                )
        if created:
            print("first buyer")
        else:
            print("exist buyer")
    except Exception as e:
        print(e)
    # make jwt token

    # response jwt token
    return Response(data={
            "result" : "user created"
    })
