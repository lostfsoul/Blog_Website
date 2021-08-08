from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    api_key = '13782a5c66d551072668b00cbdcc06ff'
    r = requests.get(f"http://api.mediastack.com/v1/news?access_key={api_key}&countries=us")
    req = r.json()
    data = req['data']
    title = []
    description = []
    image = []
    url = []
    for item in data:
        title.append(item['title'])
        description.append(item['description'])
        image.append(item['image'])
        url.append(item['url'])
    news = zip(title,description,image,url)
    return render(request,'yamiapp/index.html',{'news': news})