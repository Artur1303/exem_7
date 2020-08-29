from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from webapp.forms import PolForm, ChoiceForm
from webapp.models import Pol, Choice


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'pols'
    model = Pol
    paginate_by = 2
    ordering = ['-datetime']


class PolView(DeleteView):
    template_name = 'pol_view.html'
    model = Pol

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pol = self.object
        interview = pol.interview.all()
        context['interview'] = interview
        return context


class PolCreatView(CreateView):
    template_name = 'pol_create.html'
    model = Pol
    form_class = PolForm

    def get_success_url(self):
        return reverse('pol_view', kwargs={'pk': self.object.pk})


class PolUpdateView(UpdateView):
    template_name = 'pol_update.html'
    model = Pol
    form_class = PolForm
    context_object_name = 'pols'

    def get_success_url(self):
        return reverse('pol_view', kwargs={'pk': self.object.pk})


class PolDeleteView(DeleteView):
    template_name = 'pol_delete.html'
    model = Pol
    context_object_name = 'pols'
    success_url = reverse_lazy('index')


class PolChoicesCreateView(CreateView):
    model = Choice
    template_name = 'choice_create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        pol = get_object_or_404(Pol, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.interview = pol
        choice.save()
        return redirect('pol_view', pk=pol.pk)


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice_update.html'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('pol_view', kwargs={'pk': self.object.interview.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice_delete.html'


    def get_success_url(self):
        return reverse('pol_view', kwargs={'pk': self.object.interview.pk})


class AnsverList(View):
    def get(self, request, *args, **kwargs):
       self.pol=get_object_or_404(Pol,pk = self.kwargs['pk'])
       



       return redirect('index')