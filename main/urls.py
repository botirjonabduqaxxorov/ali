from django.urls import path, include
from . import views
from .views import register_view, login_user, logout_user, home_view

urlpatterns = [
    path('base/', views.base, name='base'),
    path('xodim/', include('main.xodim.urls'), name='xodim'),
    path('davomat/', include('main.davomat.urls'), name='davomat'),
    path('register/', register_view, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', home_view, name='home'),
]   