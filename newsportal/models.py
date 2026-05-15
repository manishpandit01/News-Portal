from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)
    
    class Meta:
        abstract=True 
        
class Category(TimeStampModel):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=["name"]
        verbose_name="category"
        verbose_name_plural="Categories"
        
class Tag(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Advertisement(TimeStampModel):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="advertisements/%Y/%m/%d",blank=False)
    
    def __str__(self):
        return self.title
    
class OurTeam(TimeStampModel):
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    image=models.ImageField(upload_to="team_image/%y/%m/%d", blank=False)
    description=models.TextField()
    
    def __str__(self):
        return self.name
    
class Post(TimeStampModel):
    STATUS_CHOICES=[
        ("active","Active"),
        ("in_active","Inactive")
    ]
    title=models.CharField(max_length=200)
    content=models.TextField()
    featured_image=models.ImageField( upload_to="post_image/%Y/%m/%d",blank=False)
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    status=models.CharField( max_length=50,choices=STATUS_CHOICES,default="active")
    views_count=models.PositiveBigIntegerField(default=0)
    is_breaking_news=models.BooleanField(default=False)
    published_at=models.DateTimeField(null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tag)


    def __str__(self):
        return self.title
    
class Contact(TimeStampModel):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=["created_at"] # Contact.objects.all()=> order_by("created_at")