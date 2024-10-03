from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm, cfCaptchaForm
from patients.models import Patient, PatientDetail, LabData
from django.core.management import call_command
from login_required import login_not_required

# Production
@login_not_required
def home(request):
    if request.method == 'POST':
        form = cfCaptchaForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None and form.is_valid():
            login(request, user)
            print('VALID')
            messages.success(request, ("Pomyślnie zalogowany"))
            return redirect('home')

        else:
            print('INVALID')
            messages.success(request, ("Błąd logowania, proszę spróbować jeszcze raz"))
            return redirect('home')   
    else:
        return render(request, 'home.html', {
        'patient': Patient.objects.all().order_by('-date', '-hcc_number'),
        'patient_details':PatientDetail.objects.all(),
        'patient_lab':LabData.objects.all(),
        'patient_count':Patient.objects.all().count(),
        'cfcaptcha_form': cfCaptchaForm()
        })

def logout_user(request):
        logout(request)
        messages.success(request, ("Pomyślnie wylogowany"))
        return redirect('home')    


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Log in
            user = authenticate(request, username=username, password=password)
            login(request, user)
            print('VALID')
            messages.success(request, ("Pomyślnie zarejestrowany"))
            return redirect('list-user')
        else:
            print('INVALID')
            messages.success(request, ("Błąd w rejestracji, proszę spróbować jeszcze raz"))
            return redirect('register-user')  
    else:
        return render(request, 'register_user.html', {'form':form})

def update_user(request, user_id):
    if request.user.is_authenticated:
        users = User.objects.get(pk=user_id)

        users_form = SignUpForm(request.POST or None, instance=users)
        if users_form.is_valid():
            users_form.save()
            messages.success(request, ("Twój Profil został zaktualizowany"))
            return redirect('list-user')

        users_form = SignUpForm(instance=users)
        return render(request, 'update_user.html', {'user_form':users_form})
    else:
        messages.success(request, ("Musisz się zalogować..."))
        return redirect('home')


def delete_user(request, user_id):
    if request.user.is_authenticated:
        users = User.objects.get(pk=user_id)

        users.delete()
        messages.success(request, ("Usunięto pomyślnie"))
        return redirect('list-user')
    else:
        messages.success(request, ("Musisz się zalogować..."))
        return redirect('home')


def list_user(request):
    if request.user.is_authenticated:
        users = User.objects.all()

        return render(request, 'list_user.html', {'users':users})
    else:
        messages.success(request, ("Musisz się zalogować..."))
        return redirect('home')
    
def trial(request):
    if request.user.is_authenticated:
        call_command('dbbackup')
        messages.success(request, ("Backup zrobiony pomyślnie"))
        return redirect('home')
    else:
        messages.success(request, ("Musisz się zalogować..."))
        return redirect('home')