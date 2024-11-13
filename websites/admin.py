from django.contrib import admin
from websites.models import WebsiteModule
from websites.models import WesiteNewModule,ContactForm
class WebsiteAdmin(admin.ModelAdmin):
    list_display=('icons_entry','title_entry','desc_content')


class WebstieNewAdmin(admin.ModelAdmin):
    list_display=('doctors_name','doctors_desc','doctors_image')

class ContactAdmin(admin.ModelAdmin):
    list_display=('first_name','email','phone','gender','department','date','comments')


admin.site.register(WebsiteModule,WebsiteAdmin)    
admin.site.register(WesiteNewModule,WebstieNewAdmin)
admin.site.register(ContactForm,ContactAdmin) 

# Register your models here.
