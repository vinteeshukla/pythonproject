from ast import Return, keyword
from cmath import rect
from email.mime import message
from multiprocessing import context
from multiprocessing.sharedctypes import Value
from re import A
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,get_object_or_404
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import urllib.request
import requests
import json
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from django.http import JsonResponse
from django.template import RequestContext,loader
from chatbot.models import MyModel, New_Gambit_container,text,user,syllabus,DetailForm,NewJoin_Detail,Scratch_values,Gambit_container,New_chatbot_values
from django.template import Context, RequestContext
from chatbot.forms import Detailstored
from django.forms.models import model_to_dict
from django.core.files import File
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.views.generic import View
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings


@csrf_exempt 
def homepage(request):
     return render(request,'home.html')
    #response = "<h1>Welcome to Sessions of TechVidvan Employee Portal</h1><br>"
    #  data= Gambit_container() #call model object
    #  data.gambit_name = request.GET.get('node_name', '') 
   
    #  data.gambit_id = request.GET.get('node_id', '') 

     #request.session.get['name'] 
     #request.session.get['id']
     
    #  #return render(request, 'mainPage.html',locals()) 
    #  print(request.session['name'])

    #  if request.session.get('name'):
    #     response += "name : {0} <br>".format(request.session.get('name'))
    #  if request.session.get('id'):
    #     response += "id : {0} <br>".format(request.session.get('id'))
    #  #return render(request, "home.html")
    #  return HttpResponse(response,'home.html')
    

     
        
# def setsession(request):  
#     request.session()
#     return HttpResponse("User session is set")  
  
def newhomepage(request):
    data = list(syllabus.objects.values())
    return render(request,'new_home.html') 
    
    


def flowChart(request):
    data3 =list(text.objects.values())
    return JsonResponse(data3,safe=False,)


def mainPage(request):
    data = DetailForm.objects.all()
    return render(request,'mainPage.html',{'data':data})


def beautifulSoup(request):
     worf_quote = "Sir, I protest. I am not a merry man!"
     words_in_quote  = word_tokenize (worf_quote)
     stop_words = set(stopwords.words("english"))
     filtered_list = []
     for word in words_in_quote:
      if word.casefold() not in stop_words:
        filtered_list.append(word)
        print(len(filtered_list))
     all_user_profile1 =DetailForm.objects.filter(name='neha')
     return render(request,'scrap.html',locals())


def json(request):
    data = list(DetailForm.objects.filter(chatbot_title='chatbot_1').values())
    
    return JsonResponse(data,safe=False,)  
    



@csrf_exempt   
def post_new(request):
     if request.method == "GET":
        data= DetailForm() #call model object
        data.name = request.GET.get('name', '') 
        data.title = request.GET.get('title', '')
       
        data.description = request.GET.get('description', '')
        data.detail_id = request.GET.get('detail_id', )
        data.chatbot_title = request.GET.get('chatbot_title', '')
        data.save()
        print(data.title)
        # return render(request, "loggedin.html",locals())
        return HttpResponse(data)
     else :
        data =   request.POST.get('name', '') 
        data.delete()
        context = {}
        return render(request, 'home.html',context) 


        
@csrf_exempt   
def form_data(request):
     if request.method == "GET":
        data= DetailForm() #call model object
        data.name = request.GET.get('name', '') 
        data.title = request.GET.get('title', '')
        data.description = request.GET.get('description', '')
        data.detail_id = request.GET.get('detail_id', '')
        data.chatbot_title = request.GET.get('chatbot_title', '')
        data.x_coordinate_of_button = request.GET.get('x_coordinate_of_button')
        data.y_coordinate_of_button = request.GET.get('x_coordinate_of_button')
        data.save()
        # return render(request, "loggedin.html",locals())
        return HttpResponse('ok')
# @csrf_exempt   
# def json_format(request):
#      if request.method == "GET":
        
#         data = list(DetailForm.objects.all().values())
#         context = {'data':data}
#         data1 =MyModel()
#         data1.the_json = context.keys()
#         print(data1)
#         return HttpResponse(data1)

@csrf_exempt   
def json_format(request):
  r = requests.get("http://127.0.0.1:8000/newjoindetails/") 
  json_dict = r.json()  
  print(json_dict)
  data1 =MyModel()
  data1.the_json = json_dict
  data1.save()
  #title = data1['data']['chatbot_title']
  print(data1)
  return HttpResponse(data1)


def json_update_view(request):
        r = requests.get("http://127.0.0.1:8000/newjoindetails/") 
        json_dict = r.json()  
        data1 =MyModel()

        the_json1 = request.GET.get('json_dict', None)
        id1 = request.GET.get('id', None)

        obj = MyModel.objects.get(id=id1)
        obj.the_json = the_json1
        
        obj.save()

        user = {'id':obj.id,'the_json':obj.the_json}

        data = {
            'user': user
        }
        return JsonResponse(data)  
        

def  json_delete(request):
        id1 = request.GET.get('id', None)
        MyModel.objects.filter(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    

def PII(request):
    if request.method == 'POST':
        form = DetailForm(request.POST,)
        if form.is_valid():
            form.description = request.description
            form.save()
          
            return render(request, 'mini_chat.html')
        print(form)
    else:
        form = Detailstored(request.POST)
        return render(request, 'mini_chat.html', {'form':form})


def New_join_detail(request):
        data = list(DetailForm.objects.all().values())
        
        context = {'data':data}
        return JsonResponse(context,safe=False,)

def writetofile(request):
    data = str(DetailForm.objects.all())
    print(data)
    with open('detailform.json', 'a') as outfile:
      outfile.write(data)
     
    return HttpResponse("ok") 


def readfile(request):
    f = open('detailform.json', 'r')
    if f.mode == 'r':
       contents =f.read()
       print (contents)
    return JsonResponse(contents,safe=False,)

def json_New_join(request):
    data = dict(NewJoin_Detail.objects.values())
    print(data)

# @csrf_exempt
# def gambit_container_delete(request):
#     query = DetailForm.objects.all().delete()
#     print(query)
   
    
    
#     return HttpResponse("Deleted!")



@csrf_exempt
def gambit_container_delete(request):
   
    context ={}
 
   
    obj = get_object_or_404(DetailForm, detail_id = 1)
 
 
    if request.method =="POST":
       
        obj.delete()
        
        return HttpResponseRedirect("/")
 
    return render(request, "home.html", context)


  

def gambit_container_add(request):
    data= Gambit_container() #call model object
    data.gambit_name = request.GET.get('node_name', '') 
    data.gambit_id = request.GET.get('node_id', '') 
    #data.gambit_name = request.GET.get('node_name') 
    #data.gambit_id = request.GET.get('node_id') 
    data.chatbot_name = request.GET.get('chatbot_name','') 
    data.save()
    #print(data.charbot_name)
    #print(data)
    
    return render(request, 'mainPage.html',locals())
def retain_nodes(request):
    data =list(Gambit_container.objects.values())
    context={
          'data':data
    }
    return JsonResponse(context,safe=False,)
    
def update_nodes(request):
    member = Gambit_container.objects.get(gambit_id=request.GET.get('node_id',''))
    
    member.gambit_name = request.GET.get(gambit_name=request.GET.get('node_name', '') )
    context={
        'data':member
    }
    return render(request,'home.html',context)


def update(request, name):
  mymember = DetailForm.objects.get(name=request.GET.get('name', ''))
  template = loader.get_template('home.html')
  
  context = {
    'data': mymember,
  }
  return HttpResponse(template.render(context, request))


def updaterecord(request, detail_id):
  member = DetailForm.objects.get(detail_id=request.GET.get('detail_id', ''),chatbot_title=request.GET.get('chatbot_title', ''))
  member.title = request.GET.get('title', request.GET.get('title', '') )
  member.description = request.GET.get('description', request.GET.get('description', '') )
  member.chatbot_title = request.GET.get('chatbot_title',request.GET.get('chatbot_title', ))
  member.name = request.GET.get('name',request.GET.get('name','' ))
  print(member)
  member.save()
  return render(request, 'home.html',locals()) 

def viewname(request):
    all_user_profile =Scratch_values.objects.all()
   # profile_admin = DetailForm.objects.filter(name='admin')
    return render(request,'mainPage.html',locals())  
@csrf_exempt
def chatbotname_del(request):
    data = Scratch_values.objects.get(scratch_id=request.GET.get('scratch_id', ))
    print(data)
    data.delete()
   
    return render(request,'mainPage.html',locals())



def Json_scratch(request):
    data = list(Scratch_values.objects.values())
    return JsonResponse(data,safe=False,)   

def viewhome(request):
    all_user_profile1 = Scratch_values.objects.all()
    print(all_user_profile1)
   
    return render(request,'home.html',locals()) 

def main_chatbot_page(request):
    data= Scratch_values() 
    data.chatbot_title = request.GET.get('name', '') 
    data.scratch_id = request.GET.get('id', '')
    data.save()
    print(data)
    return render(request, 'mainPage.html',locals()) 


def new_chatbot_gambit(request):
    data =  New_chatbot_values.objects.all() 
    print(data)  
    return render(request,'home.html',locals())  
 

@csrf_exempt   
def New_Gambit_container_value(request):
     if request.method == "GET":
        data= New_Gambit_container() #call model object
        data.New_Gambit_created_id = request.GET.get('New_Gambit_created_id', ) 
        data.New_Gambit_created_name = request.GET.get('New_Gambit_created_name', '')
        data.chatbot_name = request.GET.get('chatbot_name', '')
        data.connec_btn_value = request.GET.get('connec_btn_value', )
       
        data.save()
        # return render(request, "loggedin.html",locals())
        return HttpResponse('ok')
     else :
        data =   request.POST.get('New_Gambit_created_name', '') 
        data.delete()
        context = {}
        return render(request, 'home.html',context) 


def delete1(request):
  data = New_Gambit_container.objects.delete()
  return HttpResponse("deleted")
  
def update1(request):
  mymember = New_Gambit_container.objects.filter(chatbot_name=request.POST['chatbot_name'])
  template = loader.get_template('home.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))    

def updaterecord1(request):
  member = New_Gambit_container.objects.filter(chatbot_name='chatbot_1')
  member.connec_btn_value = request.GET.get('connec_btn_value', request.GET.get('connec_btn_value', '') )
  member.New_Gambit_created_name = request.GET.get('New_Gambit_created_name', request.GET.get('New_Gambit_created_name', '') )
  
 # member.chatbot_name = request.GET.get('chatbot_name', request.GET.get('chatbot_name', '') )
  member.update_or_create()
  return render(request, 'home.html',locals()) 


def New_chat_detail(request):
        data = list(New_Gambit_container.objects.all().values())
        context = {'data':data}
        return JsonResponse(context,safe=False,)

@method_decorator(csrf_exempt)
def post1(request):
       
        json_data = json.loads(request.body.decode('utf-8'))

        DetailForm.objects.create(title=json_data['title'], description=json_data['description'], name=json_data['name'],
                             detail_id=json_data['detail_id'])
        data = {'message': "Success"}
        return JsonResponse(data)


class ChatterBotAppView(TemplateView):
    template_name = 'home.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    global dataStr

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.
        * The JSON data should contain a 'text' attribute.
        """
       # data_file = open('job_intents.json').read()
        #input_data = json.loads(data_file)
        dataStr = request.body.decode('utf-8')
        
        # input_data = dataStr.json()
        print(dataStr)
        # if 'text' not in dataStr:
        #     return JsonResponse({
        #         'text': [
        #             'The attribute "text" is required.'
        #         ]
        #     }, status=400)

        response = self.chatterbot.get_response(dataStr)
        
        response_data = response.serialize()
       
        return JsonResponse(response_data, safe=False)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })

        
        
        
