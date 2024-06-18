from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Nutri import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
     path('form/', views.form, name='form'),
    path('names/', views.index, name='recommend_recipe'),
     path('contact/', views.contact, name='contact'),
    path('graph/', views.graph, name='graph'),
    path('names/details/', views.get_food_details, name='get_food_details'),
    path('save_food/', views.save_food, name='save_food'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

