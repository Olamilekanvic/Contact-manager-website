from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import Contact, Category
# Create your views here.

def add(request):
    categories = Category.objects.all()

    if request.method == 'GET':
        return render(request, 'contact/add.html', {'categories': categories})

    else:

        category_id = request.POST.get('category')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        city = request.POST.get('city')
        image = request.POST.get('image')

        Contact.objects.create(
            category_id=category_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            zipcode=zipcode,
            city=city,
            image=image,
        )
        return redirect('frontpage')


def edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        contact.category_id = request.POST.get('category')
        contact.first_name = request.POST.get('first_name')
        contact.last_name = request.POST.get('last_name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.address = request.POST.get('address')
        contact.zipcode = request.POST.get('zipcode')
        contact.city = request.POST.get('city')
        contact.image = request.POST.get('image')
        contact.save()
        
        return redirect('frontpage')
    else:    
        return render(request, 'contact/edit.html', {'contact': contact, 'categories': categories})


def delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        contact.delete()

    return redirect('frontpage')        


def casual(request):
    contacts = Contact.objects.filter(category_id=4)
    query = request.GET.get('query', '')
    if query:
        contacts = contacts.filter(
            Q(first_name__icontains=query)
            |
            Q(last_name__icontains=query)
            |
            Q(email__icontains=query)
            |
            Q(phone__icontains=query)
            |
            Q(address__icontains=query)
            |
            Q(zipcode__icontains=query)
            |
            Q(city__icontains=query)
        )
    return render (request, 'contact/casual_detail.html', {'contacts': contacts, 'query': query})



def family(request):
    contacts = Contact.objects.filter(category_id=3)
    query = request.GET.get('query', '')
    if query:
        contacts = contacts.filter(
            Q(first_name__icontains=query)
            |
            Q(last_name__icontains=query)
            |
            Q(email__icontains=query)
            |
            Q(phone__icontains=query)
            |
            Q(address__icontains=query)
            |
            Q(zipcode__icontains=query)
            |
            Q(city__icontains=query)
        )
    return render (request, 'contact/family_detail.html', {'contacts': contacts, 'query': query})


def private(request):
    contacts = Contact.objects.filter(category_id=2)
    query = request.GET.get('query', '')
    if query:
        contacts = contacts.filter(
            Q(first_name__icontains=query)
            |
            Q(last_name__icontains=query)
            |
            Q(email__icontains=query)
            |
            Q(phone__icontains=query)
            |
            Q(address__icontains=query)
            |
            Q(zipcode__icontains=query)
            |
            Q(city__icontains=query)
        )
    return render (request, 'contact/private_detail.html', {'contacts': contacts, 'query': query})


def work(request):
    contacts = Contact.objects.filter(category_id=1)
    query = request.GET.get('query', '')
    if query:
        contacts = contacts.filter(
            Q(first_name__icontains=query)
            |
            Q(last_name__icontains=query)
            |
            Q(email__icontains=query)
            |
            Q(phone__icontains=query)
            |
            Q(address__icontains=query)
            |
            Q(zipcode__icontains=query)
            |
            Q(city__icontains=query)
        )
    return render (request, 'contact/work_detail.html', {'contacts': contacts, 'query': query})
