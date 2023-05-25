from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from website.models import Menu
from website.forms import ContactForm
from django.contrib import messages

# Create your views here.
def index_view(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        family_name = request.POST.get('family_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, family_name, email)

        form = ContactForm(request.POST)
        # if form.is_valid():
        form.save()
    
    menu = Menu.objects.order_by('-price')
    context = {'menu': menu}

    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html')

def menu_view(request):
    menu = Menu.objects.order_by('-price')
    context = {'menu': menu}
    return render(request, 'menu.html', context)

# def contact_view(request):
#     print("Gorbe")
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, 'Your Ticket Submited Successfully. Thank You!')
#         else: 
#             messages.add_message(request, messages.ERROR, 'Ooops! Your Ticket Didnt Submit.')
    
#     return render(request, 'index.html', {})  
        # form = ContactForm() 
    # return render(request, 'index.html', {'form': form})

def test_view(request):

    return render(request, 'test.html', {})
