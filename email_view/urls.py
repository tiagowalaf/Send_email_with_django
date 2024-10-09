from django.urls import path
from . import views
urlpatterns = [
    path('', views.mostrar_form, name='ver_template'),
    path('enviar_email/', views.enviar_email, name='enviar_email'),
]
