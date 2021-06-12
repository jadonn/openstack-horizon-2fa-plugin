from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _


from horizon import tables
from horizon import exceptions
from horizon import forms

from openstack_dashboard import api
from keystoneclient import v3 as keystone

from .tables import CredentialsTable
from .forms import CreateCredential

class IndexView(tables.DataTableView):
	table_class = CredentialsTable
	template_name = 'identity/totp_secret/index.html'

	def get_data(self):
		manager = api.keystone.keystoneclient(self.request, admin=True).credentials
		return manager.list()

class CreateCredentialView(forms.ModalFormView):
	form_class = CreateCredential
	template_name = 'identity/totp_secret/create_credential.html'
	success_url = reverse_lazy("horizon:identity:totp_secret:index")
	modal_id = "create_credential_modal"
	modal_header = _("Create Credential")
	submit_label = _("Create Credential")
	submit_url = reverse_lazy("horizon:identity:totp_secret:create_credential")
