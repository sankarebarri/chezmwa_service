from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contacts(request):
    # This shoud be house id generated
    # generate_house_code
    house_id = request.GET.get('neighborhood_list')
    name = ""
    email = ""
    telephone = 0
    message = ""
    if request.method == "POST":
        name = request.POST['name']
        if house_id:
            house_id = house_id
        email = request.POST['email']
        telephone = request.POST['telephone']
        message = request.POST['message']

        contact = Contact(name=name, email=email, telephone=telephone, message=message)
        contact.save()

    send_mail(
        f'Property Listing Inquiry from {name}', #Subject
        f'There has been an inquiry for a listing id:{house_id}, message:{message}', #Message
        'email', #Sender e-mail
        ['mathservant@gmail.com'], #Reciever e-mail
        fail_silently=False
    )

    messages.success(request, 'Your request has been successfully submitted. We will get back to you soon. Thanks')
    return render(request, 'contacts/contacts.html')
