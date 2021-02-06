from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from FoodApp.views import Home,createReview,LogOut,LogIn,register



urlpatterns=[
    path('',Home,name='home'),
   path('create/<str:pk>/',createReview,name='review'),
   path('login/',LogIn,name='login'),
   path('logout/',LogOut,name='logout'),
   path('register/',register,name='register')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)