from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
      model = Choice
      extra = 3

class PollAdmin(admin.ModelAdmin):
      inlines = [ChoiceInline]
      
admin.site.register(Poll, PollAdmin)