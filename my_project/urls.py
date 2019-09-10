from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from rest_framework import routers
from accounts.views import hello
#Rest Framework router for Hello Api
router_search = routers.DefaultRouter()
router_search.register(r'api', hello,base_name='base')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

urlpatterns += router_search.urls