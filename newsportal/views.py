from datetime import timedelta
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin


from newsportal.forms import ContactForm
from newsportal.models import Advertisement, Contact, OurTeam, Post

# Create your views here.
class SidebarMixin:
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        
        context["popular_post"]=Post.objects.filter(
            published_at__isnull=False,status="active"
        ).order_by("-published_at")[:5]
        
        context["advertisement"]=(
            Advertisement.objects.all().order_by("-created_at").first()
        )
        
        
        return context

class HomeView(SidebarMixin,TemplateView):   
    template_name="newsportal/home.html"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        
        context["breaking_news"]=Post.objects.filter(
            published_at__isnull=False, status="active", is_breaking_news=True
        ).order_by("-published_at")[:3]
        
        context["featured_post"]=(
            Post.objects.filter(published_at__isnull=False,status="active").order_by("-published_at","-views_count").first()
        )

        context["trending_news"]=Post.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")[:4]
        
        one_week_ago=timezone.now()-timedelta(days=7)
        context["weekly_top_posts"]=Post.objects.filter(
            published_at__isnull=False, status="active", published_at__gte=one_week_ago
        ).order_by("-published_at","-views_count")[:5]
        
        return context
    
class PostListView(SidebarMixin,ListView):
    model=Post
    template_name="newsportal/list/list.html"
    context_object_name="posts"
    paginate_by=1
    
    def get_queryset(self):
        return Post.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")
        
class PostDetailView(SidebarMixin,DetailView):
    model=Post
    template_name="newsportal/detail/detail.html"
    context_object_name="post"
    
    def get_queryset(self):
        query=super().get_queryset()
        query=query.filter(published_at__isnull=False,status="active")
        return query    
        
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        
        current_post=self.object
        current_post.views_count+=1
        current_post.save()
        
        context["related_articles"]=(
            Post.objects.filter(
            published_at__isnull=False,
            status="active",
            category=self.object.category,
        )
        .exclude(id=self.object.id)
        .order_by("-published_at","-views_count")[:2]
        )
        
        return context
    
class PostByCategoryView(SidebarMixin,ListView):
    model=Post
    template_name="newsportal/list/list.html"
    context_object_name="posts"
    paginate_by=1
    
    def get_queryset(self):
        query=super().get_queryset()
        query=query.filter(
            published_at__isnull=False,
            status="active",
            category__id=self.kwargs["category_id"],
        ).order_by("published_at")
        return query
    
class PostByTagView(SidebarMixin,ListView):
    model=Post
    template_name="newsportal/list/list.html"
    context_object_name="posts"
    paginate_by=1
    
    def get_queryset(self):
            query=super().get_queryset()
            query=query.filter(
                published_at__isnull=False,
                status="active",
                tag__id=self.kwargs["tag_id"],
            ).order_by("published_at")
            return query

class AboutView(TemplateView):
    template_name="newsportal/about.html"
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["our_teams"]=OurTeam.objects.all()
        return context
    
class ContactCreateView(SuccessMessageMixin,CreateView):
    model=Contact
    template_name="newsportal/contact.html"
    form_class=ContactForm
    success_url=reverse_lazy("contact")
    success_message="Your message has been sent sucessfully."
    
    def form_invalid(self, form):
        messages.error(
            self.request,"There was an error sending your message. please check the form." )
        return super().form_invalid(form)
    
    