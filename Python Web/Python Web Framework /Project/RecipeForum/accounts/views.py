
from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import  UserCreationForm
from django.contrib import  messages
from django.contrib.auth.models import User


def logOut(request):
    logout(request)
    return render(request, 'logout.html')



# def register(request):
   
#     # form.fields['username'].widget.attrs.update({
#     #         'placeholder': 'Enter your Username'
#     #     })
#     # form.fields['password1'].widget.attrs.update({
#     #         'placeholder': 'Enter your Passoword'
#     #     })
#     # form.fields['password2'].widget.attrs.update({
#     #         'placeholder': 'Repeat your Passoword'
#     #     })
    
#     if request.method == "POST":
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         user_name = request.POST['username']
#         # username= form.cleaned_data.get("username")
#         # passwordvalue1= form.cleaned_data.get("password1")
#         # passwordvalue2= form.cleaned_data.get("password2")
        
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             messages.success(request, f'welcome {username}, your account is created')
#             redirect('recipe:all_recipe')
#             # return render(request, 'register.html')
#     else:
#         form = UserCreationForm()

#     context = {
#         'form' : form
#     }



#     return render(request, 'register.html', context)




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
       
        if form.is_valid():
            # form.save()
            user_name = request.POST['username']
            messages.success(request, f'welcome {user_name}, your account is created')
            return redirect('recipe:all_recipe')
    
    form = UserCreationForm()
    form.fields['username'].widget.attrs.update({
        'placeholder': 'Enter your username'
    })
    form.fields['password1'].widget.attrs.update({
    'placeholder': 'Enter your password'
    })
    form.fields['password2'].widget.attrs.update({
        'placeholder': 'Repeat your password'
    })
    context = {
        'form': form
    }
    return render(request, 'register.html', context)



def profiles(request):

    all_users =User.objects.values()
    context = {
        'users': all_users
    }


    return render(request, 'profiles.html', context)



# from django.shortcuts import render
# from .forms import Signupform
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login


# def signup(request):
#     firstname=''
#     lastname=''
#     emailvalue=''
#     uservalue=''
#     passwordvalue1=''
#     passwordvalue2=''

#     form= Signupform(request.POST or None)
#     if form.is_valid():
#         fs= form.save(commit=False)
#         firstname= form.cleaned_data.get("first_name")
#         lastname= form.cleaned_data.get("last_name")
#         emailvalue= form.cleaned_data.get("email")
#         uservalue= form.cleaned_data.get("username")
#         passwordvalue1= form.cleaned_data.get("password1")
#         passwordvalue2= form.cleaned_data.get("password2")
#         if passwordvalue1 == passwordvalue2:
#             try:
#                 user= User.objects.get(username=uservalue)
#                 context= {'form': form, 'error':'The username you entered has already been taken. Please try another username.'}
#                 return render(request, 'siteusers/signup.html', context)
#             except User.DoesNotExist:
#                 user= User.objects.create_user(uservalue, password= passwordvalue1, email=emailvalue)
               
# 		user.save()

#                 login(request,user)

#                 fs.user= request.user

#                 fs.save()
#                 context= {'form': form}
#                 return render(request, 'siteusers/signup.html', context)
            
#         else:
#             context= {'form': form, 'error':'The passwords that you provided don\'t match'}
#             return render(request, 'siteusers/signup.html', context)
        

#     else:
#         context= {'form': form}
#         return render(request, 'siteusers/signup.html', context)

