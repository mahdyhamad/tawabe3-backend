from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['full_name',
                  'mobile_number',
                  
                  'building_number',
                  'street_name',
                  'area',
                  'city',

                  'sticker_id',
                  'name_field',
                  'class_field',
                  'school_field',
                  'quantity',
                  'stickerImage',
                  'added_notes',

                  'order_fees',
                  'delivery_fees',
                  'total_fees']
        