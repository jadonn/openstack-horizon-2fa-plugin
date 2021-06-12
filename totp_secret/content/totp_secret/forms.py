from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms as horizon_forms
from django import forms

from openstack_dashboard import api

class CreateCredential(horizon_forms.SelfHandlingForm):
	user_id = forms.CharField(label=_("User ID"))
	credential_type = forms.ChoiceField(
		required=True,
		choices=[("totp", "Time-based One Time Password Secret")]
	)
	blob = forms.CharField(label=_("Blob"))

	def handle(self, request, data):
		try:
			manager = api.keystone.keystoneclient(self.request, admin=True).credentials
			return manager.create(data["user_id"], data["credential_type"], data["blob"])
		except Exception:
			exceptions.handle(request, _("Unable to create credential."))


