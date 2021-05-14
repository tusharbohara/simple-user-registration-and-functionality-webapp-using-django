import json

from django.contrib.auth import views, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView

from web.forms import ConsumerRegistrationForm
from web.models import Consumer


class Login(views.LoginView):
    template_name = 'registration/login.html'


def register_guest(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        form1 = ConsumerRegistrationForm(request.POST)
        if form1.is_valid() and user_form.is_valid():
            data = form1.cleaned_data
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user_form.save()
            new_user = User.objects.get(username=username)
            new_user.first_name = data['first_name']
            new_user.last_name = data['last_name']
            new_user.email = data['email']
            new_user.save()
            new_consumer = Consumer(first_name=data['first_name'], last_name=data['last_name'],
                                    gender=data['gender'], blood_group=data['blood_group'],
                                    date_of_birth=data['date_of_birth'], marital_status=data['marital_status'],
                                    phone=data['phone'], email=data['email'],
                                    country=data['country'], state=data['state'],
                                    district=data['district'], city=data['city'],
                                    )
            new_consumer.user = new_user
            new_consumer.save()
            return redirect('web:dashboard')
        else:
            user_form = UserCreationForm(request.POST)
            form = ConsumerRegistrationForm(request.POST)
            return render(request, 'web/guest-registration.html', {
                'user_form': user_form,
                'form': form,
            })
    else:
        user_form = UserCreationForm()
        form = ConsumerRegistrationForm()
    return render(request, 'web/guest-registration.html', {'form': form, 'user_form': user_form})


@login_required(login_url='/')
def dashboard(request):
    return render(request, 'web/index.html', {})


@login_required(login_url="/login/")
def profile(request):
    if not request.user.is_superuser:
        con = Consumer.objects.get(pk=request.user.id)
        context = {
            "person": con,
        }
    else:
        context = {}
    return render(request, 'web/profile.html', context)


class PasswordChange(views.PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('web:profile')


@login_required(login_url='/')
def register_user(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        form = ConsumerRegistrationForm(request.POST)
        if form.is_valid() and user_form.is_valid():
            data = form.cleaned_data
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user_form.save()
            new_user = User.objects.get(username=username)
            new_user.first_name = data['first_name']
            new_user.last_name = data['last_name']
            new_user.email = data['email']
            new_user.save()
            new_con = Consumer(first_name=data['first_name'], last_name=data['last_name'],
                               gender=data['gender'], blood_group=data['blood_group'],
                               date_of_birth=data['date_of_birth'], marital_status=data['marital_status'],
                               phone=data['phone'], email=data['email'],
                               country=data['country'], state=data['state'],
                               district=data['district'], city=data['city'],
                               )
            new_con.user = new_user
            new_con.save()
            return redirect('web:dashboard')
        else:
            user_form = UserCreationForm(request.POST)
            form = ConsumerRegistrationForm(request.POST)
            return render(request, 'web/register-user.html', {
                'user_form': user_form,
                'form': form,
            })
    else:
        user_form = UserCreationForm()
        form = ConsumerRegistrationForm()
    return render(request, 'web/register-user.html', {'form': form, 'user_form': user_form})


class UserList(PermissionRequiredMixin, ListView):
    permission_required = 'web.view_consumer'
    raise_exception = True

    template_name = 'web/view-user.html'
    model = Consumer

    # def get_queryset(self):
    #     if self.request.user.is_superuser or self.request.user.is_staff:
    #         return Consumer.objects.all()
    #     else:
    #         return Consumer.objects.filter(user=self.request.user)


class UserDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'web.view_consumer'
    raise_exception = True

    model = Consumer
    template_name = 'web/detail-user.html'


class UserUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'web.change_consumer'
    raise_exception = True

    model = Consumer
    fields = ('first_name', 'last_name',
              'gender', 'date_of_birth', 'marital_status',
              'blood_group',
              'country', 'state', 'district', 'city',
              'phone', 'email',
              )
    template_name = 'web/update-user.html'

    def get_success_url(self):
        return reverse('web:userDetail', kwargs={"pk": self.kwargs["pk"]})


@permission_required('web.delete_consumer', raise_exception=True)
@login_required(login_url="/")
def delete_user(request):
    if request.method == "POST":
        con = Consumer.objects.get(pk=request.POST["id"])
        user = User.objects.get(pk=request.POST["id"])
        con.delete()
        user.delete()
        response_data = {}
        response_data['msg'] = 'User Delete Successfull.'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        resp_data = {}
        resp_data['msg'] = 'User Delete UnSuccessfull.'
        return HttpResponse(
            json.dumps(resp_data),
            content_type="application/json"
        )
