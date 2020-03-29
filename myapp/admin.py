from django.contrib import admin
from .models import Order, Sticker
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
# Register your models here.


admin.site.site_header = "Tawabe3 Admin Dashboard"
admin.site.site_title = "tawabe3 admin"
admin.site.index_title = "Welcome to Tawabe3"
admin.site.unregister(Group)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'mobile_number']
    list_filter = ['ordered_on', 'delivery_on' ,'order_status', 'delivery_status']

    fieldsets = [
        ('Contact Details',  {'fields': ['full_name', 
                                         'mobile_number']}),

        ('Delivery Details', {'fields': ['building_number', 
                                         'street_name',
                                         'area',
                                         'city',
                                         'delivery_on',
                                         'delivery_status']}),

        ('Order Details', {'fields': ['name_field', 
                                      'class_field',
                                      'school_field',
                                      'sticker_name',
                                      'sticker_id',
                                      'stickerImage',
                                      'quantity',
                                      'order_status',
                                      'ordered_on']}),

        ('Invoice Details', {'fields': ['order_fees', 
                                        'delivery_fees',
                                        'total_fees']}),
    ]
    list_display = (
        'pk',
        'full_name',
        'ordered_on',
        'total_fees',
        'city',
        'completed',
        'delivered')
    
    


@admin.register(Sticker)
class StickerAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "sticker_display"]
    list_display = (
        "id",
        "name",
        "category"
    )
    def sticker_display(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.sticker_image.url,
            width=obj.sticker_image.width*0.3,
            height=obj.sticker_image.height*0.3))
