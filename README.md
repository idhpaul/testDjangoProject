
# Package
1. Django REST Framework API Key
   * guide : <https://florimondmanca.github.io/djangorestframework-api-key/guide/#making-authorized-requests>
   * `pip3 install "djangorestframework-api-key==3.*"`
2. djangorestframework-simplejwt
   * guide : <https://django-rest-framework-simplejwt.readthedocs.io/en/latest/>
   * `pip3 install djangorestframework-simplejwt`
3. ~~drfpasswordless~~
   * ~~guide : <https://github.com/aaronn/django-rest-framework-passwordless>~~
   * ~~`pip3 install drfpasswordless`~~
4. ~~allauth~~
   * ~~guide : <https://docs.allauth.org/en/latest/index.html>~~
   * ~~`pip3 install django-allauth`~~

## Command
* python3 manage.py startapp \<appname>
---
* python3 manage.py makemigrations \<appname>
* python3 manage.py migrate \<appname>


## App name convention
* all-lowercase names
   > user, core ..

## User Sequence Diagram
```
sequenceDiagram
    actor c as User
    participant s as IAP_Backend

    c->>+s:[GET] /wake
    s-->>-c:server public key(=pubkey), sign

    c-->>c: Verification pubkey and sign

    rect rgb(0, 0, 0)
        note left of c: RSA Crypto<br/>RSA-OAEP-256
        c->>+s:[POST] /auth
        Note right of s: [Request Body]<br/>pubkey.encrypt<br/>({<br/>'email':'foo@foo.com',<br/>'device_id':'bad8274e04c6f2c6',<br/>'device_os':'Android'<br/>})
        s-->>-c:jwt token
    end


    rect rgb(100, 100, 1000)
        note left of c: Consume goods
        c->>+s:[POST] /consume
        Note right of s: [Request Body]<br/>{<br/>'type':'[free|pay|contenet_type]',<br/>'target':'<userid><br/>}
        s-->>-c:result
    end

#doc : https://mermaid.js.org/syntax/sequenceDiagram.html
#config : "noteAlign": "left"

```


    
    
