from django.shortcuts import render
from django.http import HttpResponse

def table(request, number, count):
    if number < 1 or count < 1:
        return HttpResponse("Both number and count must be greater than zero.", status=400)
    
    result = []
    for i in range(1, count + 1):
        result.append(f"{number} * {i} = {number * i}")
    
    context = {
        'number': number,
        'count': count,
        'result': result
    }
    
    return render(request, 'tables/table.html', context)
