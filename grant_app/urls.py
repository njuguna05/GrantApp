"""grant_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
  https://docs.djangoproject.com/en/3.2/topics/http/urls/

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

from django.urls import include, path
from django.contrib import admin  # Import admin for Django admin functionality

# Consider adding more imports for your views if needed
# from . import views  # Import views from your current app (grant_app)

urlpatterns = [
    path('admin/', admin.site.urls),  # Correct access to Django admin URLs
    path('api/', include('grants.urls')),  # Include URLs from your API app
    # path('', views.HomeView.as_view(), name='home'),  # Use a class-based view for the root
]