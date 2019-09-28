from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models	import User
from .forms import VideoForm, VideoEditForm
from .models import Video
from django.db import models
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_list_or_404, get_object_or_404
from moviepy.editor import VideoFileClip

# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('video_list')
	else:
		form = UserCreationForm()
	return render(request, 'registration/signup.html', {'form': form})





@login_required
def video_list(request):
    if request.method == 'GET':
        filter_criteria = int(request.GET.get('filter',0))
        sort_method = int(request.GET.get('sort',0))
        search_qry =   request.GET.get('q', '')


        videos = Video.objects.all()
        if(search_qry != ''):
            videos = videos.filter(Q(title__icontains=search_qry))
        if filter_criteria == 1:#sort < 4
            videos = videos.filter(duration__lte = 240)
        elif filter_criteria == 2:#long >20
            videos = videos.filter(duration__gt = 240)

        if sort_method == 1:#sort < 4
            videos = videos.order_by('-created_date')
        elif sort_method == 2:#long >20
            videos = videos.order_by('-title')
        print(videos)
        paginator = Paginator(videos, 3)
        page = request.GET.get('page', 1)
        try:
            videos = paginator.get_page(page)
        except PageNotAnInteger:
            videos = paginator.get_page(1)
        except EmptyPage:
            videos = paginator.get_page(paginator.num_pages)
        return render(request, 'video_list.html', {'videos': videos, 'filter':filter_criteria, 'sort' : sort_method, 'query': search_qry})






@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                obj = form.save(commit=False)
                vid = request.FILES['video']
                clip = VideoFileClip(vid.temporary_file_path())
                obj.duration = clip.duration
                obj.save()
                #print(round(clip.duration/60),'min')#FOR DURATION
                return redirect("video_list")
            except OSError:
                pass
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})




@login_required
def video_edit(request, id=None):
    if request.method == 'POST':
        print(request.POST)
        print(id,'>>>>>>>>>>>>>>')
        form = VideoEditForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            video = Video.objects.get(id = id)
            video.title = request.POST['title'] 
            video.description = request.POST['description'] 
            video.tags = request.POST['tags'] 
            video.categories = request.POST['categories'] 
            video.save()
        return redirect("video_list")

        #return render(request, 'video_list.html')
   
    else:
        
        #video = Video.objects.filter(id = id).first()

        video = Video.objects.get(id = id)
        form = VideoEditForm(instance=video)
        print(video)
        form.title = video.title
        return render(request, 'video_edit_form.html', {'form': form, 'video': video})
