"""helloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse
import math

def rootRouteHandler(request):
    response = HttpResponse("<h1>Welcome!</h1>")
    return response

def rectangle_area(request, height, width):
    # height * width
    response = HttpResponse(f"<h1>The area of a rectangle with a height: {height} and length: {width} equals {height * width}</h1>")
    return response
    # 400 = bad request

def rectangle_perimeter(request, height, width):
    # 2 (height * width)
    response = HttpResponse(f"<h1>The perimeter of a rectangle with a height: {height} and width: {width} equals {2 * (height + width)}</h1>")
    return response

def circle_area(request, radius):
    # pi (radius ** 2)
    response = HttpResponse(f"<h1>The area of a circle with a radius: {radius} equals {math.pi * radius ** 2}</h1>")
    return response

def circle_perimeter(request, radius):
    # 2 * pi * radius
    response = HttpResponse(f"<h1>The perimeter of a circle with a radius: {radius} equals {math.pi * 2 * radius}</h1>")
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rootRouteHandler),
    path('rectangle/area/<int:height>/<int:width>/', rectangle_area),
    path('rectangle/perimeter/<int:height>/<int:width>/', rectangle_perimeter),
    path('circle/area/<int:radius>/', circle_area),
    path('circle/perimeter/<int:radius>/', circle_perimeter),
]
