from django.forms import ModelForm
from django import forms
from .models import Vehicles, OdometerReading, FuelLog, ServiceLog
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row,Column, HTML
from crispy_forms.bootstrap import Tab, TabHolder

class VehiclesForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = "__all__"
        # widgets = {"tags": }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                    Row(
                        Column(HTML("<h4>Basic</h4>"),css_class='col-6'),
                    ),
                    Row(
                        Column('model', 'license_plate', 'tags',
                            css_class='form_group col-md-6'),
                        
                        Column('number_of_seats','location', 'number_of_doors',css_class='form_group col-md-6'),
                    ),
                    Row(
                        Column(HTML("<h4>Properties</h4>"),css_class='col-6'),
                        Column(HTML("<h4>Advanced</h4>"),css_class='col-6')
                    ),
                    Row(
                        Column( 'driver', 'chasis_number','color', 'model_year',css_class='form_group col-md-6'),
                        Column('last_odometer', 'first_contract_date',
                            'residual_value',css_class='form_group col-md-6'),
                    ),
                    Row(
                        Column(HTML("<h4>Performance Options</h4>"),css_class='col-6'),
                    ),
                    Row(
                        Column('transmission',
                    'fuel_type',
                    'horsepower',
                    'power',css_class='form_group col-md-6'),
                    )
                )
        self.helper.add_input(Submit('submit', "Submit"))

class OdometerForm(forms.ModelForm):
    class Meta:
        model = OdometerReading
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', "Submit"))

class FuelForm(forms.ModelForm):
    class Meta:
        model = FuelLog
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                    Row(
                        Column(HTML("<h4>Vehicle Details</h4>"),css_class='col-6'),
                        Column(HTML("<h4>Pesonal Details</h4>"),css_class='col-6'),
                    ),
                    Row(
                        Column('vehicle', 'liter', 'Price_per_litre','total_price','odometer_Value',
                            css_class='form_group col-md-6'),
                        
                        Column('date','purchaser', 'invoice_reference','vendor', css_class='form_group col-md-6'),
                    ),
        )
        self.helper.add_input(Submit('submit', "Submit"))

class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceLog
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                    Row(
                        Column(HTML("<h4>Vehicle Details</h4>"),css_class='col-6'),
                        Column(HTML("<h4>Pesonal Details</h4>"),css_class='col-6'),
                    ),
                    Row(
                        Column('vehicle', 'service_type','total_price','odometer_Value',
                            css_class='form_group col-md-6'),
                        
                        Column('date','purchaser', 'invoice_reference', 'vendor', css_class='form_group col-md-6'),
                    ),
        )
        self.helper.add_input(Submit('submit', "Submit"))
    