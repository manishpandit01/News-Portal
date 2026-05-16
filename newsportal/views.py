from django.shortcuts import render

from newsportal.models import Advertisement, Post

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