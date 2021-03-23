from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.core.signing import Signer
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import send_mail
import random,os
from random import randint
import codecs
from django.contrib import messages
import requests


class CooperativeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cooperative
        depth=1
        fields=('__all__')
        extra_kwargs={'user':{'required':False}}


class UserSerializer(serializers.ModelSerializer):
    cooperative=CooperativeSerializer(required=True)
        
    class Meta:
        model=User
        fields=('email','password','name','Cooperativedistrict','cooperativesector','leaderphone','harvesttype')
        
    def create(self,validated_data):
        insert=User.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        password=make_password(validated_data['password']),
        leaderphone=validated_data['leaderphone'],
        cooperativesector=validated_data['cooperativesector'],
        Cooperativedistrict=validated_data['cooperativedistrict']
        )
        email=validated_data['email']
        name=validated_data['name']
        signer = Signer()
        subject='Verification from  smart ikigega'
        message='This link is for activating your account on Smart Ikigega \n'+'your Username:  '+name+'\n https://www.smart ikigega.rw/activation/'+email+'/'+signer.sign(email)
        from_email=settings.EMAIL_HOST_USER
        rt=send_mail(subject,message,from_email,[str(email),],fail_silently=False)
        Cooperative_data=validated_data.pop('Cooperative')
        Cooperative=Cooperative.objects.create(
        user=insert,
        name=Cooperative_data['name'],
        harvesttype=Cooperative_data['harvesttype'],
        email=Cooperative_data['email'],
        password1=Cooperative_data['password1'],
        password2=Cooperative_data['password2'],
        leaderphone=Cooperative_data['leaderphone'],
        district=Cooperative_data['district'],
        Cooperativesector=Cooperative_data['Cooperativesector'],
        # district =Cooperative_data['district']

        )
        return insert 




class farmerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Regfarmer
        depth=1
        fields=('__all__')
        extra_kwargs={'farmercode':{'required':False}}

    def create(self,validated_data):
        firstname=validated_data['firstname']
        telephone=validated_data['telephone']
        def random_with_N_digits(n):
            range_start = 10**(n-1)
            range_end = (10**n)-1
            return randint(range_start, range_end)
        nost= random_with_N_digits(6)
  
        if firstname != None or telephone !=None:

            subject='Thank you for Using smart ikigega'
            message='Dear '+str(validated_data['firstname']) +' '+str(validated_data['lastname']) +'\n'+'your code is : '+str(nost)
            from_email=settings.EMAIL_HOST_USER
            rt=send_mail(subject,message,from_email,[str(email),],fail_silently=True)
            mess='Dear '+str(validated_data['firstname']) +' '+str(validated_data['lastname']) +'\n'+'your  new cityplus code is : '+str(nost)
            sendsms = requests.post('http://rslr.connectbind.com:8080/bulksms/bulksms?username=1212-pathos&password=Chance@1&type=0&dlr=1&destination='+str(telephone)+'&source=CityPlus&message='+str(mess)+'')
            pass
        else:
            pass 
     

        insert=Regfarmer.objects.create(
        firstname=validated_data['firstname'],
        lastname=validated_data['lastname'],
        gender=validated_data['gender'],
        district=validated_data['district'],
        village=validated_data['village'],
        country=validated_data['country'],
        dateofbirth=validated_data['dateofbirth'],
        telephone=validated_data['telephone'],
        Cooperativesreg=validated_data['Cooperativesreg'],
        farmercode=nost
        )
    
        msg="Done"
        return msg




   
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model= Harvestrecord
        depth=1
        fields=('__all__')
        extra_kwargs={'usered':{'required':False}}

    def create(self,validated_data):
        farmer=validated_data['farmercode']
        gid=Regfarmer.objects.filter(farmercode=farmer)
        for ft in gid:
            id=ft.id
        farmerid=Regfarmer.objects.get(id=id)

        insert=Harvestrecord.objects.create(usered=farmerid,
        farmercode=validated_data['code'],
        Quantity=validated_data['quantity'])
        return insert


class RecordingSerializeren(serializers.ModelSerializer):
    class Meta:
        model=Recorder
        depth=1
        fields=('__all__')
        extra_kwargs={'user':{'required':False}}
  

class RecorderSerializer(serializers.ModelSerializer):
    Recording=RecordingSerializeren(required=True)
    class Meta:
        model=User
        fields=('username','password','Recording','email','first_name','last_name')

    def create(self,validated_data):
        if User.objects.filter(username=validated_data['username']).exists():
            msg="the user name exist"
            return msg
        else:
            rand=random.randint(1111,99999)
            passw=str(validated_data['first_name'])+str(rand)

            insert=User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password('password'),
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
            )
            email=validated_data['email']
        
            
            signer = Signer()
            subject='Thank you for Using Smart ikigega'
            message='Dear '+validated_data['first_name']+'  '+validated_data['last_name']+'\n'+'https://www.cityplus.rw/login/'+'\n'+'Username: '+email+'\n'+'Password: '+passw+'\n'+'Thank you are now employed by'+"str(request.user)"
            from_email=settings.EMAIL_HOST_USER
            rt=send_mail(subject,message,from_email,[str(email),],fail_silently=True)

            record_data=validated_data.pop('Recording')

            Cooperative=Recorder.objects.create(
            user=insert,
            phone=record_data['phone'],
            name=record_data['name'],
            username=record_data[' username'],
            password=record_data['password']

            )
            return insert
            

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profilecooperative
        fields=('__all__')
        depth=1
        extra_kwargs={'farmer':{'required':False}}

    def create(self,validated_data):
        farmerident=validated_data['cooperativename']
        gid=User.objects.filter(username=farmerident)
        
        for ft in gid:
            id=ft.id
        farmerid=User.objects.get(id=id)

        insert=Profilecooperative.objects.create(farmer=farmerid,
        image=validated_data['image'],
        cooperativename=validated_data['cooperativename']
        )
        return insert


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Loan  
        # depth=1
        fields=('__all__')           
class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Insurance  
        # depth=1
        fields=('__all__')           

class PayharvestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payharvest  
        # depth=1
        fields=('__all__')                   


        
class RegisterSerializer(serializers.ModelSerializer):
   class Meta:
       model = Cooperative
       depth = 1 
       fields = ('__all__')