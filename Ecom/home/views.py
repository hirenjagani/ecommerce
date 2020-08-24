from django.contrib.auth import authenticate,login,get_user_model
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .forms import Contact,Login,Register

def index(request):

   context={
       "content":"hello user"
   }


   return render(request,'index.html',context)

def loginf(request):
    login_form=Login(request.POST or None)
    context = {
        "form": login_form
    }
    # print("user loggedin")
    # print(request.user.is_authenticated)

    if login_form.is_valid():
        # print(login_form.cleaned_data)
        username=login_form.cleaned_data.get("username")
        password=login_form.cleaned_data.get("password")
        user=authenticate(request,username=username,password=password)
        # print(user)

        if user is not None:

            login(request,user)
            return redirect('/')
        else:
            print("error")
    return render(request,'login.html',context)

User= get_user_model()

def register(request):
    if request.method=='POST':
      form = Register(request.POST)

      if form.is_valid():

        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user=User.objects.create_user(username,email,password)
        login(request,user)
        return redirect('index')
    else:
        form = Register()
    return render(request,'register.html',{'form':form})



def contact(request):
    contact_form=Contact(request.POST or None)
    context={
        "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request,'contact.html',context)


def contact_done(request):
    return render(request,'contactdone.html',{})