from django import forms
from.models import TaxiDetails,Customer,PaymentReceipt
class TaxiDetailsForm(forms.ModelForm):
    class Meta:
        model=TaxiDetails
        fields=['registration_number',"model",'capacity','availability']
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','email','phone_number']
        
class PaymentReceiptForm(forms.ModelForm):
    class Meta:
        model=PaymentReceipt
        fields=['customer','taxi','amount']        
            