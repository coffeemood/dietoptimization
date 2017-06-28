from django.conf.urls import url
from . import views # Importing current app so we can refference the current views' url

urlpatterns = [

    url(r'^$', views.index, name = 'index'),
    # url(r'^store/', 'views.store', name = 'store'),

]