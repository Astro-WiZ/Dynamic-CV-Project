from django.db import models

SCORE_TYPES_CHOICES = (
    ('PERCENTAGE', 'Percentage'),
    ('GPA', 'GPA'),
)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to="profile")
    bio = models.TextField()
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    default = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-id',)

class Skill(models.Model):
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.profile.name +' - '+ self.title
    

class Link(models.Model):
    profile = models.OneToOneField(Profile, related_name='link', on_delete= models.CASCADE)
    github = models.URLField()
    linkedin = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    spotify = models.URLField()
    discord = models.CharField(max_length=11)
    website = models.URLField()
    webqr = models.ImageField(upload_to='qrs')
    
    def __str__(self):
        return self.profile.name



class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)
    score = models.FloatField()
    score_type = models.CharField(max_length=100, choices=SCORE_TYPES_CHOICES)
    
    def __str__(self):
        return self.profile.name + " - " +self.degree
    


class Project(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.profile.name +" - "+ self.title
    
    
    
class ProfileDescription(models.Model):
    profile = models.OneToOneField(Profile, related_name='description', on_delete=models.CASCADE)
    objective = models.TextField()
    activities = models.TextField()
    
    def __str__(self):
        return self.profile.name + " - Profile Description"
    