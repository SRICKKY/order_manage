from django import forms

class OrderForm(forms.Form):
	customer_name = forms.CharField(max_length=50)
	item = forms.CharField(max_length=20)
	rate = forms.IntegerField()
	quantity = forms.IntegerField()
	total = forms.IntegerField()