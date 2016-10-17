from django.contrib import admin

from .models import Experience, Education, Company, Recipe, Ingredient, Direction


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title',)


class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 3


class DirectionInline(admin.StackedInline):
    model = Direction
    extra = 3


class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientInline, DirectionInline)


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Company)
admin.site.register(Education)
admin.site.register(Recipe, RecipeAdmin)
