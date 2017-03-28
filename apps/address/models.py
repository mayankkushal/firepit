from django.db import models
from django.utils.translation import ugettext_lazy as _
from oscar.apps.address.abstract_models import AbstractUserAddress


class UserAddress(AbstractUserAddress):
	country = models.ForeignKey(
        'address.Country',
        on_delete=models.CASCADE,
        verbose_name=_("Country"),
        default='India')
	state = models.CharField(_("State"), max_length=255, blank=True, default='Telangana', null=True)
		

from oscar.apps.address.models import *  # noqa
