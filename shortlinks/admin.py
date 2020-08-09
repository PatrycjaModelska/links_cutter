from django.contrib import admin
from shortlinks.models import Link


class LinkAdmin(admin.ModelAdmin):
	list_display = ("short_url","long_url")


admin.site.register(Link)