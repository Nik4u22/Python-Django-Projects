from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class ContactBook(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    image = models.FileField(_("Avatar Image"),)
    mobile_number = models.CharField(_("Mobile Number"), max_length=10)
    email = models.EmailField(_("User Email"), max_length=254)
    label = models.CharField(_("Label"), max_length=50)
    name = models.CharField(_("Name"), max_length=50)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True, auto_now_add=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("ContactBook")
        verbose_name_plural = _("ContactBooks")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ContactBook_detail", kwargs={"pk": self.pk})
