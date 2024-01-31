from rest_framework import serializers

from .models import Metrics, Departments

class DepartmentsSerializer(serializers.ModelSerializer):
    start_date_raw = serializers.CharField(read_only=True, source="metric.start_date")
    start_date = serializers.SerializerMethodField(read_only=True)
    
    def get_start_date(self, obj):
        if obj is not None:
            return obj.metric.start_date.strftime('%b %Y')
        else:
            return None
            
    def get_contests(self, obj):
        if obj is not None:
            print(obj)
            return None
        else:
            return None
    
    class Meta:
        model = Departments
        fields = ['id', 'functions', 'new', 'retained', 'churned', 'metric_id', 'created_on', 'start_date', 'start_date_raw']
        
   

class MetricsSerializer(serializers.ModelSerializer):
    departments = DepartmentsSerializer(many=True)
    class Meta:
        model = Metrics
        fields = ['id', 'start_date', 'created_on', 'departments']