from django.shortcuts import render
import csv
from django.http import HttpResponse
from django.core import serializers
from django.template.loader import get_template
#from xhtml2pdf import pisa

from .models import Project


def index(request):
    return render(request,'index.html')

def project(request):
    return render(request,'project.html')

def chart(request):
    projects = Project.objects.all()
    return render(request,'chart.html', {'projects': projects})

def projects_view(request):
    query = request.GET.get('q', '')
    location=request.GET.get('lga', '')
    projects = Project.objects.all()
    if query:
        projects = Project.objects.filter(contract_title__icontains=query)
    if location:
        projects = Project.objects.filter(lga__icontains=location)
    return render(request,'project.html', {'projects': projects})

def export_csv(request):
    query = request.GET.get('q', '')
    location=request.GET.get('location', '')
    projects = Project.objects.all()
    if query:
        projects = Project.objects.filter(contractor__icontains=query)
    if location:
        projects = Project.objects.filter(location__icontains=location)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="projects.csv"'

    writer = csv.writer(response)
    writer.writerow(['contract_title', 'budget_amount', 'contract_amount', 'contractor','lga','mda'])

   
    for project in projects:
        writer.writerow([project.contract_title, project.budget_amount, project.contract_amount, project.contractor, project.mda])

    return response

# def export_pdf(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="projects.pdf"'

#     projects = Project.objects.all()
#     template = get_template('project_pdf.html')
#     html = template.render({'projects': projects})

#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

def export_json(request):

    query = request.GET.get('q', '')
    location=request.GET.get('location', '')
    projects = Project.objects.all()
    if query:
        projects = Project.objects.filter(contractor__icontains=query)
    if location:
        projects = Project.objects.filter(location__icontains=location)

    response = HttpResponse(content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="projects.json"'

  
    data = serializers.serialize('json', projects)
    response.write(data)

    return response



