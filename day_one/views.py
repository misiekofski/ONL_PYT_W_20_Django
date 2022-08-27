from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show_number(request, number):
    answer = f"""
    <html>
        <body>
        <p>The answer is {number}!</p>
        </body>
    </html>
    """

    return HttpResponse(answer)
