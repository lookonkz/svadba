from  django import  forms
from  .models import Order
from cvety.models import Cvety

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "phone"]
