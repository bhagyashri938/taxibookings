

# Create your views here.
from django.shortcuts import render, redirect
from.models import TaxiDetails, Customer, PaymentReceipt
from.forms import TaxiDetailsForm, CustomerForm, PaymentReceiptForm

def index(request):
    return render(request, 'index.html')

def taxi_list(request):
    taxis = TaxiDetails.objects.all()
    return render(request, 'taxi_list.html', {'taxis': taxis})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def receipt_list(request):
    receipts = PaymentReceipt.objects.all()
    return render(request, 'receipt_list.html', {'receipts': receipts})

def create_taxi(request):
    if request.method == 'POST':
        form = TaxiDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taxi_list')
    else:
        form = TaxiDetailsForm()
    return render(request, 'create_taxi.html', {'form': form})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'create_customer.html', {'form': form})

def create_receipt(request):
    if request.method == 'POST':
        form = PaymentReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receipt_list')
    else:
        form = PaymentReceiptForm()
    return render(request, 'create_receipt.html', {'form': form})
