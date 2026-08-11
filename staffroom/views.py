from django.shortcuts import render
from django.views.generic import TemplateView


class StaffroomTemplateView(TemplateView):
    template_name = "staffroom/index.html"
