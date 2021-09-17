#!/usr/bin/python
import requests
import hashlib
import re
req=requests.session()
url=''#fill this part
def html_tags(html):
    _patron=re.compile('<.*?>')
    return re.sub(_patron,'',html)
def response_data(html):
    print('==================THIS IS HTML CONTENT CLEANED==================')
    res=html_tags(html)
    print(res)
def converter_data(res):
    res=hashlib.md5(res).hexdigest()
    result=dict(hash=res)
    print('==================THIS IS HTML KEY==================')
    print(result)
    return result
def get_request(url,req):
    html=''
    try:
        if url!='':
            rget=req.get(url)
            html=rget.content
        else:
            print('===No Inputs===')
    except:    
        print('===url no valid===')

    return html
def send_request(url,res):
    if url!='' and res!='':
        result=req.post(url=url,data=res)
    else:
        print('===No Inputs===')
