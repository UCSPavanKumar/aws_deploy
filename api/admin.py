from django.contrib import admin

# Register your models here.
from .models import Attendant,Voucher,Transactions,ClientMaster

admin.site.register(Attendant)
admin.site.register(Voucher)
admin.site.register(Transactions)
admin.site.register(ClientMaster)