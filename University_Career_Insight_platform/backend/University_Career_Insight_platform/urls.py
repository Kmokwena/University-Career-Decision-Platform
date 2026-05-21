"""
URL configuration for University_Career_Insight_platform project.

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

from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from bursary.views import BursaryViewSet
from universities.views import UnviersityViewSet
from qualification.views import QualificationViewSet
from career.views import CareerViewSet

router = DefaultRouter()
router.register(r'bursaries', BursaryViewSet)
router.register(r'universities', UnviersityViewSet)
router.register(r'qualification', QualificationViewSet)
router.register(r'career', CareerViewSet)



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.homepage),
    path('about/', views.about),
    path('api/', include(router.urls)),
    
]
