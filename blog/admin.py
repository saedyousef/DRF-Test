from django.contrib import admin
from blog.models import Category, Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['category__title']
    fields = ['title', 'description', 'category']
    list_display = ('title', 'author', 'get_category', 'publish_date')

    # Get the title attribute from Categor.
    def get_category(self, obj):
        return obj.category.title

    # Label for get_category.
    get_category.short_description = "Category"

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'description')

# Regsitering models to be shown on Admin Site.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
