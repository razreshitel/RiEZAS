from django.contrib import admin
from .models import Child, EducationalMaterial, EducationalActivity, ParentRequest

class ChildAdmin(admin.ModelAdmin):
    list_display = ('id', 'child_name', 'birth_date', 'parent_name')
    search_fields = ('child_name', 'parent_name')

admin.site.register(Child, ChildAdmin)

class EducationalMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', )

admin.site.register(EducationalMaterial, EducationalMaterialAdmin)

class EducationalActivityAdmin(admin.ModelAdmin):
    def child_name(self, obj):
        return obj.child.child_name
    child_name.short_description = 'Имя ребенка'

    list_display = ('id', 'activity_name', 'child_name', 'date')
    search_fields = ('activity_name', 'child__child_name')

admin.site.register(EducationalActivity, EducationalActivityAdmin)

class ParentRequestAdmin(admin.ModelAdmin):
    def child_name(self, obj):
        return obj.child.child_name
    child_name.short_description = 'Имя ребенка'

    list_display = ('id', 'child_name', 'request_description', 'created_dt')
    search_fields = ('child__child_name', 'request_description')

admin.site.register(ParentRequest, ParentRequestAdmin)
