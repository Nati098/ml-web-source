from django.contrib import admin
from main_app.models import *


# Register your models here.
admin.site.register(Article)
admin.site.register(WebDemo)
admin.site.register(Section)
admin.site.register(UserRole)
admin.site.register(User)

# for the future
# @admin.register(FavouriteArticle)
# class FavouriteArticleAdmin(admin.ModelAdmin):
#     list_display = ['article', 'name', 'email', 'last_updated']
