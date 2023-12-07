"""URLs for Email API handler"""
from django.urls import path
from imap.api.views import EmailCredentialsView

urlpatterns = [
    path('email-credentials/', EmailCredentialsView.as_view(), name='email-credentials'),
]
