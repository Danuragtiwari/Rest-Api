from rest_framework import serializers 
from .models import Singer,Song 

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song 
        fields=['id','title','singer','duration']
    
class SingerSerializer(serializers.ModelSerializer):
    # song=serializers.StringRelatedField(many=True,read_only=True)  #to many reelation that why highlight it man!
    # song=serializers.PrimaryKeyRelatedField(many=True,read_only=True)  #it is used to get in 1,2,3 
    # song=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    # song=serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')  #add duration tooo
    song=serializers.HyperlinkedIdentityField(view_name='song-detail')
    class Meta:
        model=Singer 
        fields=['id','name','gender','song'] #,'song' check it man!