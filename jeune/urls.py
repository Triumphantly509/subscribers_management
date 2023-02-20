from jeune import views
from django.urls import path

app_name = 'jeune'

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.welcome, name = "welcome"),
    path('unsubscribe', views.unsubscribe, name = "unsubscribe"),
    path('emails', views.emails, name = "emails"),
]