from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, UserRegisterForm


def userRegister(request):

    dados = request.session.get('dados')
    form = UserRegisterForm(dados)
    return render(request, 'user/user-register.html', {'form': form})


def userCreate(request):
    if not request.POST:
        raise Http404
    POST = request.POST
    request.session['dados'] = POST
    form = UserRegisterForm(POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Usuario criado com sucesso')
        del (request.session['dados'])

    return redirect('user:user_register')


def loginView(request):
    form = LoginForm()
    return render(request, 'user/login.html', {
        'form': form,
        'form_action': reverse('user:login_create')
    })


def loginCreate(request):

    if not request.POST:
        raise Http404

    form = LoginForm(request.POST)
    login_url = reverse('user:login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),

        )
        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect('inventory:home')
        else:
            messages.error(request, 'Invalid credentials')
    else:
        messages.error(request, 'Invalid username or password')

    return redirect(login_url)


@login_required(login_url='user:login')
def logoutUser(request):
    if not request.POST:
        return redirect(reverse('user:login'))
    logout(request)
    return redirect(reverse('user:login'))
