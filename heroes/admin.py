from django.contrib import admin
from .models import Character, Power, Affiliation


@admin.register(Power)
class PowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Affiliation)
class AffiliationAdmin(admin.ModelAdmin):
    list_display = ('name', 'universe', 'type')
    list_filter = ('universe', 'type')
    search_fields = ('name',)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'real_name', 'character_type', 'universe', 'status', 'power_level')
    list_filter = ('character_type', 'universe', 'status', 'gender')
    search_fields = ('name', 'real_name', 'alias')
    filter_horizontal = ('powers', 'affiliations', 'allies', 'enemies')
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'real_name', 'alias', 'character_type', 'universe')
        }),
        ('Características', {
            'fields': ('gender', 'species', 'occupation', 'status', 'power_level')
        }),
        ('Poderes y Afiliaciones', {
            'fields': ('powers', 'affiliations')
        }),
        ('Relaciones', {
            'fields': ('allies', 'enemies')
        }),
        ('Apariencia y Multimedia', {
            'fields': ('profile_image', 'background_image', 'primary_color', 'secondary_color')
        }),
        ('Descripción', {
            'fields': ('biography', 'background_story', 'notable_quotes')
        }),
        ('Información Adicional', {
            'fields': ('first_appearance', 'created_by', 'base_of_operations')
        }),
    )

