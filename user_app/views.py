from django.shortcuts import render,redirect
from django.db.models import Count
from .models import CustomUser
import json
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser, Project
import re
from django.utils import timezone
from django.db.models import Count
import matplotlib.pyplot as plt
import io
import base64
from django.views.decorators.csrf import csrf_exempt
import logging

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 验证账号格式
        if not re.match(r'^0\d{7}$|^\d{12}$', username):
            messages.error(request, '账号格式错误，必须是 8 位以 0 开头或 12 位数字。')
            return redirect('register')

        # 验证密码格式
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
            messages.error(request, '密码必须包含字母和数字，且长度不少于 8 位。')
            return redirect('register')

        # 判断账号类型
        if username.startswith('0'):
            account_type = 'teacher'
        else:
            account_type = 'student'

        try:
            CustomUser.objects.create_user(username=username, password=password, account_type=account_type)
            messages.success(request, '注册成功，请登录。')
            return redirect('login')
        except:
            messages.error(request, '注册失败，请重试。')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.account_type == 'teacher':
                return redirect('admin_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            messages.error(request, '账号或密码错误。')

    return render(request, 'login.html')

def admin_dashboard(request):
    # 检查用户是否已认证且为教师类型，如果不是则重定向到登录页面
    if not request.user.is_authenticated or request.user.account_type != 'teacher':
        return redirect('login')

    students = CustomUser.objects.filter(account_type='student')

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # 解析日期并处理日期格式错误
    if start_date:
        start_date = parse_date(start_date)
        if not start_date:
            return JsonResponse({'error': 'Invalid start date format'}, status=400)
    if end_date:
        end_date = parse_date(end_date)
        if not end_date:
            return JsonResponse({'error': 'Invalid end date format'}, status=400)

    if start_date and end_date:
        daily_counts = CustomUser.objects.filter(
            account_type='student',
            last_login_time__range=[start_date, end_date]
        ).annotate(
            date=Count('last_login_time__date')
        ).values('last_login_time__date', 'date')
    else:
        daily_counts = CustomUser.objects.filter(account_type='student').annotate(
            date=Count('last_login_time__date')
        ).values('last_login_time__date', 'date')

    labels = [str(entry['last_login_time__date']) for entry in daily_counts]
    data = [entry['date'] for entry in daily_counts]

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'labels': labels, 'data': data})

    return render(request, 'admin_dashboard.html', {
       'students': students
    })

def student_dashboard(request):
    if not request.user.is_authenticated or request.user.account_type != 'student':
        return redirect('login')

    user_projects = Project.objects.filter(user=request.user)
    return render(request, 'student_dashboard.html', {'user_projects': user_projects})

def upload_project(request):
    if not request.user.is_authenticated or request.user.account_type != 'student':
        return redirect('login')

    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        project_file = request.FILES.get('project_file')

        Project.objects.create(user=request.user, project_name=project_name, project_file=project_file)
        return redirect('student_dashboard')

    return render(request, 'upload_project.html')

logger = logging.getLogger(__name__)
@csrf_exempt
def save_student_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user = request.user
        user.name = name
        user.save()
        logger.info(f"用户 {user.username} 的姓名已更新为 {name}")
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})