from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import *
from api.serializers import *
# Create your views here.


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def clientListAll(request):
        """Display all the clients from database"""
        clients = ClientMaster.objects.all()
        serializer = ClientSerializer(clients,many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def createClient(request):
        """Authenticate and Create client """
        client = ClientMaster.objects.create(client_name=request.data['name'])
        serializer = ClientSerializer(client)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def createAgent(request):
        """Authenticate user and create agent"""
        client = ClientMaster.objects.create(client_name=request.data['name'])
        serializer = ClientSerializer(client)
        return Response(serializer.data)

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

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def agentListAll(request):
    agents = AgentMaster.objects.all()
    serializer = AgentSerializer(agents,many=True)
    return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated, ))
def agent_details(request,pk):
    try:
        agent = AgentMaster.objects.get(agent_id=pk)
    except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = AgentSerializer(agent)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = AgentSerializer(agent,data=request.data)
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
         agent.delete()
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