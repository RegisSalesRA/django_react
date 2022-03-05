from django.contrib import admin
from core.models import Post,Category, NewUser




# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(NewUser)