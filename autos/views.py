from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Make,Auto
from django.urls import reverse_lazy



# Create your views here.
class MainView(LoginRequiredMixin,View):
    def get(self,request):
        lst=Auto.objects.all()
        count=Make.objects.count()
        cntx={"make_count":count,"auto_list":lst}
        return render(request,'autos/auto_list.html',cntx)

class MakeView(LoginRequiredMixin,View):
    def get(self,request):
        ml=Make.objects.all()
        ctx={"make_list":ml}
        return render(request,'autos/make_list.html',ctx)


class MakeCreate(LoginRequiredMixin,CreateView):
    model = Make
    fields = "__all__"
    success_url = reverse_lazy('autos:all')

class MakeUpdate(LoginRequiredMixin,UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy("autos:all")

class MakeDelete(LoginRequiredMixin,DeleteView):
    model=Make
    success_url=reverse_lazy("autos:all")

class AutoCreate(LoginRequiredMixin,CreateView):
    model=Auto
    fields="__all__"
    success_url = reverse_lazy("autos:all")

class AutoUpdate(LoginRequiredMixin,UpdateView):
    model=Auto
    success_url=reverse_lazy("autos:all")
    fields="__all__"

class AutoDelete(LoginRequiredMixin,DeleteView):
    model=Auto
    success_url=reverse_lazy("autos:all")



