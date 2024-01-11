from django.shortcuts import render
from CoffeApp.models import menu
from CoffeApp.models import contact1
from django.contrib import messages
from math import ceil

# Create your views here.
def coffee(request):
    return render(request,"coffeeApp/index.html")
def base(request):
    return render(request,"coffeeApp/base.html")
def copy(request):
    return render(request,"coffeeApp/copy.html")
def menus(request):
    allProds=[]                                            
    menuitems=menu.objects.values('category','id')       
    cats={item['category'] for item in menuitems}                                       
    for cat in cats:    
        prod = menu.objects.filter(category=cat)
        n=len(prod)
        nSlides=n // 4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params= {"allProds": allProds}
    return render(request,"coffeeApp/menu.html", params)

def checkout(request):
    return render(request,"coffeeApp/checkout.html")
def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        emailID=request.POST.get("email") 
        desc=request.POST.get("desc")
        phone=request.POST.get("phone")

        myquery=contact1(name=name, emailID=emailID, desc=desc, phone=phone)
        myquery.save()
        messages.info(request,"We Will get back with you soon...")
    return render(request,"coffeeApp/contact.html")
