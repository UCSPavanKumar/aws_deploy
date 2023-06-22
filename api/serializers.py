from rest_framework import serializers
from .models import Transactions,Attendant,ClientMaster,Voucher

class TransactionSerializer(serializers.ModelSerializer):

  
   class Meta:
      model = Transactions
      fields = '__all__'

class AttendantSerializer(serializers.ModelSerializer):
   class Meta:
      model=  Attendant
      fields = '__all__'

class VoucherSerializer(serializers.ModelSerializer):
   class Meta:
      model = Voucher
      fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
   class Meta:
      model = ClientMaster
      fields = '__all__'