from django.forms import ModelForm, CharField
from quotes.models import Quote, Author


class QuoteForm(ModelForm):
    author = CharField(max_length=200)

    class Meta:
        model = Quote
        fields = ["quote", "tags"]

    def clean_author(self):
        author_name = self.cleaned_data["author"]
        author, _ = Author.objects.get_or_create(fullname=author_name)
        return author


class AuthorForm(ModelForm):
    fullname = CharField(required=True)
    born_date = CharField(max_length=50, min_length=20, required=True)
    born_location = CharField(max_length=50, min_length=20, required=True)
    description = CharField(required=True)

    class Meta:
        model = Author
        fields = ("fullname", "born_date", "born_location", "description")
