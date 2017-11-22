from django.contrib import admin

# Register your models here.
from blog.models import Post, Category


# class PostAdmin:
#     pass
#
#
# class CategoryAdmin:
#     pass


admin.site.register(Post)
admin.site.register(Category)
