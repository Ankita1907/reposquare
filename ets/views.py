from django.db.models import query
from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth import logout
from .models import Property, Pictures, Contacts
from django.contrib.auth.decorators import login_required


def index(request):
    all_properties = Property.objects.all()
    return render(request, "ets/index.html", {'all_properties':all_properties})




@login_required(login_url='')
def single_landing(request,id):
    property = Property.objects.get(id=id)
    all_images = Pictures.objects.filter(property=property)
    print(all_images)
    return render(request, "ets/single_landing.html", {'property': property, 'all_images':all_images})


def contactus(request):
    message = 'fill proper details. Please Check again'

    if request.method == 'POST':
        
        _name = request.POST.get('name')
        _mail = request.POST.get('mail')
        _address =request.POST.get('address')
        _phone = request.POST.get('phone')
        _altphone = request.POST.get('altphone')
        
        print(_name)
        print(_mail)
        print(_address)
        print(_phone)
        print(_altphone)

        if (_name!="") :

            Contacts.objects.create(name=_name, email=_mail, address=_address, phone=_phone, altphone=_altphone)
            Contacts.save
            return redirect('/')

        elif (_mail!="") :

            Contacts.objects.create(name=_name, email=_mail, address=_address, phone=_phone, altphone=_altphone)
            Contacts.save
            return redirect('/')

        elif (_address!="") :

            Contacts.objects.create(name=_name, email=_mail, address=_address, phone=_phone, altphone=_altphone)
            Contacts.save
            return redirect('/')
        
        elif (_phone!="") :

            Contacts.objects.create(name=_name, email=_mail, address=_address, phone=_phone, altphone=_altphone)
            Contacts.save
            return redirect('/')

        elif (_altphone!="") :

            Contacts.objects.create(name=_name, email=_mail, address=_address, phone=_phone, altphone=_altphone)
            Contacts.save
            return redirect('/')

        else:
            return render(request, 'ets/contactus.html')
            


        

    else:
       return render(request, 'ets/contactus.html')


def search(request):
     query = request.GET['query']
     if len(query)>60:
         all_properties = []
     else:
         all_propertiesname = Property.objects.filter(name__icontains=query)
         all_propertiesdesc = Property.objects.filter(desc__icontains=query)

         all_properties = all_propertiesname.union(all_propertiesdesc)
         all_propertieslocations = Property.objects.filter(locations__icontains=query)
         all_properties = all_properties.union(all_propertieslocations)

     
     return render(request, "ets/search.html", {'all_properties':all_properties, 'query': query})