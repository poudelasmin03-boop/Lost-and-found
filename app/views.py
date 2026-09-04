from django.shortcuts import render, redirect
from .models import Itemdetails
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
import numpy as np
import cv2


# ================= Home =================
def home_views(request):
    recent_items = Itemdetails.objects.all().order_by('-created_at')[:6]
    return render(request, 'home.html', {'recent_items': recent_items})


# ================= Found Item Form =================
@login_required(login_url='login')
def Foundform(request):
    if request.method == "POST":
        itemName = request.POST.get('itemName')
        itemDescription = request.POST.get('itemDescription')
        itemTag = request.POST.get('itemTag', 'other')
        itemImage = request.FILES.get('itemImage')
        location = request.POST.get('location')
        foundDate = request.POST.get('foundDate')
        phoneNo = request.POST.get('phoneNo')

        # Validate image presence
        if not itemImage:
            return render(request, 'foundform.html', {'error': 'Please upload an image of the item.'})

        try:
            # Check image clarity using OpenCV
            image_data = np.frombuffer(itemImage.read(), np.uint8)
            image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

            if image is None:
                return render(request, 'foundform.html', {'error': 'Could not read the image. Please upload a valid image file.'})

            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            score = cv2.Laplacian(gray_image, cv2.CV_64F).var()

            if score < 100:
                return render(request, 'foundform.html', {
                    'error': f"Image is too blurry (sharpness score: {score:.1f}). Please upload a clearer photo."
                })

            # Reset file pointer after reading
            itemImage.seek(0)

        except Exception as e:
            return render(request, 'foundform.html', {'error': f'Image processing error: {str(e)}'})

        # Store the item
        Itemdetails.objects.create(
            user=request.user,
            itemName=itemName,
            itemDescription=itemDescription,
            itemTag=itemTag,
            itemImage=itemImage,
            location=location,
            foundDate=foundDate,
            phoneNo=phoneNo,
        )

        return render(request, 'foundform.html', {'success': 'Item reported successfully! Thank you for helping the community.'})

    return render(request, 'foundform.html')


# ================= Browse All Items =================
def all_items(request):
    items = Itemdetails.objects.all().order_by('-created_at')
    total_items = items.count()
    return render(request, 'items.html', {'items': items, 'total_items': total_items})


# ================= Search Items =================
def search_items(request):
    name = request.GET.get('name', '').strip()
    location = request.GET.get('location', '').strip()

    if not name and not location:
        return redirect('items')

    filters = Q()
    if name:
        filters |= Q(itemName__icontains=name)
    if location:
        filters |= Q(location__icontains=location)

    items = Itemdetails.objects.filter(filters).order_by('-created_at')
    total_items = items.count()

    return render(request, 'items.html', {
        'items': items,
        'total_items': total_items,
        'search_query': name,
        'location_query': location,
    })


# ================= Services Page =================
def services_view(request):
    return render(request, 'services.html')


# ================= About Page =================
def about_view(request):
    return render(request, 'about.html')


# ================= Register =================
def register_views(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if not username or not email or not password:
            return render(request, "register.html", {"register_error": "All fields are required."})

        if password != password2:
            return render(request, "register.html", {"register_error": "Passwords do not match."})

        if len(password) < 6:
            return render(request, "register.html", {"register_error": "Password must be at least 6 characters."})

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"register_error": "Username already exists."})

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"register_error": "Email already registered."})

        User.objects.create_user(username=username, email=email, password=password)
        return redirect("login")

    return render(request, "register.html")


# ================= Login =================
def login_views(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            return render(request, "login.html", {"error": "Username not found."})

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)

        return render(request, "login.html", {"error": "Incorrect password."})

    return render(request, "login.html")


# ================= Logout =================
def logout_views(request):
    logout(request)
    return redirect('home')