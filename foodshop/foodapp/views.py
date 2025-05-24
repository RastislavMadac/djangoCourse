from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
 

# Create your views here. 

def index(request): 

    return render(request, 'foodapp/index.html') 

def register(request): 

    if request.method == 'POST': 

        # vezmi data z formuláře, validuj a ulož do tabulky auth_user 

        form = CustomUserCreationForm(request.POST) 

        if form.is_valid(): 

            form.save() 

            return redirect('login')  # po registraci přesměrujme na přihlášení 

    else: 

        form = CustomUserCreationForm() 

        return render(request, 'foodapp/register.html', { 

            'form': form, 

        }) 

 

 
