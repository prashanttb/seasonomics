from django.shortcuts import render
from django.http import HttpResponse
from .models import SeasonomicsTree

# Create your views here.
def trees(request):
    # coal = ProjectDetails.objects.all()
    tree1=SeasonomicsTree.objects.all()
    # print(tree1)
    context = {'tree1':tree1 }
   
    return render(request, 'trees/viewtrees.html', context )

