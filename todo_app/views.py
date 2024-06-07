from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from .models import Task, Course
from .forms import TaskForm, CreateTaskForm, UpdateTaskForm, CreateCoursekForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def hello_world(request):
    return HttpResponse('Hola mundo')

def about(request):
    return HttpResponse("""
    <h1>Sobre Django</h1>
    <p>asodk oasdm oaskm kolasmd lkasm lksamd lkasmdl mask</p>                 
    """)

def json_tasks(request):
    tasks = list(Task.objects.values())
    return JsonResponse(tasks, safe = False)

@login_required
def index(request):
    courses = Course.objects.filter(user = request.user)
    tasks = Task.objects.filter(course__in = courses).order_by('-created_at')
    if request.method == "POST":
        courseId = request.POST['course']
        Task.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            course = Course.objects.get(id = courseId)
        )
        messages.success(request, "Tarea creada exitosamente!")
        return redirect('index')
    else:
        form = CreateTaskForm()
        courses = Course.objects.filter(user = request.user)
        form.fields['course'].queryset = courses
        return render(
            request, 
            'tasks/index.html',
            {
                'form': form,
                'tasks': tasks
            }
        )

    #form = TaskForm()
    # tasks_values = Task.objects.values()
    # print(tasks)
    # print(tasks_values)

@login_required
def update_task(request, task_id):
    #task = Task.objects.get(id = task_id)
    task = get_object_or_404(Task, id = task_id)
    user_courses = request.user.course_set.all()
    if task.course not in user_courses:
        raise Http404
    if request.method == "POST":
        form = UpdateTaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.completed = form.cleaned_data['completed']
            task.course = form.cleaned_data['course']
            task.save()
            messages.success(request, 'Tarea actualizada correctamente!')
            return redirect('index')
    else:
        form = UpdateTaskForm(
            initial = {
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'course': task.course
            }
        )
        form.fields['course'].queryset = user_courses
        return render(
            request,
            'tasks/update_task.html',
            {
                'form': form
            }
        )

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id = task_id)
    user_courses = request.user.course_set.all()
    if task.course not in user_courses:
        raise Http404
    if request.method == 'GET':
        return render(
            request,
            'tasks/delete_task.html',
            {
                'task': task
            }
        )
    else:
        task.delete()
        messages.success(request, 'Tarea eliminada correctamente!')
        return redirect('index')

@login_required
def courses(request):
    courses = Course.objects.filter(user = request.user).order_by('-created_at')
    if request.method == "GET":
        return render(
            request,
            'courses/courses.html',
            {
                'courses': courses,
                'form': CreateCoursekForm()
            }
        )
    else:
        form = CreateCoursekForm(request.POST)
        if form.is_valid():
            Course.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                credits = form.cleaned_data['credits'],
                teacher = form.cleaned_data['teacher'],
                user = request.user
            )
        messages.success(request, 'Curso creado correctamente!')
        return redirect('courses')