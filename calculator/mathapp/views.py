from django.shortcuts import render

def calculate_power(request):
    power = None
    i = ''
    r = ''
    
    if request.method == 'POST':
        try:
            i = float(request.POST.get('intensity', 0))
            r = float(request.POST.get('resistance', 0))
            power = i ** 2 * r
        except (ValueError, TypeError):
            power = "Invalid input"

    context = {
        'i': i,
        'r': r,
        'power': power
    }

    return render(request, 'power_calc.html', context)
 