from allauth.account.views import LoginView, LogoutView, SignupView
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView
from django.views.generic import View

from b_store.settings import DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL
from .forms import UserUpdateForm, ContactForm
from .models import *


class ProductView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(parent_category=None)
        products = Product.objects.all()
        context = {
            'products': products,
            'categories': categories
        }
        return render(request, 'products.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class CategoryView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category_id=pk)
        context['category'] = Category.objects.filter(id=pk)
        context['categories'] = Category.objects.filter(parent_category=None)
        return context


class BaseLoginView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('base')

    def get_success_url(self):
        return self.success_url


class BaseRegisterView(SignupView):
    template_name = 'account/signup.html'
    success_url = reverse_lazy('base')


class BaseLogoutView(LogoutView):
    next_page = reverse_lazy('login')


def profile(request):
    if request.method == "POST":
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if update_user.is_valid():
            update_user.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        update_user = UserUpdateForm(instance=request.user)

    data = {
        'update_user': update_user
    }
    return render(request, 'profile.html', data)


def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "contact.html", {'form': form})


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')
