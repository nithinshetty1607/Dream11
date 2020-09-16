from django.shortcuts import render
from .models import prediction_new,prediction_archive_new
from .forms import PredForm
from django import forms

# Create your views here.
def first(request):
    return render(request,'nav.html')

def home(request):
    if request.method=="POST":
        form=PredForm(request.POST)
        if form.is_valid():
            name={}
            name=request.POST['name']   
            email=request.POST['email']
            team_name=request.POST['team_name']
            player_name=request.POST['player_name']
            
            
            
            pred=prediction_new(name=name,email=email,team_name=team_name,player_name=player_name)
            pred.save()

            return render(request,'dummy.html',context={'form': form,'name':name})
        else:

            print("invalid")
        #     print (form.errors)
            error="filll All The Fields"
            return render(request,'home.html',context={'form': form})

        
    else:
        print("No Post")
        form=PredForm()
    return render(request,'home.html')

