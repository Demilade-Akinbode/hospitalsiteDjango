from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

def index(request):
    if request.method == "POST":
        doctor_select = request.POST['info_form_doc']
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']

        appointment_details = "NAME: " + your_name + "\n" + "PHONE NO: " + your_phone + "\n" + "EMAIL: " + your_email + "\n" + "SCHEDULE: " + your_schedule + "\n" + "PREFERRED DATE: " + your_date    
      
        #send an email
        send_mail(
            'Appointment for Doctor: ' + doctor_select , #subject
            appointment_details, #message
            your_email, #email from
            ['demiladeakinbode@gmail.com'], # to email
        ) 
        
        return render(request, 'hpms_temp/appointment.html', {'title' : 'Appointment', 
        'doctor_select': doctor_select, 
        'your_name' : your_name,
        'your_phone': your_phone,
        'your_email': your_email,
        'your_schedule': your_schedule,
        'your_date': your_date})
    else:
        return render(request, 'hpms_temp/index.html')


def about(request):
        return render(request, 'hpms_temp/about.html', {'title' : 'About'})

def contact(request):
    if request.method == "POST":
        contact_name= request.POST['contact-name']
        contact_email= request.POST['contact-email']
        contact_message= request.POST['contact-message']
        messages.success(request, f'Your message has been sent! We will contact you shortly..')

        #send an email
        send_mail(
            'Contact message from ' + contact_name , #subject
            contact_message, #message
            contact_email, #email from
            ['demiladeakinbode@gmail.com'], # to email
        )

        return render(request, 'hpms_temp/contact.html', {'title' : 'Contact Us', 'contact_name': contact_name})
    else:
        return render(request, 'hpms_temp/contact.html', {'title' : 'Contact Us'})

def services(request):
    if request.method == "POST":
        doctor_select = request.POST['info_form_doc']
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']

        appointment_details = "NAME: " + your_name + "\n" + "PHONE NO: " + your_phone + "\n" + "EMAIL: " + your_email + "\n" + "SCHEDULE: " + your_schedule + "\n" + "PREFERRED DATE: " + your_date    
      
        #send an email
        send_mail(
            'Appointment for Doctor: ' + doctor_select , #subject
            appointment_details, #message
            your_email, #email from
            ['demiladeakinbode@gmail.com'], # to email
        ) 
        
        return render(request, 'hpms_temp/appointment.html', {'title' : 'Appointment', 
        'doctor_select': doctor_select, 
        'your_name' : your_name,
        'your_phone': your_phone,
        'your_email': your_email,
        'your_schedule': your_schedule,
        'your_date': your_date})
    else:
        return render(request, 'hpms_temp/services.html', {'title' : 'Our Services'})

def appointment(request):
    if request.method == "POST":
        doctor_select = request.POST['info_form_doc']
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']

        appointment_details = "NAME: " + your_name + "\n" + "PHONE NO: " + your_phone + "\n" + "EMAIL: " + your_email + "\n" + "SCHEDULE: " + your_schedule + "\n" + "PREFERRED DATE: " + your_date    
      
        #send an email
        send_mail(
            'Appointment for Doctor: ' + doctor_select , #subject
            appointment_details, #message
            your_email, #email from
            ['demiladeakinbode@gmail.com'], # to email
        ) 

        return render(request, 'hpms_temp/appointment.html', {'title' : 'Appointment', 
        'doctor_select': doctor_select, 
        'your_name' : your_name,
        'your_phone': your_phone,
        'your_email': your_email,
        'your_schedule': your_schedule,
        'your_date': your_date})
    else:
        return render(request, 'hpms_temp/index.html', {'title' : 'Appointment'})
    