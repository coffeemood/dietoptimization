from django.conf.urls import url
from . import views # Importing current app so we can refference the current views' url

urlpatterns = [

    url(r'home', views.index, name = 'home'),
    url(r'carb', views.carb, name = 'carb')
    # url(r'^store/', 'views.store', name = 'store'),

]