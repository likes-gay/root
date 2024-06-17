from django.shortcuts import render

def index(request, path):
	return render(request, "main/index.html")