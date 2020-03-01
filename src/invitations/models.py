from django.db import models


class Invite(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=250)
    reason = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Invite"
        verbose_name_plural = "Invites"

    def __str__(self):
        return f"{self.email} - {self.reason}"
