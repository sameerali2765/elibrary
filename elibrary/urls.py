"""elibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include , path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home ,name='Home'),
    path('About/', views.About ,name='About'),
    path('Contact/', views.Contact,name='Contact'),

    #account url
    path('account/login', views.Login,name='handleLogin'),
    path('account/Register', views.Register,name='Register'),
    path('account/Registers', views.handleRegister,name='Registers'),

    #profile
    path('account/profile', views.profile,name='profile'),
    path('account/profile/update', views.Profile_Update,name='Profile_Update'),

    # book app
    path('books/',views.Books ,name='books'),
    path('book_detail/<str:id>', views.Book_Detail ,name="book_detail"),
    path('filter-data/',views.filter_data , name="filter_data"),
    path('search/',views.Search, name="search"),
    # path('pdf/<str:id>',views.Viewer, name="pdf"),
    # path('book-category/', views.bookcategory ,name="book_category"),
  

   
   path('accounts/',include('django.contrib.auth.urls')),
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

