from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy
from vehicleapp.forms import VehiclesForm, OdometerForm, FuelForm, ServiceForm
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from . import models
import os 

def dashboard(request):
    return render(request, 'dashboard.html')

def index(request):
    return render(request, 'succes.html')

class VehicleCreateView(CreateView):
    template_name = os.path.join('vehicleapp','VehiclesCreate.html')
    form_class = VehiclesForm

class OdometerReadingCreate(CreateView):
    template_name = os.path.join('vehicleapp','OdometerReading.html')
    form_class = OdometerForm

class FuelCreateView(CreateView):
    template_name = os.path.join('vehicleapp','FuelLogs.html')
    form_class = FuelForm

class ServiceCreateView(CreateView):
    template_name = os.path.join('vehicleapp','Servicelogs.html')
    form_class = ServiceForm
    

class VehicleDetailView(DetailView):
    model = models.Vehicles
    template_name = os.path.join('detail','vehicle-detail.html')

class OdometerDetailView(DetailView):
    model = models.OdometerReading
    template_name = os.path.join('detail','odometer-detail.html')

class FuelDetailView(DetailView):
    model = models.FuelLog
    template_name = os.path.join('detail', 'fuel-detail.html')

class ServiceDetailView(DetailView):
    model = models.ServiceLog
    template_name = os.path.join('detail', 'service-detail.html')

class VehicleListView(ListView):
    template_name = os.path.join('list', 'vehicle-list.html')
    context_object_name = 'vehicle_list'

    def get_queryset(self):
        return models.Vehicles.objects.order_by('pk')

class VehicleUpdateView(UpdateView):
    form_class = VehiclesForm
    model = models.Vehicles
    template_name = os.path.join('vehicleapp', 'VehiclesCreate.html')

class VehicleDeleteView(DeleteView):
    model = models.Vehicles
    success_url = reverse_lazy('vehicleapp:vehiclelist')
    template_name = os.path.join('vehicleapp', 'vehicles_confirm_delete.html')

class Odometerlist(ListView):
    template_name = os.path.join('list', 'odo-list.html')
    context_object_name = 'odometer_list'

    def get_queryset(self):
        return models.OdometerReading.objects.order_by('pk')

class OdometerUpdate(UpdateView):
    form_class = OdometerForm
    model = models.OdometerReading
    template_name = os.path.join('vehicleapp', 'OdometerReading.html')

class OdometerDelete(DeleteView):
    template_name = os.path.join('vehicleapp', 'odometer_confirm_delete.html')
    model = models.OdometerReading
    success_url = reverse_lazy('vehicleapp:odometer-list')

class FuelList(ListView):
    template_name = os.path.join('list','fuel-list.html')
    context_object_name = 'fuel-list'

    def get_queryset(self):
        return models.FuelLog.objects.order_by('pk')
    
class FuelUpdate(UpdateView):
    form_class = FuelForm
    model = models.FuelLog
    template_name = os.path.join('vehicleapp', 'FuelLogs.html')

class FuelDelete(DeleteView):
    template_name = os.path.join('vehicleapp', 'fuellog_confirm_delete.html')
    model = models.FuelLog
    success_url = reverse_lazy('vehicleapp:fuel-list')

class ServiceList(ListView):
    template_name = os.path.join('list', 'service-list.html')
    context_object_name = 'service-list'

    def get_queryset(self):
        return models.ServiceLog.objects.order_by('pk')

class ServiceUpdate(UpdateView):
    form_class = ServiceForm
    model = models.ServiceLog
    template_name = os.path.join('vehicleapp', 'Servicelogs.html')

class ServiceDelete(DeleteView):
    template_name = os.path.join('vehicleapp', 'service_confirm_delete.html')
    model = models.ServiceLog
    success_url = reverse_lazy('vehicleapp:service-list')