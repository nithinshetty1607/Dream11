from django.shortcuts import render
from .models import prediction

# Create your views here.


def home(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        player_name=request.POST['player_name']
        
        pred=prediction(name=name,email=email,player_name=player_name)
        pred.save()
        return render(request,'dummy.html')
    else:
        return render(request,'home.html')
