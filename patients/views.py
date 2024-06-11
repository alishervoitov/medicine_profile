from django.shortcuts import render, redirect

from patients.models import Patient


def register(request):
    print(request.POST)
    user_message: str = ''
    password_message: str = ''
    if request.method == 'POST':
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        phone_number = request.POST.get('phone_number', None)
        gender = request.POST.get('gender', None)
        password = request.POST.get('password', None)
        password1 = request.POST.get('password1', None)
        user: Patient = Patient.objects.filter(phone_number=phone_number)
        if user:
            user_message = 'This phone number is busy'
        else:
            user = Patient.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                gender=gender,
                password=password
            )
            user.set_password(password)
            user.save()
            return redirect('home')