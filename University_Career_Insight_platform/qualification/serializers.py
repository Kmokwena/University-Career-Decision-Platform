from rest_framework import serializers
from .models import Qualification, ThroughputStats


class ThroughputStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThroughputStats
        field = ['cohort_year', 'total_intake', 'graduated_n_plus_2', 'success_rate']

class QualificationSerializer(serializers.ModelSerializer):
    stats = ThroughputStatsSerializer(read_only=True, required=False)

    class Meta:
        model = Qualification
        field = ['id', 'qualification_name', 'qualification_code', 'duration', 'field_of_study', 'stats']