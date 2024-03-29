from Tkinter import *
import urllib,urllib2
import copy
from bs4 import BeautifulSoup

iter1=1
strg1=u""

iter2=1
strg2=u""

iter3=1
strg3=u""



def asin_lookup(product_name):

    query_product_name = product_name.replace(' ', '+')
    asin_query_url = "http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + query_product_name + "&rh=i%3Aaps%2Ck%3A" + query_product_name
    
    soup = BeautifulSoup(urllib2.urlopen(asin_query_url))
    query_result=soup.find(id="result_" + str(1))
    
    query_result_asin = copy.copy(query_result)
    matched_asin_string = query_result_asin.get('name')
    return matched_asin_string

def scrape_url(url1,url2,url3):

    #Product A
    content1 = urllib2.urlopen(url1).read()
    soup1 = BeautifulSoup(content1, "html.parser")
    rows1 =soup1.find_all('div',attrs={"class" : "reviewText"})

    for row1 in soup1.find_all('div',attrs={"class" : "reviewText"}):
        global iter1,strg1
        strg1 = strg1 +unicode(iter1)+u"." + row1.text + u"\n\n"
        iter1=iter1+1
    with open('output1.txt','w') as f1:
        f1.write(strg1.encode('utf8'))
    f1.close()

    #Product B
    content2 = urllib2.urlopen(url2).read()
    soup2 = BeautifulSoup(content2, "html.parser")
    rows2 =soup2.find_all('div',attrs={"class" : "reviewText"})

    for row2 in soup2.find_all('div',attrs={"class" : "reviewText"}):
        global iter2,strg2
        strg2 = strg2 +unicode(iter2)+u"." + row2.text + u"\n\n"
        iter2=iter2+1
    with open('output2.txt','w') as f2:
        f2.write(strg2.encode('utf8'))
    f2.close()


    #Product C
    content3 = urllib2.urlopen(url3).read()
    soup3 = BeautifulSoup(content3, "html.parser")
    rows3 =soup3.find_all('div',attrs={"class" : "reviewText"})

    for row3 in soup3.find_all('div',attrs={"class" : "reviewText"}):
        global iter3,strg3
        strg3 = strg3 +unicode(iter3)+u"." + row3.text + u"\n\n"
        iter3=iter3+1
    with open('output3.txt','w') as f3:
        f3.write(strg3.encode('utf8'))
    f3.close()


    

def urlprep(asin_id1,asin_id2,asin_id3):
    urla='http://www.amazon.in/product-reviews/'
    urlb='/ref=cm_cr_pr_top_link_'
    url1_1=urla+str(asin_id1)+urlb
    url2_2=urla+str(asin_id2)+urlb
    url3_3=urla+str(asin_id3)+urlb
    urlc='?ie=UTF8&pageNumber='
    urld='&showViewpoints=0&sortBy=bySubmissionDateDescending'
    for j in range(1,3):
        url1=url1_1+str(j)+urlc+str(j)+urld
        url2=url2_2+str(j)+urlc+str(j)+urld
        url3=url3_3+str(j)+urlc+str(j)+urld
        scrape_url(url1,url2,url3)
        
def scrape(query1,query2,query3):
    asin_id1=asin_lookup(query1)
    asin_id2=asin_lookup(query2)
    asin_id3=asin_lookup(query3)
    urlprep(asin_id1,asin_id2,asin_id3)
    
        

def printinp():

    query1=var1.get()
    query2=var2.get()
    query3=var3.get()
    
    scrape(query1,query2,query3)

    print "Done"
    



top = Tk()

Label(top, text='Product A').grid(row=0)
Label(top, text='Product B').grid(row=1)
Label(top, text='Product C').grid(row=2)


var1= StringVar(top)
var1.set("Choose Product") 
option1 = OptionMenu(top, var1, "Nokia Lumia 520", "Sony Xperia M", "Apple iPhone 4")
option1.grid(row=0,column=1)

var2= StringVar(top)
var2.set("Choose Product")
option2 = OptionMenu(top, var2, "Nokia Lumia 520", "Sony Xperia M", "Apple iPhone 4")
option2.grid(row=1,column=1)

var3= StringVar(top)
var3.set("Choose Product") 
option3 = OptionMenu(top, var3,"Nokia Lumia 520", "Sony Xperia M", "Apple iPhone 4" )
option3.grid(row=2,column=1)

B = Button(top, text ="Submit",command=printinp)
B.grid(row=3,column=1)

top.mainloop()







        

