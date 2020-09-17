from django import forms
from .models import prediction_new,prediction_archive_new




class PredForm(forms.Form):
    FILTER_CHOICES= [
  ('Chennai Super Kings','Chennai Super Kings'),
('Delhi Capitals','Delhi Capitals'),
('Kings XI Punjab','Kings XI Punjab'),
('Kolkata Knight Riders','Kolkata Knight Riders'),
('Mumbai Indians','Mumbai Indians'),
('Royal Challengers Bangalore','Royal Challengers Bangalore'),
('Rajasthan Royals','Rajasthan Royals'),
('Sunrisers Hyderabad','Sunrisers Hyderabad'),
    ]

    name = forms.CharField(label='name', max_length=100 ,required=True)
    email = forms.CharField(label='email', max_length=100,required=True)
    team_name=forms.ChoiceField(choices = FILTER_CHOICES)
    player_name=forms.CharField(label='player_name', max_length=100,required=True)


    def clean(self):
        cleaned_data = self.cleaned_data
        name1=self.cleaned_data['name']
        email1=self.cleaned_data['email']
        # team_name=self.clened_data['team_name']
        # player_name=self.cleaned_data['player_name']
        for instance in prediction_new.objects.all():
            if (instance.name==name1):
                raise forms.ValidationError(name1+" already Predicted")
            elif (instance.email==email1):
                raise forms.ValidationError(email1+" already Predicted")
        
            # elif (name1==""):
            #     raise forms.ValidationError("Fill all the fields")
            # elif (email1==""):
            #     raise forms.ValidationError("Fill all the fields")
            # elif (team_name==""):
            #     raise forms.ValidationError("Fill all the fields")
            # elif (player_name==""):
            #     raise forms.ValidationError("Fill all the fields")
     
        # if email and prediction_new.objects.get(email=email):
        #     raise forms.ValidationError(email+" already Predicted")
        return cleaned_data
    # def clean_name(self):
    #     cleaned_data = self.cleaned_data
    #     if self.cleaned_data['name'].strip() == '':
    #         raise forms.ValidationError('field cannot be blank!')
    #     return cleaned_data['name']  
    #     for instance in prediction_new.objects.all():
    # 		if (instance.name==name):
    #             raise forms.ValidationError(name + ' is already added'
    #     return name
    #     # match=prediction_new.objects.get(name=name)
    #     # if(match):
            
    #     #     raise forms.ValidationError(name +" already exists")
    #     # else:
    #     #     return name
    # def clean_email(self):
        
    #     email=self.cleaned_data['email']
    #     for instance in prediction_new.objects.all():
    #         if (instance.email == email):
    #             raise forms.ValidationError(email + ' is already added')
	#     return email
       
        # match_e=prediction_new.objects.get(email=email)
        # if(match_e):
            
        #     raise forms.ValidationError(email+" already exists")
        # else:
        #     return email





    


