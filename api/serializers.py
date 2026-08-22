from rest_framework import serializers
from api.models import OperationRecord


class OperationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationRecord
        fields = ["id", "operation", "cipher_id", "input_text", "output_text", "created_at"]