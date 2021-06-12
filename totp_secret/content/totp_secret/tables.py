from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from horizon import tables
from openstack_dashboard import api
from openstack_dashboard import policy


class QueryFilterAction(tables.FilterAction):
	name = "queryfilter"

class CreateCredentialAction(tables.LinkAction):
	name = "credential"
	verbose_name = _("Create Credential")
	url = "horizon:identity:totp_secret:create_credential"
	classes = ("ajax-modal",)
	icon = "plus"

class DeleteCredentialsAction(tables.DeleteAction):
	@staticmethod
	def action_present(count):
		return ungettext_lazy(
			u"Delete Credential",
			u"Delete Credentials",
			count
		)

	@staticmethod
	def action_past(count):
		return ungettext_lazy(
			u"Deleted Credential",
			u"Deleted Credentials",
			count
		)

	policy_rules = (("identity", "identity:delete_user"),)

	def allowed(self, request, datum):
		if not api.keystone.keystone_can_edit_user() or \
			(datum and datum.id == request.user.id):
			return False
		return True
	
	def delete(self, request, obj_id):
		manager = api.keystone.keystoneclient(request,admin=True).credentials
		return manager.delete(obj_id)

class CredentialsTable(tables.DataTable):
	name = tables.Column("id", verbose_name=_("ID"))
	user_id = tables.Column("user_id", verbose_name=_("User ID"))
	type = tables.Column("type", verbose_name=_("Type"))
	blob = tables.Column("blob", verbose_name=_("Blob"))
	project_id = tables.Column("project_id", verbose_name=_("Project ID"))

	class Meta(object):
		name = "credentials"
		verbose_name = _("Credentials")
		table_actions = (QueryFilterAction, CreateCredentialAction,DeleteCredentialsAction,)
