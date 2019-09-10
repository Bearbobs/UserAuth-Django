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

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class hello(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        if request.method == 'GET':

            q = self.request.query_params.get('token')

            return JsonResponse("Correct Token Received Access Granted :"+q, safe=False)