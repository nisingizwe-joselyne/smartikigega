from django.urls import path
from .import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static
                                                         
urlpatterns=[
    path('',views.welcome, name='harvest'),
    path('kiny',views.kiny, name='kiny'),
    path('cooperative',views.cooperative, name='cooperative'),
    path('work',views.work, name='work'),
    path('signin',views.signin, name='signin'),
    path('adminsignin',views.adminsignin, name='adminsignin'),
    path('record',views.record, name='record'),
    path('recorderadd',views.recorderadd, name='recorderadd'),
    path('pay',views.pay, name='pay'),
    path('reg',views.reg, name='regpage'),
    path('regfarm',views.regfarm, name='regfarmpage'),
    # path('about-us',views.about, name='about'),
    # path('digital-ikigega',views.Ikigega, name='ikigega'),
    # path('farmercreate/',views.farmercreate, name='farmercreate'),
    path('loan/endpoints/',views.LoanRequest, name='loanendpoints'),
    path('insurance/endpoints/',views.InsuranceRequest, name='insurancendpoints'),
    # path('payharvest/endpoints/',views.Harvestpay, name='payharvestpoints'),
    path('registration', views.registration, name='register'),
    path('harvestrecording', views.Harvestrecording, name='recording'),
    path('digital/',views.digital, name='digital'),
    path('digitalapp/',views.digitalapp, name='digitalapp'),
    path('dashboard/get_admin/staff',views.dashboard,name='dashboard'),
    path('activation/<str:email>/<str:un>',views.activation,name='activation'),
    path('activate/',views.activate,name='activate'),
    path('reset-now/smartikigega-password/<username>/',views.resetnow, name='resetnow'),
    path('smartikigega/reset/', views.reset, name='reset'),
    path('proove/get_admin/<int:pk>',views.prooving,name='proove'),
    path('farmerreg/',views.Farmerreg,name='farmerreg'),
    path('addrecorder/',views.addRecorder,name='addrecorder'),
    path('login/', views.login, name='login'),
    path('loginadmin/', views.loginadmin, name='loginadmin'),
    path('logout/', views.logout, name='logout'),
    path('user-login/', CustomAuthToken.as_view()),
    # path('<int:id>deleteInfos', views.delreg, name='deleteInfos'),
    # path('<int:id>updateInfos',views.updatereg, name='updateInfos'),
    # path('reg/endpoint', views.registerEndpoint, name='endpoint'),
    # path('deleteEndpoints/<int:id>', views.deleteEndpoint, name='deleteEndpoints'),
    # path('user-creation/', CustomAuthToken.as_view())
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)