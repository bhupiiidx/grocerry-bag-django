from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Item

def homepage(request):
    items = ''
    getdate = ''
    try:
        items = Item.objects.filter(user=request.user).order_by('-id')
        getdate = request.GET.get('date')
        if getdate:
            items = Item.objects.filter(user=request.user, date=getdate).order_by('-id')
        else:
            items = Item.objects.filter(user=request.user).order_by('-id')
    except :
        pass
    context = {
        'items': items,
        'getdate': getdate,
    }
    return render(request, "index.html", context)

@login_required
def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        status = request.POST.get("status")
        date = request.POST.get("date")
        if name and quantity and status and date:
            new_item = Item(name=name, quantity=quantity,
                            status=status, date=date, user=request.user)
            new_item.save()
            messages.success(request," ",name, ' added successfully!')
            return redirect('home')
        messages.error(request, "One or more field(s) is missing!")
        return redirect('add-item')
    return render(request, "add.html")

@login_required
def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    date = item.date.strftime("%Y-%m-%d")
    if request.method == 'POST':
        print("request.POST =================================================================",request.POST)
        item.name = request.POST.get("name")
        item.quantity = request.POST.get("quantity")
        item.status = request.POST.get("status")
        item.date = request.POST.get("date")
        item.save()
        messages.success(request, " ", item.name, ' updated successfully!')
        return redirect('home')
    return render(request, "update.html", {'item': item, 'date': date})

@login_required
def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    messages.error(request, 'Item deleted successfully!')
    return redirect('home')