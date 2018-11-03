from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'Ask_Gel0/main_page.html', {})