from django.shortcuts import render,redirect
from .models import User_sign

def sign_up(request):
    dict={}
    if request.method == "POST":
        username = request.POST['userid']
        password = request.POST['password'] 
        image = request.FILES['image_user']
        phonenumber = request.POST['phonenumber']
        userid = list(User_sign.objects.values_list('user_name', flat = True))
        if username in userid :
            dict.update({"Error":"Already Registered."})
            return render(request,'sign-up.html',dict)
        
        login = User_sign()
        login.user_name = username
        login.password = password
        login.image = image
        login.phone_number = phonenumber
        login.save()
        request.session['username'] = username
        return redirect('user-page') 
    return render(request,'sign-up.html')




def log_in(request):
    if(request.method == "POST"):
        userid = list(User_sign.objects.values_list('user_name', flat = True))
        password = list(User_sign.objects.values_list('password', flat = True))
        user_id = request.POST['userid']
        dict={}
        user_password = request.POST['password']
        if user_id in userid:
            
            if user_password == password[userid.index(user_id)]:
                # dict.update({'username':user_id})
                request.session['username'] = user_id
                return redirect('user-page')
            else:
                dict.update({"Error":"UserId/Password Invalid"})
                return render(request,'sign_in.html',dict)
    return render(request,'sign_in.html')

# def log_in_r(request):
#     if(request.method == "POST"):
#         userid = list(User_sign.objects.values_list('user_name', flat = True))
#         password = list(User_sign.objects.values_list('password', flat = True))
#         user_id = request.POST['userid']
#         dict={}
#         user_password = request.POST['password']
#         if user_id in userid:
            
#             if user_password == password[userid.index(user_id)]:
#                 # dict.update({'username':user_id})
#                 request.session['username'] = user_id
#             else:
#                 dict.update({"Error":"UserId/Password Invalid"})
#                 return render(request,'login_redirect.html',dict)
#     return render(request,'login_redirect.html')



# <input type="file" name="image_user" accept=".jpeg,.png,.jpg" />
#         <input type="text" name="phonenumber" maxlength="10" pattern="\d{10}" title="Please enter exactly 10 digits" />
#           {% csrf_token %}



