from django.views.generic import FormView, TemplateView
from django_tables2 import SingleTableView, SingleTableMixin

from sandbox.forms import SandboxForm
from sandbox.servers_data import SERVERS_DATA
from sandbox.tables import ServerTable


class SandboxView(FormView):
    template_name = 'sandbox.html'
    form_class = SandboxForm


class TableSandboxView(SingleTableMixin, TemplateView):
    table_class = ServerTable
    template_name = 'table_sandbox.html'

    def get_table_data(self):
        return SERVERS_DATA
