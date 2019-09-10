from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse
from django.core import serializers
from collections import ChainMap
import requests
from rest_framework.permissions import IsAuthenticated


#Api to check authentication
class hello(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        if request.method == 'GET':
            #query term
            q = self.request.query_params.get('token')
            #Api endpoint,can be change according to use.
            return JsonResponse("Correct Token Received Access Granted :"+q, safe=False)

#Post Api for login
class login(viewsets.ViewSet):
    def list(self, request):
        if request.method == 'POST':

            q = self.request.query_params.get('username')
            p = self.request.query_params.get('password')

            return 