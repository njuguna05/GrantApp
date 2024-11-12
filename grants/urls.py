from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserViewSet, GrantViewSet, GrantTypeViewSet,ApplicationViewSet,BeneficiaryViewSet, GrantReviewViewSet,
DisbursementViewSet, DocumentViewSet, GrantCommitmentViewSet, FundRequestViewSet, FundReceiptViewSet,
    DonorViewSet, GranteeViewSet, GranteeCommitmentViewSet, GranteeReportingViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'grants', GrantViewSet)
router.register(r'grant_types', GrantTypeViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'beneficiaries', BeneficiaryViewSet)
router.register(r'grant_reviews', GrantReviewViewSet)
router.register(r'disbursements', DisbursementViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'grant-commitments', GrantCommitmentViewSet)
router.register(r'fund-requests', FundRequestViewSet)
router.register(r'fund-receipts', FundReceiptViewSet)
router.register(r'donors', DonorViewSet)
router.register(r'grantees', GranteeViewSet)
router.register(r'grantee-commitments', GranteeCommitmentViewSet)
router.register(r'grantee-reports', GranteeReportingViewSet)





urlpatterns = [
    path('', include(router.urls)),
]
