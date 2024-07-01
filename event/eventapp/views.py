from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import CustSignUpForm,HostSignUpForm,EventForm,TicketInformationForm
from .models import Record_cust,Record_host,Event
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html',{})


def login_cust(request):
	# Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('customer_login')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('customer_login')
    else:
        return render(request, 'cust_login.html', {})


def login_host(request):
    events = Event.objects.all()
    host = Record_host.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('host_login')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('host_login')
    else:
        return render(request, 'host_login.html', {'events':events,'host':host})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')
    

def register_cust(request):
    if request.method == 'POST':
        form = CustSignUpForm(request.POST)
        if form.is_valid():
            #gets the information from the form
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            city = form.cleaned_data.get('city')

            Record_cust.objects.create(
                username=username, 
                email=email, 
                first_name=first_name, 
                last_name=last_name, 
                phone=phone, 
                gender=gender,
                city=city,
                
            )
            
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('customer_login')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustSignUpForm()
    return render(request, 'register.html', {'form': form})


def register_host(request):
    if request.method == 'POST':
        form = HostSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            city = form.cleaned_data.get('city')
            organisation = form.cleaned_data.get('organisation')
            university = form.cleaned_data.get('university')
            
            # Create and save the user's profile
            Record_host.objects.create(
                username=username, 
                email=email, 
                first_name=first_name, 
                last_name=last_name, 
                phone=phone, 
                gender=gender,
                city=city,
                organisation=organisation,
                university=university
            )
            
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('host_login')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = HostSignUpForm()
    return render(request, 'register2.html', {'form': form})
    

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False) # Assign current user as the host
            event.save()
            # Redirect to ticket information form with event_id in URL
            return redirect('ticket_information', event_id=event.id)
    else:
        form = EventForm()
    
    return render(request, 'event_form.html', {'form': form})


def ticket_information(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        ticket_form = TicketInformationForm(request.POST)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
             # Assign the event to the ticket
            ticket.save()
            # Create and save the user's profile
            # Record_host.objects.create(
            #     username = ticket_form.cleaned_data.get('Location')
            #     email = form.cleaned_data.get('Contact')
            #     first_name = form.cleaned_data.get('Last Date')
            #     last_name = form.cleaned_data.get('Price')
                
            # )
            return redirect('host_login')  # Redirect to success page after saving ticket info
    else:
        ticket_form = TicketInformationForm()

    return render(request, 'ticket.html', {'ticket_form': ticket_form, 'event_id': event.id})
