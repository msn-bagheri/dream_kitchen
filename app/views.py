from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from app.serializers import UserFormSerializer


@never_cache
def index(request):
    return render(request, 'index.html', {})


@never_cache
def gallery(request):
    return render(request, 'gallery.html', {})


@never_cache
def reservation(request):
    return render(request, 'reservation.html', {})


@never_cache
def about(request):
    return render(request, 'about.html', {})

@never_cache
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

