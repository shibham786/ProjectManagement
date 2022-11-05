from django.contrib import admin
from .models import Project,Task,Permissions,UserProjectPermission

# Register your models here.
#for display all field in admin side
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc','create_by')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'desc','project')

class PermissionAdmin(admin.ModelAdmin):
    list_display = ('id','permission_name', 'desc')

class UserProjectPermissionAdmin(admin.ModelAdmin):
    list_display = ('id','permission', 'user')
admin.site.register(Project,ProjectAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Permissions,PermissionAdmin)
admin.site.register(UserProjectPermission,UserProjectPermissionAdmin)
