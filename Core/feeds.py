from datetime import datetime
import glob
import logging
import os
from pyexpat.errors import messages
import sys
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import requests
from wsgiref import headers
from bs4 import BeautifulSoup
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Blog
from django.urls import reverse
from django.utils import feedgenerator

   


import csv
import ntpath

from Core import models


        
res =[] 
temp_res = [] 
results = [] 
item= []
title= []
desc = []

class createfeed(Feed):

        

        def link(self, obj):

                return obj

        def description(self, obj):

                headers = { 
                                'Access-Control-Allow-Origin': '*',
                                'Access-Control-Allow-Methods': 'GET',
                                'Access-Control-Allow-Headers': 'Content-Type',
                                'Access-Control-Max-Age': '3600',
                                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
                                }
                
                response = requests.get(obj,headers= headers) 
                description = BeautifulSoup(response.content, "html.parser") 

                return description

        def title(self, obj):
                
                return title
                
        def items(self):

                return Blog.objects.filter(status =1)       

                
def uploadFile(request):
                if request.method == "POST":
                        # Fetching the form data
                        fileTitle = request.POST["fileTitle"]
                        uploadedfile = request.FILES["uploadedFile"]
                        # Saving the information in the database
                        print(fileTitle)
                        document = models.Document(
                         title = fileTitle,
                         upFile= uploadedfile,
                         uploadedFile = uploadedfile
                         
                        )
                        document.save()
                documents = models.Document.objects.all()
            
                return render(request, "Core/upload-file.html", context = {
                        "files": documents
                        })

def checkfile(self,upFile):
        # import pdb; pdb.set_trace()        
        if len(os.listdir('../feedcreator/media/Uploaded Files') ) == 0:
                                        print("Directory is empty")
        else:                
                with open (os.path.join('../feedcreator/media/Uploaded Files',upFile)) as csvfile:
                        
                                csvReader = csv.reader(csvfile)    
                                for row in csvReader:        
                                        results.append(row[0])
        
        for a in results:
                headers = { 
                                'Access-Control-Allow-Origin': '*',
                                'Access-Control-Allow-Methods': 'GET',
                                'Access-Control-Allow-Headers': 'Content-Type',
                                'Access-Control-Max-Age': '3600',
                                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
                                }
                urls=a,
                response = requests.get(a,headers= headers) 
                desc = BeautifulSoup(response.content, "html.parser") 
                ti = desc.title.string
                f = feedgenerator.Atom1Feed(
                link=a,
                title=ti,    
                description=desc,
                language="en",
                
                )
                f.add_item(
                     title=ti,
                     link=a,
                     pubdate=datetime.now(),
                     description=desc,
                )
                print (a)
                
                return HttpResponse(f.writeString('UTF-8') , content_type='application/xml')
                
       
      
                        
                



                        



                
