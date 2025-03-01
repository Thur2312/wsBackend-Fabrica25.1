from rest_framework import generics
from .models import Usuario
from .serializers import UserSerializer
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TranslateText(APIView):

    def post(self, request, format=None):
        texto = request.data.get('text', '')
        traducao_type = request.data.get('traducao_type', 'yoda')

        api_url = f'https://api.funtranslations.com/translate/{traducao_type}.json'
        response = requests.post(api_url, data={'texto': texto})

        if response.status_code == 200:
            texto_traduzido = response.json().get('contents', {}).get('traduzido', '')
            Traducao = Usuario.objects.create(
                texto_original = texto,
                texto_traduzido = texto_traduzido,
                traducao_type = traducao_type
            )
            serializer = UserSerializer(Traducao)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'Erro': 'Falha na tradução'}, status=response.status_code)

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

class UsuarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer