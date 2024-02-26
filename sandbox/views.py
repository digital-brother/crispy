from django.views.generic import FormView

from sandbox.forms import SandboxForm


class SandboxView(FormView):
    template_name = 'sandbox.html'
    form_class = SandboxForm

