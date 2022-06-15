from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from recetas.models import receta_1a3, receta_4a6, receta_7a10
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import receta_1a3, receta_4a6, receta_7a10
from recetas.forms import FormCrearReceta_1a3, FormCrearReceta_4a6, FormCrearReceta_7a10
from django.contrib.auth.mixins import LoginRequiredMixin

########################################################## CREATE VIEW ########################################################################

class CrearReceta_1a3(LoginRequiredMixin, CreateView):
    model = receta_1a3
    form_class = FormCrearReceta_1a3
    template_name = 'crear_receta_1a3.html'
    success_url = reverse_lazy('recetas:lista_recetas')
    login_url = reverse_lazy('users_app:user_login')

class CrearReceta_4a6(LoginRequiredMixin, CreateView):
    model = receta_4a6
    form_class = FormCrearReceta_4a6
    template_name = 'crear_receta_4a6.html'
    success_url = reverse_lazy('recetas:lista_recetas')
    login_url = reverse_lazy('users_app:user_login')

class CrearReceta_7a10(LoginRequiredMixin, CreateView):
    model = receta_7a10
    form_class = FormCrearReceta_7a10
    template_name = 'crear_receta_7a10.html'
    success_url = reverse_lazy('recetas:lista_recetas')
    login_url = reverse_lazy('users_app:user_login')

########################################################### LIST VIEW ########################################################################

class ListaRecetas(LoginRequiredMixin, ListView):
    model = receta_1a3
    template_name= 'recetas.html'
    login_url = reverse_lazy('users_app:user_login')
    
    def get_context_data(self):
        context = {}
        lista_recetas_1a3 = receta_1a3.objects.all()
        lista_recetas_4a6 = receta_4a6.objects.all()
        lista_recetas_7a10 = receta_7a10.objects.all()
        context['lista_recetas_1a3'] = lista_recetas_1a3
        context['lista_recetas_4a6'] = lista_recetas_4a6
        context['lista_recetas_7a10'] = lista_recetas_7a10
        return context


########################################################### DETAIL VIEW ######################################################################

class DetailReceta_1a3(LoginRequiredMixin, DetailView):
    model = receta_1a3
    template_name = 'detail_receta_1a3.html'
    login_url = reverse_lazy('users_app:user_login')

class DetailReceta_4a6(LoginRequiredMixin, DetailView):
    model = receta_4a6
    template_name = 'detail_receta_4a6.html'
    login_url = reverse_lazy('users_app:user_login')

class DetailReceta_7a10(LoginRequiredMixin, DetailView):
    model = receta_7a10
    template_name = 'detail_receta_7a10.html'
    login_url = reverse_lazy('users_app:user_login')

########################################################### DELETE VIEW ######################################################################

class EliminarReceta_1a3(LoginRequiredMixin, DeleteView):
    model = receta_1a3
    template_name = 'eliminar_receta_1a3.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_success_url(self):
        return reverse('recetas:lista_recetas')

class EliminarReceta_4a6(LoginRequiredMixin, DeleteView):
    model = receta_4a6
    template_name = 'eliminar_receta_4a6.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_success_url(self):
        return reverse('recetas:lista_recetas')

class EliminarReceta_7a10(LoginRequiredMixin, DeleteView):
    model = receta_7a10
    template_name = 'eliminar_receta_7a10.html'
    login_url = reverse_lazy('users_app:user_login')

    def get_success_url(self):
        return reverse('recetas:lista_recetas')

########################################################### UPDATE VIEW ######################################################################


class ActualizarReceta_1a3(LoginRequiredMixin, UpdateView):
    model = receta_1a3
    template_name = 'actualizar_receta_1a3.html'
    fields = '__all__'
    login_url = reverse_lazy('users_app:user_login')

    def get_success_url(self):
        return reverse('recetas:detail_receta_1a3', kwargs = {'pk':self.object.pk})

class ActualizarReceta_4a6(LoginRequiredMixin, UpdateView):
    model = receta_4a6
    template_name = 'actualizar_receta_4a6.html'
    fields = '__all__'
    login_url = reverse_lazy('users_app:user_login')

    def get_success_url(self):
        return reverse('recetas:detail_receta_4a6', kwargs = {'pk':self.object.pk})

class ActualizarReceta_7a10(LoginRequiredMixin, UpdateView):
    model = receta_7a10
    template_name = 'actualizar_receta_7a10.html'
    fields = '__all__'
    login_url = reverse_lazy('users_app:user_login')

    def get_success_url(self):
        return reverse('recetas:detail_receta_7a10', kwargs = {'pk':self.object.pk})

########################################################### FUNCION BUSCAR ######################################################################


def buscar_receta_1a3(request):
    recetas = receta_1a3.objects.filter(nombre__icontains=request.GET['search'])
    if recetas.exists():
        context = {'recetas':recetas}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'buscar_receta_1a3.html', context = context)

def buscar_receta_4a6(request):
    recetas = receta_4a6.objects.filter(nombre__icontains=request.GET['search'])
    if recetas.exists():
        context = {'recetas':recetas}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'buscar_receta_4a6.html', context = context)

def buscar_receta_7a10(request):
    recetas = receta_7a10.objects.filter(nombre__icontains=request.GET['search'])
    if recetas.exists():
        context = {'recetas':recetas}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'buscar_receta_7a10.html', context = context)



