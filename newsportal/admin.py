from django.contrib import admin

from newsportal.models import Advertisement, Category, Contact, OurTeam, Post, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Advertisement)
admin.site.register(OurTeam)
admin.site.register(Contact)