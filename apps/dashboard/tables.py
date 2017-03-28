from apps.catalogue.models import Store
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy
from django_tables2 import A, Column, LinkColumn, TemplateColumn
import django_tables2 as tables

from oscar.core.loading import get_class, get_model

DashboardTable = get_class('dashboard.tables', 'DashboardTable')


class StoreTable(DashboardTable):
    name = LinkColumn('dashboard:store_update', args=[A('pk')]) #, args=[A('pk')]
    description = TemplateColumn(
        template_code='{{ record.description|default:""|striptags'
                      '|cut:"&nbsp;"|truncatewords:6 }}')
    # mark_safe is needed because of
    # https://github.com/bradleyayers/django-tables2/issues/187
    actions = TemplateColumn(
        template_name='dashboard/store_row_actions.html',
        orderable=False)

    icon = "sitemap"
    caption = ungettext_lazy("%s Store", "%s Stores")

    class Meta(DashboardTable.Meta):
        model = Store
        fields = ('name', 'description')
