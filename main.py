import os

class SistemaMonitoramentoEspacial:
    MAX_HISTORICO = 10

    def __init__(self):
        self.historico = []

    def exibir_menu(self):
        print("\n" + "=" * 15 + " SISTEMA DE MONITORAMENTO ESPACIAL " + "=" * 15)
        print("1. Inserir Dados de Telemetria")
        print("2. Visualizar Status Operacional")
        print("3. Executar Análise e Tomada de Decisão")
        print("4. Encerrar Sistema")
        print("=" * 65)

    def inserir_dados(self):
        print("\n--- Cadastro de Informações de Telemetria ---")

        # Leitura da Temperatura
        while True:
            try:
                temperatura = float(input("Digite a temperatura atual da nave (°C): "))
                break
            except ValueError:
                print("[Erro] Por favor, insira um valor numérico válido para a temperatura.")

        # Leitura e Validação da Energia
        while True:
            try:
                energia = int(input("Digite a porcentagem de energia armazenada nas baterias (0-100): "))
                if 0 <= energia <= 100:
                    break
                print("[Erro] Porcentagem inválida! Insira um valor entre 0 e 100.")
            except ValueError:
                print("[Erro] Digite um número inteiro válido.")

        # Leitura e Validação da Comunicação
        while True:
            try:
                comunicacao = int(input("Digite o status da comunicação (0 = Falha, 1 = OK): "))
                if comunicacao in [0, 1]:
                    break
                print("[Erro] Status inválido! Digite 0 para Falha ou 1 para OK.")
            except ValueError:
                print("[Erro] Digite apenas 0 ou 1.")

        # Estruturação dos dados simulados
        nova_leitura = {
            "temperatura": temperatura,
            "energia": energia,
            "comunicacao": "ONLINE" if comunicacao == 1 else "OFFLINE",
            "captacao_solar": "OTIMIZADA" if energia < 80 and comunicacao == 1 else "CONSERVAÇÃO/LIMITADA",
            "status_modulos": {
                "Suporte de Vida": "OPERACIONAL",
                "Painéis Solares": "ATIVO" if energia < 95 else "STANDBY (Carga Completa)",
                "Sistemas Críticos": "OPERACIONAL"
            }
        }

        # Gerenciamento do histórico
        if len(self.historico) >= self.MAX_HISTORICO:
            self.historico.pop(0)
            print("\n[Aviso] Histórico cheio. A leitura mais antiga foi descartada.")

        self.historico.append(nova_leitura)
        print("\n[Sucesso] Dados cadastrados com sucesso!")

    def visualizar_status(self):
        print("\n--- Status Operacional da Missão ---")

        if not self.historico:
            print("Nenhum dado cadastrado até o momento.")
            return

        # Obtém a leitura mais recente
        atual = self.historico[-1]

        print(f"Temperatura Geral: {atual['temperatura']:.2f}°C")
        print(f"Banco de Baterias: {atual['energia']}%")
        print(f"Captação dos Painéis Solares: {atual['captacao_solar']}")
        print(f"Canal de Comunicação: {atual['comunicacao']}")

        print("\n--- Status dos Módulos de Operação ---")
        for modulo, status in atual['status_modulos'].items():
            print(f"  > Módulo [{modulo}]: {status}")

    def executar_analise(self):
        print("\n--- Análise de Condições e Resposta Automatizada ---")

        if not self.historico:
            print("Nenhum dado disponível para análise. Insira dados primeiro.")
            return

        atual = self.historico[-1]
        alertas_ativos = 0

        # 1. Verificação de Temperatura e Resposta Automatizada
        if atual['temperatura'] > 80:
            print("[ALERTA CRÍTICO] Superaquecimento detectado!")
            print("  [RESPOSTA AUTOMATIZADA] Ativando dissipadores térmicos e redirecionando fluído refrigerante.")
            atual['status_modulos']['Sistemas Críticos'] = "ALERTA (Resfriamento Ativo)"
            alertas_ativos += 1
        elif atual['temperatura'] < 0:
            print("[ALERTA] Temperatura abaixo do ideal estipulado.")
            print("  [RESPOSTA AUTOMATIZADA] Ativando aquecedores internos com energia solar sobressalente.")
            alertas_ativos += 1

        # 2. Verificação de Energia
        if atual['energia'] < 20:
            print("[ALERTA CRÍTICO] Restrição severa de energia (Baterias < 20%)!")
            print(
                "  [RESPOSTA AUTOMATIZADA] Entrando em Modo de Economia Extrema. Desligando subsistemas não-essenciais.")
            atual['status_modulos']['Suporte de Vida'] = "MODO ECO (Energia Restrita)"
            atual['status_modulos']['Painéis Solares'] = "ORIENTAÇÃO MÁXIMA AO SOL (Emergência)"
            alertas_ativos += 1

        # 3. Verificação de Comunicação
        if atual['comunicacao'] == "OFFLINE":
            print("[ALERTA] Falha de comunicação com a estação terrestre!")
            print("  [RESPOSTA AUTOMATIZADA] Reiniciando transponder de rádio e reorientando antenas de alto ganho.")
            alertas_ativos += 1

        # Diagnóstico Final
        if alertas_ativos == 0:
            print("✔ Sistemas operando dentro dos parâmetros normais.")
            print("✔ Matriz energética limpa estável e módulos em perfeita operação.")
        else:
            print(f"\n[Inventário] Total de anomalias tratadas pelo sistema inteligente: {alertas_ativos}")


def rodar_sistema():
    sistema = SistemaMonitoramentoEspacial()

    while True:
        sistema.exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            sistema.inserir_dados()
        elif opcao == "2":
            sistema.visualizar_status()
        elif opcao == "3":
            sistema.executar_analise()
        elif opcao == "4":
            print("\nEncerrando o sistema de monitoramento. Missão finalizada com segurança.")
            break
        else:
            print("\n[Erro] Opção inválida! Tente novamente.")

        input("\nPressione ENTER para continuar...")
        # Limpa o console para melhor usabilidade
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    rodar_sistema()