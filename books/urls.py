from django.contrib import admin
from django.urls import include , path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views




urlpatterns = [
    url(r'^viewer.html$', TemplateView.as_view(template_name="viewer.html", content_type="text/html"), name="viewer"),
   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
