from django.conf.urls import url

from totp_secret.content.totp_secret import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^create_credential/$', views.CreateCredentialView.as_view(), name='create_credential'),
]