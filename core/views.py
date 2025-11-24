from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import MetricaSeguranca
from .serializers import MetricaSerializer

class MetricaViewSet(viewsets.ModelViewSet):
    queryset = MetricaSeguranca.objects.all()
    serializer_class = MetricaSerializer
    
    # Configuração de Filtros
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dominio', 'data'] # Habilita ?dominio=X

    # Action Customizada: Resumo Gerencial
    @action(detail=False, methods=['get'])
    def resumo(self, request):
        """
        Retorna apenas os dados da data mais recente (ex: a foto de hoje)
        """
        # Pega a primeira data que aparece no banco (já está ordenado por data desc)
        registro_recente = MetricaSeguranca.objects.first()
        
        if not registro_recente:
            return Response([])

        # Filtra tudo que for dessa data
        dados_do_mes = MetricaSeguranca.objects.filter(data=registro_recente.data)
        
        serializer = self.get_serializer(dados_do_mes, many=True)
        return Response(serializer.data)