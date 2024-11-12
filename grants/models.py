from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid

from django.utils import timezone

# from django.contrib.auth import get_user_model

# User = get_user_model()

class User(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Grant Manager'),
        ('reviewer', 'Grant Reviewer'),
        ('applicant', 'Applicant'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='applicant')


class Grant(models.Model):
    grant_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    available_funds = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('closed', 'Closed'), ('upcoming', 'Upcoming')])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Application(models.Model):
    application_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    submission_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=[('submitted', 'Submitted'), ('under_review', 'Under Review'), ('approved', 'Approved'), ('rejected', 'Rejected')])
    total_funding = models.DecimalField(max_digits=12, decimal_places=2)
    approved_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class GrantReview(models.Model):
    review_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField()
    comments = models.TextField()
    review_date = models.DateTimeField(default=timezone.now)


class Disbursement(models.Model):
    disbursement_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='disbursements')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    disbursement_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')])


class Document(models.Model):
    document_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='documents')
    file_name = models.CharField(max_length=255)
    file_path = models.FileField(upload_to='documents/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(default=timezone.now)
    
class Beneficiary(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    # Address Information
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    
    # Grant/Beneficiary Status (optional)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
class GrantType(models.Model):
    # Fields for the GrantType
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    # Date information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    



# Updated models with relationship to Grant

# 1. GrantCommitment
class GrantCommitment(models.Model):
    commitment_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE, related_name='commitments')
    grant_name = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)
    commitment_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('closed', 'Closed')])
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.grant_name


# 2. FundRequest
class FundRequest(models.Model):
    request_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE, related_name='fund_requests')
    grant_commitment = models.ForeignKey(GrantCommitment, on_delete=models.CASCADE, related_name='fund_requests')
    requested_amount = models.DecimalField(max_digits=15, decimal_places=2)
    request_date = models.DateTimeField(default=timezone.now)
    purpose = models.TextField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('denied', 'Denied')])

    def __str__(self):
        return f"Request {self.request_id} for {self.grant_commitment.grant_name}"


# 3. FundReceipt
class FundReceipt(models.Model):
    receipt_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE, related_name='fund_receipts')
    grant_commitment = models.ForeignKey(GrantCommitment, on_delete=models.CASCADE, related_name='fund_receipts')
    received_amount = models.DecimalField(max_digits=15, decimal_places=2)
    receipt_date = models.DateTimeField(default=timezone.now)
    received_from = models.CharField(max_length=255)

    def __str__(self):
        return f"Receipt {self.receipt_id} for {self.grant_commitment.grant_name}"


# 4. Donor
class Donor(models.Model):
    donor_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


# 5. Grantee
class Grantee(models.Model):
    grantee_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# 6. GranteeCommitment
class GranteeCommitment(models.Model):
    grantee = models.ForeignKey(Grantee, on_delete=models.CASCADE, related_name='commitments')
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE, related_name='grantee_commitments')
    grant_commitment = models.ForeignKey(GrantCommitment, on_delete=models.CASCADE, related_name='grantee_commitments')
    amount_committed = models.DecimalField(max_digits=15, decimal_places=2)
    commitment_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('completed', 'Completed')])

    def __str__(self):
        return f"Commitment of {self.amount_committed} by {self.grantee.name}"


# 7. GranteeReporting
class GranteeReporting(models.Model):
    report_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    grantee = models.ForeignKey(Grantee, on_delete=models.CASCADE, related_name='reports')
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE, related_name='grantee_reports')
    grant_commitment = models.ForeignKey(GrantCommitment, on_delete=models.CASCADE, related_name='reports')
    report_date = models.DateTimeField(default=timezone.now)
    period_start = models.DateField()
    period_end = models.DateField()
    report_details = models.TextField()
    status = models.CharField(max_length=50, choices=[('submitted', 'Submitted'), ('reviewed', 'Reviewed'), ('approved', 'Approved')])

    def __str__(self):
        return f"Report {self.report_id} for {self.grant_commitment.grant_name}"

    

