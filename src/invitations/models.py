from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.db.models.signals import post_save
from templated_email import send_templated_mail

STATUS_CHOICES = (
    ("pending", "Pending"),
    ("approved", "Approved"),
    ("rejected", "Rejected"),
)


class Invite(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=250)
    reason = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default="pending")

    class Meta:
        verbose_name = "Invite"
        verbose_name_plural = "Invites"

    def __str__(self):
        return f"{self.email} - {self.reason}"


def invite_post_create(sender, instance, created, **kwargs):
    if created:
        site = Site.objects.get(id=1)
        send_templated_mail(
            template_name="new_invite",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=settings.ADMIN_EMAILS,
            context={"invite": instance, "site_url": site.domain},
        )


post_save.connect(invite_post_create, sender=Invite)


class DataSuggestion(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default="pending")
    reject_reason = models.TextField(blank=True, null=True)
