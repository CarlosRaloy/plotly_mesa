from django.shortcuts import render

from django_plotly_dash import DjangoDash
from .database import hola
from dash import dcc
from dash import html, dash_table
import dash_mantine_components as dmc
from datetime import date
from . import charts

import logging
from django.views.generic import TemplateView
logger = logging.getLogger(__name__)

class Plot1DView(TemplateView):
    template_name = "main.html"
    def get_context_data(self, **kwargs):
        context = super(Plot1DView, self).get_context_data(**kwargs)
        context['plot'] = charts.plot1d()
        return context
class Plot2DView(TemplateView):
    template_name = "avg_times.html"
    def get_context_data(self, **kwargs):
        context = super(Plot2DView, self).get_context_data(**kwargs)
        context['plot2'] = charts.avg_times()
        return context