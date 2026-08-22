from django.db import models

class OperationRecord(models.Model):
    OPERATION_CHOICES = [
        ("encrypt", "encrypt"),
        ("decrypt", "decrypt"),
    ]
    
    operation = models.CharField(max_length=10, choices=OPERATION_CHOICES)
    cipher_id = models.CharField(max_length=32)
    input_text = models.TextField()
    output_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.operation}:{self.cipher_id}:{self.created_at}"