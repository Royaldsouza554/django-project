# Create your views here.
# views.py
from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import csv
from io import BytesIO
from reportlab.pdfgen import canvas


def search(request):
    query = request.GET.get('q')
    if query:
        if len(query) > 20:
            # Query length validation failed
            return render(request, 'search.html', {'error': 'Search query must be 20 characters or less'})
        else:
        
            results = Book.objects.filter(title__icontains=query).prefetch_related('authors')

        return render(request, 'search_results.html', {'results': results, 'query': query})
    else:
        return render(request, 'search.html', {'error': 'Please enter a search query'})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponse('Thank you for the feedback')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})

def custom_contact(request):
    form = ContactForm()
    return render(request, 'custom_contact_form.html', {'form': form})

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

# Create view for a Book
class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'publication_date', 'authors', 'publisher']
    success_url = reverse_lazy('book-list')

# Update view for a Book
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'publication_date', 'authors', 'publisher']
    success_url = reverse_lazy('book-list')

# Delete view for a Book
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')    

def export_books_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    #This initializes a CSV writer object that will write to the HttpResponse object
    writer = csv.writer(response) 

    # Write the header row
    writer.writerow(['Title', 'Publication Date', 'Publisher'])

    # Write data rows
    books = Book.objects.all()
    for book in books:
        writer.writerow([book.title, book.publication_date, book.publisher.name])

    return response




from django.http import HttpResponse
from reportlab.pdfgen import canvas

def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hello.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    return response

