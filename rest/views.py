from django.shortcuts import render
from rest_framework import viewsets

from .models import Top, Tovar
from .serializers import TopSerializer, TovarSerializer


class TopViewSet(viewsets.ModelViewSet):
    queryset = Top.objects.all()
    serializer_class = TopSerializer


class TovarViewSet(viewsets.ModelViewSet):
    queryset = Tovar.objects.all()
    serializer_class = TovarSerializer


def home(request):
    top = Top.objects.all()
    tovar = Tovar.objects.all()

    return render( request, "home.html", { "top": top, "tovar": tovar })


def index(request):
    top = Top.objects.all()
    return render( request, "index.html", { "top": top } )