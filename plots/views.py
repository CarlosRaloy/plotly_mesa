from django.shortcuts import render
from .charts import app

def plot(request, **kwargs):

    context = {
        'plot': app,
    }

    return render(request,'main.html', context)
