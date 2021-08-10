from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from skintone import views

app_name = 'skin'
urlpatterns = [
    path('', views.home, name='home'),
    path('coding/', views.coding, name='coding'),
    path('readmore/', views.readmore, name='readmore'),
    path('robust/', views.robust, name='robust'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('preview/', views.preview, name='preview'),
    path('capture/', views.capture, name='capture'),
    path('preview/result/', views.result, name='result'),
    #path('imgprocess/', views.imgprocess, name='imgprocess')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)