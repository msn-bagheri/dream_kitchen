from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework.response import Response

from app.models import UserForm
from app.serializers import UserFormSerializer


def index(request):
    return render(request, 'index.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def reservation(request):
    return render(request, 'reservation.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def design_consultation(request):
    if request.method == 'POST':
        data = request.POST
        data._mutable = True
        data.update(request.FILES)
        serializer = UserFormSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Thank you for choosing us.')
        else:
            return HttpResponse(serializer.errors)

