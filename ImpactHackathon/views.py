from ImpactHackathon.models import Demand, Sales
from django.shortcuts import render
from datetime import date, datetime, timedelta
from django.db.models import Count, Sum, Avg
from django.http import HttpResponseRedirect

def dashboardView(request):
    template_name = 'index.html'

    month = []
    year = []
    sales = Sales.objects.all().order_by('salesDate')
    crop = Sales.objects.values('cropName').distinct()
    average = Sales.objects.values('cropName').annotate(total_sales=Sum('quantity'))
    for s in sales:
        month.append(s.salesDate.month)
        year.append(s.salesDate.year)

    print(average)
    return render(request, template_name, context={'year': year, 'month': month, 'sales': sales, 'crop': crop, 'average': average})

def avgPriceView(request):
    template_name = 'averageprice.html'


    sales = Sales.objects.all().order_by('salesDate')
    crop = Sales.objects.values('cropName').distinct()
    average = Sales.objects.values('cropName').annotate(total_sales=Sum('quantity'))

    averagedate = Demand.objects.filter(orderDate__month='07', orderDate__year='2020')
    avgprice = Demand.objects.values('cropName').filter(orderDate__month='07', orderDate__year='2020').annotate(average_price=Avg('unitPrice'))
    print(avgprice)

    print(average)
    return render(request, template_name,
                  context={'sales': sales, 'crop': crop, 'average': average, 'avgprice': avgprice, 'averagedate': averagedate})

def cropCycleView(request):
    template_name = 'cropcycle.html'

    sales = Sales.objects.all().order_by('salesDate')
    crop = Sales.objects.values('cropName').distinct()
    average = Sales.objects.values('cropName').annotate(total_sales=Sum('quantity'))
    demand = Demand.objects.values('cropName', 'orderDate__month').annotate(average_price=Sum('quantity'))
    kangkongdemand = Demand.objects.values('cropName', 'orderDate__month').annotate(average_price=Sum('quantity')).order_by('-average_price').filter(cropName='Kangkong').first()
    potatodemand = Demand.objects.values('cropName', 'orderDate__month').annotate(average_price=Sum('quantity')).order_by('-average_price').filter(cropName='Potato').first()

    kangkongplant = Demand.objects.filter(cropName='Kangkong', orderDate__month='7', orderDate__year='2020').order_by('orderDate').first()
    kangkongplantday = kangkongplant.orderDate - timedelta(days=14)
    potatoplant = Demand.objects.filter(cropName='Potato', orderDate__month='7', orderDate__year='2020').order_by(
        'orderDate').first()
    potatoplantday = potatoplant.orderDate - timedelta(days=70)
    return render(request, template_name, context={'sales': sales, 'crop': crop, 'average': average, 'demand': demand, 'potatodemand': potatodemand, 'kangkongdemand': kangkongdemand,
                                                   'kangkongplant': kangkongplantday, 'potatoplant': potatoplantday})

def inventoryView(request):
    template_name = 'inventory.html'

    crop = Sales.objects.values('cropName').distinct()
    sales = Sales.objects.values('cropName').filter(salesDate__month='7', salesDate__year='2020').annotate(total_sales=Sum('quantity'))
    demand = Demand.objects.values('cropName').filter(orderDate__month='7', orderDate__year='2020').annotate(total_stock=Sum('quantity'), price=Avg('unitPrice'))


    return render(request, template_name, context={'sales': sales, 'crop': crop, 'demand': demand})

def salesordersView(request):
    template_name = 'salesorders.html'

    if request.method == 'POST':
        salesID = request.POST.get('salesID')
        request.session['salesID'] = salesID
        return HttpResponseRedirect("/invoice/")

    crop = Sales.objects.values('cropName').distinct()
    sales = Demand.objects.filter(orderDate__month='7', orderDate__year='2020')
    demand = Demand.objects.values('cropName').filter(orderDate__month='7', orderDate__year='2020').annotate(total_stock=Sum('quantity'), price=Avg('unitPrice'))


    return render(request, template_name, context={'sales': sales, 'crop': crop, 'demand': demand})

def salesinvoiceView(request):
    template_name = 'invoice.html'

    salesID = request.session['salesID']
    crop = Sales.objects.values('cropName').distinct()
    sales = Demand.objects.get(id=salesID)
    demand = Demand.objects.values('cropName').filter(orderDate__month='7', orderDate__year='2020').annotate(total_stock=Sum('quantity'), price=Avg('unitPrice'))


    return render(request, template_name, context={'sales': sales, 'crop': crop, 'demand': demand, 'salesID': salesID})

def indexView(request):
    template_name = 'dashboard.html'

    return render(request, template_name)

def coopdashboardView(request):
    template_name = 'coopdashboard.html'

    return render(request, template_name)

def loginView(request):
    template_name = 'login.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        if username == 'restaurant':
            return HttpResponseRedirect('/index/')
        elif username == 'coop':
            return HttpResponseRedirect('/coopdashboard/')
    return render(request, template_name)
