import datetime
from operator import truediv
from todolist.models import Task
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='login/')
def show_todolist(request):
    data_user = Task.objects.filter(user=request.user)
    context = {
        'data': data_user,
        'username': request.user
    }
    return render(request,'todolist.html',context)

def create_new_todolist(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        add_todolist = Task(
            user = request.user,
            title = title,
            description = description,

        )
        add_todolist.save()
        return redirect('todolist:show_todolist')
    return render(request, 'addtodolist.html')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)    

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def delete_task(request,id):
    if request.method == "DELETE":
        task = Task.objects.filter(id=id)
        task.delete()
    return JsonResponse({"var":"todo"})

def ganti_status(request,id):
    task = Task.objects.filter(user=request.user).get(pk=id)
    if(task.status=="0"):
        task.status = "1"
        task.save()
    else:
        task.status = "0"
        task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='login/')
def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', task), content_type='application/json')

@login_required(login_url='login/')
def post_json(request):
    if request.method == "POST":
        add_todolist = Task(
            title = request.POST.get('todo'),
            description = request.POST.get('desc'),
            user = request.user,
            date = datetime.datetime.now(),
            status = False
        )
        add_todolist.save()
    return JsonResponse({"var" : "todolist"})



