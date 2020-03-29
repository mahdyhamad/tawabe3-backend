from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from django.http import HttpResponse
# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request):
        
        # set the variables

        full_name = request.data['full_name']
        mobile_number = request.data['mobile_number']
      
        building_number = request.data['building_number']
        street_name = request.data['street_name']
        area = request.data['area']
        city = request.data['city']

        sticker_id = request.data['sticker_id']
        name_field = request.data['name_field']
        class_field = request.data['class_field']
        school_field = request.data['school_field']
        quantity = request.data['quantity']
        stickerImage = request.data['stickerImage']
        added_notes = request.data['notes']

        order_fees = request.data['order_fees']
        delivery_fees = request.data['delivery_fees']
        total_fees = request.data['total_fees']

        Order.objects.create(
            full_name = full_name,
            mobile_number = mobile_number,
            
            building_number = building_number,
            street_name = street_name,
            area = area,
            city = city,

            sticker_id = sticker_id,
            name_field = name_field,
            class_field = class_field,
            school_field = school_field,
            quantity = quantity,
            stickerImage = stickerImage,
            added_notes = added_notes,

            order_fees = order_fees,
            delivery_fees = delivery_fees,
            total_fees = total_fees)
        return HttpResponse({'message':'order creater'}, status=200)