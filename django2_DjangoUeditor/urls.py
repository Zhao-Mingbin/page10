"""django2_DjangoUeditor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import os

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django2_DjangoUeditor import settings
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('', views.home,name='主页'),
    path('base/', views.base, name='基础'),
    path('intro/', views.intro, name='研究方向'),
    path('news/',include('blog.urls')),
    path('knews/',include('blog.urlsknews')),
    path('aboutus/',views.aboutus,name='联系我们'),
    path('results/',views.results,name='研究成果'),
    path('members/',include('blog.urlsmembers')),

]

if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=media_root)