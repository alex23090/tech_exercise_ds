from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LeadGeneratorForm


def home(request):
    return render(request, 'core/home.html')


@login_required
def lead_generator(request):
    form = LeadGeneratorForm()
    return render(request, 'core/lead-generator.html', {'form': form})
