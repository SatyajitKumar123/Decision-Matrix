from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm
from .services import calculate_pyramid_data

@login_required
def dashboard(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    
    # Fetch Data
    tasks = Task.objects.filter(user=request.user)
    
    # Handle the "Total Time" input (Default to 8 hours if not specified)
    try:
        total_hours = float(request.GET.get('hours', 8))
    except ValueError:
        total_hours = 8.0
        
    # Run the Math Engine (Service Layer)
    pyramid_tasks = calculate_pyramid_data(tasks, total_daily_hours=total_hours)

    context = {
        'form': form,
        'tasks': tasks,
        'pyramid_tasks': pyramid_tasks,
        'total_hours': total_hours,
    }
    
    return render(request, 'core/dashboard.html', context)