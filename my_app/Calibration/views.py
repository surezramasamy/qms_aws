from django.shortcuts import render
from django.http import HttpResponse
from .models import Instruments_List,Fixture_List
from django.views.generic import (ListView)
from datetime import datetime
import datetime
from .utils import get_plot,get_plot1,get_plot2,get_plot3,get_plot4
from django.db.models import Count
from django.db.models.functions import ExtractMonth
import io, base64
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from django.db.models import Q


class Basic(ListView):
    context_object_name = 'Info'
    template_name=  'home.html'



'''Fixtures and templates'''

def cal(request):    
    
    queryset = Fixture_List.objects.order_by('Status').values('Status').annotate(count=Count('Description'))
    y = list(queryset.values_list('count', flat=True))
    x = list(queryset.values_list('Status', flat=True))
    chart=get_plot(x,y)

    queryset1 = Fixture_List.objects.order_by('Location_used').values('Location_used').annotate(count=Count('Description'))
    y1 = list(queryset1.values_list('count', flat=True))
    x1 = list(queryset1.values_list('Location_used', flat=True))
    chart1=get_plot1(x1,y1)

    queryset5 = Fixture_List.objects.order_by('Location_used').values('Location_used').annotate(Fixtures=Count('Status'))
    dframe1 = pd.DataFrame(queryset5.values("Location_used","Status","Fixtures"))
    dframe2=dframe1.pivot(index='Location_used', columns='Status').fillna(0)
    dframe1 = dframe1.to_html()
    dframe4 = dframe2.to_html()
    graph5 = get_plot4(dframe2)




    queryset2=Fixture_List.objects.order_by("Verification_Plan").annotate(Plan=Count('id'))
    x2 = list(queryset2.values_list('Verification_Plan', flat=True))
    y2 = list(queryset2.values_list('Plan', flat=True))
    df = pd.DataFrame(queryset2.values("Verification_Plan","Plan"))
    df['month2'] = pd.to_datetime(df['Verification_Plan']).dt.to_period('M')
    df1 = df.to_html()

    queryset3=Fixture_List.objects.order_by("Verified_on").annotate(Actual=Count('id'))
    x3 = list(queryset3.values_list('Verified_on', flat=True))
    y3 = list(queryset3.values_list('Actual', flat=True))
    df2 = pd.DataFrame(queryset3.values("Verified_on","Actual"))
    df2['month2'] = pd.to_datetime(df2['Verified_on']).dt.to_period('M')
    df3 = df2.to_html()

    df4=pd.concat([df, df2]).groupby(['month2']).sum().reset_index()
    df6=df4.set_index('month2')
    df5 = df6.to_html()
    graph = get_plot2(df4)

    qs4 = Fixture_List.objects.order_by('Verification_Freq').values('Verification_Freq').annotate(count=Count('Description'))
    qs5 = pd.DataFrame(qs4.values("Verification_Freq","count"))
    df7=qs5.set_index("Verification_Freq")
    df8 = df7.to_html()
    graph2 = get_plot3(df7)


    context = {
        'chart': chart,
        'chart1': chart1,
        'graph' : graph,
        'graph2' : graph2,
        'graph5' : graph5,
        #
        'df1': df1,
        'df3': df3,
        'df5': df5,
        'df8': df8,
        'dframe4':dframe4,
    }
    return render(request,"cal.html",context)

'''Instruments '''

from .utils import get_plot5,get_plot6

def cal2(request):
    queryset = Instruments_List.objects.order_by('Status').values('Status').annotate(count=Count('Description'))
    y = list(queryset.values_list('count', flat=True))
    x = list(queryset.values_list('Status', flat=True))
    chart=get_plot5(x,y)

    
    queryset2=Instruments_List.objects.order_by("Calibration_Plan").annotate(Plan=Count('id'))
    x2 = list(queryset2.values_list('Calibration_Plan', flat=True))
    y2 = list(queryset2.values_list('Plan', flat=True))
    df = pd.DataFrame(queryset2.values("Calibration_Plan","Plan"))
    df['month2'] = pd.to_datetime(df['Calibration_Plan']).dt.to_period('M')
    df1 = df.to_html()

    queryset3=Instruments_List.objects.order_by("Date_of_Calibration").annotate(Actual=Count('id'))
    x3 = list(queryset3.values_list('Date_of_Calibration', flat=True))
    y3 = list(queryset3.values_list('Actual', flat=True))
    df2 = pd.DataFrame(queryset3.values("Date_of_Calibration","Actual"))
    df2['month2'] = pd.to_datetime(df2['Date_of_Calibration']).dt.to_period('M')
    df3 = df2.to_html()

    df4=pd.concat([df, df2]).groupby(['month2']).sum().reset_index()
    df6=df4.set_index('month2')
    df5 = df6.to_html()
    graph = get_plot2(df4)





    qs4 = Instruments_List.objects.order_by('Calibration_Freq').values('Calibration_Freq').annotate(count=Count('Description'))
    qs5 = pd.DataFrame(qs4.values("Calibration_Freq","count"))
    df7=qs5.set_index("Calibration_Freq")
    df8 = df7.to_html()
    graph2 = get_plot6(df7)


    context = {
        'chart': chart,
        'graph' : graph,
        'graph2' : graph2,




    }
    return render(request,"cal2.html",context)




class Instruments_Listview(ListView):
    context_object_name = 'Instruments'
    model = Instruments_List
    template_name=  'Calibration3.html'
    now = datetime.datetime.now()
    after = now + datetime.timedelta(days=7)
    queryset = Instruments_List.objects.filter(Next_calibration_Due__lte = after)
    ordering = ['Next_calibration_Due']

class Instruments_Listview2(ListView):
    context_object_name = 'Instruments2'
    model = Instruments_List
    template_name=  'calibration2.html'
    queryset = Instruments_List.objects.filter(Q(Status = "Conditionally_accepted") | Q(Status = "Rejected") )
    ordering = ['Status']

class Instruments_Listview3(ListView):
    context_object_name = 'Instruments'
    model = Instruments_List
    template_name=  'Calibration.html'
    


class Fixtures_Listview(ListView):
    from dateutil.relativedelta import relativedelta
    context_object_name = 'Fixtures'
    model = Fixture_List
    template_name=  'Fixtures.html'
    now = datetime.datetime.now()
    after = now + datetime.timedelta(days=7)
    queryset = Fixture_List.objects.filter(Next_Verification_Due__lte = after)
    ordering = ['Next_Verification_Due']

class Fixtures_Listview2(ListView):
    context_object_name = 'Fixtures2'
    model = Fixture_List
    template_name=  'Fixtures2.html'
    queryset =Fixture_List.objects.filter(Q(Status = "Conditionally_accepted") | Q(Status = "Rejected") )
    ordering = ['Status']
