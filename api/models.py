from django.db import models
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'attendant_{0}/{1}'.format(instance.atdt_id, filename)
# Create your models here.
class Attendant(models.Model):
    atdt_id         = models.AutoField(primary_key=True)
    first_name      = models.CharField(max_length=200,blank=False)
    last_name       = models.CharField(max_length=200,blank=False)
    employee_id     = models.CharField(max_length=200,blank=False)
    location_id     = models.CharField(max_length=200,blank=False)
    password        = models.CharField(max_length=400,blank=False)
    vouchers        = models.IntegerField()
    profile         = models.ImageField(upload_to=user_directory_path)

class ClientMaster(models.Model):
    client_id           = models.AutoField(primary_key=True)
    client_name         = models.CharField(max_length=200,blank=False) 
    address             = models.CharField(max_length=400,blank=False,default='c_addr') 
    contact_name        = models.CharField(max_length=400,blank=False,default='c_name')
    contact_no          = models.CharField(max_length=400,blank=False,default='c_no')
    active_vouchers     = models.IntegerField(default=0)
    used_vouchers       = models.IntegerField(default=0)
    last_order_date     = models.DateField()
    last_order_amount   = models.IntegerField()

class Voucher(models.Model):
    voucher_id      = models.AutoField(primary_key=True)
    validity_date   = models.DateField(blank=False)
    amount          = models.BigIntegerField(blank=False)
    balance         = models.BigIntegerField()
    last_used       = models.CharField(max_length=200)
    start_date      = models.DateField()
    end_date        = models.DateField()
    client_id       = models.ForeignKey(ClientMaster,on_delete=models.CASCADE)
    status          = models.CharField(max_length=1,default='A')

class Transactions(models.Model):
    txn_date        = models.DateField(blank=False)
    txn_id          = models.AutoField(primary_key=True) 
    txn_amount      = models.BigIntegerField(blank=False)
    initial_amount  = models.BigIntegerField()
    redeem_amount   = models.BigIntegerField()
    balance         = models.BigIntegerField()
    agent_id        = models.ForeignKey(Attendant,on_delete=models.CASCADE)
    voucher_id      = models.ForeignKey(Voucher,on_delete=models.CASCADE)
