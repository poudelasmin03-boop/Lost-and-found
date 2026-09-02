from django.shortcuts import render,redirect
from .models import Itemdetails
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import numpy as np
from django.db.models import Q
import cv2
# Create your views here.
def home_views(request):
  return render(request,'base.html')


def Foundform(request):
   if request.method  == "POST":
     itemName = request.POST.get('itemName')
     itemDescription = request.POST.get('itemDescription')
     itemImage = request.FILES.get('itemImage')
     location = request.POST.get('location')
     foundDate = request.POST.get('foundDate')
     phoneNo = request.POST.get('phoneNo')
     
     #checking image clearity
     if not  itemImage:
         print("error")
         return
     
     
     image_data = np.frombuffer(itemImage.read(), np.uint8)
     image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
     
    #  image = cv2.imread("itemImage")
     print(image)
     if image is None:
       return render(request,'foundform.html',{'error':"Empty Image." })
         
     
     gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
     
     score = cv2.Laplacian(gray_image,cv2.CV_64F).var()
     if score<100:
       return render(request,'foundform.html',{'error':"Image isn't clear." })
   
    #End 
    
    #storing data
    
     items =  Itemdetails.objects.create(
       user  = request.user,
       itemName =itemName,
       itemDescription = itemDescription,
       itemImage = itemImage,
       location =location,
       foundDate =foundDate,
       phoneNo = phoneNo,
      
       
       
     )
     
     items.save()
     #end here 
     return render(request,'base.html',{'message':"Successfully Posted"})
     
     
   return render(request,"foundform.html")
 
 
 # ================= Register =================
def register_views(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "register_error": "Username already exists.",
                'openRegister':False
            })

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {
                "register_error": "Email already exists.",
                
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "register.html",{'openRegister':True})


# ================= Login =================



def login_views(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        
        if not User.objects.filter(username = username).exists():
            return render(request, "login.html", {
                "error": "Invalid username.",
            })
            
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect("home")

        return render(request, "login.html", {
            "error": "Incorrect password.",
        })

    return render(request, "login.html")
  
  
  
  
#======logout views=====
def logout_views(request):
    logout(request)

    return redirect('home')  


# ======Get items ===== 
def FoundItems(request,id):
    items = Itemdetails.objects.all()
    return render(request,"foundform.html",{"items":items})




# ====Search Items====

def search_items(request):
    name =  request.GET.get('name')
    location = request.GET.get('location')
    
    if name or location:
        if Itemdetails.objects.filter(Q(itemName = name) | Q(location__icontains = location)):
            items = Itemdetails.objects.all()
            return render(request,'foundform.html',{'items':items})
        
        
    
        return render(request,'foundform.html',{'error':"error"})    
            