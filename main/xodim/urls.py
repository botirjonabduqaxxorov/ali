from main.xodim import views
from django.urls import path

urlpatterns = [
    path('xodimlar_list/', views.XodimlarList, name = 'xodimlar_list' ),
    path('xodimlar_create/', views.XodimlarCreate, name = 'xodimlar_create' ),
    path('xodimlar_update/<int:id>/', views.XodimlarUpdate, name = 'xodimlar_update' ),
    path('xodimlar_delete/<int:id>/', views.XodimlarDelete, name = 'xodimlar_delete' ),
]