from django import forms

# class CvetyFilterForm(forms.Form):
#     min_price = forms.IntegerField(label="от", required=False)
#     max_price = forms.IntegerField(label="до", required=False)
#     ordering = forms.ChoiceField(label="сортировка", required=False, choices=[
#         ["name", "по алфавиту"], ["price", "Дешевле с верху"], ["-price", "Дорогие сверху"]
#         ])