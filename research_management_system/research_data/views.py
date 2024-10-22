from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import ResearchProject, ResearchData
from .forms import ResearchProjectForm, ResearchDataForm

def home(request):
    return render(request, 'home.html')

def research_project_list(request):
    projects = ResearchProject.objects.all()
    return render(request, 'research_data/home.html', {'projects': projects})

def research_project_detail(request, pk):
    project = get_object_or_404(ResearchProject, pk=pk)
    return render(request, 'research_data/project_detail.html', {'project': project})

def upload_data(request, pk):
    project = get_object_or_404(ResearchProject, pk=pk)
    if request.method == "POST":
        form = ResearchDataForm(request.POST, request.FILES)
        if form.is_valid():
            research_data = form.save(commit=False)
            research_data.project = project
            research_data.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ResearchDataForm()
    return render(request, 'research_data/upload_data.html', {'form': form})

