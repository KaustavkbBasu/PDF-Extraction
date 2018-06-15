from django.shortcuts import render
import PyPDF2
from ext.models import Pdf
from ext.forms import PdfForm,forms
import pdfkit
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, createStringObject
from django.http import HttpResponse
from django.views.generic import View
from ext.utils import render_to_pdf
from django.template.loader import get_template
# Create your views here.
def show_pdf(request):
    inpfn = 'Resume_KaustavBasu.pdf'
    pdfFileObject = open('Resume_KaustavBasu.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    count = pdfReader.numPages
    for i in range(count):
        page = pdfReader.getPage(i)
        content = page.extractText()

    # print(content)
    # pdf_toread = PdfFileReader(open("Programming Assignment.pdf", "rb"))
    pdf_info = pdfReader.getDocumentInfo()
    # print(type(pdf_info))
    # print(pdf_info)
    # author = pdf_info.author

    pdf = Pdf()
    form = PdfForm()
    if request.method == "POST":
        form = PdfForm(request.POST)
        if form.is_valid():
    # print(creator)
            pdf.author = pdf_info.author
            pdf.title = pdf_info.title
            pdf.subject = pdf_info.subject
                    # pdf.keywords = pdf_info.keywords
                        # pdf.created = pdf_info.CreationDate
                        # pdf.modified = pdf_info.ModDate
            pdf.Creator = pdf_info.creator
            pdf.Producer = pdf_info.producer
            pdf.content = form.cleaned_data['content']
            pdf.save()
            # pdfFileObject.close()

    # template = get_template('invoice.html')
    # context = pdf.content
    # html = template.render(context)
    # pdf = render_to_pdf('invoice.html', context)
    # if pdf:
    #     response = HttpResponse(pdf, content_type='application/pdf')
    #     filename = "Invoice_%s.pdf" %("12341231")
    #     content = "inline; filename='%s'" %(filename)
    #     download = request.GET.get("download")
    #     if download:
    #         content = "attachment; filename='%s'" %(filename)
    #         response['Content-Disposition'] = content
    #     return response
    # return HttpResponse("Not found")

    return render(request,'ext/about.html', {'content': content})

class GeneratePDF(View):


    def get(self, request, *args, **kwargs):
        info = Pdf.objects.values_list('content', flat=True)
        # print(info)
        template = get_template('invoice.html')
        context = {
             "invoice_id": 123,
             "customer_name": info,
             "amount": 1399.99,
             "today": "Today",
         }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            # fin = open('Programming Assignment.pdf', 'rb')
            # reader = PdfFileReader(fin)
            #
            # writer.appendPagesFromReader(reader)
            # metadata = reader.getDocumentInfo()
            # writer.addMetadata(metadata)
            #
            # # Write your custom metadata here:
            # # writer.addMetadata({
            # #     '/Some': 'Example'
            # # })
            #
            # fout = open(filename, 'wb')
            # writer.write(fout)
            #
            # fin.close()
            # fout.close()
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

    # def metadata(self):
    #     fin = open('Programming Assignment.pdf', 'rb')
    #     reader = PdfFileReader(fin)
    #
    #     writer.appendPagesFromReader(reader)
    #     metadata = reader.getDocumentInfo()
    #     writer.addMetadata(metadata)
    #
    #     # Write your custom metadata here:
    #     # writer.addMetadata({
    #     #     '/Some': 'Example'
    #     # })
    #
    #     fout = open('result.pdf', 'wb')
    #     writer.write(fout)
    #
    #     fin.close()
    #     fout.close()
