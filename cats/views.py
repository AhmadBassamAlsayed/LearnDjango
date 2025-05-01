from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from rest_framework.reverse import reverse_lazy

from .models import  Cat,Breed
# Create your views here.
class MainView(LoginRequiredMixin, View):
    def get (self ,request):
        cnt=Breed.objects.all().count()
        ls=Cat.objects.all()
        ctx={"cat_list":ls,"breed_count":cnt}
        return render(request,"cats/cat_list.html",ctx)

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        br=Breed.objects.all()
        ctx={"breed_list":br}
        return render(request,"cats/breed_list.html",ctx)

class CatCreate(LoginRequiredMixin, CreateView):
    model=Cat
    fields="__all__"
    success_url = reverse_lazy("cats:all")

class CatUpdate(LoginRequiredMixin, UpdateView):
    model=Cat
    fields="__all__"
    success_url = reverse_lazy("cats:all")

class CatDelete(LoginRequiredMixin, DeleteView):
    model=Cat
    success_url = reverse_lazy("cats:all")

class BreedCreate(LoginRequiredMixin, CreateView):
    model=Breed
    success_url = reverse_lazy("cats:all")
    fields="__all__"

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model=Breed
    fields="__all__"
    success_url = reverse_lazy("cats:all")

class BreedDelete(LoginRequiredMixin, DeleteView):
    model=Breed
    success_url=reverse_lazy("cats:all")