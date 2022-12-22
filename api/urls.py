from django.urls import path , include
from account.api.views import ( 
    UserSignupApiView , 
    PhoneApiView , 
    PhoneVerifyApiView , 
    MyTokenObtainPairView ,
    LoginApiView
)
from . import views



urlpatterns = [ 
    path('account/', include('account.api.urls') ),
    path('signup/', UserSignupApiView.as_view() ),
    path('signin/', LoginApiView.as_view() ),  
    path('signup/phone', PhoneApiView.as_view() ),
    path('signup/phone/verify', PhoneVerifyApiView.as_view() ),
    path('loans/', include('client.api.urls')),  
    path('users/', include('client.api.users_urls')),  
    path('admin/', include('client.api.admin.urls')),  
    path('payment/verify', views.VerifyPaymentApiView.as_view()),    
    path('generate', views.Generate.as_view()),    
    # path('generate')
]      