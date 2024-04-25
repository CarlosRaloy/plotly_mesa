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


class Plot3DView(TemplateView):
    template_name = "improve.html"

    def get_context_data(self, **kwargs):
        context = super(Plot3DView, self).get_context_data(**kwargs)
        context['plot3'] = charts.calculate_improve()
        return context
    

class Plot4DView(TemplateView):
    template_name = "dash.html"

    def get_context_data(self, **kwargs):
        context = super(Plot4DView, self).get_context_data(**kwargs)
        context['plot5'] = charts.dashboard()
        return context
    

class Plot5DView(TemplateView):
    template_name = "companies.html"

    def get_context_data(self, **kwargs):
        context = super(Plot5DView, self).get_context_data(**kwargs)
        context['plot5'] = charts.company()
        return context