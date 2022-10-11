from django.views.generic import TemplateView
from django.urls import reverse


class IndexView(TemplateView):

    template_name = "index.html"

    def get_success_url(self):
        return reverse("index")