from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Transaction, Category, EcoScore
from .forms import TransactionForm
from .forms import CategoryForm
from transformers import pipeline
generator = pipeline("text2text-generation", model="google/flan-t5-small")
from django.shortcuts import get_object_or_404

def sustainability_tip():
    result = generator(
        "One practical eco-friendly budgeting tip:",
        max_new_tokens=30,  
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7       
    )
    return result[0]["generated_text"]


@login_required
def dashboard(request):
    all_transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    transactions = all_transactions[:4]
    total_spent = all_transactions.aggregate(Sum('amount'))['amount__sum'] or 0
    eco_spent = all_transactions.filter(category__eco_friendly=True).aggregate(Sum('amount'))['amount__sum'] or 0
    non_eco_spent = total_spent - eco_spent

    tip = sustainability_tip()
    context = {
        'transactions': transactions,   
        'total_spent': total_spent,
        'eco_spent': eco_spent,
        'non_eco_spent': non_eco_spent,
        'tip': tip,
    }
    return render(request, 'budget/dashboard.html', context)


@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    transaction.delete()
    return redirect('transactions') 

@login_required
def transactions_view(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'budget/transactions.html', {'transactions': transactions})


@login_required
def add_purchase(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transactions')
    else:
        form = TransactionForm()
    return render(request, 'budget/add_purchase.html', {'form': form})

@login_required
def purchase_history(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'budget/purchase_history.html', {'transactions': transactions})


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_purchase')
    else:
        form = CategoryForm()
    return render(request, 'budget/add_category.html', {'form': form})