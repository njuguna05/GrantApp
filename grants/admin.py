
from django.contrib import admin
from .models import (Disbursement, Document, Grant, Beneficiary, GrantType, Application, GrantReview,GrantCommitment, 
                     FundRequest, FundReceipt, Donor, Grantee, GranteeCommitment, GranteeReporting, GrantCommitment, FundRequest, FundReceipt,
    Donor, Grantee, GranteeCommitment, GranteeReporting)

# Register your models here.
# Register the GrantType model
class GrantAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ['title', 'description']
    list_filter = ['created_at']
    ordering = ['title']

# Register the Beneficiary model
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'date_joined')
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['date_joined']
    ordering = ['last_name']

# Register the Grant model
class GrantTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ['name']
    list_filter = ['created_at']
    ordering = ['name']

    # Defining the inline for applications
    # class ApplicationInline(admin.TabularInline):
    #     model = Application
    #     extra = 1  # Number of empty forms to show for this inline

    # inlines = [ApplicationInline]

# Register the Application model
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('grant', 'applicant', 'status', 'created_at', 'approved_amount')
    search_fields = ['grant__title', 'beneficiary__first_name', 'beneficiary__last_name']
    list_filter = ['status', 'applicant']
    ordering = ['applicant']

# Register the GrantReview model (if applicable)
class GrantReviewAdmin(admin.ModelAdmin):
    list_display = ('application', 'reviewer', 'score', 'review_date')
    search_fields = ['reviewer__first_name']
    list_filter = ['review_date', 'score']
    ordering = ['review_date']

class DisbursementAdmin(admin.ModelAdmin):
    list_display = ('disbursement_id', 'application', 'amount', 'disbursement_date', 'status')
    search_fields = ('disbursement_id', 'application__id')
    list_filter = ('status', 'disbursement_date')

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_id', 'application', 'file_name', 'file_path', 'uploaded_by', 'uploaded_at')
    search_fields = ('document_id', 'application__id', 'file_name')
    list_filter = ('uploaded_at',)




# @admin.register(Grant)
# class GrantAdmin(admin.ModelAdmin):
#     list_display = ('grant_id', 'name', 'start_date', 'end_date', 'total_funding')
#     search_fields = ('name',)



class GrantCommitmentAdmin(admin.ModelAdmin):
    list_display = ('commitment_id', 'grant', 'total_amount', 'commitment_date', 'status')
    search_fields = ('grant__name', 'status')



class FundRequestAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'grant', 'requested_amount', 'request_date', 'status')
    search_fields = ('grant__name', 'status')



class FundReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_id', 'grant', 'received_amount', 'receipt_date', 'received_from')
    search_fields = ('grant__name', 'received_from')



class DonorAdmin(admin.ModelAdmin):
    list_display = ('donor_id', 'name', 'email')
    search_fields = ('name', 'email')



class GranteeAdmin(admin.ModelAdmin):
    list_display = ('grantee_id', 'name', 'contact_person', 'email')
    search_fields = ('name', 'contact_person')



class GranteeCommitmentAdmin(admin.ModelAdmin):
    list_display = ('grantee', 'grant', 'amount_committed', 'commitment_date', 'status')
    search_fields = ('grantee__name', 'grant__name', 'status')



class GranteeReportingAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'grantee', 'grant', 'report_date', 'status')
    search_fields = ('grantee__name', 'grant__name', 'status')




# Registering the models with the admin interface
admin.site.register(GrantType, GrantTypeAdmin)
admin.site.register(Beneficiary, BeneficiaryAdmin)
admin.site.register(Grant, GrantAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(GrantReview, GrantReviewAdmin)
admin.site.register(Disbursement, DisbursementAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(GrantCommitment)
admin.site.register(FundRequest)
admin.site.register(FundReceipt)
admin.site.register(Donor)
admin.site.register(Grantee)
admin.site.register(GranteeCommitment)
admin.site.register(GranteeReporting)
