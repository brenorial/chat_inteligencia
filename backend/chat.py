import os

def main():
    print("Bem-vindo ao Sistema de Suporte!")
    while True:
        print("\nDigite o número referente à categoria ou digite 'sair' para encerrar:")
        print("1. PAINEL")
        print("2. COMPUTADORES")
        print("3. TELEVISÃO DE RETORNO")
        print("4. CÂMERA PTZ")
        print("5. INTERFACE DE ÁUDIO")
        print("6. OBS")
        print("7. HOLYRICS")
        
        user_input = input("\nEscolha uma categoria: ").strip().lower()
        
        if user_input == "sair":
            print("Encerrando o sistema. Até logo!")
            break
        
        responses = {
            "1": {
                "1.1": "Painel não dá imagem:\n- CHECK\n  Processadora\n  Disjuntor da sala de instrumentos\n  Disjuntor do templo (escrito TELÃO)",
                "1.2": "Processadora não liga:\n- CHECK\n  Disjuntor sala de mídia (ligar todos os botões)\n  Filtro de linha na parte inferior da mesa\n  Splitter HDMI em cima da processadora"
            },
            "2": {
                "2.1": "PC não dá imagem:\n- CHECK\n  Apertar novamente botão de ligar CPU\n  Apertar novamente botão de ligar Monitor\n  Filtro de linha na parte inferior da mesa (deve estar ligado, aceso)",
                "2.2": "PC não funciona mouse ou teclado:\n- CHECK\n  Trocar pilhas\n  Tirar e recolocar USB do mouse e teclado\n  Verificar se ao colocar USB aparece 'Dispositivo não reconhecido'",
                "2.3": "Sem internet:\n- CHECK\n  Roteador ligado, apertar cabos de rede\n  Caso roteador esteja piscando luzes ao mesmo tempo: tirar fonte, esperar 10 segundos e recolocar\n  Conectar celular ao Wifi MidiaIBMDC, para conferir se há rede\n  Recolocar cabo de rede no servidor"
            },
        }
        
        if user_input in responses:
            print("\nDigite o subnúmero referente ao problema específico:")
            for key, value in responses[user_input].items():
                print(f"{key} - {value.split(':')[0]}")
            sub_input = input("\nEscolha um subnúmero: ").strip().lower()
            
            if sub_input in responses[user_input]:
                print(f"\n{responses[user_input][sub_input]}")
            else:
                print("Subnúmero inválido. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
