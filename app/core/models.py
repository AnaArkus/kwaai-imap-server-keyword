"""Django models utilities."""

from django.db import models

class EmailCredentials(models.Model):
    email_address = models.EmailField()
    password = models.CharField(max_length=255)
    imap_server = models.CharField(max_length=255)

    def __str__(self):
        return self.email_address