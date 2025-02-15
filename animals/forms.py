# animals/forms.py

from django import forms

class SimulatorForm(forms.Form):
    temperature = forms.IntegerField(label='Температура (°C)', min_value=-50, max_value=50)
    food_availability = forms.IntegerField(label='Наличие пищи (%)', min_value=0, max_value=100)
    humidity = forms.IntegerField(label='Влажность (%)', min_value=0, max_value=100)