from django.shortcuts import render , redirect
from .forms import SlotForm
from .models import bookSlot

# Create your views here.
def index(request):
    return render(request,'index.html')

def bookSlot(request):
    if request.method == 'POST':
        form = SlotForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('index')
    
    else:
        return render(request,'bookSlot.html')
    
    return render(request,'bookSlot.html')