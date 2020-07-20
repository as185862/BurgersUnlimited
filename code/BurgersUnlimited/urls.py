"""BurgersUnlimited URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_v

from burger import views
from users import views as user_v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('burger/', include('burger.urls'), name='main-burger'),
    path('', RedirectView.as_view(url='burger/')),
    path('Register/', user_v.register, name='Register'),
    path('login/', auth_v.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_v.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    ] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
