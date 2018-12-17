from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'DOB', 'created_at', 'updated_at')
    ordering = ('last_name',)

class GameAdmin(admin.ModelAdmin):
    list_display = ('matchup', 'opp1', 'opp2', 'difference', 'get_week')
    ordering = ('matchup',)
    raw_id_fields = ('week',)
    def get_week(obj):
        return obj.week.week
    get_week.short_description = "Week"
    get_week.admin_order_field = "week__week"


admin.site.register(Game, GameAdmin)
admin.site.register(Plan)
admin.site.register(Week)
admin.site.register(User, UserAdmin)
