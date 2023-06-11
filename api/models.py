from django.db import models

# Create your models here.
class AgentMaster(models.Model):
    agent_id    = models.AutoField(primary_key=True)
    agent_name  = models.CharField(max_length=200,blank=False)

class ClientMaster(models.Model):
    client_id   = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=200,blank=False) 

class Voucher(models.Model):
    voucher_id = models.AutoField(primary_key=True)
    validity_date = models.DateField(blank=False)
    amount = models.BigIntegerField(max_length=10,blank=False)
    client_id = models.ForeignKey(ClientMaster,on_delete=models.CASCADE)
    status = models.CharField(max_length=1,default='A')

class Transactions(models.Model):
    txn_date    = models.DateField(blank=False)
    txn_amount  = models.BigIntegerField(blank=False,max_length=20)
    agent_id    = models.ForeignKey(AgentMaster,on_delete=models.CASCADE)
    voucher_id = models.ForeignKey(Voucher,on_delete=models.CASCADE)
