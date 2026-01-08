from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'urgency_score', 'risk_score', 'reward_score', 'get_total_score', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    
    @admin.display(description='Total Score')
    def get_total_score(self, obj):
        return obj.total_score