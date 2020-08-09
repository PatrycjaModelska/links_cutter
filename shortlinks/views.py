from django.shortcuts import render, reverse, redirect, HttpResponse
from django.views.generic import CreateView, ListView, DetailView
import uuid

from .forms import *

# from django.utils.decorators import method_decorator


# Dwa ważne pliki w tym projekcie!
# Plik Procfile po to aby Herocu wiedziało jak odpalić naszą aplikację. Wskazujemy tam plik wsgi, od którego ma zacząć. 
# W pliku runtime wskazujemy, jakiego pythona chcemy używać w Heroku.

class Create_Short_Link(CreateView):
    model = Link
    form_class = LinkForm
    template_name = "create_short_link.html"

    # @method_decorator(csrf_exempt)
    def form_valid(self, form, *args, **kwargs):
        self.object = form.save(commit=False)
        if not self.object.long_url.startswith(("http://", "https://")):
            self.object.long_url = f"http://{self.object.long_url}"

        link = Link.objects.filter(long_url=self.object.long_url).first()
        if not link:
            self.object.short_url = str(uuid.uuid4())
            self.object.save()
            return super().form_valid(form)

        return HttpResponse("Link już istnieje")

    @property
    def success_url(self):
        return reverse('listoflinks')


class List_Of_Links(ListView):
    model = Link
    template_name = "list_of_links.html"
    context_object_name = "links"


def get_long_url(request, short_url):
    if request.method == "GET":
        qs = Link.objects.filter(short_url=short_url)
        if qs.exists():
            link = qs.first()
            return redirect(link.long_url)
    return HttpResponse("error")