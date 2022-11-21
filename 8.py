# Update Data:- partial update data and full update data:
# Partial update:- some of the field is updated
# Full update :-All the field is updated

# Code

# instance:-old data stored in database.
# Validated_data:-new data from user for updation

from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name=serializers.CharFoield(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    
# For complete update
# By default,serializers must be passed values for all required fields or they will raise validation errors.
# required all data rom front end /client
serializer=StudentSerializer(stu,data=pythondata)
if serializer.is_valid():
    serializer.save()
    
# For partial update:- All data is not required
serializer=StudentSerializer(stu,data=pythondata,partial=True)
