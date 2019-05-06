from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request, 'home.html')

def count(request):
	data = request.GET['fulltextarea']
	data_list = data.split()
	list_length = len(data_list)

	worddictionary = {}

	for word1 in data_list:
		if word1 in worddictionary:
			worddictionary[word1] += 1
		else:
			worddictionary[word1] = 1

	return render(request,'count.html', {'fulltext':data, 'word':list_length, 'worddictionary':worddictionary.items() })

def about(request):
	return render(request, 'about.html')