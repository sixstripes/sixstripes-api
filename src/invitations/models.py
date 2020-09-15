from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.db.models.signals import post_save
from mailchimp3 import MailChimp
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


def add_subscriber_to_mailchimp(sender, instance, created, **kwargs):
    if created:
        client = MailChimp(mc_api=settings.MAILCHIMP_API_KEY, mc_user=settings.MAILCHIMP_USERNAME)
        client.lists.members.create_or_update(
            settings.MAILCHIMP_LIST_ID,
            subscriber_hash=instance.email,
            data={
                "email_address": instance.email,
                "status": "subscribed",
                "status_if_new": "subscribed",
                "merge_fields": {
                    "FNAME": instance.name.split(" ")[0],
                    "LNAME": " ".join(instance.name.split(" ")[1:]),
                }
            }
        )

post_save.connect(invite_post_create, sender=Invite)
post_save.connect(add_subscriber_to_mailchimp, sender=Invite)


class DataSuggestion(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default="pending")
    reject_reason = models.TextField(blank=True, null=True)
