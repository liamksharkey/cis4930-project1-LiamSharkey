from django.contrib import admin
from .models import Game, WeatherRecord      
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'release_date')
    search_fields = ('name',)
    list_filter = ('price',)
    fields = ('name', 'price', 'release_date')
    fieldsets = (
        (None, {'fields': ('name', 'price')}),
        ('Date Information', {'fields': ('release_date',)}),
    )

admin.site.register(Game, GameAdmin)
admin.site.register(WeatherRecord)