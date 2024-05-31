from django.shortcuts import render, redirect
from.forms import RegisterForm
from django.views.generic import View

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

class RegisterView(View):
    template_name = 'users/register.html'

    def get(self, request):
        return render(request, self.template_name)