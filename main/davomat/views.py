from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Davomat, Xodimlar

@login_required()
def davomat_list(request):
    davomat = Davomat.objects.all()
    xodimlar = Xodimlar.objects.all()
    return render(request, 'dashboard/davomat/davomat_list.html', {'davomat': davomat, 'xodimlar': xodimlar})

def davomat_create(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        xodim = Xodimlar.objects.get(id=id)
        Davomat.objects.create(xodim=xodim)
        return redirect('davomat_list') 
    
    

@login_required()
def davomat_delete(request, id):
    try:
        davomat = Davomat.objects.get(id=id)
    except Davomat.DoesNotExist:
        return redirect('davomat_list')  

    if request.method == 'POST':
        davomat.delete()
        return redirect('davomat_list')

    return render(request, 'dashboard/davomat/davomat_confirm_delete.html', {'davomat': davomat})
