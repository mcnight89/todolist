from django.db import models
from uuid import uuid4
from ToDo.core.models import User


class TgUser(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    verification_code = models.CharField(max_length=100, null=True, blank=True, default=None)

    @staticmethod
    def _generate_verification_code() -> str:
        return str(uuid4())

    def set_verification_code(self):
        code = self._generate_verification_code()
        self.verification_code = code
        self.save(update_fields=('verification_code',))

        return code
