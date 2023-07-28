from django.contrib import admin
from todo.models import ToDo


# class StatusFilter(admin.SimpleListFilter):
#     title = 'Status'
#     parameter_name = 'status'
#
#     def lookups(self, request, model_admin):
#         return (
#             ('new', 'New'),
#             ('active', 'Active'),
#             ('completed', 'Completed'),
#         )
#
#     def queryset(self, request, queryset):
#         if self.value() == 'new':
#             return queryset.filter(status='New')
#         elif self.value() == 'active':
#             return queryset.filter(status='Active')
#         elif self.value() == 'completed':
#             return queryset.filter(status='Completed')

def custom_action(modeladmin, request, queryset):
    pass


custom_action.short_description = "Custom action"


class ToDoAdmin(admin.ModelAdmin):
    # list_filter = (StatusFilter,)
    actions = [custom_action]
    actions_on_top = [custom_action]


admin.site.register(ToDo, ToDoAdmin)
