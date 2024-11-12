from rest_framework import viewsets
from .models import (Application, Beneficiary, Grant, GrantType, GrantReview, Disbursement, Document, User,GrantCommitment, FundRequest, FundReceipt,
    Donor, Grantee, GranteeCommitment, GranteeReporting)
from .serializers import (GrantSerializer,GrantTypeSerializer ,ApplicationSerializer,BeneficiarySerializer, GrantReviewSerializer,
                          DisbursementSerializer, DocumentSerializer, UserSerializer,GrantCommitmentSerializer, FundRequestSerializer, FundReceiptSerializer,
    DonorSerializer, GranteeSerializer, GranteeCommitmentSerializer, GranteeReportingSerializer)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GrantViewSet(viewsets.ModelViewSet):
    queryset = Grant.objects.all()
    serializer_class = GrantSerializer
    
class GrantTypeViewSet(viewsets.ModelViewSet):
    queryset = GrantType.objects.all()
    serializer_class = GrantTypeSerializer
    
class BeneficiaryViewSet(viewsets.ModelViewSet):
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class GrantReviewViewSet(viewsets.ModelViewSet):
    queryset = GrantReview.objects.all()
    serializer_class = GrantReviewSerializer


class DisbursementViewSet(viewsets.ModelViewSet):
    queryset = Disbursement.objects.all()
    serializer_class = DisbursementSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer




# ViewSet for Grant
class GrantViewSet(viewsets.ModelViewSet):
    queryset = Grant.objects.all()
    serializer_class = GrantSerializer


# ViewSet for GrantCommitment
class GrantCommitmentViewSet(viewsets.ModelViewSet):
    queryset = GrantCommitment.objects.all()
    serializer_class = GrantCommitmentSerializer


# ViewSet for FundRequest
class FundRequestViewSet(viewsets.ModelViewSet):
    queryset = FundRequest.objects.all()
    serializer_class = FundRequestSerializer


# ViewSet for FundReceipt
class FundReceiptViewSet(viewsets.ModelViewSet):
    queryset = FundReceipt.objects.all()
    serializer_class = FundReceiptSerializer


# ViewSet for Donor
class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer


# ViewSet for Grantee
class GranteeViewSet(viewsets.ModelViewSet):
    queryset = Grantee.objects.all()
    serializer_class = GranteeSerializer


# ViewSet for GranteeCommitment
class GranteeCommitmentViewSet(viewsets.ModelViewSet):
    queryset = GranteeCommitment.objects.all()
    serializer_class = GranteeCommitmentSerializer


# ViewSet for GranteeReporting
class GranteeReportingViewSet(viewsets.ModelViewSet):
    queryset = GranteeReporting.objects.all()
    serializer_class = GranteeReportingSerializer

