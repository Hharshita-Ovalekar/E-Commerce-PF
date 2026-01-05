from django.http import HttpResponse
from django.contrib.auth.models import Group

from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response

from .decorators import allowed_users
from .models import Product
from .serializers import ProductListSerializer ,RegisterSerializer, LoginSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
def home(request):

    return HttpResponse("Hi This is home page of our website!!")



@allowed_users(allowed_roles=['seller'])
def seller_dashboard(request):

    return HttpResponse("only seller logged can see this")


@api_view(["GET"])
def product_list(request):
    products = Product.objects.filter(is_active=True).order_by("-created_at")

    serializer = ProductListSerializer(
        products,
        many=True,
        context={"request": request}
    )

    return Response({
        "count": products.count(),
        "products": serializer.data
    })

@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"})
    return Response(serializer.errors, status=400)

@api_view(["POST"])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.validated_data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logged out successfully"})
    except Exception:
        return Response({"error": "Invalid token"}, status=400)
