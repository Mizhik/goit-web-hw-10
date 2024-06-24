from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views import View
from .forms import QuoteForm, AuthorForm
from .models import Quote, Author


def all_quotes(request):
    data = Quote.objects.all()
    per_page = 10
    paginator = Paginator(data, per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "quotes/all-quotes.html", {"page_obj": page_obj})


def about_author(request, author_name: str):
    author = get_object_or_404(Author, fullname=author_name)
    return render(request, "quotes/about-author.html", context={"author": author})


# def all_quotes(request):
#     quotes = Quote.objects.all()
#     return render(request, "quotes/all-quotes.html", context={"quotes": quotes})


class QuoteAdd(View):
    template_name = "quotes/add-quote.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": QuoteForm()})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            author_name = form.cleaned_data["author"]
            author, _ = Author.objects.get_or_create(fullname=author_name)
            quote.author = author
            quote.save()
            return redirect(to="quotes:all-quotes")
        else:
            return render(request, self.template_name, {"form": form})


class AuthorAdd(View):
    template_name = "quotes/add-author.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": AuthorForm()})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:all-quotes")
        else:
            return render(request, self.template_name, {"form": form})
