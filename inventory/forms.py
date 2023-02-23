import re
from xml.dom import ValidationErr

from django import forms
from django.core.exceptions import ValidationError

from inventory.models import Category, Items, Store


def strong_password(password):
    regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).*$')

    if not regex.match(password):
        raise ValidationError((
            'Invalid Arguments'
        ),
            code='Invalid'
        )


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ItemsForms(forms.ModelForm):
    # teste = forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(attrs={'teste':'teste'}),
    #     error_messages={'ta maluco?':'a porra de campo tem quer preeenchido caralho'},
    #     help_text=('Precisa de ajuda?')
    # )

    class Meta:
        model = Items
        fields = '__all__'

        labels = {
            'categoryId': 'Categoria',
            'storeId': 'Loja',
            'name': 'Nome',
            'brand': 'Marca',
            'model': 'Modelo',
            'patrimony': 'Patrimonio',
            'obs': 'Obs',
        }
        # exclude = ['categoryId','storeId']
        widgets = {
            'categoryId': forms.Select(attrs={'class': 'form-control'}),
            'storeId': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'patrimony': forms.TextInput(attrs={'class': 'form-control'}),
            'obs': forms.Textarea(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'name': {
                'required': 'Defina um nome ao item',
            }
        }
        help_text = {'name': 'Defina um nome'}


class StoreForms(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
