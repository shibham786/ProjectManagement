from tkinter import CASCADE
from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here. 
#Project (id UUID, name, desc, created_by, created_at, project_color_identity)

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name = models.CharField(max_length=200,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    create_by = models.ForeignKey(User,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    project_color = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return str(self.name)



class Task(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    task_name = models.CharField(max_length=200,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.task_name)

class Permissions(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    permission_name = models.CharField(max_length=200,null=True)
    desc = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.permission_name)
    

class UserProjectPermission(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    permission = models.ForeignKey(Permissions,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

  

   

    
    
