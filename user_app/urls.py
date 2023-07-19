from django.urls import path
from .views import Log_in, Log_out, Sign_Up, Info

urlpatterns = [
    path('signup/', Sign_Up.as_view(), name='signup'),
    path('login/', Log_in.as_view(), name="login"),
    path("logout/", Log_out.as_view(), name="logout"),
    path("info/", Info.as_view(), name="info"),
]
