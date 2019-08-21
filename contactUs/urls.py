from rest_framework import routers
from .api import ContactUsViewSet

router = routers.DefaultRouter()
router.register('api/contactus', ContactUsViewSet, 'contactus')

urlpatterns = router.urls
