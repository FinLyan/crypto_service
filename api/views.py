from rest_framework.decorators import api_view
from rest_framework.response import Response
from crypto_core.registry import list_ciphers, get_cipher
from rest_framework import status
from api.models import OperationRecord
from crypto_core.exceptions import DecryptionError, InvalidKeyError, InvalidTextError, UnsupportedCipherError

def _perform_operation(request, operation):
    missing = [f for f in ("cipher", "key", "text") if not isinstance(request.data.get(f), str)]
    if missing:
        return Response(
            {"error": f"отсутствуют или не являются строками поля: {', '.join(missing)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    cipher_id = request.data["cipher"]
    key = request.data["key"]
    text = request.data["text"]

    try:
        cipher = get_cipher(cipher_id)
    except UnsupportedCipherError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    try:
        result = cipher.encrypt(text, key) if operation == "encrypt" else cipher.decrypt(text, key)
    except (InvalidKeyError, InvalidTextError, DecryptionError) as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    OperationRecord.objects.create(
        operation=operation, cipher_id=cipher_id, input_text=text, output_text=result,
    )
    return Response({"result": result})

@api_view(["GET"])
def ciphers_list(request):
    return Response(list_ciphers())

@api_view(["POST"])
def encrypt(request):
    return _perform_operation(request, "encrypt")

@api_view(["POST"])
def decrypt(request):
    return _perform_operation(request, "decrypt")