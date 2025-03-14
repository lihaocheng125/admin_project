以下是为你完善后的 `README.md` 文件，补充了更多详细信息，让项目介绍更加全面：

# 学途共享

## 项目简介
“学途共享” 是一个基于 Django 框架开发的教学项目管理平台。该平台旨在为教师和学生提供一个便捷、高效的项目管理与交流的环境。教师可以通过平台实时了解学生的项目参与情况，包括登录时间、时长等，同时还能以图表和表格的形式直观查看学生信息和项目提交情况。学生则可以通过平台提交自己的项目，参与到教学项目管理的流程中。

## 项目功能

### 注册与登录
- 提供用户注册和登录功能，区分教师和学生两种角色。不同角色登录后将进入不同的功能页面。

### 教师功能
- **学生项目参与情况监控**：教师可以在后台查看每个学生提交项目的登录时间和时长，了解学生参与项目的积极性和投入度。
- **数据可视化**：通过图表形式直观展示学生的项目参与数据，帮助教师快速把握整体情况。
- **学生信息与项目管理**：将学生的姓名、学号和上传的项目信息整理成表格，方便教师查看和管理。
- **项目统计**：教师可以查看学生提交的项目总数，了解项目的整体进度。

### 学生功能
- **项目提交**：学生可以登录平台，提交自己的项目，方便教师进行审核和管理。

## 项目特点
- **角色分明**：清晰区分教师和学生两种角色，为不同角色提供针对性的功能，提高使用效率。
- **数据可视化**：通过图表展示学生项目参与数据，使教师能够更直观地了解学生情况，做出更科学的决策。
- **便捷管理**：以表格形式呈现学生信息和项目信息，方便教师进行查看、筛选和管理。

## 安装指南

### 环境要求
- **操作系统**：支持 Windows、Linux、macOS 等主流操作系统。
- **编程语言**：Python 3.7 及以上版本。
- **数据库**：建议使用 MySQL 或 SQLite 数据库。
- **其他依赖**：项目依赖的 Python 库可以通过 `requirements.txt` 文件进行安装。

### 安装步骤
1. **克隆项目仓库**：
```bash
git clone https://github.com/lihaocheng125/admin_project.git
```
2. **进入项目目录**：
```bash
cd admin_project
```
3. **创建并激活虚拟环境（可选但推荐）**：
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
.\venv\Scripts\activate
4. **安装项目依赖**：
```bash
pip install -r requirements.txt
```
5. **配置数据库**：
打开项目的 `settings.py` 文件，配置数据库连接信息。使用 SQLite 数据库：
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
6. **执行数据库迁移**：
```bash
python manage.py makemigrations
python manage.py migrate
```
7. **创建超级用户（可选）**：
```bash
python manage.py createsuperuser
```
按照提示输入用户名、邮箱和密码，用于登录 Django 管理后台。

## 使用方法

### 启动项目
```bash
python manage.py runserver
```
在浏览器中访问 `http://127.0.0.1:8000`，即可进入项目登录页面。

### 教师使用
- 教师使用注册的账号登录后，进入教师功能页面。
- 在后台页面中查看学生的项目登录时间、时长等信息。
- 查看图表和表格，了解学生信息和项目提交情况。

### 学生使用
- 学生使用注册的账号登录后，进入学生功能页面。
- 在页面中提交自己的项目。

## 项目结构
```
project-root/
├── manage.py             # Django 项目管理脚本
├── admin_project/    # 项目主目录
│   ├── __init__.py
│   ├── settings.py       # 项目配置文件
│   ├── urls.py           # 项目 URL 配置文件
│   ├── wsgi.py           # WSGI 配置文件
├── user_app/             # 应用程序目录
│   ├── migrations/       # 数据库迁移文件
│   ├── templates/        # 模板文件目录
│   ├── static/           # 静态文件目录
│   ├── __init__.py
│   ├── admin.py          # 管理后台配置文件
│   ├── apps.py           # 应用程序配置文件
│   ├── models.py         # 数据模型文件
│   ├── tests.py          # 测试文件
│   ├── urls.py           # 应用程序 URL 配置文件
│   ├── views.py          # 视图函数文件
├── requirements.txt      # 项目依赖文件
├── README.md             # 项目说明文件
```
