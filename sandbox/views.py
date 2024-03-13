from django.views.generic import FormView
from django_tables2 import SingleTableView

from sandbox.forms import SandboxForm
from sandbox.models import Server
from sandbox.tables import ServerTable


class SandboxView(FormView):
    template_name = 'sandbox.html'
    form_class = SandboxForm


class TableSandboxView(SingleTableView):
    model = Server
    table_class = ServerTable
    template_name = 'table_sandbox.html'
