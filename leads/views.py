from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create views.


def lead_list(request):
    """  Lead detail views """
    leads = Lead.objects.all()
    context = {
        "leads": leads,
    }
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pk):
    """  Lead list views """
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead,
    }
    return render(request, "leads/lead_detail.html", context)
