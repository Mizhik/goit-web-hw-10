from django.urls import path
from quotes import views
from quotes.views import QuoteAdd, AuthorAdd


app_name = "quotes"

urlpatterns = [
    path("", views.all_quotes, name="all-quotes"),
    path("add-quote/", QuoteAdd.as_view(), name="add-quote"),
    path("add-author/", AuthorAdd.as_view(), name="add-author"),
    path("author/<str:author_name>", views.about_author, name="about-author"),
]
