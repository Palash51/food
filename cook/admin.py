from django.contrib import admin

from .models import Cook, Vacancy


class VacancyAdmin(admin.ModelAdmin):
    model = Vacancy
    list_display = ['businessunit', 'position', 'created', 'is_open']


class CookAdmin(admin.ModelAdmin):
	model = Cook
	list_display = ['name', 'email', 'information']



admin.site.register(Cook, CookAdmin)
admin.site.register(Vacancy, VacancyAdmin)
