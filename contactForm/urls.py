from django.urls import path
from .views import ContactForm


urlpatterns = [
    path('contact', ContactForm.as_view(), name='contact'),
]