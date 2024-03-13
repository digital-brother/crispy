import django_tables2 as tables


class ServerTable(tables.Table):
    domain = tables.Column()
    city = tables.Column()
    ip = tables.Column()
