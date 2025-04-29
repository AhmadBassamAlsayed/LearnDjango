from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Make,Auto
from django.urls import reverse_lazy
from .forms import MakeForm



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

class MakeCreate(LoginRequiredMixin,View):
    template = 'autos/make_form.html'
    success_url = reverse_lazy("autos:all")
    def get(self,request):
        form=MakeForm()
        ctx={"form":form}
        return render(request,self.template,ctx)

    def post(self,request):
        form=MakeForm(request.POST)
        if not form.is_valid():
            ctx = {"form":form}
            return render(request,self.template,ctx)
        make=form.save()
        return redirect(self.success_url)

class MakeUpdate(LoginRequiredMixin,View):
    template = 'autos/make_form.html'
    model=Make
    success_url = reverse_lazy("autos:all")
    def get(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        form=MakeForm(instance=make)
        ctx={"form":form}
        return render(request,self.template,ctx)
    def post(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        form =MakeForm(request.POST,instance=make)
        if not form.is_valid():
            ctx = {"form":form}
            return render(request,self.template,ctx)
        make =form.save()
        return redirect(self.success_url)

class MakeDelete(LoginRequiredMixin,View):
    template = 'autos/make_confirm_delete.html'
    model=Make
    success_url = reverse_lazy("autos:all")
    def get(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        ctx={"make":make}
        return render(request,self.template,ctx)

    def post(self,request,pk):
        make =get_object_or_404(self.model,pk=pk)
        make.delete()
        return redirect(self.success_url)

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
    fields="__all__"


