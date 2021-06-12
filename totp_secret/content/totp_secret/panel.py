from django.utils.translation import ugettext_lazy as _
import horizon

class TotpSecretPanel(horizon.Panel):
	name = _("TOTP Secrets")
	slug = "totp_secret"

from openstack_dashboard.dashboards.identity import dashboard

dashboard.Identity.register(TotpSecretPanel)