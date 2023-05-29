from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

def clothing_list(request):
    items = models.Clothingitem.objects.all()
    return render(request, 'man_shop/clothing_list.html', {'items': items})

def clothing_details(request, item_id):
    item = get_object_or_404(models.Clothingitem, pk=item_id)
    return render(request, 'man_shop/clothing_details.html', {'item': item})

def create_item_list(request):
    #POST GET DELETE PUT
    method = request.method
    if method == "POST":
        form = forms.ClothitemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Продукт успешно удален")
    else:
        form = forms.ClothitemForm()
    return render(request, "crud/create_item.html", {"form": form})

def delete_item_list(request, id):
    item_id = get_object_or_404(models.Clothingitem, id=id)
    item_id.delete()
    return HttpResponse("Анкета успешно удалена")

def update_item_list(request, id):
    item_id = get_object_or_404(models.Clothingitem, id=id)
    if request.method == "POST":
        form = forms.ClothitemForm(instance=item_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные успешно обновлены')
        else:
            form = forms.ClothitemForm(instance=item_id)
        context = {
            "form": form,
            "item_id": item_id
        }
        return render(request, "crud/update_item.html", context)

