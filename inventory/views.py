from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import ListView
from weasyprint import CSS, HTML

from inventory.models import Category, Items, Store

from .forms import CategoryForms, ItemsForms


class Report(View):
    def get(self, request):
        context = {"palavra": 'samuel'}
        html_tring = render_to_string('report.html', context)
        html = HTML(string=html_tring)

        html.write_pdf(target='/tmp/report.pdf', stylesheets=[
                       CSS('base_static/global/assets/css/sb-admin-2.min.css',)])
        fs = FileSystemStorage('/tmp')
        with fs.open('report.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="report.pdf"'
        return response


class SearchResultsView(ListView):
    model = Category
    template_name = 'pages/search-results.html'

    def get_queryset(self):

        query = self.request.GET.get("q")
        object_list = Category.objects.filter(
            Q(name__icontains=query) | Q(id__icontains=query)
        )

        if list(object_list) == [] or query == '':
            object_list = False
            return object_list
        return object_list


@login_required(login_url='user:login')
def home(request):
    return render(request, 'index.html')

# ===============view Items==================  #


@login_required(login_url='user:login')
def item_register(request):
    # request.session['number'] = request.session.get('number') or 1
    # request.session['number'] += 1
    category = Category.objects.all()
    store = Store.objects.all()

    register_form_data = request.session.get('register_form_data', None)
    form = ItemsForms(register_form_data)

    context = {"category": category, "store": store, "form": form}
    return render(request, 'pages/item/item-create.html', context)


@login_required(login_url='user:login')
def item_create(request):
    # tratar dados do dormulario

    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = ItemsForms(POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Item cadastrado com sucesso')
        del (request.session['register_form_data'])

    return redirect('inventory:item_register')


def item_read(request):
    contact_list = Items.objects.all()
    paginator = Paginator(contact_list, 5)  # Show 5 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/item/item-read.html', {'page_obj': page_obj})


@login_required(login_url='user:login')
def item_update(request, pk):
    category = Category.objects.all()
    store = Store.objects.all()
    item = get_object_or_404(Items, id=pk)
    form = ItemsForms(instance=item)
    b = ""
    c = ""
    for a in category:
        if a == item.categoryId:
            b = int(a.id)

        else:
            pass

    for a in store:
        if a == item.storeId:
            c = int(a.id)

        else:
            pass

    if request.method == "POST":
        form = ItemsForms(request.POST, instance=item)

        if form.is_valid():

            form.save()
            messages.success(request, 'Item atualizado com sucesso')
            return redirect('inventory:item_read')
        else:
            messages.error(request, 'Falha')
            return redirect('inventory:item_read')

    context = {'item': item, 'category': category,
               'store': store, 'b': b, 'c': c, }

    return render(request, 'pages/item/item-update.html', context)


@login_required(login_url='user:login')
def item_delete(request, pk):
    itemDelete = get_object_or_404(Items, id=pk)
    itemDelete.delete()
    return redirect('inventory:item_read')
