from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from datetime import datetime , timedelta

def date(request):
    date = datetime.now()
    html = f'''<html>
    <body>
    {date}</body>
    </html>'''
    return HttpResponse(html)

def dateWithOffset(req , offset=0):
  html = f'''<html>
  <body>
  <div> 
   {datetime.now()}<br>
   {offset} + time : {datetime.now() + timedelta(hours=4)}<br>
   {offset} - time : {datetime.now() - timedelta(hours=4)}
   </div>
     </body>
  </html>'''

  return HttpResponse(html)