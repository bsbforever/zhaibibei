__author__ = '42274'

import requests
from bs4 import BeautifulSoup
import MySQLdb
def geturl():
    url_list=[]
    url='https://docs.oracle.com/cd/B28359_01/server.111/b28278/toc.htm'
    r = requests.get(url,verify=False)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    #print soup
    url1=soup.find_all('h2',attrs = {'class' : 'tocheader'})

    for i in url1:
        try:
            #print i
            num=i.find('span',attrs = {'class' : 'secnum'})
            if num is not None:
                url=i.find('a',attrs = {'href' : True})['href']
                url='https://docs.oracle.com/cd/B28359_01/server.111/b28278/'+url
                url_list.append(url)


        except Exception, e:
            print e
    #print error_list
    return url_list

def oracle(url):
    error_list=[]
    #url='https://docs.oracle.com/cd/B28359_01/server.111/b28278/e0.htm#ORA-00000'
    r = requests.get(url,verify=False)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    #print soup
    live_list=soup.find_all('div',attrs = {'class' : 'msgentry'})

    for i in live_list:
        try:
            #print i
            error_code=i.find_all('a',attrs = {'id' : True})[1]['id']
            error_message=i.find('span',attrs = {'class' : 'msg'}).text.strip()
            error_cause=i.find('div',attrs = {'class' : 'msgexplan'}).text.strip()
            error_action=i.find('div',attrs = {'class' : 'msgaction'}).text.strip()
            #print error_code
            #print error_message
            #print error_cause
            #print error_action

            #break
            error_dic={}
            error_dic['error_code']=error_code
            error_dic['error_message']=error_message
            error_dic['error_cause']=error_cause
            error_dic['error_action']=error_action
            error_list.append(error_dic)

        except Exception, e:
            print e
    #print error_list
    return error_list

def orasearch(code):
    length=len(code.split('-')[1])
    if length !=5:
        code=code.split('-')[0]+'-'+'0'*(5-length)+code.split('-')[1]
    sql='select error_message,error_cause,error_action from wechat_oraerror where error_code=\''+code+'\''
    db = MySQLdb.connect("localhost","root","dgvtG@ng6","wechat" )
    #print sql
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    db.close()
    if data is not None:
        result='\n\n\n'.join(data)
    else:
        result='Please Check The Error Code. ext:ORA-00600'
    return result
if __name__=="__main__":

    #print final_url
    code='ORA-00600'
    print orasearch(code)

