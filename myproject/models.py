from .pgp import decrypt_data
from django.db import models



class EncryptedData(models.Model):
    data = models.TextField()
    encrypted_data = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if self.data and not self.encrypted_data:
            self.encrypted_data = str(encrypt_data(self.data, 'recipient_key'))
        super().save(*args, **kwargs)

    def get_data(self):
        if self.encrypted_data:
            return decrypt_data(self.encrypted_data)
        else:
            return self.data
