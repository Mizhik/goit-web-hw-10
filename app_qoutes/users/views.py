from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from users.forms import RegisterForm


class RegisterView(View):
    template_name = "users/register.html"
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quotes:all-quotes")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            messages.success(
                request,
                f"Congratulations, {username}! You have successfully registered",
            )
            return redirect(to="users:login")
        return render(request, self.template_name, {"form": form})
