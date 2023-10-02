from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
#from app.models import User
from django.contrib import messages
from .emailBackend import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from .emailBackend import EmailBackEnd
from django.conf import settings
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        #print('ode')
        
        user=EmailBackEnd.authenticate(request, username=email, password=password)
        print('jojojo',user)
        if user is not None:
            print('jo')
            auth.login(request, user)
            return redirect('home')
        
        else:
            messages.info(request, 'Invalid Credential')
            return redirect('login')
    else:
        return render(request, 'registration/login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('login')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # check email
        if User.objects.filter(email=email).exists():
            messages.warning(request,'This Email seems to be in our database !')
            return redirect('register')

        # check username
        elif User.objects.filter(username=username).exists():
            messages.warning(request,'Username is taken, please, try use something unique !')
            return redirect('register')
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password = password
            )
            
            user.set_password(password)
            user.save()
            return redirect('login')
    
    return render(request, 'registration/register.html')

# def user_login(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(email, password)
		
#         user = EmailBackEnd.authenticate(request,
#                                      username=email,
        
#                                      password=password)
#         #if user.is_authenticated:
#         # print("Before redirect to home")
#         if user != True:
#            print("Before redirect to home")
#            user.save()
#            #print("Before redirect to home")
#            login(request,user)
#            #print("Before redirect to home")
#            return redirect('home')
#         else:
#            messages.error(request,'Email and Password Are Invalid !')
#            return redirect('login')
# def user_login(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']
#         print(email, password)

#         user = auth.authenticate(request, email=email, password=password)
#         if user:
#         # user = User.objects.get(email=email)
        
#         # print('>>>@@',user)
#         # if user !=None:
#             print('>tunde')
#             auth.login(request, user)
#             return redirect('home')
            
#         else:
#             messages.error(request, 'Email and Password Are Invalid !')
#             return redirect('login')
    # else:
    #     # Handle GET requests (e.g., rendering the login form)
    #     # You may want to add this part if needed.
    #     return render(request, 'registration/login.html')
# def user_login(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(email, password)

#         try:
#             user = EmailBackEnd.authenticate(request, username=email, password=password)
#             if user ==True:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Email and Password Are Invalid !')
#                 return redirect('login')
#         except Exception as e:
#             messages.error(request, f'An error occurred: {str(e)}')
#             return redirect('login')
    # else:
    #     # Render the login form template for GET requests
    #     return render(request, 'registration/login.html')
    # return None

def profile(request):
    return render(request, 'registration/profile.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        
        user.save()
        
        messages.success(request, 'Profile updated successfully')
        return redirect('profile')
    #return render(request, 'components/msg.html')
    
#     if request.method == "POST":
#         username = request.POST.get('username')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user_id = request.user.id
#         user = User.objects.get(id=user_id)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.username = username
#         user.email = email

#         if password != None and password != "":
#             user.set_password(password)
#         user.save()
#         messages.success(request,'Profile Successfully Updated. ')
#         return redirect('profile')
#         print(user_id)
    
