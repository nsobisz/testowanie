"""
URL configuration for testproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


def division_by_zero(request):
   division_by_zero = 1 / 0
   
def not_supported(request):
    wrong_type = "sf" / "sf"

def non_exist_variable(request):
    print(x)

def no_return(request):
    print("hi")

def no_8_table(request):
    tab = [1,2,3]
    return tab[8]

def no_lib(request):
    import dupa



urlpatterns = [
    path('admin/', admin.site.urls),
    path('sentry-debug/', no_return),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

