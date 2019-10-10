from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_required
import pandas as pd
import json
from pprint import pprint
# Create your views here.

# To view Login page 
def home(request):
    return render(request,'login.html')

""" Login Method:
Input: Uername & Password """
def login(request):
    if request.method == 'POST':
        username = request.POST['uname'] # Extracting username from login form
        password = request.POST['pwd'] # Extracting password from login form
        user = authenticate(username=username, password=password) # validating the user
        if user is not None:
           user_login(request, user) # Make user login, if validation got success
           return redirect('firstpage')
        else:
           return redirect('home') 
    else:
        return render(request, 'login.html')

""" Logout Method:
Input : requested user """
def logout(request):
   logout_required(request) # alias name for logout to avaoid recurssion
   return redirect('home')

""" Home page:
Input : HTTP Request """
@login_required
def firstpage(request):

    #chart1

    df = pd.read_csv(r'I:\Kiski_Project\Kiski\Graphs\static\csv\Growth_1000_inception.csv')
 
    df['year'] = pd.DatetimeIndex(df['Trade_Dt']).year
    
    df['month'] = pd.DatetimeIndex(df['Trade_Dt']).month
    df['day'] = pd.DatetimeIndex(df['Trade_Dt']).day
    df['month']=df.month.map("{:02}".format)
    df['day']=df.day.map("{:02}".format)
    df['Trade_Dt'] = df['year'].apply(str) +'-'+ df['month'].apply(str)+'-'+ df['day'].apply(str)

    df=df.groupby(['Trade_Dt','year','month','day'],as_index = False).agg('sum')
    # df= df.sort_values(['Trade_Dt','year','month']).groupby(['Trade_Dt','year','month'],as_index = False).agg('sum')
    df=df.groupby(["Trade_Dt"]).apply(lambda x: x.sort_values(["Trade_Dt"], ascending = True)).reset_index(drop=True)
    
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
   
 #chart2
    df = pd.read_csv(r'I:\Kiski_Project\Kiski\Graphs\static\csv\page1_table.csv')
    df['year'] = pd.DatetimeIndex(df['Trade_Dt']).year
    
    df['month'] = pd.DatetimeIndex(df['Trade_Dt']).month
    df['day'] = pd.DatetimeIndex(df['Trade_Dt']).day
    df['month']=df.month.map("{:02}".format)
    df['day']=df.day.map("{:02}".format)
    df['Trade_Dt'] = df['day'].apply(str) +'/'+ df['month'].apply(str)+'/'+ df['year'].apply(str)


    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)

    df=pd.read_csv(r'I:\Kiski_Project\Kiski\Graphs\static\csv\page1_ytd.csv')
    ytd=df.YTD.values.tolist()
    year=df.YEAR.values.tolist()
    context={'data':data,'data2':chart_data,'ytd':ytd,'year':year}

    return render(request, 'page1.html',context)

@login_required
def secondpage(request):
    return render(request, 'page2.html')

def thirdpage(request):

    df=pd.read_csv(r'I:\Kiski_Project\Kiski\Graphs\static\csv\page3_fama_french.csv')
    df1=df[['Trade_Dt']] 
    list1=[]
    for i in range (0,len(df1)-1):
        list1.append(df1.loc[[i]])
    Row_list1=[]
    for index, rows in df1.iterrows(): 
    # Create list for the current row 
        my_list =rows.Trade_Dt 
        Row_list1.append(my_list)
    # print(Row_list1) 
    df2=df[['Market']] 
    list2=[]
    for i in range (0,len(df2)-1):
        list2.append(df2.loc[[i]])
    Row_list2=[]
    for index, rows in df2.iterrows(): 
    # Create list for the current row 
        my_list =rows.Market 
        Row_list2.append(my_list) 
    df3=df[['Growth']] 
    list3=[]
    for i in range (0,len(df3)-1):
        list3.append(df3.loc[[i]])
    Row_list3=[]
    for index, rows in df3.iterrows(): 
    # Create list for the current row 
        my_list =rows.Growth 
        Row_list3.append(my_list) 
    df4=df[['Momentum']] 
    list4=[]
    for i in range (0,len(df4)-1):
        list4.append(df4.loc[[i]])
    Row_list4=[]
    for index, rows in df4.iterrows(): 
    # Create list for the current row 
        my_list =rows.Momentum 
        Row_list4.append(my_list) 
    df5=df[['Quality']] 
    list5=[]
    for i in range (0,len(df5)-1):
        list5.append(df5.loc[[i]])
    Row_list5=[]
    for index, rows in df5.iterrows(): 
    # Create list for the current row 
        my_list =rows.Quality 
        Row_list5.append(my_list)
    df6=df[['Size']] 
    list6=[]
    for i in range (0,len(df6)-1):
        list6.append(df6.loc[[i]])
    Row_list6=[]
    for index, rows in df6.iterrows(): 
    # Create list for the current row 
        my_list =rows.Size 
        Row_list6.append(my_list)
    # print(df) 
    df7=df[['Fund']]  
    list7=[]
    for i in range (0,len(df7)-1):
        list7.append(df7.loc[[i]])
    Row_list7=[]
    for index, rows in df7.iterrows(): 
    # Create list for the current row 
        my_list =rows.Fund
        Row_list7.append(my_list)

    df8=df[['Alpha']]  
    list8=[]
    for i in range (0,len(df8)-1):
        list8.append(df8.loc[[i]])
    Row_list8=[]
    for index, rows in df8.iterrows(): 
    # Create list for the current row 
        my_list =rows.Alpha
        Row_list8.append(my_list) 

    df9=df[['Capex']]  
    list9=[]
    for i in range (0,len(df9)-1):
        list9.append(df9.loc[[i]])
    Row_list9=[]
    for index, rows in df9.iterrows(): 
    # Create list for the current row 
        my_list =rows.Capex
        Row_list9.append(my_list)   
    list1=Row_list1
    list2=Row_list2
    list3=Row_list3
    list4=Row_list4
    list5=Row_list5
    list6=Row_list6
    list7=Row_list7
    list8=Row_list8
    list9=Row_list9
    
    multi_factor_df=pd.read_csv(r'I:\Kiski_Project\Kiski\Graphs\static\csv\page3_multi_factor.csv')
    # print(multi_factor_df)
    multi_factor_dates=multi_factor_df.Trade_Dt.unique().tolist()
    print(multi_factor_dates)
    


    context={'list1':list1,'list2':list2,'list3':list3,'list4':list4,'list5':list5,'list6':list6,'list7':list7,'list8':list8,'list9':list9,"multi_factor_dates":multi_factor_dates}
    return render(request, 'page3.html',context)

@login_required
def fourthpage(request):
    df1=pd.read_csv(r'I:\Kiski_Project\Kiski\Graphs\static\csv\pie_drilldown_sector.csv')
    df1=df1.sort_values('Gross_Exposure_Percentage')
    #print(df1.columns)
    trade_dt=list(df1['trade_dt'])
    # color=["red","blue","green","yellow","pink","black","red","grey","green","yellow","pink","black","red","grey"]
    trade_dt = list(dict.fromkeys(trade_dt))
   #print(len(trade_dt))
    sectors_list_total=[]

    for each in trade_dt:
       c=0
       each_date= df1[df1['trade_dt']==each]
    #    print(each)
       sec_list=list(each_date['sector'])
       pnl_list=list(each_date['Gross_Exposure_Percentage'])
   #print(len(sec_list))
       
       sectors_list_each=[]
       for i in range(0,len(sec_list)):
           
           dict1={'date':each,'name':sec_list[i],'y':pnl_list[i],'drilldown':sec_list[i]}   
           
           sectors_list_each.append(dict1)
           c=c+1
    #    print(c)
      
       sectors_list_total.append(sectors_list_each)
  
    ticker_csv=pd.read_csv(r'I:\Kiski_Project\Kiski\Graphs\static\csv\pie_drilldown_region.csv')
    ticker_list_total=[]
    for i in range(0,len(trade_dt)):
       ticker_list1=[]
       ticker_each=ticker_csv[ticker_csv['trade_dt']==trade_dt[i]]
       for j in range(0,len(sectors_list_total[i])):
           sector_match=ticker_each[ticker_each['sector']==sectors_list_total[i][j]['name']]
           ticker_list=list(sector_match['region'])
           pnl_list=list(sector_match['Percentage'])
           ticker_pnl=[]
           for k in range(0,len(ticker_list)):
                   temp_list=[]
                   temp_list.append(ticker_list[k])
                #    print(pnl_list[k])
                #    print(float(pnl_list[k]))
                   temp_list.append(float(pnl_list[k]))
                   ticker_pnl.append(temp_list)

           dict2={'date':trade_dt[i],'name':sectors_list_total[i][j]['name'],'id':sectors_list_total[i][j]['name'],"data":ticker_pnl}
           
           ticker_list1.append(dict2)
       ticker_list_total.append(ticker_list1)

#    context={"sector":sectors_list_total,'region':ticker_list_total}
    df1=pd.read_csv(r'I:\Kiski_Project\Kiski\Graphs\static\csv\bar_drilldown_sector.csv')
    trade_dt=list(df1['Trade_Dt'])
    trade_dt = list(dict.fromkeys(trade_dt))
    sectors_names=[]
    #print(len(trade_dt))
    sectors_list_total2=[]
    for each in trade_dt:
        each_date= df1[df1['Trade_Dt']==each]
        sec_list=list(each_date['Sector'])
        sectors_names.append(sec_list)
        pnl_list=list(each_date['PNL'])
    #print(len(sec_list))
        sectors_list_each=[]
        for i in range(0,len(sec_list)):
            dict1={'name':sec_list[i],'y':pnl_list[i],"drilldown":sec_list[i],'date':each,}
            sectors_list_each.append(dict1)
        sectors_list_total2.append(sectors_list_each)

    ticker_csv=pd.read_csv(r'I:\Kiski_Project\Kiski\Graphs\static\csv\bar_drilldown_ticker.csv')
    #print(ticker_csv.columns)
    ticker_list_total2=[]
    for i in range(0,len(trade_dt)):
        ticker_list1=[]
        ticker_each=ticker_csv[ticker_csv['Trade_Dt']==trade_dt[i]]
        for j in range(0,len(sectors_list_total2[i])):
            sector_match=ticker_each[ticker_each['Sector']==sectors_list_total2[i][j]['name']]
            ticker_list=list(sector_match['Client_Symbol'])
            pnl_list=list(sector_match['PNL'])
            ticker_pnl=[]
            for k in range(0,len(ticker_list)):
                    temp_list=[]
                    temp_list.append(ticker_list[k])
                    temp_list.append(pnl_list[k])
                    ticker_pnl.append(temp_list)
            dict2={'name':sectors_list_total2[i][j]['name'],"id":sectors_list_total2[i][j]['name'],"data":ticker_pnl,'date':trade_dt[i]}
            ticker_list1.append(dict2)
        ticker_list_total2.append(ticker_list1)
    context={"sector":sectors_list_total,'region':ticker_list_total,"date":trade_dt,"sector2":sectors_list_total2,"ticker":ticker_list_total2,"sec_names":sectors_names}

    # return render(request,'drilldown.html',context)


   
    return render(request,'page4.html',context)
    
@login_required
def fifthpage(request):
    df = pd.read_csv(r'I:\Kiski_Project\Kiski\Graphs\static\csv\VaR_PNL_monitoring.csv')

    df1=df[['Positive_Var90D','Negative_Var90D']] 
    list1=[]
    list3=[]
    for i in range (0,len(df1)-1):
        list1.append([df1.loc[[i]]])
    df2=df[['PNL']] 
    
    df3=df[['Trade_Dt']] 
    list2=[]
    for i in range (0,len(df2)-1):
        list2.append([df2.loc[[i]]])
    Row_list =[] 
  
    for index, rows in df1.iterrows(): 
    # Create list for the current row 
        my_list =[rows.Positive_Var90D,rows.Negative_Var90D] 
        
        # append the list to the final list 
        Row_list.append(my_list) 
    Row_list2 =[] 
    for i in range (0,len(df3)-1):
        list3.append([df3.loc[[i]]])
    Row_list3 =[] 
  
    for index, rows in df3.iterrows(): 
    # Create list for the current row 
        my_list =rows.Trade_Dt
        
        # append the list to the final list 
        Row_list3.append(my_list) 

    for index, rows in df2.iterrows(): 
    # Create list for the current row 
        my_list =rows.PNL
        
        # append the list to the final list 
        Row_list2.append(my_list) 
    list1=Row_list
    list2=Row_list2
    list3=Row_list3


    df=pd.read_csv(r'I:\Kiski_Project\Kiski\Graphs\static\csv\var_attribution_reduction.csv')
    df1=df[['trade_dt']] 
    list4=[]
    for i in range (0,len(df1)-1):
        list4.append(df1.loc[[i]])
    Row_list4=[]
    for index, rows in df1.iterrows(): 
    # Create list for the current row 
        my_list =rows.trade_dt 
        Row_list4.append(my_list) 
    df2=df[['India']] 
    list5=[]
    for i in range (0,len(df2)-1):
        list5.append(df2.loc[[i]])
    Row_list5=[]
    for index, rows in df2.iterrows(): 
    # Create list for the current row 
        my_list =rows.India 
        Row_list5.append(my_list) 
    df3=df[['Brazil']] 
    list6=[]
    for i in range (0,len(df3)-1):
        list6.append(df3.loc[[i]])
    Row_list6=[]
    for index, rows in df3.iterrows(): 
    # Create list for the current row 
        my_list =rows.Brazil 
        Row_list6.append(my_list) 
    df4=df[['China']] 
    list7=[]
    for i in range (0,len(df4)-1):
        list7.append(df4.loc[[i]])
    Row_list7=[]
    for index, rows in df4.iterrows(): 
    # Create list for the current row 
        my_list =rows.China 
        Row_list7.append(my_list)


    df5=df[['Mexico']] 
    list8=[]
    for i in range (0,len(df5)-1):
        list8.append(df5.loc[[i]])
    Row_list8=[]
    for index, rows in df5.iterrows(): 
    # Create list for the current row 
        my_list =rows.Mexico 
        Row_list8.append(my_list) 


    df6=df[['Taiwan']] 
    list9=[]
    for i in range (0,len(df6)-1):
        list9.append(df6.loc[[i]])
    Row_list9=[]
    for index, rows in df6.iterrows(): 
    # Create list for the current row 
        my_list =rows.Taiwan 
        Row_list9.append(my_list) 
    
    df7=df[['Philippines']] 
    list10=[]
    for i in range (0,len(df7)-1):
        list10.append(df7.loc[[i]])
    Row_list10=[]
    for index, rows in df7.iterrows(): 
    # Create list for the current row 
        my_list =rows.Philippines 
        Row_list10.append(my_list) 
 
  
    list4=Row_list4
    list5=Row_list5
    list6=Row_list6
    list7=Row_list7
    list8=Row_list8
    list9=Row_list9
    list10=Row_list10

    context={'data':list1,'data2':list2,'data3':list3,'list4':list4,'list5':list5,'list6':list6,'list7':list7,'list8':list8,'list9':list9,'list10':list10}
    return render(request, 'page5.html',context)

@login_required
def sixthpage(request):
    df = pd.read_csv(r'I:\Kiski_Project\Kiski\Graphs\static\csv\page6_T12M_upside_downside.csv')
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    context={'data4':chart_data}
    
    return render(request, 'page6.html',context)



   