from rest_framework import viewsets
from .models import Application, Beneficiary, Grant, GrantType, GrantReview, Disbursement, Document, User
from .serializers import GrantSerializer,GrantTypeSerializer ,ApplicationSerializer,BeneficiarySerializer, GrantReviewSerializer, DisbursementSerializer, DocumentSerializer, UserSerializer

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
