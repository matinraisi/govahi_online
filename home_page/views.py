from django.shortcuts import render


# Create your views here.
def home_page(request ):
    return render(request ,'home_page/home.html')
    
    
# def search1(request):
#     return render(request ,'home_page/download.html')
    

# def search(request):
    
#     form = SearchForm(request.GET)

#     if form.is_valid():
#         national_id = form.cleaned_data['national_id']
#         try:
#             result = NationalID.objects.get(national_id=national_id)
#             return render(request, 'home_page/download.html', {'result': result})
#         except NationalID.DoesNotExist:
#             form.add_error('national_id', 'شماره ملی پیدا نشد.')

#     return render(request, 'home_page/search.html', {'form': form})