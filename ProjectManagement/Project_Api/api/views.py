
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.contrib.auth.models import User
from .serializer import ProjectSerializer, UserSerializer,TaskSerializer,PermissionSerializer,UserProjectPermissionSerializer
from .models import Project,Task,Permissions
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

# def Hello(request):
#     return HttpResponse("Hello world")


#registration api
class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectApi(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        print(request.user.id)
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects,many=True)
        return Response({'status':200,'Data':serializer.data})

    def post(self,request):
        print(request.user)
        # request.data.update({
        #     "create_by": request.user.id
        # })
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def put(self,request,pk):
        id = pk
       
        proj = Project.objects.get(id=id)
        print("project crator",proj.create_by.id)
        print("user id",request.user.id)
        
        if proj.create_by.id == request.user.id:
            serializer = ProjectSerializer(proj,data=request.data)
            if serializer.is_valid():
                        serializer.save()
                        return Response({'status':200,'Data':serializer.data})
            return Response({'Erorr': 404})
        else:
            return Response({'401': 'You are not authorized to update this'})
        #return Response({'msg':'calling put'})

    def delete(self,request):
        proj = Project.objects.get(id=request.data['id'])
        print(proj)
        if proj.create_by.id == request.user.id:
            if proj:
                    proj.delete()
                    return Response({'status':200,'Message':'Record Delete Successfully'})
            return Response({'Erorr': 404})
        else:
            return Response({'msg': 'You are not authorized' })

class TaskApi(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        pid = request.data['id']
        print(request.data['id'])
        project_tasks = Project.objects.get(id=pid).task_set.all()
        serializer = TaskSerializer(project_tasks,many=True)
        return Response({'status':200,'Data':serializer.data})

    # this is custom method which is working eeee
    # def gettask(self,request):
    #     pid = request.data['id']
    #     # print(pk)
    #     print(request.data['id'])
    #     project_tasks = Project.objects.get(id=pid).task_set.all()
    #     serializer = TaskSerializer(project_tasks,many=True)
    #     return Response({'status':200,'Data':serializer.data})
    
    def post(self,request):
        
        try:
            projObj = Project.objects.get(id=request.data['project'])

            if projObj is not None:
                if projObj.create_by.id == request.user.id:
                    serializer = TaskSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({'status':200,'data':serializer.data})
                else:
                    return Response({'status':401,'data':'UnAuthorized Access'})
        except Exception:
                return Response({'msg':'not project exists'})
            
    def put(self,request,*args, **kwargs):
        try:
           #  projObj = Project.objects.get(id=request.data['project'])
             taskObj = Task.objects.get(id=request.data['id'])
             print(f' in the put method {taskObj.project.create_by.id}')
            #  return Response({'msg':'mila'})
         
             if taskObj.project.create_by.id == request.user.id:
                    serializer = TaskSerializer(taskObj,data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({'status':200,'data':serializer.data})
                    else:
                        return Response({'status':400,'data':'error occur'})
             else:
                    return Response({'status':401,'data':'UnAuthorized Access'})
        except Exception:
            return Response({'msg':'not task exists'})
    
    def delete(self,request):
        task = Task.objects.get(id=request.data['id'])
        print(task)
        if task.project.create_by.id == request.user.id:
            if task:
                    task.delete()
                    return Response({'status':200,'Message':'Record Delete Successfully'})
            return Response({'Erorr': 404})
        else:
            return Response({'msg': 'You are not authorized' })


class PermissionApi(APIView):
    #yeh sirf admin access karega
    permission_classes = [IsAdminUser]
    
    def get(self,request):
        print(request.user.id)
        permissions = Permissions.objects.all()
        serializer = PermissionSerializer(permissions,many=True)
        return Response({'status':200,'Data':serializer.data})
    
    def post(self,request):
        try:
            serializer = PermissionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,'Data':serializer.data})
        except Exception as e:
             return Response({'status':400,'Data':e})
    
    def put(self,request):
        try:
            permission = Permissions.objects.get(id=request.data['id'])
            serializer = PermissionSerializer(instance=permission,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,'Data':serializer.data})
        except Exception as e:
             return Response({'status':400,'Data':e})
    
    def delete(self,request):
        try:
            permission = Permissions.objects.get(id=request.data['id'])
           
            if permission:
                permission.delete()
                return Response({'status':200,'Data':'Record Delete SuccessFully'})
        except Exception as e:
             return Response({'status':400,'Data':e})

class UserProjectPermissionApi(APIView):
      permission_classes = [IsAuthenticated]

      def post(self,request):
        try:
            projObj =  Project.objects.get(id=request.data['project'])
            userObj =  User.objects.get(id=request.data['user'])
            permissionObj =  Permissions.objects.get(id=request.data['permission'])
            try:
               
                       
                 serializer = UserProjectPermissionSerializer(data=request.data)
                 if serializer.is_valid():
                    serializer.save()
                    return Response({'status':200,'Data':serializer.data})
            except Exception as e:
                    return Response({'status':400,'Data':e})

        except ObjectDoesNotExist as e:
             return Response({'status':400,'Data':e})








            



        
       


    



