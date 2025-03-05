from django.contrib import admin
from .models import *



@admin.register(MainInfo)
class MainInfoModelAdmin(admin.ModelAdmin):
    list_display = ['name','address']
    list_display_links = ['name','address']
    search_fields = ['name','address']
admin.site.register(Gallery)


#------------Home--------------
admin.site.register(HomeStatus)
admin.site.register(ImageCycle)
admin.site.register(Properties)
admin.site.register(MoreInfo)
admin.site.register(SubMoreInfo)
admin.site.register(PropertyListing)
admin.site.register(ContactAgent)
admin.site.register(PropertyAgents)
admin.site.register(ClientOpinions)
#------------About-------------
admin.site.register(AboutStatus)


#------------Contact-------------
admin.site.register(ContactModel)