import datetime
from django.http import HttpRequest
from django.shortcuts import render


from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_api_key.models import APIKey

# Create your views here.

@api_view(['POST'])
@permission_classes([HasAPIKey])
def bar(request:HttpRequest):

    key = request.META["HTTP_X_API_KEY"]
    api_key = APIKey.objects.get_from_key(key)
    api_key.revoked = True
    api_key.save()
    
    return Response(data={
            "result" : "bar pass"
    })

@api_view(['POST'])
@permission_classes([HasAPIKey])
def foo(request:HttpRequest):
    return Response(data={
            "result" : "permission pass"
    })


@api_view(['POST'])
def apikey(request:HttpRequest):

    now = datetime.datetime.now()
    print(now)
    expiry_5min = datetime.datetime.now() + datetime.timedelta(minutes=5)
    print(expiry_5min)

    api_key, key = APIKey.objects.create_key(name="oneoff-test-key",expiry_date=expiry_5min)

    return Response(data={
            "key" : key
        })

    # if request.method == 'POST':
    #     targetTransscribe = TargetTranscribeSerializer(data=request.data)

    #     targetTransscribe.is_valid(raise_exception=True)

    #     print("start transcirbe")
    #     result_transcribe = runSpeechModel(targetTransscribe.data['data']['objectName'])
    #     print("end transcirbe")

    #     return Response(data={
    #         "resultTranscribeID" : result_transcribe,
    #     })
    # else:
    #     stateTranslate = StateTranscribeSerializer(data=request.data)

    #     stateTranslate.is_valid(raise_exception=True)

    #     print("start translate state")
    #     result_state_translate = getTrnascriptionJob(stateTranslate.data['data']['transcribeJobID'])
    #     print("end ranslate state")
        
    #     return Response(data={
    #         "resultTranscribeState" : result_state_translate
    #     })