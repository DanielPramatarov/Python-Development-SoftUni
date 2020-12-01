
from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import logout , login, authenticate
from django.contrib.auth.forms import  UserCreationForm
from django.contrib import  messages
from django.contrib.auth.models import User
from accounts.models import UserProfile
from recipe.models import Item
from accounts.forms import ProfileForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import Group
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })  

def logOut(request):
    logout(request)
    return render(request, 'logout.html')


def SignUp(request):
    if request.user.is_authenticated:
        return redirect('User_Profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('pass')
            repeat_password = request.POST.get('repeat-pass')
            # password = request.POST.get('password')
        

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('accounts:User_Profile')
            else:
                messages.info(request, 'Username OR password is incorrect')

        
        context = {}
        return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
       
        if form.is_valid():
            user =    form.save()
            profile = UserProfile(
                  user =user  
            ) 
            profile.save()
            group = Group.objects.get(name='Users')
            user.groups.add(group)
            # user_name = request.POST['username']
            
            login(request,user)
            return redirect('accounts:User_Profile')
    
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


def userRecipes(request, pk ):
    profile = UserProfile.objects.get(pk=pk)
    recipes = Item.objects.all()
    user_recipes = []

    for recipe in recipes:
        if recipe.user_name == profile.user:
            user_recipes.append(recipe)


    context = {
    'recipes': user_recipes,
    'profile':profile
   
        
    }
    return render(request, 'user_recipes.html', context)






def detailProfile(request, pk):
    profile = UserProfile.objects.get(pk=pk)

    recipe_count = Item.objects.all()
    current_user_count_recipes = 0

    if recipe_count != 0:
        for recipe in recipe_count:
            
            if recipe.user_name ==  profile.user:
                current_user_count_recipes += 1

    # user = User.objects.get(pk=pk)
    

    
    context = {
        'profile': profile,
        'count': current_user_count_recipes,
        
    }
    return render(request, 'view_user.html', context)




def profiles(request):

    all_users = User.objects.values()
    UserProfiles = UserProfile.objects.all()    
    for user in UserProfiles:
        print(user.profile_image)

    paginator = Paginator(UserProfiles, 6) 

    page_number = request.GET.get('page')
    UserProfiles = paginator.get_page(page_number)

    context = {
        'users': UserProfiles,
        'all_users':UserProfiles,
        
    }


    return render(request, 'profiles.html', context)




def edit_profile(request):
    profile = ""
    UserProfiles = UserProfile.objects.all()
    for prof in UserProfiles:
        if request.user == prof.user:
            profile = prof
    if request.method == 'GET':
        context = {
            'profile': profile,
            'form': ProfileForm(instance=profile),
        }

        return render(request, 'edit_profile.html', context)

    elif  request.method == "POST":
        form = ProfileForm(request.POST, request.FILES,  instance=profile )
        if form.is_valid():
            form.save() 
            return redirect('accounts:User_Profile')
        context = {
            'profile': profile,
            'form': ProfileForm(instance=profile),
        }

        return render(request, 'edit_profile.html', context)
        


def User_Profile(request):
    profile = ""
    UserProfiles = UserProfile.objects.all()
    for prof in UserProfiles:
        if request.user == prof.user:
            profile = prof

   
    recipe_count = Item.objects.all()
    current_user_count_recipes = 0
    status = ""

    all_recipes = Item.objects.all()
    users_recipes = []

    dislikes = 0
    likes = 0
    for recipe in all_recipes:

        if recipe.user_name == request.user:
            likes += recipe.likes.count()
            dislikes += recipe.Dislikes.count()
            users_recipes.append(recipe)

    

    
    if recipe_count != 0:
        for recipe in recipe_count:
            
            if recipe.user_name ==  profile.user:
                current_user_count_recipes += 1

    
    if request.user.is_active:
        status = "active"
    else:
        status = "offline"


    
    context = {
        'profile': profile,
        'count': current_user_count_recipes,
        'status':status,
        'user_recipes': users_recipes,
        'likes':likes,
        'dislikes':dislikes,
        
    }

    


    return render(request, 'User_profiles.html', context)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?


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

