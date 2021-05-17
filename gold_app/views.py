from django.shortcuts import render,redirect
from time import localtime, strftime
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'activities' not in request.session:
        request.session['activities']=[]
        
    context = {
            "activities":request.session['activities']
    }    
    return render(request, 'index.html', context)
    
def process_gold(request):
    if request.method == "POST":
        place = request.POST['place']
        gold = request.session['gold']
        activities = request.session['activities']
        date_time = strftime("%B %d, %Y %H:%M %p", localtime())
        
        
        if place == "farm":
            current_gold = random.randint(10,20)
            gold += current_gold 
            request.session['gold'] = gold
            request.session.modified = True
            
        if place == "cave":
            current_gold= random.randint(5,10)
            gold += current_gold 
            request.session['gold'] = gold 
            request.session.modified = True
            
            
        if place == "house":
            current_gold = random.randint(2,5)
            gold += current_gold 
            request.session['gold'] = gold 
            request.session.modified = True

        if place == "casino":
            current_gold = random.randint(-50,50)
            winOrLose = current_gold
            if current_gold >= 0:
                winOrLose = "green"
            else:
                winOrLose = "red"    
                
            
            gold += current_gold
            request.session['gold'] = gold 
            request.session.modified = True     
            
        if current_gold >= 0:
            print = f"Earned {current_gold} golds from the {place} {date_time}"
            
        else:
            print = f"Entered a casino and lost {current_gold} from the {place} {date_time}"
            
                
            
        activities.append(print)
        request.session['activities'] = activities         
            
    return redirect("/")    
            
        
def reset(request):
    if request.method =="POST":
        if 'reset' in request.POST:
            request.session.flush()
    return redirect("/")    
        
               

        
            
              
            
        
        
                   
        
            
    

      
    
            
        
            
            
    
        
        
            
            
            
