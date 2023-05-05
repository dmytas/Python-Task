from django.shortcuts import render, redirect
from .forms import EmployeeForm


def register_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()

            return redirect('menu')
    else:
        form = EmployeeForm()

    return render(request, 'register_employee.html', {'form': form})


def home(request):
    return render(request, 'home.html')
