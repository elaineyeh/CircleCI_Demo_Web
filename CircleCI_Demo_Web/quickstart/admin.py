from django.contrib import admin
from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin

from quickstart.models import SeriesName, Article


class ArticleResource(resources.ModelResource):
    series_name = fields.Field(column_name = 'series_name', attribute='series_name', widget=widgets.ManyToManyWidget(SeriesName, field='name', separator='|'))

    class Meta:
        model = Article
        fields = ('id', 'title', 'user', 'description', 'create_date')
        export_order = ('id', 'title', 'user', 'description', 'create_date')


class ArticleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ArticleResource
    readonly_fields = ('create_date',)


admin.site.register(SeriesName)
admin.site.register(Article, ArticleAdmin)