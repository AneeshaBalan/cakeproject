from django.shortcuts import render,redirect
from django.views.generic import View
from django import forms
from myapp.models import CakeBox
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


# Create your views here.
class CakeForm(forms.ModelForm):
    class Meta:
        model=CakeBox
        fields="__all__"
        # widget={
        #     "name":forms.TextInput(attrs={"class":"form-control"}),
        #     "flavour":forms.TextInput(attrs={"class":"form-control"}),
        #     "price":forms.NumberInput(attrs={"class":"form-control"}),
        #     "shape":forms.TextInput(attrs={"class":"form-control"}),
        #     "weight":forms.TextInput(attrs={"class":"form-control"}),
        #     "layer":forms.TextInput(attrs={"class":"form-control"}),
        #     "image":forms.FileInput(attrs={"class":"form-control"}),

        # }
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "flavour":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "shape":forms.TextInput(attrs={"class":"form-control"}),
            "weight":forms.TextInput(attrs={"class":"form-control"}),
            "layer":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
        
        }
# class CakeRegisterForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=["first_name","last_name","email","username","password"]
#         widget={
#             "first_name":forms.TextInput(attrs={"class":"form-control"}),
#             "last_name":forms.TextInput(attrs={"class":"form-control"}),
#             "email":forms.EmailInput(attrs={"class":"form-control"}),
#             "username":forms.TextInput(attrs={"class":"form-control"}),
#             "password":forms.PasswordInput(attrs={"class":"form-control"}),
#         }
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "user_name":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
        }
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class CakeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=CakeForm()
        return render(request,"cakeadd.html",{"form":form})
    def post(self,request,*args,**kwards):
        form=CakeForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cakelist")
        return render(request,"cakeadd.html",{"form":form})
    
class CakeListView(View):
    def get(self,request,*args,**kwargs):
        qs=CakeBox.objects.all()
        return render(request,"index.html",{"cakebox":qs})
    
class CakeDetailsView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=CakeBox.objects.get(id=id)
        return render(request,"cakedetails.html",{"cake":qs})

class CakeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        CakeBox.objects.get(id=id).delete()
        return redirect("cakelist")
    
class CakeEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cake=CakeBox.objects.get(id=id)
        form=CakeForm(instance=cake)
        return render(request,"cakeedit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cake=CakeBox.objects.get(id=id)
        form=CakeForm(instance=cake,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cakedetails",pk=id)
        return render(request,"cakeedit.html",{"form":form})
    
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
           uname=form.cleaned_data.get("username")
           pswd=form.cleaned_data.get("password")
           usr=authenticate(request,username=uname,password=pswd)
           if usr:
               login(request,usr)
               return redirect("cakelist")
        return render(request,"login.html",{"form":form})

        
















    
