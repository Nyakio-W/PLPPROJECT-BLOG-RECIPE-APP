#to render html pages
from typing import Concatenate
import random
from django.http import HttpResponse
from django.template.loader import render_to_string


from articles.models import Article

def home_view(request,*args,**kwargs):

  
  # name = "Justin" # hard coded
  # random_id = random.randint(1,5) 
    
  # article_obj = Article.objects.get()

  article_queryset = Article.objects.all()
  
    
  context = { 
    'object_list': article_queryset,
    # 'object': article_obj,
    # 'title': article_obj.title,
    # 'id': article_obj.id,
    # 'content': article_obj.content
  }
  
  HTML_STRING = render_to_string('home-view.html',context=context)
  
  # HTML_STRING = '''<H1>{title}(id:{id}) </H1> <p>{content}</p>'''.format(**context)

  
  
  return HttpResponse(HTML_STRING)