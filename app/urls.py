
from django.urls import path
from .views import home_views,Foundform,register_views,login_views,logout_views
urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("",include("app.urls"))
    path("",home_views,name="home"),
    path("foundform/",Foundform,name="foundform"),
    path('register/', register_views, name='register'),
    path('login/', login_views, name='login'),
    path('logout/', logout_views, name='logout'),
]