
import pandas as pd

FILENAME = 'C:/Users/12014/.spyder-py3/MyFlaskApp/data_test_JAN24_2020.csv'
dataFrame= pd.read_csv(FILENAME,sep='|')
dataFrame=dataFrame.drop('Unnamed: 0',axis=1)
dataFrame.head()
#print("shit")
        #null values check.
dataFrame.fillna('nan',inplace=True)
    
dataFrame.isnull().sum()
def unique_val():
    uni_vals=dataFrame['template'].unique()
    return uni_vals





def dataAnalysis(lst):
    
    dataFrame['month_year']=pd.to_datetime(dataFrame['time']).dt.to_period('M')
    
    
    df=dataFrame[dataFrame['template'].isin(lst)]
    
         
    Sent_emails=df.groupby('month_year')['sent'].sum()
    
    
    s=pd.DataFrame({'month_year':Sent_emails.index, 'sent':Sent_emails.values})
    
  
        
    def sent():    
        return Sent_emails
        
        
        
    # Delivered (number of emails delivered). sent-soft_bounces-hard_bounces
    #total e-mails sent.    
    total_sent=df.groupby('month_year')['sent'].sum()

    
    soft_bon=df.groupby('month_year')['soft_bounces'].sum()
    hard_bon=df.groupby('month_year')['hard_bounces'].sum()
   
    
    Delivered_emails= total_sent - soft_bon - hard_bon
    
    
    g=pd.DataFrame({'Delivered_emails':Delivered_emails.values})
    s['Delivered_emails']=g['Delivered_emails']

    
    def delivered():    
        return Delivered_emails
        
          #Delivery rate is Delivered mails / sent
    
    Deli_rate= Delivered_emails/Sent_emails
    
    
    gg=pd.DataFrame({'Delivered_rate':Deli_rate.values})
    s['Delivered_rate']=gg['Delivered_rate']
    
   
    def deli_rate():    
        return Deli_rate
    
    #Open rate email opened by email delivered
        
    total_open= df.groupby('month_year')['opens'].sum()
   
    open_rate = total_open / Delivered_emails
    
    
    ggg=pd.DataFrame({'open_rate':open_rate.values})
    s['open_rate']=ggg['open_rate']
    
    def open_rate():    
        return open_rate
    
    
    #click rate is no. of emails clicked by delivered emails
     
    total_click= df.groupby('month_year')['clicks'].sum()

    
    click_rate= total_click/Delivered_emails
    
    
    gggg=pd.DataFrame({'click_rate':click_rate.values})
    s['click_rate']=gggg['click_rate']
    #ht= s.to_html(open('C:/Users/12014/.spyder-py3/MyFlaskApp/templates/table.html', 'a')) 
#    df.to_csv('file1.csv') 
    cs=s.to_csv('C:/Users/12014/.spyder-py3/MyFlaskApp/templates/file1.csv') 
    
    def click_rate():    
        return click_rate
    
        
    return s.to_html()


#dataAnalysis(['NEW COLLECTION - MAY 2018','RB Onboarding E1 CANADA FRA'])

    

