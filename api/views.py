from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import *
from api.serializers import *
from django.utils import timezone
# Create your views here.



"""All Create API Functions"""
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def createAttendant(request):
        """Authenticate and Create client """
        try:
            # attendant = Attendant.objects.create(
            #                                 first_name      = request.data['first_name'],
            #                                 last_name       = request.data['last_name'],
            #                                 employee_id     = request.data['employee_id'],
            #                                 location_id     = request.data['location_id'],
            #                                 password        =  request.data['password'],
            #                                 vouchers        = 0
            #                                 )
            serializer = AttendantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                 return Response(serializer.errors)
        except Exception as e:
             return Response({'status':str(e)})

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def createVoucher(request):
        """Authenticate user and create agent"""
        try:
            # voucher = Voucher.objects.create(   voucher_id=request.data['voucher_id'],
            #                                     initial_amount=request.data['initial_amount'],
            #                                     balance = request.data['balance'],
            #                                     last_used =request.data['last_used'],
            #                                     start_date=request.data['start_date'],
            #                                     end_date=request.data['end_date'],
            #                                     status=request.data['status'] ,
            #                                     client_id_id=client)
            serializer = VoucherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                client = ClientMaster.objects.get(client_id=request.data['client_id'])
                client.active_vouchers = client.active_vouchers+1
                client.save(update_fields=['active_vouchers'])
                return Response(serializer.data)
            else:
                 return Response(serializer.errors)
        except Exception as e:
              return Response({'status':str(e)})

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def createClient(request):
        """Authenticate user and create agent"""
        try:
            # client = ClientMaster.objects.create(
            #                                 client_name         = request.data['client_name'],
            #                                 address             = request.data['address'],
            #                                 contact_name        = request.data['contact_name'],
            #                                 contact_no          = request.data['contact_no'],
            #                                 active_vouchers     = request.data['active_vouchers'],
            #                                 used_vouchers       = request.data['used_vouchers'],
            #                                 last_order_date     = request.data['last_order_date'],
            #                                 last_order_amount   = request.data['last_order_amount'],
            # )
            serializer = ClientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                 return Response(serializer.errors)
        except Exception as e:
              return Response({'status':str(e)})


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def createTransaction(request):
        """Authenticate user and create agent"""
        try:
            # attendant   = Attendant.objects.get(atdt_id     = request.data["atdt_id"])
            # voucher     = Voucher.objects.get(voucher_id    = request.data['voucher_id'])
            # try:
            #     transaction = Transactions.objects.create( 
            #                                                 initial_amount  = request.data['initial_amount'],
            #                                                 redeem_amount   = request.data['redeem_amount'],
            #                                                 left_balance    = request.data['left_balance'],
            #                                                 Voucher_id_id   = voucher.voucher_id,
            #                                                 id_id           = attendant.atdt_id
            #                                                 )
            # except Exception as e:
            #      return Response({'status':str(e)})
            serializer = TransactionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                voucher     = Voucher.objects.get(voucher_id    = request.data['Voucher_id'])
                voucher.last_transaction_id = serializer.data['txn_id']
                voucher.last_used = timezone.now
                voucher.save(update_fields=['last_transaction_id'])
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Exception as e:
             return Response({'status':str(e)})
""""""

"""All Retrieve API Functions"""
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def clientListAll(request):
        """Display all the clients from database"""
        clients = ClientMaster.objects.all()
        serializer = AttendantSerializer(clients,many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def attendantListAll(request):
        """Display all the clients from database"""
        attendants = Attendant.objects.all()
        serializer = AttendantSerializer(attendants,many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def voucherListAll(request):
        """Display all the clients from database"""
        vouchers = Voucher.objects.all()
        serializer = VoucherSerializer(vouchers,many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def transactionsListAll(request):
        """Display all the clients from database"""
        transactions = Transactions.objects.all()
        serializer = AttendantSerializer(transactions,many=True)
        return Response(serializer.data)
""""""

"""GET by ID,Update By ID,Delete by ID"""
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated, ))
def client_details(request,pk):
    try:
        client = ClientMaster.objects.get(client_id=pk)
    except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = ClientSerializer(client,data=request.data)
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
         client.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated, ))
def attendant_details(request,pk):
    try:
        atdt = Attendant.objects.get(attendant_id=pk)
    except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = AttendantSerializer(atdt)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = AttendantSerializer(atdt,data=request.data)
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
         atdt.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated, ))
def voucher_details(request,pk):
    try:
        voucher = Voucher.objects.get(client_id=pk)
    except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = VoucherSerializer(voucher)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = VoucherSerializer(voucher,data=request.data)
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
         voucher.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated, ))
def transaction_details(request,pk):
    try:
        transaction = Transactions.objects.get(transaction_id=pk)
    except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = TransactionSerializer(transaction,data=request.data)
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
         transaction.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
    
""""""
