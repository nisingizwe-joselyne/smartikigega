from django.db import models
from django.contrib.auth.models import User,auth
# from ussd.models import *
# Create your models here.
class Cooperative(models.Model):
    username=models.CharField(max_length=255)
    email=models.CharField(max_length=255) 
    password=models.CharField(max_length=255) 
    def __str__(self):
        return self.username
class Payment(models.Model):
    name=models.CharField(max_length=255,null=False,blank=False)
    pay_date=models.DateField(auto_now=True)
    pay_time=models.TimeField(auto_now=True)

class Recorder(models.Model):
    username = models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    regCooperative = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.username 
class Active(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    activate=models.FloatField(default=False)
    pub_date=models.DateTimeField(auto_now_add=True)
    
class Farmers(models.Model):
    firstname= models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    harvesttype = models.CharField(max_length=255)
    dateofbirth = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    Cooperative=models.CharField(max_length=255)
    code=models.CharField(max_length=255)
    pincode=models.CharField(max_length=255)
    sector=models.CharField(max_length=255) 
    cell=models.CharField(max_length=255) 
    def __str__(self):
        return self.firstname       

class Allfarmers(models.Model):
    firstname= models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    harvesttype = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    Cooperative=models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    farmercode=models.CharField(max_length=255)
    pincode=models.CharField(max_length=255)
    sector=models.CharField(max_length=255) 
    cell=models.CharField(max_length=255) 
    def __str__(self):
        return self.firstname              

class Regfarmer(models.Model):
    firstname= models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    dateofbirth = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    regCooperative=models.ForeignKey(User, on_delete=models.CASCADE)
    farmercode=models.CharField(max_length=255)
    def __str__(self):
        return self.firstname
class Insurance(models.Model):
    farmercode=models.ForeignKey(Regfarmer, on_delete=models.CASCADE)
    insurancetype = models.CharField(max_length=255,choices=(('imyaka15','imyaka15'),('imyaka10','imyaka10'),('imyaka itanu','imyaka itanu'),('umwaka umwe','umwaka umwe'),))
    def __str__(self):
        return self.farmercode  
class Harvestrecord(models.Model):
    recorder=models.CharField(max_length=255)
    regCooperative=models.ForeignKey(User, on_delete=models.CASCADE)
    Quantity=models.CharField(max_length=255)
    farmercode=models.CharField(max_length=255)
    firstname=models.CharField(max_length=255) 
    email=models.CharField(max_length=255)
    telephone=models.CharField(max_length=255)
    donedate=models.DateField(auto_now=True)
    donetime=models.TimeField(auto_now=True)
    def __str__(self):
        return self.firstname 
class EndpointAfripay(models.Model):
    status=models.CharField(max_length=255)
    transaction_ref=models.CharField(max_length=234)
    amount=models.FloatField()
    currency=models.CharField(max_length=234)
    payment_method=models.CharField(max_length=234)
    client_token=models.CharField(max_length=234)

class sites(models.Model):
    Cooperative=models.ForeignKey(Cooperative, on_delete=models.CASCADE)
    sitename=models.CharField(max_length=20)    
    def __str__(self):
        return self.sitename
class Loan(models.Model):
    farmercode = models.ForeignKey(Regfarmer, on_delete=models.CASCADE)
    amount= models.CharField(max_length=255)
    firstname= models.CharField(max_length=255)
    telephone= models.CharField(max_length=255)
    Quantity= models.CharField(max_length=255)
    def __str__(self):
        return self.farmercode

class Payharvest(models.Model):
    farmercode = models.ForeignKey(Regfarmer, on_delete=models.CASCADE)
    pay_amount= models.CharField(max_length=255)
    def __str__(self):
        return self.farmercode

# class Cooperativesreg(models.Model):
#     name=models.CharField(max_length=255)
#     leaderphone=models.CharField(max_length=255)
#     harvesttype=models.CharField(max_length=255)
#     Cooperativedistrict=models.CharField(max_length=255) 
#     Cooperativesector=models.CharField(max_length=255) 
#     def __str__(self):
#         return self.name

class Profilecooperative(models.Model):
    farmers=models.ForeignKey(Allfarmers, on_delete=models.CASCADE)
    image=models.ImageField(upload_to=' cooperative Logo',null=True,blank=True)
    cooperativename=models.CharField(max_length=255)
    activate_on=models.DateField(auto_now=True)
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url       

# todoreg
class Todoreg(models.Model):
    todo=models.CharField(max_length=200)   
    def __str__(self):
        return self.todo