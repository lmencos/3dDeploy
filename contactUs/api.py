from .models import ContactUs
from rest_framework import viewsets, permissions
from .serializers import ContactUsSerializer

#ContactUs viweset
class ContactUsViewSet(viewsets.ModelViewSet):
  queryset = ContactUs.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = ContactUsSerializer
