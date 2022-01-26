# Third Party Library
from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models


class RequestPost(models.Model):
    created_by: models.ForeignKey = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Post Author",
        on_delete=models.CASCADE,
    )
    request_group: models.ForeignKey = models.ForeignKey(
        Group,
        verbose_name="Request Group",
        on_delete=models.CASCADE,
    )
    detail: models.TextField = models.TextField("Detail", blank=True)
    created_at: models.DateTimeField = models.DateTimeField("Creation timestamp", auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField("last-modified timestamp", auto_now=True)
    is_open: models.BooleanField = models.BooleanField("Open", default=True)

    class Meta:
        permissions = [
            ("view_all_request_post", "Can view all request posts"),
            ("approve_request_post", "Can approve request post"),
        ]

    def __str__(self):
        return f"Requst Post #{self.pk}"
