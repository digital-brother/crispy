import django_tables2 as tables

from .models import Server


class ServerTable(tables.Table):
    class Meta:
        model = Server
        template_name = "django_tables2/bootstrap.html"
        fields = ('domain', 'city', 'ip')
