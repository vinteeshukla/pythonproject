from chatbot.models import DetailForm, text
from rest_framework import serializers, viewsets, routers 
class chat_detailSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    name_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  
    class Meta:
        model = DetailForm
        fields = (
            'pk',
            'title',
            'name_id',
            'description',
            'mobile',
            'password',
            'email')
  
  
class chat_TaskSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    message = serializers.PrimaryKeyRelatedField(queryset=DetailForm.objects.all(),
                                                  many=False)     
  
    class Meta:
        model = text
        fields = (
            'pk',
            'message',
            'time'
           )

