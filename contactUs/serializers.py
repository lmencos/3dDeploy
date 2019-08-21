from rest_framework import serializers
from .models import ContactUs

#ContactUs serializer
class ContactUsSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactUs
    fields = '__all__'

