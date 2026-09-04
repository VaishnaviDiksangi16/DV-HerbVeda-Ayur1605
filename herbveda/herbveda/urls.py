"""
URL configuration for herbveda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
# herbveda/urls.py
from django.contrib import admin
from django.urls import path
from herbs import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Welcome page (home)
    path('', views.welcome, name='welcome'),

    # Example other pages (keep your current app structure)
    path('quiz/', views.quiz_page, name='quiz'),          # you can create this view
    path('granny/', views.granny_page, name='granny'),    # you can create this view
    path('herb/<int:id>/', views.herb_detail, name='herb_detail'),  # your existing herb detail page
    path('explore/', views.herb_list, name='herb_list'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('granny-chat/', views.granny_chat, name='granny_chat'),
    
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)