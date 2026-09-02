
from django.urls import path
from .views import home_views
urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("",include("app.urls"))
    path("",home_views,name="home")
]