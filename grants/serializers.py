from rest_framework import serializers
from .models import User, Grant,GrantType, Application, GrantReview, Disbursement, Document,Beneficiary

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'role']


class GrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grant
        fields = ['grant_id', 'title', 'description', 'available_funds', 'status', 'created_at', 'updated_at']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['application_id', 'grant', 'applicant', 'submission_date', 'status', 'total_funding', 'approved_amount', 'created_at', 'updated_at']


class GrantReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantReview
        fields = ['review_id', 'application', 'reviewer', 'score', 'comments', 'review_date']


class DisbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disbursement
        fields = ['disbursement_id', 'application', 'amount', 'disbursement_date', 'status']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['document_id', 'application', 'file_name', 'file_path', 'uploaded_by', 'uploaded_at']

class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address']
        
class GrantTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantType
        fields = ['id', 'name', 'description', 'created_at']