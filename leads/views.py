from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import LeadForm, LeadModelForm
from .models import Agent, Lead

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


def lead_create(request):
    """  Lead create views """
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)


def lead_update(request, pk):
    """  Lead update views """
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {
        "form": form,
        "lead": lead,
    }
    return render(request, "leads/lead_update.html", context)


def lead_delete(request, pk):
    """  Lead delete views """
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')


# def lead_update(request, pk):
#     """  Lead update views """
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect('/leads')

    # context = {
    #     "form": form,
    #     "lead": lead,
    # }
#     return render(request, "leads/lead_update.html", context)


# def lead_create(request):
    # """  Lead create views """
    # form = LeadForm()
    # if request.method == "POST":
    #     form = LeadForm(request.POST)
    #     if form.is_valid():
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         age = form.cleaned_data['age']
    #         agent = Agent.objects.first()
    #         Lead.objects.create(
    #             first_name=first_name,
    #             last_name=last_name,
    #             age=age,
    #             agent=agent
    #         )
    #         return redirect('/leads')

    # context = {
    #     "form": form
    # }
#     return render(request, "leads/lead_create.html", context)
