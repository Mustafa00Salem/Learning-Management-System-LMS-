from rest_framework.permissions import BasePermission

class  IsTeacher(BasePermission):
    message ="Only teachers can perform this action."
    
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role =='TEACHER')
    
    
    
class  IsStudent(BasePermission):
    message = "Only students can perform this action."
    
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role =='STUDENT')
    
class  IsCourseOwner(BasePermission):
    message = "You are not the owner of this course."
    def has_object_permission(self, request, view, obj):
        return obj.instructor == request.user