from main.models import Xodimlar, Davomat
from main import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required()
def XodimlarList(request):
    xodimlar = Xodimlar.objects.all()
    return render(request, 'dashboard/xodim/xodimlar_list.html', {'xodimlar': xodimlar})

@login_required()
def XodimlarCreate(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name') 

        if not full_name: 
            return render(request, 'dashboard/xodim/xodimlar_create.html', {
                'error': "Full name field cannot be empty"
            })
        
        xodimlar = Xodimlar(
            full_name=full_name,
            phone=request.POST.get('phone', ''), 
            email=request.POST.get('email', ''),
            address=request.POST.get('address', ''),
            is_staff=bool(request.POST.get('is_staff', False))
        )
        xodimlar.save()
        return redirect('xodimlar_list') 
    return render(request, 'dashboard/xodim/xodimlar_create.html')

@login_required()
def XodimlarUpdate(request, id):
    xodimlar = models.Xodimlar.objects.get(id=id)
    if request.method == 'POST': 
        full_name = request.POST.get('full_name') 

        if not full_name: 
            return render(request, 'dashboard/xodim/xodimlar_update.html', {
                'xodimlar': xodimlar,
                'error': "Full name field cannot be empty"
            })
        
        xodimlar.full_name = full_name
        xodimlar.phone = request.POST.get('phone', '') 
        xodimlar.email = request.POST.get('email', '')
        xodimlar.address = request.POST.get('address', '')
        xodimlar.is_staff = bool(request.POST.get('is_staff', False))
        xodimlar.save()
        return redirect('xodimlar_list')
    return render(request, 'dashboard/xodim/xodimlar_update.html', {'xodimlar': xodimlar})

@login_required()
def XodimlarDelete(request, id):
    xodimlar = models.Xodimlar.objects.get(id=id)
    
    if request.method == 'POST':
        xodimlar.delete()
        return redirect('xodimlar_list')

    
    return render(request, 'dashboard/xodim/xodimlar_delete.html', {'xodimlar': xodimlar})

    

    




