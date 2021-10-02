from django import forms
from .models import Pizza, Size

# class PizzaForm(forms.Form):
#   toppings = forms.MultipleChoiceField(choices=[('pep', 'Pepperoni'), ('cheese', 'Cheese'), ('olv', 'Olives')], widget=forms.CheckboxSelectMultiple)
#   topping1 = forms.CharField(label='Topping1', max_length=100, widget=forms.TextInput)
#   topping2 = forms.CharField(label='Topping2', max_length=100)
#   topping3 = forms.CharField(label='Topping3', max_length=100)
#   size = forms.ChoiceField(label='Size', choices=[('Small','Small'), ('Medium','Medium'), ('Large','Large')])


class PizzaForm(forms.ModelForm):

  size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)


  class Meta:
    model = Pizza
    fields = ['topping1', 'topping2', 'topping3', 'size']
    labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2', 'topping3': 'Topping 3'}
    





