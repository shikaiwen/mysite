'''
Created on 2018年3月14日

@author: kevin
'''
from django.contrib import admin

class visiableblogfilter(admin.SimpleListFilter):
    
    title = "公开状态"
    parameter_name = "is_show"
    
    def lookups(self, request, model_admin):
        return (
            ("0","不显示"),
            ("1","显示"),
            )
    
    def queryset(self, request, queryset):
        
        if self.value() == "0":
            return queryset.filter(show = "0")
        if self.value() == "1":
            return queryset.filter(show = "1")
    
    