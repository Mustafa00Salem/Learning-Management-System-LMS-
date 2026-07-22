from rest_framework import serializers
from .models import Category, Course, Review


class ReviewCreateSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Review
        fields = ['course', 'rating', 'review']

    def validate(self, data):
        user = self.context['request'].user
        course = data.get('course')

        if Review.objects.filter(user=user, course=course).exists():
            raise serializers.ValidationError({
                "detail": "You Are Add Review actually"
            })
        
        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields = [
            'id',
            'user',
            'user_username',
            'rating',
            'review',
            'created_at',
            ]


class CourseSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = ['id','name', 'description','price','reviews','average_rating' ,'image']
        
        extra_kwargs={
            'image': {'required': False},
        }
    def get_average_rating(self, obj):
        return  obj.average_rating()
        
        
class CategorySerializer(serializers.ModelSerializer):
    courses = CourseSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields= ['name', 'description', 'courses']
    
    
        
        
