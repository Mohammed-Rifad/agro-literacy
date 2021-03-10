from django.contrib import admin
from .models import Farmer,Dealer,District,Product,Category,DealerNotification,KnowledgeCenterNotification,KnowledgeCenterService
from .models import Rent,Order,Complaint,Question,Subcategory

# Register your models here.
admin.site.register(Farmer)
admin.site.register(Dealer)
admin.site.register(District)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(DealerNotification)
admin.site.register(KnowledgeCenterService)
admin.site.register(KnowledgeCenterNotification)
admin.site.register(Order)
admin.site.register(Rent)
admin.site.register(Complaint)
admin.site.register(Question)