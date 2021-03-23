from django.shortcuts import render
import africastalking
from .models import*
from .serializers import*
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


username = "nesjoselyne@gmail.com"
api_key = "7d5ec7e665579ee7ef1a3a71927f74123d0542960de776089cc89b28b4977804"

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.
# authontication
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username':user.username,
            'first_name':user.first_name

        })
def welcome(request):
    return render(request,'stand.html') 
def about(request):
    return render(request,'about.html')
def Ikigega(request):
    return render(request,'ikigega.html')
    africastalking.initialize(username,api_key)

@csrf_exempt
def ussdapp(request):
    if request.method == 'POST':
        # mandatory
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        level = text.split('*')
        response = ''
        numb = text[:3]

        if text == '':
            response = 'CON welcome to  digital ikigega platform for farmers: \n'
            response += '1. Girls In Code \n'
            response += '2. SDF Program'
            # girls in code session
        elif text == '1':
            response = 'CON Welcome to Girls In Code '+str(len(level))+'\n'
            response += '1. Join the Program \n'
            response += '2. Get Activity \n'
            response += '3. Leave'

        elif text == '1*1':
            response = 'CON Enter you Name '+str(len(level))+' \n'
        elif numb == '1*1' and int(len(level))==3 and str(level[2]) in str(level):
            response = 'CON Enter your IDnumber \n'
        elif numb == '1*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON Enter your pincode \n'
        elif text == '1*2':
            response = 'CON Enter your PINCode \n'
        elif text == '1*3':
            response = 'CON Enter your Address \n'
         
        elif text == '2':
            response = 'CON Welcome to Girls In Code \n'
            response += '1. Join the Program \n'
            response += '2. Get Activity \n'
            response += '3. Leave'
        else:
            response = 'END Invalid Choice'


            

        return HttpResponse(response)

    return HttpResponse('Welcome')
@csrf_exempt
def digitalapp (request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        level = text.split('*')
        response = ''
        numb = text[:5]
        if text == '':
            response = 'CON welcome to Smart ikigega platform for farmers: \n'
            response += '1. rice \n'
            response += '2. milk \n'
            response += '3.coffee \n'
            response += '4.Wheat \n'
            response += '5.Maize \n'
            response += '6.fruits'
            #  harvesting session
        elif text == '1':
            response = 'CON welcome to  Smart ikigega platform for  rice farmers '+str(len(level))+'\n'
            response += '1. Harvesting services \n'
            response += '2. financial service \n'
            response += '3. Insurance services'
            # current harvesting session
        elif text == '1*1':
            response = 'CON  harvesting checking : \n'
            response += '1.current total harvesting \n'
            response += '2.currently monthly harvesting'
#         elif text == '1*1*1':
#             response = 'CON injizamo code yumuhinzi '+str(len(level))+ '\n'
# #             y = input
# #             y =request.POST['farmercode']
# #             v=Harvestrecord.objects.filter(farmercode=y)
# #             for rt in v:
# #                 qty = rt.Quantity
#         elif numb == '1*1*1' and int(len(level))==4 and str(level[3]) in str(level):
#             response = 'CON umusaruro mbumbe wawe ni 260kg' \n'
        elif text == '1*1*2':
            response = 'CON Enter  farmers code or phone number'+str(len(level))+ ' \n'
        elif numb == '1*1*2'and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON your monthly current harvesting is 140kg \n'
        #  financial session
        elif text == '1*2':
            response = 'CON Welcome to the financial services  \n'
            response += '1. direct loan \n'
            response += '2. pay loan \n'
            response += '3. how to get loan'
            # direct loan session
        elif text == '1*2*1':
            response = 'CON Enter farmers code or phone number '+str(len(level))+' \n'
        elif numb == '1*2*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON you want to get : \n'
            response += '1.direct loan  of 2 months/allowed loan (20000rwf) \n'
            response += '2.direct loan of 4 months/allowed loan (40000rwf) \n'
            response += '3.dierect loan of 6 months/allowed loan (80000rwf) \n'
            response += '4.dierect loan of 12 months/allowed loan (120000rwf)\n'
        elif numb == '1*2*1' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter the money you want: \n'
            
        elif numb == '1*2*1' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON  you have required to get rwf loan Enter mobile money pin code to confirm that will be paid in 2 months: \n'
        elif text == '1*2*2':
            response = 'CON Enter farmers code '+str(len(level))+' \n'
        elif numb == '1*2*2' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON Enter the money you want pay: \n'   
        elif numb == '1*2*2' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter mobile-money pin to pay: \n'   
        elif numb == '1*2*2' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON you have succesfully paid the loan thanks: \n'   
        elif text == '1*3':
            response = 'CON Other services: \n'
            response += '1.how to get crops insurance\n'
            response += '2.join crops insurance \n'
        elif text == '1*3*1':
            response = 'END how to get crops insurance: \n'
            response += 'in order to get crops insurance you have to be an active member of any registrated cooperative in our system \n'
        elif text == '1*3*2':
            response = 'END  enter the farmers code to get the insurance:'
            # 2nd session milk
        elif text == '2':
            response = 'CON welcome to  Smart ikigega platform for milk owner '+str(len(level))+'\n'
            response += '1. Harvesting services \n'
            response += '2. financial service \n'
            response += '3.insurance services '
            # current harvesting session
        elif text == '2*1':
            response = 'CON  harvesting checking '+str(len(level))+': \n'
            response += '1.current total harvesting \n'
            response += '2.currently monthly harvesting \n'
            response += '3.other '
        elif text == '2*1*1':
            response = 'CON Enter farmers code or phone number \n'
        elif numb == '2*1*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON your current total  harvesting is \n'
            response += '1.july:215kg \n'
            response += '2.august:260kg \n'
            response += '3.sept:60kg '
        elif text == '2*1*2':
            response = 'CON Enter  farmers code or phone number \n'
        elif numb == '2*1*2'and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON your monthly current harvesting is 140kg \n'
        #  financial session
        elif text == '2*2':
            response = 'CON Welcome to the financial services  \n'
            response += '1. direct loan \n'
            response += '2. pay loan \n'
            response += '3. how to get loan'
            # direct loan session
        elif text == '2*2*1':
            response = 'CON Enter farmers code or phone number '+str(len(level))+' \n'
        elif numb == '2*2*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON you want to get : \n'
            response += '1.direct loan  of 2 months/allowed loan (20000rwf) \n'
            response += '2.direct loan of 4 months/allowed loan (40000rwf) \n'
            response += '3.dierect loan of 6 months/allowed loan (80000rwf) \n'
            response += '4.dierect loan of 12 months/allowed loan (120000rwf)\n'
        elif numb == '2*2*1' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter the money you want: \n'
        elif numb == '2*2*1' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON  you have required to get 25000 rwf loan Enter mobile money pin code to confirm that will be paid in 2 months: \n'
        elif text == '2*2*2':
            response = 'CON Enter farmers code '+str(len(level))+' \n'
        elif numb == '2*2*2' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON Enter the money you want pay: \n'   
        elif numb == '2*2*2' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter mobile-money pin to pay: \n'   
        elif numb == '2*2*2' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON you have succesfully paid the loan thanks: \n'   
        elif text == '2*3':
            response = 'CON Other services: \n'
            response += '1.how to get harvesting insurance \n'
            response += '2.get harvesting insurance\n'
        elif text == '2*3*1':
            response = 'END how to get harvesting insurance: \n'
            response += 'in order to get ur harvesting insurance you have to be a member of any registrated cooperative \n'
        elif text == '2*3*2':
            response = 'END you have to be a user of our platform atleast 2 month before getting the harvesting insurance '
            # 3rd session..... coffee
        elif text == '3':
            response = 'CON welcome to  digital ikigega platform for farmers '+str(len(level))+'\n'
            response += '1. Harvesting services \n'
            response += '2. financial service \n'
            response += '3.insurance services'
            # current harvesting session
        elif text == '3*1':
            response = 'CON  harvesting checking '+str(len(level))+': \n'
            response += '1.current total harvesting \n'
            response += '2.currently monthly harvesting \n'
            response += '3.other '
        elif text == '3*1*1':
            response = 'CON Enter farmers code or phone number \n'
        elif numb == '3*1*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON your current total  harvesting is \n'
            response += '1.july:215kg \n'
            response += '2.august:260kg \n'
            response += '3.sept:60kg '
        elif text == '3*1*2':
            response = 'CON Enter  farmers code or phone number \n'
        elif numb == '3*1*2'and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON your monthly current harvesting is 140kg \n'
        #  financial session
        elif text == '3*2':
            response = 'CON Welcome to the financial services  \n'
            response += '1. direct loan \n'
            response += '2. pay loan \n'
            response += '3. how to get loan'
            # direct loan session
        elif text == '3*2*1':
            response = 'CON Enter farmers code or phone number '+str(len(level))+' \n'
        elif numb == '3*2*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON you want to get : \n'
            response += '1.direct loan  of 2 months/allowed loan (20000rwf) \n'
            response += '2.direct loan of 4 months/allowed loan (40000rwf) \n'
            response += '3.dierect loan of 6 months/allowed loan (80000rwf) \n'
            response += '4.dierect loan of 12 months/allowed loan (120000rwf)\n'
        elif numb == '3*2*1' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter the money you want: \n'
        elif numb == '3*2*1' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON  you have required to get 25000 rwf loan Enter mobile money pin code to confirm that will be paid in 2 months: \n'
        elif text == '3*2*2':
            response = 'CON Enter farmers code '+str(len(level))+' \n'
        elif numb == '3*2*2' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON Enter the money you want pay: \n'   
        elif numb == '3*2*2' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter mobile-money pin to pay: \n'   
        elif numb == '3*2*2' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON you have succesfully paid the loan thanks: \n'   
        elif text == '3*3':
            response = 'CON Other services: \n'
            response += '1.how to become our platform user \n'
            response += '2.how to get loan \n'
        elif text == '3*3*1':
            response = 'END how to use our platform: \n'
            response += 'in order to become the user you have to be a member of any registrated cooperative \n'
        elif text == '3*3*2':
            response = 'END you have to be a user of our platform atleast 4 month before getting the loan '
            # session four.....Wheat
        elif text == '3':
            response = 'CON welcome to  digital ikigega platform for farmers '+str(len(level))+'\n'
            response += '1. Harvesting services \n'
            response += '2. financial service \n'
            response += '3. other services'
            # current harvesting session
        elif text == '3*1':
            response = 'CON  harvesting checking '+str(len(level))+': \n'
            response += '1.current total harvesting \n'
            response += '2.currently monthly harvesting \n'
            response += '3.other '
        elif text == '3*1*1':
            response = 'CON Enter farmers code or phone number \n'
        elif numb == '3*1*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON your current total  harvesting is \n'
            response += '1.july:215kg \n'
            response += '2.august:260kg \n'
            response += '3.sept:60kg '
        elif text == '3*1*2':
            response = 'CON Enter  farmers code or phone number \n'
        elif numb == '3*1*2'and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON your monthly current harvesting is 140kg \n'
        #  financial session
        elif text == '3*2':
            response = 'CON Welcome to the financial services  \n'
            response += '1. direct loan \n'
            response += '2. pay loan \n'
            response += '3. how to get loan'
            # direct loan session
        elif text == '3*2*1':
            response = 'CON Enter farmers code or phone number '+str(len(level))+' \n'
        elif numb == '3*2*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON you want to get : \n'
            response += '1.direct loan  of 2 months/allowed loan (20000rwf) \n'
            response += '2.direct loan of 4 months/allowed loan (40000rwf) \n'
            response += '3.dierect loan of 6 months/allowed loan (80000rwf) \n'
            response += '4.dierect loan of 12 months/allowed loan (120000rwf)\n'
        elif numb == '3*2*1' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter the money you want: \n'
        elif numb == '3*2*1' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON  you have required to get 25000 rwf loan Enter mobile money pin code to confirm that will be paid in 2 months: \n'
        elif text == '3*2*2':
            response = 'CON Enter farmers code '+str(len(level))+' \n'
        elif numb == '3*2*2' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON Enter the money you want pay: \n'   
        elif numb == '3*2*2' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter mobile-money pin to pay: \n'   
        elif numb == '3*2*2' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON you have succesfully paid the loan thanks: \n'   
        elif text == '3*3':
            response = 'CON Other services: \n'
            response += '1.how to get crops insurance \n'
            response += '2. get insurance \n'
        elif text == '3*3*1':
            response = 'END how to use our platform: \n'
            response += 'in order to become the user you have to be a member of any registrated cooperative \n'
        elif text == '3*3*2':
            response = 'CON Enter farmer code\n '
        # session four ...wheat
        elif text == '4':
            response = 'CON welcome to  digital ikigega platform for farmers '+str(len(level))+'\n'
            response += '1. Harvesting services \n'
            response += '2. financial service \n'
            response += '3. Insurance services'
            # current harvesting session
        elif text == '4*1':
            response = 'CON  harvesting checking '+str(len(level))+': \n'
            response += '1.current total harvesting \n'
            response += '2.currently monthly harvesting \n'
            response += '3.other '
        elif text == '4*1*1':
            response = 'CON Enter farmers code or phone number \n'
        elif numb == '4*1*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON your current total  harvesting is \n'
            response += '1.july:215kg \n'
            response += '2.august:260kg \n'
            response += '3.sept:60kg '
        elif text == '4*1*2':
            response = 'CON Enter  farmers code or phone number \n'
        elif numb == '4*1*2'and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON your monthly current harvesting is 140kg \n'
        #  financial session
        elif text == '4*2':
            response = 'CON Welcome to the financial services  \n'
            response += '1. direct loan \n'
            response += '2. pay loan \n'
            response += '3. how to get loan'
            # direct loan session
        elif text == '4*2*1':
            response = 'CON Enter farmers code or phone number '+str(len(level))+' \n'
        elif numb == '4*2*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON you want to get : \n'
            response += '1.direct loan  of 2 months/allowed loan (20000rwf) \n'
            response += '2.direct loan of 4 months/allowed loan (40000rwf) \n'
            response += '3.dierect loan of 6 months/allowed loan (80000rwf) \n'
            response += '4.dierect loan of 12 months/allowed loan (120000rwf)\n'
        elif numb == '4*2*1' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter the money you want: \n'
        elif numb == '4*2*1' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON  you have required to get 25000 rwf loan Enter mobile money pin code to confirm that will be paid in 2 months: \n'
        elif text == '4*2*2':
            response = 'CON Enter farmers code '+str(len(level))+' \n'
        elif numb == '4*2*2' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON Enter the money you want pay: \n'   
        elif numb == '4*2*2' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter mobile-money pin to pay: \n'   
        elif numb == '4*2*2' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON you have succesfully paid the loan thanks: \n'   
        elif text == '4*3':
            response = 'CON Other services: \n'
            response += '1.how to become our platform user \n'
            response += '2.how to get loan \n'
        elif text == '4*3*1':
            response = 'END how to use our platform: \n'
            response += 'in order to become the user you have to be a member of any registrated cooperative \n'
        elif text == '4*3*2':
            response = 'END you have to be a user of our platform atleast 4 month before getting the loan '
        # fiifth session ....Maize
        elif text == '5':
            response = 'CON welcome to  digital ikigega platform for farmers '+str(len(level))+'\n'
            response += '1. Harvesting services \n'
            response += '2. financial service \n'
            response += '3. Insurance services'
            # current harvesting session
        elif text == '5*1':
            response = 'CON  harvesting checking '+str(len(level))+': \n'
            response += '1.current total harvesting \n'
            response += '2.currently monthly harvesting \n'
            response += '3.other '
        elif text == '5*1*1':
            response = 'CON Enter farmers code or phone number \n'
        elif numb == '5*1*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON your current total  harvesting is \n'
            response += '1.july:215kg \n'
            response += '2.august:260kg \n'
            response += '3.sept:60kg '
        elif text == '5*1*2':
            response = 'CON Enter  farmers code or phone number \n'
        elif numb == '5*1*2'and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON your monthly current harvesting is 140kg \n'
        #  financial session
        elif text == '5*2':
            response = 'CON Welcome to the financial services  \n'
            response += '1. direct loan \n'
            response += '2. pay loan \n'
            response += '3. how to get loan'
            # direct loan session
        elif text == '5*2*1':
            response = 'CON Enter farmers code or phone number '+str(len(level))+' \n'
        elif numb == '5*2*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON you want to get : \n'
            response += '1.direct loan  of 2 months/allowed loan (20000rwf) \n'
            response += '2.direct loan of 4 months/allowed loan (40000rwf) \n'
            response += '3.dierect loan of 6 months/allowed loan (80000rwf) \n'
            response += '4.dierect loan of 12 months/allowed loan (120000rwf)\n'
        elif numb == '5*2*1' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter the money you want: \n'
        elif numb == '5*2*1' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON  you have required to get 25000 rwf loan Enter mobile money pin code to confirm that will be paid in 2 months: \n'
        elif text == '5*2*2':
            response = 'CON Enter farmers code '+str(len(level))+' \n'
        elif numb == '5*2*2' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON Enter the money you want pay: \n'   
        elif numb == '5*2*2' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter mobile-money pin to pay: \n'   
        elif numb == '5*2*2' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON you have succesfully paid the loan thanks: \n'   
        elif text == '5*3':
            response = 'CON Other services: \n'
            response += '1.how to get harvesting insurance \n'
            response += '2.get harvesting insurance \n'
        elif text == '5*3*1':
            response = 'END how to get harvesting insurance: \n'
            response += 'in order to get harvesting insurance you have to be an active member of registered cooperatives in our system \n'
        elif text == '5*3*2':
            response = 'CON enter farmers code\n '
        elif numb == '5*3*2'and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON you will get the notification on of ur request by phone\n'
        # 6th session ....fruits
        else:
            response = 'END Invalid Choice'
 

            

        return HttpResponse(response)

    return HttpResponse('ikigega')

def registration(request):
    select = Registration.objects.all()
    if request.method == 'POST':
        names = request.POST['names']
        email = request.POST['email']
        phone = request.POST['phone']
        insert = Registration(names=names,email=email,phone=phone)
        try:
            insert.save()
            return render(request,'register.html',{'message':'data has been inserted succesful','data':select})
        except :
            return render(request,'register.html',{'message':'failed to insert','data':select})
    return render(request,'register.html',{'data':select})

def delreg(request,id):
    select = Registration.objects.all().order_by('id')
    deleteInfos = Registration.objects.get(id=id).delete()
    return render(request,'register.html',{'message':'data has been deleted','data':select})
def updatereg(request,id):
    select = Registration.objects.all().order_by('id')
    update = Registration.objects.get(id=id)
    if request.method=='POST':
        update.names = request.POST['names']
        update.email =request.POST['email']
        update.phone = request.POST['phone']
        try:
            update.save()
            return render(request, 'updateregister.html',{'message':'Data has been updated','data':select,'update':update})
        except:
            return render(request, 'updateregister.html',{'message':'Fails to update','data':select,'update':update})
    return render(request, 'updateregister.html',{'data':select,'update':update})

# =========building the sereliazer endpoint
@csrf_exempt
def registerEndpoint(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        reg = Registration.objects.all()
        serializer = RegisterSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request) #request data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'sucecesful', 'data':serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)

        # delete/put/get/

@csrf_exempt
def deleteEndpoint(request,id):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        # try:
        #     reg = Registration.objects.get(id=id)
        # except Registration.objects.get(id=id) DoesNotExist:
        #      return JsonResponse({'message':'data has been deleted'}, status= 409)
        reg = Registration.objects.get(id=id)
        serializer = RegisterSerializer(reg, many=False)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        delete = Registration.objects.get(id=id).delete()
        return JsonResponse({'message':'data has been deleted'}, status= 409)
    if request.method == 'PUT':
        # try:
        #     reg = Registration.objects.get(id=id)
        # except Registration.objects.get(id=id) DoesNotExist:
        #      return JsonResponse({'message':'data has been deleted'}, status= 409)
        data = JSONParser().parse(request)
        reg = Registration.objects.get(id=id)
        serializer = RegisterSerializer(reg, data=data)
        if serializer.is_valid:
            serializer.save()
            return JsonResponse({'message':'successfull updated','data':serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)

# def injira(request):
#     context = {}
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         kir = Profile.objects.filter(username=username)
#         for kiru in kir:
#             account = kiru.accounttype
#         user = authenticate(request, username=username,
#                             password=password, is_superuser=1)
#         if user is not None and user.is_superuser == 1:
#             # user.is_active:
#             login(request, user)
#             return HttpResponseRedirect(reverse('success'))
#         elif user is not None and user.is_superuser == 0:
#             if  account == 'agent':
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('agents'))
#             else:
#                 return render(request, 'home/authentication-login.html', {'error':'You are not allowed to enterlogin here!' })
#         else:
#             ki = "Password and Username Incorrect! Try Again"
#             sel = Addcontent.objects.all().filter(
#                 category="back").order_by('-id')[:1]
#             return render(request, 'home/authentication-login.html', {'error': ki, 'back': sel, })
#     else:
#         context = {}
#         sel = Addcontent.objects.all().filter(
#             category="back").order_by('-id')[:1]
#         return render(request, 'home/authentication-login.html', {'back': sel, })
# @user_passes_test(lambda u: u.is_superuser, login_url='injira')
# def index(request):
#     return render(request, 'home/authentication-login.html')
# def loggedout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#     return render(request, 'home/authentication-login.html')
# def logout(request):
#     return render(request, 'home/authentication-login.html')





