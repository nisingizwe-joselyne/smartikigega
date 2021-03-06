from django.urls import path
from .import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static
                                                         
urlpatterns=[
    path('',views.welcome, name='harvest'),
    path('kiny',views.kiny, name='kiny'),
    path('cooperative',views.cooperative, name='cooperative'),
    path('ndash',views.ndash, name='ndash'),
    path('cooaddfarmer',views.cooaddfarmer, name='cooaddfarmer'),
    path('work',views.work, name='work'),
    path('loanpage',views.loanpage, name='loanpage'),
    path('insurancepage',views.insurancepage, name='insurancepage'),
    path('signin',views.signin, name='signin'),
    path('adminsignin',views.adminsignin, name='adminsignin'),
    path('record',views.record, name='record'),
    path('recorderadd',views.recorderadd, name='recorderadd'),
    path('pay',views.pay, name='pay'),
    path('editp',views.editp, name='editp'),
    path('addus',views.addus, name='addus'),
    path('reg',views.reg, name='regpage'),
    path('regfarm',views.regfarm, name='regfarmpage'),
     path('<int:id>deleteInfos', views.delreg, name='deleteInfos'),
    path('<int:id>updateInfos', views.updatereg, name='updateInfos'),
    path('todolist', views.todo, name='todo'),
    path('insurance/endpoints/',views.InsuranceRequest, name='insurancendpoints'),
    # path('payharvest/endpoints/',views.Harvestpay, name='payharvestpoints'),
    path('registration', views.registration, name='register'),
    path('harvestrecording', views.Harvestrecording, name='recording'),
    path('digital/',views.digital, name='digital'),
    path('digitalapp/',views.digitalapp, name='digitalapp'),
    path('dashboard/get_admin/staff',views.dashboard,name='dashboard'),
    path('activation/<str:email>/<str:un>',views.activation,name='activation'),
    path('activate/',views.activate,name='activate'),
    path('reset-now/smartikigega.herokuapp-password/<username>/',views.resetnow, name='resetnow'),
    path('smartikigega/reset/', views.reset, name='reset'),
    path('proove/get_admin/<int:pk>',views.prooving,name='proove'),
    path('farmerreg/',views.Farmerreg,name='farmerreg'),
    path('coofarmerreg/',views.CooFarmerreg,name='coofarmerreg'),
    path('addrecorder/',views.addRecorder,name='addrecorder'),
    path('loanrequest/', views.Loanrequesting, name='loanrequest'),
    path('insurancerequest/', views.Insurancerequesting, name='insurancerequest'),
    path('login/', views.login, name='login'),
    path('inside/',views.inside,name='inside'),
    path('loginadmin/', views.loginadmin, name='loginadmin'),
    path('logout/', views.logout, name='logout'),
    path('members-list/get',views.membersli, name='members-list/get'),
    path('farmers-list/get',views.farmersli, name='farmers'),
    path('recoders-list/get',views.recordersli, name='recorders'),
    path('recods-list/get',views.harvestli, name='records'),
    path('adduser/',views.adduser,name='adduser'),
    path('user-login/', CustomAuthToken.as_view()),
    # path('<int:id>deleteInfos', views.delreg, name='deleteInfos'),
    # path('<int:id>updateInfos',views.updatereg, name='updateInfos'),
    # path('reg/endpoint', views.registerEndpoint, name='endpoint'),
    # path('deleteEndpoints/<int:id>', views.deleteEndpoint, name='deleteEndpoints'),
    # path('user-creation/', CustomAuthToken.as_view())
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)