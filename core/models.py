from django.db import models


class MetricaSeguranca(models.Model):
    #  colunas da planilha

    data = models.DateField(help_text="Data de referência da coleta")

    # Kpis principais
    dominio = models.CharField(max_length=255)
    total_usuarios = models.IntegerField(default=0)
    total_grupos = models.IntegerField(default=0)
    # riscos de segurança
    sistemas_risco = models.IntegerField(default=0)
    usuarios_bloqueados = models.IntegerField(default=0)
    # higiene do AD.
    grupos_vazios = models.IntegerField(default=0)
    # nuvem
    usuarios_azure = models.IntegerField(default=0)
    contas_admin = models.IntegerField(default=0, verbose_name="Admins Totais")
    senhas_nao_expiram = models.IntegerField(default=0, verbose_name="Senhas que não expiram")
    usuarios_obsoletos = models.IntegerField(default=0, verbose_name="Usuários Stale")

    class Meta:
        # trazer o mais recente primeiro
        ordering = ['data']
    
    def __str__(self):
        # oque aparece na interface de admin
        return f"{self.dominio} - {self.data}"

