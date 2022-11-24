from rest_framework import serializers
from .models import Student 


class StudentSerializer(serializers.ModelSerializer):
    # name=serializers.CharField(read_only=True)
    class Meta:
        model=Student
        fields=['id','name','roll','city']
        # read_only_fields=['name','city']
        extra_kwars={'name':{'read_only':True}}

# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=100)
#     roll=serializers.IntegerField()
#     city=serializers.CharField(max_length=100)
    
#     def create(self,validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         print(instance.name,'1')
#         instance.name=validated_data.get('name',instance.name)
#         print(instance.name,'2')
#         instance.roll=validated_data.get('roll',instance.roll)
#         instance.city=validated_data.get('city',instance.city)
#         instance.save()
#         return instance
        
        