from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import MetricaSeguranca
from .serializers import MetricaSerializer
from drf_spectacular.utils import extend_schema

class MetricaViewSet(viewsets.ModelViewSet):
    queryset = MetricaSeguranca.objects.all().order_by('data')
    serializer_class = MetricaSerializer


    # AQUI: Usamos o decorador @extend_schema para documentar
    @extend_schema(
        summary="Dados consolidados para Dashboard",
        description="Retorna JSON estruturado com séries temporais e KPIs para gráficos.",
        responses={200: None}, # Como é um JSON livre, deixamos None ou criamos um Serializer dummy
        tags=["Dashboard"]
    )
    # Action Customizada: Dados Agregados para o Dashboard
    @action(detail=False, methods=['get'])
    def dashboard_data(self, request):
        # 1. Filtra dados do domínio principal ordenados por data
        qs = self.queryset.filter(dominio='antt.gov.br').order_by('data')
        
        # Previne erro se tabela estiver vazia
        if not qs.exists():
            return Response({"erro": "Sem dados"}, status=404)

        # 2. Extrai as Listas (Series Temporais)
        datas = [obj.data.strftime("%d/%m") for obj in qs]
        
        # Métricas de Risco
        risco_os = [obj.sistemas_risco for obj in qs]
        lockouts = [obj.usuarios_bloqueados for obj in qs]
        senhas_eternas = [obj.senhas_nao_expiram for obj in qs]
        
        # Métricas de Gestão/Higiene
        admins = [obj.contas_admin for obj in qs]
        stale = [obj.usuarios_obsoletos for obj in qs]
        vazios = [obj.grupos_vazios for obj in qs]

        # 3. Monta o JSON de Resposta
        data = {
            "labels": datas,
            
            "riscos": {
                "os_antigo": risco_os,
                "bloqueados": lockouts,
                "compliance_senhas": senhas_eternas
            },
            
            "gestao": {
                "admins": admins,
                "usuarios_stale": stale,
                "grupos_vazios": vazios
            },
            
            # Cards do Topo (Último valor registrado)
            "kpis": {
                "total_admins": admins[-1] if admins else 0,
                "total_stale": stale[-1] if stale else 0,
                "total_risco": risco_os[-1] if risco_os else 0,
                # Azure é um campo único, pegamos o último valor válido
                "total_azure": qs.last().usuarios_azure if qs else 0
            }
        }
        
        return Response(data)