from rest_framework import serializers
from .models import Transactions,ClientMaster,AgentMaster,Voucher

class TransactionSerializer(serializers.ModelSerializer):
   class Meta:
      model = Transactions
      fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
   class Meta:
      model=  ClientMaster
      fields = '__all__'

class VoucherSerializer(serializers.ModelSerializer):
   class Meta:
      model = Voucher
      fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
   class Meta:
      model = AgentMaster
      fields = '__all__'