from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.
def imagePath(instance, filname):
    return '/'.join(['orders', str(instance.full_name) , str(instance.id), filname])

def stickerPath(instance, filename):
    filename = str(instance.id)
    return '/'.join(['stickers',filename])

STATUS = [
    (True, 'complete'),
    (False, 'incomplete')
]

STICKERS_CATEGORIES = [
    ("Basic", "Basic"),
    ("Boy", "Boys"), 
    ("Girl", "Girls"), 
    ("Youth", "Youth")
    ]

def DeliveryDate(date:datetime = datetime.now()):
    return date + timedelta(days=3)



class Sticker(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length = 50)
    category = models.CharField(choices=STICKERS_CATEGORIES, max_length = 30)
    sticker_image = models.ImageField(upload_to=stickerPath)
    
    def __str__(self):
        return str(self.pk)


class Order(models.Model):
    # Contact details
    full_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=10, null=True)

    # Delivery details
    building_number = models.CharField(max_length=20)
    street_name = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    delivery_on = models.DateField(default=DeliveryDate())
    delivery_status = models.BooleanField(default=False, choices=STATUS) 

    # Order Details
    sticker_name = models.ForeignKey(Sticker, on_delete=models.CASCADE, default=1) # maps to stickers table
    sticker_id = models.IntegerField(blank=True)
    name_field = models.CharField(max_length=40)
    class_field = models.CharField(max_length=40, blank=True, null=True)
    school_field = models.CharField(max_length=40, blank=True, null=True)
    quantity = models.PositiveIntegerField(null=False)
    stickerImage = models.ImageField(blank=True, null=True, upload_to=imagePath)
    added_notes = models.TextField(max_length=100, blank=True, null=True)
    order_status = models.BooleanField(default=False, choices=STATUS)
    ordered_on = models.DateTimeField(default=timezone.now)

    def delivered(self):
        return self.delivery_status
    def completed(self):
        return self.order_status

    delivered.boolean = True
    completed.boolean = True

    # Fees Details
    order_fees = models.PositiveIntegerField()
    delivery_fees = models.PositiveIntegerField()
    total_fees = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Orders"

    
    def __str__(self):
        return self.full_name

