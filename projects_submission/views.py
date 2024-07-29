from django.shortcuts import render , redirect
from .forms import StudentForm

def project_submission(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_success')
    else:
        form = StudentForm()
    return render(request, 'project_form.html', {'form': form})
