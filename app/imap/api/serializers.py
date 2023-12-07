
"""Email IMAP serializer"""
from rest_framework import serializers
from core.models import EmailCredentials

class EmailCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCredentials
        fields = '__all__'
