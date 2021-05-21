from django.shortcuts import render,redirect
import africastalking
from .models import*
# from ussd.models import *
from .serializers import*
import codecs
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser,FileUploadParser
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import urllib,json

username = "nesjoselyne@gmail.com"
api_key = "0f4078cd9b9d29c63e3f5c4296d7e76adc2ffa2e9cc1e244684c3272f9e34854"
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import datetime
from random import randint
from django.core.signing import Signer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def welcome(request):
    return render(request,'harvest.html') 
def kiny(request):
    return render(request,'kiny.html') 
def loanpage(request):
    return render(request,'loan.html')  
def insurancepage(request):
    return render(request,'insurance.html')        
def editp(request):
    return render(request,'editp.html')  
def addus(request):
    return render(request,'addus.html')        
def index(request):
    return render(request,'index.html') 
def cooperative(request):
    return render(request,'cooperative.html') 
def reg(request):
    return render(request,'reg.html')

def regfarm(request):
    return render(request,'farmerreg.html')   

def work(request):
    return render(request,'work.html')    

def pay(request):
    return render(request,'pay.html')    
 
def signin(request):
    return render(request,'signin.html')      
def record(request):
    # st=Recorder.objects.filter(name=request.user)
    print("hfyfhfy")
    print(request.user)
    return render(request,'record.html')
def recorderadd(request):
    return render(request,'addrecorder.html')  
def adminsignin(request):
    return render(request,'adminsignin.html')  
def cooaddfarmer(request):
    return render(request,'cooaddfarmer.html')    

    # ussd
@csrf_exempt
def digital (request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_numer = request.POST.get('phonenumer')
        text = request.POST.get('text')
        level = text.split('*')
        response = ''
        num = text[:3]

        if text == '':
            response = 'CON murakaza neza kurubuga rwabahinzi Smart ikigega \n'
            response += '1.ikigega pay \n'
            response += '2.ibijyanye numusaruro \n'
            response += '3.kwiyandikisha mukigega \n'
            response += '4.kubarura umusaruro \n'
            #  harvesting session
        elif text == '1':
            response = 'CON kwishyura \n'
            response += '1.uri mukigega \n'
            response += '2.momo isanzwe'
        elif text == '1*1':
            response = 'CON shyiramo code yumuhinzi '+str(level)+' \n' 
        #    elif Farmers.objetcs.filter(code=str(level[2])).exists():
        #         response = 'CON shyiramo ingano yumusaruro mu biro cg litiro '+str(level)+' \n'
        #     else:
        #         response = 'END code washyizemo ntibaho '+str(level)+' \n'
        elif num == '1*1' and int(len(level))==3 and str(level[2]) in str(level):
            response = 'CON shyiramo ingano yumusaruro ugiye kugura \n' 
        elif num == '1*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON shyiramo amafaranga ugiye kwishyura \n' 
        elif num == '1*1' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON  wahisemo kwishyura'+ str(level[4]) + 'ugiye kwishyura kuri' + str(level[2]) +'shyiramo umubare wibanga wemeze kwishyura  \n'
            insert=Harvestrecord(code=str(level[2]),Quantity=str(level[3]))
            insert.save()
        elif text == '1*2':
            response = 'CON nimero ya mobile : '+str(len(level))+ '\n'        
            # insert=Harvestrecord.objects.create(farmercode=str(level[2]))
            # insert.save()
        elif num == '1*2' and int(len(level))==2 and str(level[3]) in str(level):
            response = 'CON umubare wamafaranga  \n'
        elif num == '1*2' and int(len(level))==3 and str(level[4]) in str(level):
            response = 'CON wahisemo kwishyura'+ str(level[4]) + 'ugiye kwishyura kuri' + str(level[2]) +'shyiramo umubare wibanga wemeze kwishyura  \n'   
         
        
        elif text == '2':
            response = 'CON  hitamo \n'
            response += '1.kureba umusaruro mbumbe \n'
            response += '2.ubwishingizi bwumusaruro \n'
            response += '3.ikigega Loan'
        elif text == '2*1':
            response = 'CON  shyiramo code yawe ubashe kureba umusaruro :' +str(len(level))+ '\n'
            
        elif num == '2*1'and int(len(level))==3 and str(level[2]) in str(level):
            # insert=Harvestrecord(Quantity=str(level[3]))
            # if insert.is_valid():
             response = 'CON hitamo kureba \n'
             response += '1.umusaruro wukukwezi\n'
             response += '2.umusaruro mbumbe wose'
            # response = 'CON code mwashyizemo ntibaho : \n'
                 
        elif text =='2*1*1':
            response = 'CON umusaruro wa' + str(level[2]) +'wukukwezi ni 360kg'+str(level[3])+'\n'
        elif text =='2*1*2':
            response = 'CON umusaruro mbumbe wa' + str(level[2]) + 'ni 3600kg'+str(level[3])+'\n'
        elif text == '2*2':
            response = 'CON  ubwishingizi bw \n'
            response += '1.umwaka umwe \n'
            response += '2.imyaka itanu  \n'
            response += '3.imyaka icumi '   
        elif text == '2*2*1':
            response = 'CON  shyiramo code yawe ubashe kwinjira mu bwishingizi bwumwaka umwe:' +str(len(level))+ '\n'
        elif num == '2*2*1'and int(len(level))==4 and str(level[3]) in str(level):
             response = 'CON kwiyandikisha gusaba ubwishingizi bwumwaka byagenze neza murahabwa igisubizo mu masaha macye'+str(len(level))+'\n'   
            #  insert=Insurance.objects.filter(farmercode=str(level[4])) 
            #  insert.save()     

        elif text == '2*2*2':
            response = 'CON  shyiramo code yawe ubashe kwinjira mubwishingizi bwimyaka itanu :' +str(len(level))+ '\n'
        elif num == '2*2*2'and int(len(level))==4 and str(level[3]) in str(level):  
            response = 'CON kwiyandikisha gusaba ubwishingizi bwimyaka 5 byagenze neza murahabwa igisubizo mu masaha macye'+str(len(level))+'\n' 
            # insert=Insurance.objects.filter(farmercode=str(level[4])) 
            # insert.save()                        
            # response = 'CON code mwashyizemo ntibaho : \n'
        elif text == '3':
            response = 'CON  hitamo kwiyandikisha  nk \n'
            response += '1. itsinda(cooperative)\n'
            response += '2.umuhinzi ku giti cye '
        elif text == '3*1':
            response = 'CON  shyiramo izina rya cooperative :' +str(len(level))+ '\n'
            # insert = Cooperativesreg.objects.create(name=str(level[2]))
            # insert.save() 
        elif num == '3*1'and int(len(level))==3 and str(level[2]) in str(level):
            response = 'CON  shyiramo izina ryumuyobozi wa cooperative' +str(len(level))+ '\n'
            # insert= Cooperativesreg.objects.create(leadername=str(level[3]))
            # insert.save()   

        elif num == '3*1'and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON  shyiramo numero zumuyobozi wa cooperative :' +str(len(level))+ '\n'
            # insert= Cooperativesreg.objects.create(leaderphone=str(level[4]))
            # insert.save()   
        elif num == '3*1'and int(len(level))==5 and str(level[4]) in str(level):  
            response = 'CON  ubusabe bwawe bwo kwiyandikisha mukigega nkitsinda bwakiriwe urahabwa igisubizo mu gihe gito' +str(len(level))+ '\n'  
        elif text == '3*2':
            response = 'CON  shyiramo izina rya mbere :' +str(len(level))+ '\n'
            # insert= Regfarmer.objects.create(firstname=str(level[2]))
            # insert.save()
        elif num == '3*2'and int(len(level))==3 and str(level[2]) in str(level):
            response = 'CON  shyiramo izina rya kabiri \n'
            # insert= Regfarmer.objects.create(lastname=str(level[3]))
            # insert.save()
        elif num == '3*2'and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON  shyiramo numero yawe ya telephone \n'
            # insert= Regfarmer.objects(telephone=str(level[4]))    
            # insert.save()

        elif num == '3*2' and int(len(level))==5 and str(level[4]) in str(level):  
            response = 'CON  ubusabe bwawe bwo kwiyandikisha mukigega bwakiriwe urahabwa igisubizo mu gihe gito \n'
        elif text == '4':
            response = 'CON  shyiramo code yawe ubashe kubarura :' +str(len(level))+ '\n'
        elif num == '4'and int(len(level))==2 and str(level[1]) in str(level):  
            response = 'CON  shyiramo izina rya cooperative \n'  
            # insert=Cooperative.objects.filter(name=str(level[2]))  
            # insert.save()
        elif num == '4' and int(len(level))==3 and str(level[2]) in str(level):  
            response = 'CON  shyiramo code yumuhinzi \n'  
            # insert=Harvestrecord.objects.filter(farmercode=str(level[3]))  
            # insert.save()
        elif num == '4' and int(len(level))==4 and str(level[3]) in str(level):  
            response = 'CON  shyiramo ibiro yagize \n'  
            # insert=Harvestrecord.objects(Quantity=str(level[4]))  
            # insert.save()    
        else:
            response = 'END Invalid Choice'
        
        return HttpResponse(response)

    return HttpResponse('harvest')    
    # 2nd ussd

@csrf_exempt
def digitalapp(request):

    if request.method == 'POST':
        ## mandatory
        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST.get("text")
        level = text.split('*')
        response =""
        num = text[:3]
        st =text[:1]
     
        farmers=Allfarmers.objects.all().filter(number=phone_number).order_by('-id')
        for users in farmers:
            phoneuser = users.number
            fullname = users.firstname
            mypin = users.pincode
        if farmers.exists():
                      
            if text =='':
                response = "CON Murakaza neza kurubuga rw'abahinzi Smart Ikigega \n"
                response += '1.Ikigega pay \n'
                response += '2.umusaruro wanjye \n'
                response += '3.Kubarura umusaruro \n'
                response += '4.ikigega loan'
            elif text == '1':
                response = 'CON kwishyura \n'
                response += '1.uri mukigega \n'
                response += '2.momo isanzwe'
            elif text == '1*1':
                response = 'CON shyiramo code yumuhinzi '+str(level)+' \n'
            elif num == '1*1'and int(len(level))==2 and str(level[1]) in str(level):  
                mycode = str(level[2])
                cody=Allfarmers.objects.all().filter(farmercode=mycode)
                if cody.exists():
                    response='CON shyiramo ingano yumusaruro mu biro cg litiro '+str(level)+' \n'
                else:
                    response='END code mwashyizemo ntibaho '+str(level[1])+' \n'      
            elif num == '1*1' and int(len(level))==3 and str(level[2]) in str(level):
                response='CON shyiramo ingano yumusaruro mu biro cg litiro '+str(level)+' \n'
            elif num == '1*1' and int(len(level))==4 and str(level[3]) in str(level):
                 response = 'CON shyiramo amafaranga ugiye kwishyura' +str(level)+ '\n' 
            elif num == '1*1' and int(len(level))==5 and str(level[4]) in str(level):
                response = 'CON  wahisemo kwishyura'+ str(level[4]) + 'ugiye kwishyura kuri' + str(level[2]) +'shyiramo umubare wibanga wemeze kwishyura  \n'
            elif num == '1*1' and int(len(level))==6  and   str(level[5]) in str(level):    
                insert=Harvestrecord(farmercode=str(level[2]),Quantity=str(level[3]))

                try:
                    insert.save()
                    # telephone = phone_number[1:]
                    response = "END Urakoze kugura ukoresheje  Smart Kigega wishyuye: "+str(level[4])+"kuri"+str(level[2]) + "\n "
                except:
                    response = "END Kwishyura byanze"
            elif text == '1*2':
                response = 'CON nimero ya mobile : '+str(len(level))+ '\n'                
            elif num == '1*2' and int(len(level))==2 and str(level[3]) in str(level):
                response = 'CON umubare wamafaranga  \n'
            elif num == '1*2' and int(len(level))==3 and str(level[4]) in str(level):
                response = 'CON wahisemo kwishyura'+ str(level[4]) + 'ugiye kwishyura kuri' + str(level[2]) +'shyiramo umubare wibanga wemeze kwishyura  \n'   
                      
            elif text == '2':
                response = 'CON  hitamo \n'
                response += '1.kureba ingano yumusaruro \n'
                response += '2.ubwishingizi bwumusaruro '
            elif text == '2*1':
                response = 'CON shyiramo code yawe ubashe kureba umusaruro :' +str(len(level))+ '\n'
                    
            elif num == '2*1'and int(len(level))==3 and str(level[2]) in str(level):
                hcode = str(level[2])  
                hacode =Allfarmers.objetcs.all(farmercode=hcode)    
                if hacode.exists():
                    response = 'CON hitamo kureba \n'
                    response += '1.umusaruro wukukwezi\n'
                    response += '2.umusaruro mbumbe wose'
                else:
                    response = 'CON code mwashyizemo ntibaho :\n'
                        
            elif text =='2*1*1':
                Q=Harvestrecord.abjects.filter(Quantity=hacode)
                for ha in Q :
                    idhsn = ha.id
                qhacode =Harvestrecord.objects.get(id=int(idhsn))
                if qhacode.exists():
                    response = 'CON umusaruro wawe wukukwezi ni '+ str(qhacode) +'\n'
                else:
                    response = 'CON ntamusaruro mufitemo uku kwezi'+'\n'
            elif text =='2*1*2':
                response = 'CON umusaruro mbumbe wa' + str(level[2]) + 'ni 3600kg'+str(level[3])+'\n'
            elif text == '2*2':
                response = 'CON  ubwishingizi bw \n'
                response += '1.imyaka itanu \n'
                response += '2.imyaka icumi '   
            elif text == '2*2*1':
                response = 'CON  shyiramo code yawe ubashe kwinjira mu bwishingizi bwumwaka umwe:' +str(len(level))+ '\n'
                mycode = str(level[3])
                cody=Allfarmers.objects.all().filter(farmercode=mycode)
                if cody.exists():
                    response='CON ubusabe bwawe bwakiriwe murahabwa igisubizo mukanya'+str(level)+' \n'
                else:
                    response='END code mwashyizemo ntibaho'+str(level[1])+' \n'     
            # elif num == '2*2*1'and int(len(level))==4 and str(level[3]) in str(level):
            #     response = 'CON kwiyandikisha gusaba ubwishingizi bwumwaka byagenze neza murahabwa igisubizo mu masaha macye'+str(len(level))+'\n'   
            #         #  insert=Insurance.objects.filter(farmercode=str(level[4])) 
            #         #  insert.save()     

            elif text == '2*2*2':
                response = 'CON  shyiramo code yawe ubashe kwinjira mubwishingizi bwimyaka itanu :' +str(len(level))+ '\n'
            elif num == '2*2*2'and int(len(level))==4 and str(level[3]) in str(level):  
                response = 'CON kwiyandikisha gusaba ubwishingizi bwimyaka 5 byagenze neza murahabwa igisubizo mu masaha macye'+str(len(level))+'\n' 
                    # insert=Insurance.objects.filter(farmercode=str(level[4])) 
                    # insert.save()                        
                    # response = 'CON code mwashyizemo ntibaho : \n'
            # elif text == '3':
            #     response = 'CON  hitamo kwiyandikisha  nk \n'
            #     response += '1. itsinda(cooperative)\n'
            #     response += '2.umuhinzi ku giti cye '
            # elif text == '3*1':
            #     response = 'CON  shyiramo izina rya cooperative :' +str(len(level))+ '\n'
            #         # insert = Cooperativesreg.objects.create(name=str(level[2]))
            #         # insert.save() 
            # elif num == '3*1'and int(len(level))==3 and str(level[2]) in str(level):
            #     response = 'CON  shyiramo izina ryumuyobozi wa cooperative' +str(len(level))+ '\n'
            #         # insert= Cooperativesreg.objects.create(leadername=str(level[3]))
            #         # insert.save()   

            # elif num == '3*1'and int(len(level))==4 and str(level[3]) in str(level):
            #     response = 'CON  shyiramo numero zumuyobozi wa cooperative :' +str(len(level))+ '\n'
            #         # insert= Cooperativesreg.objects.create(leaderphone=str(level[4]))
            #         # insert.save()   
            # elif num == '3*1'and int(len(level))==5 and str(level[4]) in str(level):  
            #     response = 'CON  ubusabe bwawe bwo kwiyandikisha mukigega nkitsinda bwakiriwe urahabwa igisubizo mu gihe gito' +str(len(level))+ '\n'  
            # elif text == '3*2':
            #     response = 'CON  shyiramo izina rya mbere :' +str(len(level))+ '\n'
            #         # insert= Regfarmer.objects.create(firstname=str(level[2]))
            #         # insert.save()
            # elif num == '3*2'and int(len(level))==3 and str(level[2]) in str(level):
            #     response = 'CON  shyiramo izina rya kabiri \n'
            #         # insert= Regfarmer.objects.create(lastname=str(level[3]))
            #         # insert.save()
            # elif num == '3*2'and int(len(level))==4 and str(level[3]) in str(level):
            #     response = 'CON  shyiramo numero yawe ya telephone \n'
            #         # insert= Regfarmer.objects(telephone=str(level[4]))    
            #         # insert.save()

            # elif num == '3*2' and int(len(level))==5 and str(level[4]) in str(level):  
            #     response = 'CON  ubusabe bwawe bwo kwiyandikisha mukigega bwakiriwe urahabwa igisubizo mu gihe gito \n'
            elif text == '3':
                response = 'CON  shyiramo code yawe ubashe kubarura :' +str(len(level))+ '\n'
                mycode = str(level[2])
                cody=Recorder.objects.all().filter(password=mycode)
                if cody.exists():
                    response='CON shyiramo kode yumuhinzi ubashe kubarura'+str(level)+' \n'
                    hinz = str(level[3])
                    umuhinzi=Allfarmers.objects.all().filter(farmercode=hinz)
                    if umuhinzi.exists():
                        response='CON ingano yumusaruro'+str(level)+' \n'
                    else:
                        response='END code mwashyizemo ntibaho '+str(level[1])+' \n'     
                else:
                    response='END ntabwo mwanditse nkumubaruzi'+str(level[1])+' \n'     
            elif num == '4'and int(len(level))==2 and str(level[1]) in str(level):  
                response = 'CON  shyiramo izina rya cooperative \n'  
                    # insert=Cooperative.objects.filter(name=str(level[2]))  
                    # insert.save()
            elif num == '4' and int(len(level))==3 and str(level[2]) in str(level):  
                response = 'CON  shyiramo code yumuhinzi \n'  
                    # insert=Harvestrecord.objects.filter(farmercode=str(level[3]))  
                    # insert.save()
            elif num == '4' and int(len(level))==4 and str(level[3]) in str(level):  
                response = 'CON  shyiramo ibiro yagize \n'  
                    # insert=Harvestrecord.objects(Quantity=str(level[4]))  
                    # insert.save()    
            else:
                response ="END INvalid choice "
        else:
            if text =='':
                response = "CON Ikaze kuri Smart Kigega, Iyandikishe mu kigega \n"
                response += '1.Iyandikishe \n'
                response += '2.Ikigega pay \n'
                
            elif text =='1':
                response = "CON Andika amazina yawe \n"
            elif int(st)==1  and int(len(level))==2  and   str(level[1]) in str(level):
                response = "CON Shyiramo Umubare w'ibanga wawe \n"
            elif int(st)==1  and int(len(level))==3  and   str(level[2]) in str(level):
                response = "CON Andika akarere utuyemo \n" 
            elif int(st)==1  and int(len(level))==4  and   str(level[3]) in str(level):
                response = "CON Andika Umurenge utuyemo \n"
            elif int(st)==1  and int(len(level))==5  and   str(level[4]) in str(level):
                pin=str(level[2])
                district =str(level[3])
                sector =str(level[4])
                pincode = pin
                def random_with_N_digits(n):
                    range_start = 10**(n-1)
                    range_end = (10**n)-1
                    return randint(range_start, range_end)
                numb = random_with_N_digits(5)
                # insert =Farmers(number=phone_number,farmercode=numb,sector=sector,district=district, firstname=str(level[1]),pincode=pin)
                insert =Allfarmers(number=phone_number,farmercode=numb,sector=sector,district=district, firstname=str(level[1]),pincode=pin)
                try:
                
                    insert.save()
                    telephone = phone_number[1:]
                    response = "END Urakoze kwiyandikisha kuri Smart Kigega,kode ikuranga  ni: "+str(numb)+". \n Kubindi bisobanuro hamagara https://www.smartkigega.com"
                    
                except:
                    response = "END Kwiyandikisha byanze"
            elif text =='2':
                response = "CON shyiramo code yumuhinzi \n"     
            elif int(st)== 2 and int(len(level))==2  and  str(level[1]) in str(level): 
                mycode = str(level[1])
                cody=Allfarmers.objects.all().filter(farmercode=mycode)
                if cody.exists():
                    response='CON shyiramo ingano yumusaruro mu biro cg litiro '+str(level)+' \n'
                else:
                    response='END code mwashyizemo ntibaho '+str(level[1])+' \n'      
            # elif int(st)== 2  and int(len(level))==3  and   str(level[2]) in str(level): 
            #     response = "CON hitamo ubwoko bwumusaruro uguze: \n" 
            #     response += '1.umuceri \n'
            #     response += '2.ibishyimbo \n'
            #     response += '3.ikawa \n'
            #     response += '4.amata \n'   
            elif int(st)== 2  and int(len(level))==3  and   str(level[2]) in str(level): 
                response = "CON shyiramo ingano yumusaruro mu biro cg litiro" +str(level)+ "\n"  
            elif int(st)== 2  and int(len(level))==4  and   str(level[3]) in str(level): 
                response = "CON shyiramo amafaranga ugiye kwishyura" +str(level)+ "\n"      
            elif int(st)== 2  and int(len(level))==5  and   str(level[4]) in str(level): 
                response = "CON ugiye kwishyura" +str(level[4])+ 'kuri' +str(level[1]) + "shyiramo umubare wibanga wemeze \n"
            elif int(st)== 2  and int(len(level))==5  and   str(level[4]) in str(level):   
               farmercode= str(level[1])
               Quantity=str(level[3])
               insert =Harvestrecord(code=farmercode,Quantity=Quantity)
               try:
                   insert.save()
                    # telephone = phone_number[1:]
                   response = "END Urakoze kugura ukoresheje  Smart Kigega wishyuye: "+str(level[4])+"kuri"+str(level[2]) + "\n "
                    
               except:
                   response = "END Kwishyura byanze"
            else:

                response = "END Invalid choice"    

        



        return HttpResponse(response)
    
    return HttpResponse('Testing smart')   


def Loanrequesting(request):
    select =Allfarmers.objects.all()
    if request.method == 'POST':
        amount = request.POST['amount']
        farmercode = request.POST['farmercode']
        print(farmercode)
        codes=Allfarmers.objects.filter(farmercode=farmercode)
        for dt in codes:
            tel=dt.telephone
            fname=dt.firstname
            email=dt.email
      
                # print(rt)
            if amount !=None or farmercode !=None:
                if codes.count()>0:
                    Havst=Harvestrecord.objects.filter(farmercode=farmercode)
                    if Havst.count()>0:
                               subject='Inguzanyo muri smart ikigega'
                               message='kuri '+fname +'\n'+'ubusabe bwawe bwinguzanyo '+' '+str(datetime.datetime.now()) +' '+'ingana'+' '+amount +' '+ 'Bwakiriwe urahabwa ubutumwa bubyemeza mukanya'
                               from_email=settings.EMAIL_HOST_USER
                               rt=send_mail(subject,message,from_email,[str(email),],fail_silently=True)
                               insert=Loan.objects.create(amount=amount,farmercode=farmercode,telephone=tel,email=email,firstname=fname)
                               insert.save()
                               mess=email
                               return render(request,'loan.html',{'message':'data submitted successful','mess':mess,'data':select})
                    else:
                       return render(request,'loan.html',{'message':'U are not allowed to take loan '})           
                else:
                    return render(request,'loan.html',{'message':'code does  not exist'})

                  #account_sid = 'AC1b41153cd2a60b01893bb9740d2fd875'
                  #auth_token = 'efa2a032ba78dff3111fce2efafa5940'
                   #client =Client(account_sid, auth_token)
                  #message = client.messages.create(body='your Code is: '+nost,from_='+16305280341',to='+250784447864')
                  # sendsms = requests.post('http://rslr.connectbind.com:8080/bulksms/bulksms?username=1212-pathos&password=Chance@1&type=0&dlr=1&destination='+str(telephone)+'&source=smartikigega&message='+str(mess)+'')
                  # pass
                  # return render(request,'record.html',{'message':'data submitted successful','data':select})
                  # insert = Harvestrecord(Quantity=Quantity,code=code, donetime=donetime,donedate=donedate,email=email,firstname=firstname)
                  # insert.save()
            else:
                return render(request,'loan.html',{'message':'the farmercode must be filled','data':select})
    return render(request,'loan.html',{'data':select})
def InsuranceRequest(request):
    if request.method=='GET':
        reg=Insurance.objects.all()
        serializer=InsuranceSerializer(reg,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=InsuranceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'data submited successful'},status=201)
        return JsonResponse(serializer.errors,status=400)
def Harvestpay(request):
   if request.method == 'GET':
        reg = Payharvest.objects.all()
        serializer = PayharvestSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)
   elif request.method == 'POST':
        data = JSONParser().parse(request) #/request.data
        serializer = PayharvestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successfull','data':serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)
      
    #   insurancerequest
def Insurancerequesting(request):
    select =Allfarmers.objects.all()
    if request.method == 'POST':
        insurance = request.POST['insurance']
        farmercode = request.POST['farmercode']
        print(farmercode)
        codes=Allfarmers.objects.filter(farmercode=farmercode)
        for dt in codes:
            tel=dt.telephone
            fname=dt.firstname
            email=dt.email
      
                # print(rt)
            if insurance !=None or farmercode !=None:
                if codes.count()>0:
                    Havst=Harvestrecord.objects.filter(farmercode=farmercode)
                    if Havst.count()>0:
                               subject='ubwishingizi muri smart ikigega'
                               message='kuri '+fname +'\n'+'ubusabe bwawe bwubwishingizi '+' '+str(datetime.datetime.now()) +' '+'bwa'+' '+insurance+' '+ 'Bwakiriwe urahabwa ubutumwa bubyemeza mukanya'
                               from_email=settings.EMAIL_HOST_USER
                               rt=send_mail(subject,message,from_email,[str(email),],fail_silently=True)
                               insert=Loan.objects.create(insurance=insurance,farmercode=farmercode,telephone=tel,email=email,firstname=fname)
                               insert.save()
                               mess=email
                               return render(request,'insurance.html',{'message':'data submitted successful','mess':mess,'data':select})
                    else:
                       return render(request,'insurance.html',{'message':'U are not allowed to take loan '})           
                else:
                    return render(request,'insurance.html',{'message':'code does  not exist'})

                  #account_sid = 'AC1b41153cd2a60b01893bb9740d2fd875'
                  #auth_token = 'efa2a032ba78dff3111fce2efafa5940'
                   #client =Client(account_sid, auth_token)
                  #message = client.messages.create(body='your Code is: '+nost,from_='+16305280341',to='+250784447864')
                  # sendsms = requests.post('http://rslr.connectbind.com:8080/bulksms/bulksms?username=1212-pathos&password=Chance@1&type=0&dlr=1&destination='+str(telephone)+'&source=smartikigega&message='+str(mess)+'')
                  # pass
                  # return render(request,'record.html',{'message':'data submitted successful','data':select})
                  # insert = Harvestrecord(Quantity=Quantity,code=code, donetime=donetime,donedate=donedate,email=email,firstname=firstname)
                  # insert.save()
            else:
                return render(request,'insurance.html',{'message':'the farmercode must be filled','data':select})

    else: 
        return render(request,'insurance.html',{'message':'you have to enter a farmercode to get insurance','data':select})   
    return render(request,'insurance.html',{'data':select})



def editpro(request):
    tur=request.user
    pas=User.objects.get(username=tur)
    prof=Profilecooperative.objects.filter(cooperative=str(tur))
    cname=pas.username
    cpassword=pas.password
    workers=Recorder.objects.filter(cooperativename=cname)
    farmers=Farmers.objects.filter(cooperativename=cname)
    Records=Harvestrecord.objects.filter(cooperativename=cname)
    if request.method=='POST':
        username=request.POST['email']
        passw=request.POST['password']
        pass2=request.POST['pass1']
        newpass=make_password(pass2)
        if check_password(passw,cpassword) ==True:
            pas.username=username
            pas.password=newpass
            pas.save()
            for dt in workers:
                dt.cooperativename=username
                dt.save()
            for dt in farmers:
                dt.instutename=username
                dt.save()
            for dt in Records:
                dt.instutename=username
                dt.save()
            auth.logout(request)
            return redirect('login')
        else:
            messages.info(request,'please enter existing password')
            return redirect('editpro')
    else:
        return render(request,'editpro.html',{'pas':pas,'prof':prof})       

#  def logout(request):
#         auth.logout(request)
#     return redirect('/')


# def login(request):
#     if request.method=='POST':
#         userd=request.POST['username']
#         pass1=request.POST['pass']
#         user=auth.authenticate(username=userd,password=pass1)
#         if user is not None:
#             auth.login(request,user)
#             if Workers.objects.filter(user=request.user).exists():
#                 return redirect('worker')
#             elif Active.objects.filter(user=request.user).exists():
#                 return redirect('inside')
#             else:
#                 messages.info(request,'make sure if your account is Activate')
#                 return redirect('login')
#         else:
#             print(userd)
#             print(pass1)
#             messages.info(request,'Check your username and password password ')
#             return redirect('login')
#     else:
#         return render(request,'login.html')
#     return render(request,'login.html')       
def reset(request):
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(email=username).exists():

            subject='Password Resetting- Smartikigega'
            message='Dear User, you requested  password reset,  click or copy the link below \n'+'activation link is https://smartikigega.herokuapp.com/reset-now/smartikigega.herokuapp-password/'+str(username)
            from_email=settings.EMAIL_HOST_USER
            rt=send_mail(subject,message,from_email,[str(username),],fail_silently=True)
            return render(request,'reset.html',{'success':'Reset account link has been sent to your email, check inbox'})

        else:
            return render(request,'reset.html',{'success':'Sorry user with provided email does not exist!'})

    return render(request,'reset.html')
def resetnow(request,username):
    usern =User.objects.get(email=username)
    if request.method == 'POST':

       
        usern.password = make_password(request.POST['password'])
        usern.save()
        return render(request, 'resetnow.html', {'usern': usern, 'success': "Password have been changed"})
       

    return render(request, 'resetnow.html',{'usern':usern})
@csrf_exempt
def Recorderaccountcreation(request):
    if request.method=='GET':
        # reg=Teacher.objects.filter(companyname=request.username)
        reg=Recorder.objects.all()
        # print(request.username)
        serializer=RecordingSerializeren(reg,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=RecorderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'account create successful'},status=201)
        return JsonResponse(serializer.errors,status=400)

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

# def registration(request):
#     select = Cooperative.objects.all()
#     if request.method == 'POST':
#         name = request.POST['name']
#         Cooperativedistrict = request.POST['Cooperativedistrict']
#         leaderphone = request.POST['leaderphone']
#         harvesttype = request.POST['harvesttype']
#         leadername = request.POST['leadername']
#         Cooperativesector = request.POST['Cooperativesector']
#         insert = Cooperativesreg(name=name,Cooperativedistrict=Cooperativedistrict,leaderphone=leaderphone, harvesttype= harvesttype,leadername=leadername,Cooperativesector=Cooperativesector)
#         try:
#             insert.save()
#             return render(request,'cooperative.html',{'message':'your request has been succeeful submitted we will  get in touch with u soon','data':select})
#         except :
#             return render(request,'cooperative.html',{'message':'failed to insert','data':select})
#     return render(request,'cooperative.html',{'data':select})

def login(request):
    if request.method=='POST':
        userd=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=userd,password=pass1)
        if user is not None:
            auth.login(request,user)
            if Cooperative.objects.filter(username=request.user).exists():
                return redirect('dashboard')
            elif Recorder.objects.filter(username=request.user).exists():
                return redirect('record')
            elif user.is_superuser:
                return redirect('record')     
            else:
                return render(request,'signin.html',{'message':'make sure if your account is registred' })
        else:
            return render(request,'signin.html',{'message':'you are not registred as recorder ' })
            
    else:
        return render(request,'signin.html')


def loginadmin(request):
    if request.method=='POST':
        userd=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=userd,password=pass1)
        if user is not None:
            auth.login(request,user)
            if Cooperative.objects.filter(username=request.user).exists():
                return redirect('dashboard')     
            elif Recorder.objects.filter(username=request.user).exists():
                return redirect('record') 
            elif user.is_superuser:
                return redirect('dashboard')           
            else:
                return render(request,'adminsignin.html',{'message':'make sure if your account is registred'})
        else:
            print(userd)
            print(pass1)
            return render(request,'adminsignin.html',{'message':'invalid credentials' })
            
    else:
        return render(request,'adminsignin.html')
        

def Harvestrecording(request):
    select =Allfarmers.objects.all()
    # st=Recorder.objects.filter(id= str(request.user.id))
    # # prin("hfyfhfy")
    # print(st)
    if request.method == 'POST':
        Quantity = request.POST['Quantity']
        farmercode = request.POST['farmercode']
        # regCooperative=request.POST['regCooperative']
        print(farmercode)
        codes=Allfarmers.objects.filter(farmercode=farmercode)
        for dt in codes:
            tel=dt.telephone
            fname=dt.firstname
            email=dt.email
        if Quantity !=None or farmercode !=None:
            subject='umusaruro wawe muri smart ikigega'
            message='kuri '+fname +'\n'+'ugurishije umusaruro wawe kuwa '+' '+str(datetime.datetime.now()) +' '+'ungana'+' '+Quantity +' '+ 'murakoze gukoresha smartikigega'
            from_email=settings.EMAIL_HOST_USER
            rt=send_mail(subject,message,from_email,[str(email),],fail_silently=True)
                # print(rt)
            if rt == True:

        


              

                if codes.count()>0:
                    insert = Harvestrecord.objects.create(Quantity=Quantity,farmercode=farmercode,telephone=tel,email=email,firstname=fname)
                    insert.save()
                    mess=email
                    return render(request,'record.html',{'message':'data submitted successful','mess':mess,'data':select})
                else:
                    return render(request,'record.html',{'message':'code does  not exist'})

                  #account_sid = 'AC1b41153cd2a60b01893bb9740d2fd875'
                  #auth_token = 'efa2a032ba78dff3111fce2efafa5940'
                   #client =Client(account_sid, auth_token)
                  #message = client.messages.create(body='your Code is: '+nost,from_='+16305280341',to='+250784447864')
                  # sendsms = requests.post('http://rslr.connectbind.com:8080/bulksms/bulksms?username=1212-pathos&password=Chance@1&type=0&dlr=1&destination='+str(telephone)+'&source=smartikigega&message='+str(mess)+'')
                  # pass
                  # return render(request,'record.html',{'message':'data submitted successful','data':select})
                  # insert = Harvestrecord(Quantity=Quantity,code=code, donetime=donetime,donedate=donedate,email=email,firstname=firstname)
                  # insert.save()
            else:
                return render(request,'record.html',{'message':'data  not submitted','data':select})

        else: 
            return render(request,'record.html',{'message':'you have to enter a farmercode to submit','data':select})   
       
    return render(request,'record.html',{'data':select})


def registration(request):
    if request.method=='POST':
        # recaptcha_response = request.POST.get('g-recaptcha-response')
        # url = 'https://www.google.com/recaptcha/api/siteverify'
        # values = {
        #     'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        #     'response': recaptcha_response
        # }
        # data = urllib.parse.urlencode(values).encode()
        # req =  urllib.request.Request(url, data=data)
        # response = urllib.request.urlopen(req)
        # result = json.loads(response.read().decode())
        # ''' End reCAPTCHA validation '''

            
            Name=request.POST['name']
            email=request.POST['email']
            password1=request.POST['password1']
            password2=request.POST['password2']
            # leaderphone=request.POST['leaderphone']
            # district = request.POST['district']
            # harvesttype = request.POST['harvesttype']
            signer = Signer()
            passleng=len(password1)
            if password1==password2:

                if passleng>=8:

                    if User.objects.filter(username=Name).exists():
                        return render(request,'cooperative.html',{'message':'cooperative already exist' })
                    elif User.objects.filter(email=email).exists():
                        return render(request,'cooperative.html',{'message':'email already exist' })
                    else:
                        subject='Verification from smart ikigega'
                        message='This link is for activating your account on smart ikigega'+'\n'+'your Username:  '+Name+'\n'+'https://smartikigega.herokuapp.com/activation/'+email+'/'+signer.sign(email)
                        # +email+'/'+signer.sign(email)
                        from_email=settings.EMAIL_HOST_USER
                        rt=send_mail(subject,message,from_email,[str(email),],fail_silently=False)
                        print(rt)
                        if rt==True:
                            user=User.objects.create_user(email=email,username=Name,password=password1,)
                            user.save()
                            cooperative=Cooperative.objects.create(email=email,password=password1,username=Name)
                            cooperative.save()
                            mess=email
                            return render(request,'cooperative.html',{'message':'succesful registred','mess':mess })
            
                        else:
                            return render(request,'cooperative.html',{'message':' registration failed' })

                else:
                    return render(request,'cooperative.html',{'message':' password must be at least 8 characters' })
            else:
                return render(request,'cooperative.html',{'message':' password 1 and 2  dont match' })
                
    
            
    else:
              
        return render(request,'cooperative.html')

        
def logout(request):
    auth.logout(request)
    return redirect('/')

def prooving(request,pk):
    coop=User.objects.get(id=pk)
    cooperativename=coop.username
    prof=Profilecooperative.objects.filter(company=cooperativename)
    
    if prof.exists():
        for ft in prof:
            ids=ft.id
        tr=Profilecooperative.objects.get(id=ids)
        tr.vis='yes'
        tr.save()
        mess='has been done'
        return redirect('dashboard')
    else:
        messages.info(request,'This is not complete the profile')
        return redirect('dashboard')
    return render(request,'index.html')   

        # if prof.exists():
        #     if Payment.objects.filter(chur_name=str(request.user)).exists():
        #         #print('mpwmw')
        #         last_pay=Payment.objects.filter(chur_name=str(request.user)).order_by('-pay_date')[:1]
        #         for ft in last_pay:
        #             last=ft.pay_date
        #         month_pay=last + datetime.timedelta(30)
        #         date_tod=datetime.date.today()
        #         if month_pay<=date_tod:
        #             instal=10000
        #             bulk=10000
        #             total=instal+bulk
        #             return render(request,'user.html',{'last':last,'month_pay':month_pay,'bulk':bulk,'total':total,'instal':instal,'zipcod':zipcod,'prof':prof,'service':serv})
        #         else:
        #             return render(request,'user.html',{'zipcod':zipcod,'prof':prof,'service':serv})
        #     else:
        #         pay=1
        #         #print(pay)
        #         instal=20000
        #         bulk=10000
        #         total=instal+bulk
        #         return render(request,'user.html',{'bulk':bulk,'total':total,'instal':instal,'pay':pay,'zipcod':zipcod,'prof':prof,'service':serv})
def activation(request,email,un):
    signer = Signer()
    unf=signer.sign(email)
    if un == unf:
        return render(request,'activate.html')
    else:
        return redirect('index.html')

def inside(request):
    user=request.user
    if str(user) =='AnonymousUser':
        return redirect('index')
    else:
        prof=Profilecooperative.objects.filter(cooperativename=str(user))
        cl=Farmers.objects.filter(code=user)
        clien=cl.count()
        mes=Harvestrecord.objects.filter(farmercode=user)
        measr=Harvestrecord.objects.filter(code=str(request.user)).order_by('-id')
        meas=mes.count()
        work=Recorder.objects.filter(username=user)
        works=work.count()
        # num=Contact.objects.filter(user=request.user)
        if prof.exists():
            # if Payment.objects.filter(name=str(user)).exists():
            return render(request,'inside1.html',{'prof':Profilecooperative,'Farmers':clien,'meas':meas,'works':works,'measr':measr})
            # else:
            #     pay=1
            #     instal=20000
            #     bulk=10000
            #     total=instal+bulk
            #     return render(request,'inside1.html',{'bulk':bulk,'total':total,'instal':instal,'pay':pay,'prof':prof,'clien':clien,'meas':meas,'works':works,'measr':measr})

        else:
            return redirect('upload')        

def upload(request):
    profiles=Profilecooperative.objects.filter(cooperativename=str(request.user))
    if profiles.exists():
        return redirect('dashboard')
    else:
        if request.method =='POST':
            img=request.FILES['image']
            Profilecooperative.objects.create(image=img,cooperativename=str(request.user)).save()
            return redirect('inside')
        else:
            return render(request,'upload.html')       
def activate(request):
    if request.method=='POST':
        user=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=user,password=password)
        if user is not None:
            auth.login(request,user)
            if Active.objects.filter(user=request.user).exists():
                return redirect('dashboard')
            else:
                Active.objects.create(user=request.user,activate=True).save()
                return redirect('dashboard')
        else:
            return render(request,'activate.html',{'message':'incorect password and username' })
    else:
        return render(request,'activate.html')

    

def addRecorder(request):
    if str(request.user)=='AnonymousUser':
            return redirect('index')
    else:
        if Recorder.objects.filter(email=(request.user)):
            return redirect('recorder')
        else:
            # zipcod=Zipcodes.objects.all()
            coop=Cooperative.objects.filter(username=str(request.user))
            if request.method=='POST':
                Email=request.POST['Email']
                username=request.POST['username']
                phone=request.POST['phone']
                rand=random.randint(1111,99999)
                password=str(username)+str(rand)
                if Recorder.objects.filter(email=Email).exists():
                    return render(request,'addRecorder.html',{'message':'email already used'})
                else:
                    subject='comfirmation to become a recorder '
                    message='Dear '+username +'\n'+'https://smartikigega.herokuapp.com/singin/'+'\n'+'Username: '+Email+'\n'+'Password: '+password+'\n'+'Thank you are now recorder by'+str(request.user)
                    from_email=settings.EMAIL_HOST_USER
                    rt=send_mail(subject,message,from_email,[str(Email),],fail_silently=True)
                    if rt == True:
                        user=User.objects.create_user(email=Email,username=username,password=password)
                        user.save()
                        Recorder.objects.create(email=Email,username=username,phone=phone,password=password,regCooperative=request.user).save()
                        mess='succesfully added a recorder'
                        return render(request,'addRecorder.html',{'message':'successfully added as recorder','mess':mess})
                    else:
                        return render(request,'addRecorder.html',{'message':'check if your email is correct'})
            else:
                return render(request,'addRecorder.html',{coop:'prof'})

def membersli(request):
    prof=Cooperative.objects.filter(username=str(request.user))
    Rec=Recorder.objects.filter(name=str(request.user)).order_by('-id')
    Farm=Regfarmer.objects.filter(farmercode=str(request.user)).order_by('-id')
    return render(request,'member.html',{'prof':prof,'Rec':Rec,'Farm':Farm})

    # farmers list
def farmersli(request):
    prof=Cooperative.objects.filter(username=str(request.user))
    Farm=Regfarmer.objects.filter().order_by('-id')
    return render(request,'member.html',{'prof':prof,'farm':Farm}) 

    # farmers list
def recordersli(request):
    prof=Cooperative.objects.filter(username=str(request.user))
    Rec=Recorder.objects.filter().order_by('-id')
    return render(request,'Recorder.html',{'prof':prof,'Rec':Rec})     

def harvestli(request):
    prof=Cooperative.objects.filter(username=str(request.user))
    hinz=Harvestrecord.objects.filter().order_by('-id')
    return render(request,'harvestrecord.html',{'prof':prof,'Rec':hinz})      
def adduser(request):
    if str(request.user)=='AnonymousUser':
            return redirect('index')
    else:
        if User.objects.filter(user=str(request.user)):
            return redirect('addus')
        else:
            prof=Profilecooperative.objects.filter(cooperativename=str(request.user))
            if request.method=='POST':
                email=request.POST['username']
                name=request.POST['name']
                rand=random.randint(1111,99999)
                passw=str(name)+str(rand)
                if User.objects.filter(username=email).exists():
                    messages.info(request,'Email have already used')
                    return redirect('addus')
                else:
                    subject='Thank you for Smart ikigega'
                    message='Dear '+name+'  ' +'\n'+'https://smartikigega.herokuapp.com/signin/'+'\n'+'Username: '+email+'\n'+'Password: '+passw+'\n'+'Thank you are now employed by'+str(request.user)
                    from_email=settings.EMAIL_HOST_USER
                    rt=send_mail(subject,message,from_email,[str(email),],fail_silently=True)
                    User.objects.create_user(name=name,email=email,username=email,password=passw).save()
                    Recorder.objects.create(cooperativename=str(request.user),user=email).save()
                    mess='added sucessfully'
                    return render(request,'addus.html',{'mess':mess})
            else:
                return render(request,'addus.html',{'prof':prof})

                # registration of farmers in cooperative
def CooFarmerreg(request):
    # ty=Recorder.objects.filter(user=str(request.user))
    # for tr in ty:
    #     gy=tr.cooperativename
    # prof=Profilecooperative.objects.filter(cooperativename=gy)
    # # zipcod=Zipcodes.objects.all()
    # lastcode=Farmers.objects.all().order_by('-pub_date')[:1]
    # lastcodes=lastcode.count()
    # inst=Recorder.objects.get(user=request.user)
    # cooperative=inst.cooperativename
    # for gt in lastcode:
    #     codf=gt.code
    def random_with_N_digits(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
    nost = random_with_N_digits(6)
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        gender=request.POST['gender']
        # harvesttype=request.POST['harvesttype']
        tel=request.POST['number']
        # tel=request.POST['number']
        telephone =tel[1:]
        now = datetime.datetime.now()
        village=request.POST['village']
        email=request.POST['email']
        district =request.POST['district']
        # sector = request.POST['sector']
        # cell = request.POST['cell']
        years=now.year
        newcode=str(years)+str(1)
        one=1
        print(telephone)
        lastnum=Regfarmer.objects.filter(telephone=telephone)
        nums=lastnum.count()
        print(nums)
        if nums <= 12:
            Regfarmer.objects.create(district=district,village=village,email=email,firstname=firstname,lastname=lastname,gender=gender,telephone=telephone,farmercode= nost,regCooperative=request.user).save()
            Allfarmers.objects.create(district=district,village=village,email=email,firstname=firstname,lastname=lastname,gender=gender,telephone=telephone,farmercode= nost).save()
            mess='Hey '+firstname+'\n Your Code :'+str(nost)
            if email != None or tel !=None:
                subject='Registration succesfull in smartikigega'
                message='Dear '+firstname +' '+lastname +'\n'+'your new SmartIkigega code is : '+str(nost)
                from_email=settings.EMAIL_HOST_USER
                rt=send_mail(subject,message,from_email,[str(email),],fail_silently=True)
                #account_sid = 'AC1b41153cd2a60b01893bb9740d2fd875'
                #auth_token = 'efa2a032ba78dff3111fce2efafa5940'
                #client =Client(account_sid, auth_token)
                #message = client.messages.create(body='your Code is: '+nost,from_='+16305280341',to='+250784447864')
                # sendsms = requests.post('http://rslr.connectbind.com:8080/bulksms/bulksms?username=1212-pathos&password=Chance@1&type=0&dlr=1&destination='+str(tel)+'&source=CityPlus&message='+str(mess)+'')
                # pass
            else:
                pass
            return render(request,'farmerreg.html',{'mess':mess})

        else:
            return render(request,'farmerreg.html')

    else:
        return render(request,'farmerreg.html')


     # registration of farmers independently
def Farmerreg(request):
    # ty=Recorder.objects.filter(user=str(request.user))
    # for tr in ty:
    #     gy=tr.cooperativename
    # prof=Profilecooperative.objects.filter(cooperativename=gy)
    # # zipcod=Zipcodes.objects.all()
    # lastcode=Farmers.objects.all().order_by('-pub_date')[:1]
    # lastcodes=lastcode.count()
    # inst=Recorder.objects.get(user=request.user)
    # cooperative=inst.cooperativename
    # for gt in lastcode:
    #     codf=gt.code
    def random_with_N_digits(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
    nost = random_with_N_digits(6)
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        gender=request.POST['gender']
        harvesttype=request.POST['harvesttype']
        tel=request.POST['number']
        # tel=request.POST['number']
        telephone =tel[1:]
        now = datetime.datetime.now()
        village=request.POST['village']
        email=request.POST['email']
        district =request.POST['district']
        sector = request.POST['sector']
        cell = request.POST['cell']
        years=now.year
        newcode=str(years)+str(1)
        one=1
        print(telephone)
        lastnum=Farmers.objects.filter(number=telephone)
        nums=lastnum.count()
        print(nums)
        if nums <= 12:
            Farmers.objects.create(district=district,sector=sector,village=village,cell=cell,email=email,firstname=firstname,lastname=lastname,gender=gender,number=telephone,harvesttype=harvesttype,code= nost).save()
            Allfarmers.objects.create(district=district,village=village,email=email,firstname=firstname,lastname=lastname,gender=gender,telephone=telephone,farmercode= nost).save() 
            mess='Hey '+firstname+'\n Your Code :'+str(nost)
            if email != None or tel !=None:
                subject='Thank you for Using smartikigega'
                message='Dear '+firstname +' '+lastname +'\n'+'your new SmartIkigega code is : '+str(nost)
                from_email=settings.EMAIL_HOST_USER
                rt=send_mail(subject,message,from_email,[str(email),],fail_silently=True)
                #account_sid = 'AC1b41153cd2a60b01893bb9740d2fd875'
                #auth_token = 'efa2a032ba78dff3111fce2efafa5940'
                #client =Client(account_sid, auth_token)
                #message = client.messages.create(body='your Code is: '+nost,from_='+16305280341',to='+250784447864')
                # sendsms = requests.post('http://rslr.connectbind.com:8080/bulksms/bulksms?username=1212-pathos&password=Chance@1&type=0&dlr=1&destination='+str(tel)+'&source=CityPlus&message='+str(mess)+'')
                # pass
            else:
                pass
            return render(request,'farmerreg.html',{'mess':mess})

        else:
            messages.info(request,'This number is  not full')
            return render(request,'farmerreg.html')

    else:
        return render(request,'farmerreg.html')

def dashboard(request):
    if request.user.is_active:
        cooperatives=User.objects.all()
        farmers=Regfarmer.objects.filter(regCooperative=request.user)
        farmers=farmers.count()
        Record=Harvestrecord.objects.filter(regCooperative=request.user)
        Records=Record.count()
        recorder=Recorder.objects.filter(regCooperative=request.user)
        recorders=recorder.count()
        return render(request,'dashboard.html',{'cooperatives':cooperatives,'farmers':farmers,'Records':Records,'recorders':recorders})
    else:
        return render(request,'index.html')

        