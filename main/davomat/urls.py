from django.urls import path
from . import views

urlpatterns = [
    path('davomat/', views.davomat_list, name='davomat_list'),
    path('davomat_create/', views.davomat_create, name='davomat_create'),
    path('davomat_delete/<int:id>/', views.davomat_delete, name='davomat_delete'),
]
