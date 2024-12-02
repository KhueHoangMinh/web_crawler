from .models import Domain, Property, Cache
from django.contrib import admin


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'domain', 'start_url', 'enable', 'title_type', 'title_property',
        'url_container_elements_type', 'url_container_elements_property',
        'brand_type', 'brand_property', 'price_type', 'price_property',
        'type_type', 'type_property', 'transmission_type', 'transmission_property',
        'engine_type', 'engine_property', 'seats_type', 'seats_property', 'gearbox_type', 'gearbox_property',
        'date_type', 'date_property', 'odo_type', 'odo_property', 'contact_type', 'contact_property',
        'description_type', 'description_property'
    ]
    fieldsets = (
        (None, {
            'fields': ('name', 'domain', 'start_url', 'enable')
        }),
        ('URL Container Information', {
            'fields': ('url_container_elements_type', 'url_container_elements_property')
        }),
        ('Title Information', {
            'fields': ('title_type', 'title_property')
        }),
        ('Images Container Information', {
            'fields': ('images_type', 'images_property')
        }),
        ('Brand Information', {
            'fields': ('brand_type', 'brand_property')
        }),
        ('Price Information', {
            'fields': ('price_type', 'price_property')
        }),
        ('Car Type Information', {
            'fields': ('type_type', 'type_property')
        }),
        ('Transmission Information', {
            'fields': ('transmission_type', 'transmission_property')
        }),
        ('Engine Information', {
            'fields': ('engine_type', 'engine_property')
        }),
        ('Seats Information', {
            'fields': ('seats_type', 'seats_property')
        }),
        ('Gearbox Information', {
            'fields': ('gearbox_type', 'gearbox_property')
        }),
        ('Date Information', {
            'fields': ('date_type', 'date_property')
        }),
        ('Odo Information', {
            'fields': ('odo_type', 'odo_property')
        }),
        ('Contact Information', {
            'fields': ('contact_type', 'contact_property')
        }),
        ('Description Information', {
            'fields': ('description_type', 'description_property')
        }),
    )
    search_fields = ['name', 'domain']
    list_filter = ['title_type', 'brand_type', 'price_type', 'type_type', 'transmission_type', 'engine_type', 'seats_type',
                   'gearbox_type', 'date_type', 'odo_type', 'contact_type', 'description_type']


@admin.register(Cache)
class CacheAdmin(admin.ModelAdmin):
    list_display = ('domain', 'url', 'status', 'visited')


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('cache', 'title', 'brand', 'price', 'type', 'transmission', 'engine', 'seats', 'gearbox', 'date', 'odo', 'contact', 'description')
    list_filter = ('domain', 'date')
    search_fields = ('title', 'brand', 'contact')
