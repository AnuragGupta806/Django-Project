# importing api 
from django.shortcuts import render 
from newsapi import NewsApiClient 

# Create your views here. 
def index(request): 
	
	newsapi = NewsApiClient(api_key ='be7f4e2164204e63bf0984390848b3b9') 
	top = newsapi.get_top_headlines(country='in') 

	l = top['articles'] 
	desc =[] 
	news =[] 
	img =[] 
	url = []

	for i in range(len(l)): 
		f = l[i] 
		news.append(f['title']) 
		desc.append(f['description']) 
		img.append(f['urlToImage']) 
		url.append(f['url'])
	mylist = zip(news, desc, img, url) 

	return render(request, 'news/index.html', context ={"mylist":mylist}) 
