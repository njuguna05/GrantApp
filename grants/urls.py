from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, GrantViewSet, GrantTypeViewSet,ApplicationViewSet,BeneficiaryViewSet, GrantReviewViewSet, DisbursementViewSet, DocumentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'grants', GrantViewSet)
router.register(r'grant_types', GrantTypeViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'beneficiaries', BeneficiaryViewSet)
router.register(r'grant_reviews', GrantReviewViewSet)
router.register(r'disbursements', DisbursementViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
