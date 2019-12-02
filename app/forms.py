from app.models import Booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Fieldset, Layout, Submit, HTML, Row, Div, Column)
from django import forms
from . import models

class BookingForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Booking
        widgets = {"adventure": forms.HiddenInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
        )
        self.helper.add_input(Submit('submit', "Submit"))   