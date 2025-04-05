from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Item, ItemRequest
from .serializers import UserSerializer, ItemSerializer, ItemRequestSerializer

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"})
    return Response(serializer.errors)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        user = User.objects.get(username=username, password=password)
        return Response({"message": "Login successful", "role": user.role})
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials"})

@api_view(['POST'])
def post_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Item posted successfully"})
    return Response(serializer.errors)

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def request_item(request):
    serializer = ItemRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Item requested successfully"})
    return Response(serializer.errors)
