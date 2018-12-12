from rest_framework import serializers
from Student.models import Students,Courses

class coursedetails(serializers.ModelSerializer):
	class Meta:
		model = Courses
		fields = ('C_id','C_name','C_credits')

class studentlogserializer(serializers.ModelSerializer):
	S_courses = coursedetails(many=True,read_only=True)
	class Meta:
		model = Students
		fields = ('S_id','S_name','S_email','S_courses')

class courselogserializer(serializers.ModelSerializer):
	class Meta:
		model =  Students
		fields = ('S_id','S_name','S_email')