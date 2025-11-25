import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import MetricaSeguranca

class Command(BaseCommand):
    help = 'Lê o arquivo ANTT - 14d01.csv e salva no banco'

    def handle(self, *args, **kwargs):
        # Certifique-se que o arquivo está na mesma pasta do manage.py
        caminho_arquivo = 'ANTT - 14d01.csv'

        if not os.path.exists(caminho_arquivo):
            self.stdout.write(self.style.ERROR(f'Arquivo não encontrado: {caminho_arquivo}'))
            return

        # Dicionário para traduzir os meses do seu CSV (sep, oct, etc)
        mapa_meses = {
            'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06',
            'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'
        }

        with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            contador = 0
            
            for row in reader:
                try:
                    # 1. Tratamento da Data: "01.sep.2024" -> "2024-09-01"
                    partes = row['Date'].split('.') # Divide em ['01', 'sep', '2024']
                    dia = partes[0]
                    mes_texto = partes[1].lower()
                    ano = partes[2]
                    
                    mes_numero = mapa_meses.get(mes_texto)
                    if not mes_numero:
                        continue # Pula se o mês for inválido

                    data_final = f"{ano}-{mes_numero}-{dia}"

                    # 2. Função para converter texto vazio "" em 0
                    def limpar(valor):
                        if not valor or valor.strip() == '':
                            return 0
                        return int(float(valor))

                    # 3. Salvar no Banco
                    MetricaSeguranca.objects.create(
                        data=data_final,
                        dominio=row['Domain Name'],
                        total_usuarios=limpar(row['No of Users']),
                        total_grupos=limpar(row['No of Groups']),
                        sistemas_risco=limpar(row.get('No of Computer Accounts with a Risky Operating System')),
                        usuarios_bloqueados=limpar(row.get('No of Enabled Locked-out Users')),
                        grupos_vazios=limpar(row.get('No of Empty Groups')),
                        usuarios_azure=limpar(row.get('No of Azure AD Cloud users')),
                        contas_admin=limpar(row.get('No of Admin Accounts')),
                        senhas_nao_expiram=limpar(row.get('No of Enabled Accounts with Passwords That Do Not Expire')),
                        usuarios_obsoletos=limpar(row.get('No of Enabled but Stale Users'))
                )
                    contador += 1
                    
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"Erro na linha {contador}: {e}"))

        self.stdout.write(self.style.SUCCESS(f'Sucesso! {contador} linhas importadas.'))