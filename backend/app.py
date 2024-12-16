import customtkinter as ctk
import webbrowser 
from tkinter import messagebox
from dotenv import load_dotenv
import os

load_dotenv()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

faq_data = {
    "Painel": {
        "Painel não dá imagem": [
            "Verificar processadora.",
            "Conferir disjuntor da sala de instrumentos.",
            "Checar disjuntor do templo (escrito TELÃO)."
        ],
        "Processadora não liga": [
            "Checar disjuntor sala de mídia (ligar todos os botões).",
            "Filtro de linha na parte inferior da mesa (deve estar ligado, aceso).",
            "Splitter HDMI em cima da processadora."
        ],
    },
    "Computadores": {
        "PC não dá imagem": [
            "Apertar novamente botão de ligar CPU.",
            "Apertar novamente botão de ligar Monitor.",
            "Filtro de linha na parte inferior da mesa (deve estar ligado, aceso)."
        ],
        "PC não funciona mouse ou teclado": [
            "Trocar pilhas.",
            "Tirar e recolocar USB do mouse e teclado.",
            "Verificar se ao colocar USB aparece 'Dispositivo não reconhecido'."
        ],
        "Sem internet": [
            "Certificar-se que o roteador está ligado, apertar cabos de rede.",
            "Caso roteador esteja piscando luzes ao mesmo tempo, tirar fonte, esperar 10 segundos e recolocar.",
            "Conectar celular ao Wi-Fi MidiaIBMDC, para conferir se há rede.",
            "Recolocar cabo de rede no servidor."
        ],
    },
    "Televisão de Retorno": {
        "TV não liga": [
            "Disjuntor da Mídia (última alavanca da esquerda para direita).",
            "Ligar no botão físico, localizado no centro, parte inferior da televisão.",
            "Verificar se há alguma tomada desconectada na parte traseira da TV."
        ],
        "Não aparece o mesmo da tela de retorno na sala": [
            "Colocar TV em HDMI 2.",
            "Conferir se cabo HDMI está conectado.",
            "Conferir HDMI próximo à processadora."
        ],
    },
    "Câmera PTZ": {
        "Não liga": [
            "Disjuntor da Mídia (última alavanca da esquerda para direita).",
            "Ligar cabo de força (desconectado a cada fim de culto).",
            "Verificar se há alguma tomada desconectada na parte traseira da TV."
        ],
        "Não funciona controladora": [
            "Verificar cabos de conexão e estado da controladora."
        ],
    },
    "Interface de Áudio": {
        "Não chega sinal na interface": [
            "Retirar e inserir o cabo USB A.",
            "Girar botão de volume 2.",
            "Pedir para técnico abrir som da Live (Auxiliar 3)."
        ],
        "Chega sinal no OBS mas não nos alto-falantes": [
            "Retirar e inserir o cabo USB A.",
            "Aumentar volume na caixa da direita.",
            "Girar para a opção DIRECT no botão DIRECT/USB.",
            "Aumentar botão de volume 2.",
            "Girar botão grande à direita.",
            "Solicitar ao técnico de som para abrir som da Live (Auxiliar 3)."
        ],
        "Chiado": [
            "Retirar e inserir o cabo USB A.",
            "Informar ao técnico de som para tomar as medidas necessárias."
        ],
    },
    "OBS": {
        "Aplicativo não abre": [
            "Verificar se está aberto em segundo plano (CTRL + SHIFT + ESC).",
            "Fechar todos aplicativos abertos.",
            "Reiniciar máquina."
        ],
        "Não aparece a imagem da câmera": [
            "Ligar câmera na tomada.",
            "Habilitar ícone de visualização no software.",
            "Selecionar cena 'PTZ'.",
            "Subir a fonte de entrada para primeira posição.",
            "Retirar e inserir novamente o conversor HDMI/USB (ao lado da CPU)."
        ],
        "Live com som duplicado": [
            "Fechar guia do YouTube.",
            "Fechar página do Chrome.",
            "Habilitar fonte de áudio apenas Mesa/Mic Aux."
        ],
        "Não aparece legenda/versículo": [
            "Abrir e não fechar Plugin no Holyrics (Ferramentas - Plugin).",
            "Habilitar ícone de visualização no software.",
            "Subir a fonte de rede para primeira posição.",
            "Clicar duas vezes na fonte, apertar em atualizar cache da página."
        ],
    },
    "Holyrics": {
        "Não aparece as imagens": [
            "Arquivo excluído ou movido de pasta.",
            "Verifique na pasta Lixeira.",
            "Verifique na pasta Downloads.",
            "Baixe novamente."
        ],
        "Tela toda preta": [
            "Na aba de vídeo, clique no ícone da tela.",
            "Vá em Ferramentas > Painel de Comunicação > Exibir à frente de tudo (Não selecione).",
            "Reiniciar máquina."
        ],
    }
}


def mostrar_faq():
    grupo = grupo_selecionado.get()
    topico = topico_selecionado.get()

    if not (grupo and topico):
        messagebox.showwarning("Aviso", "Por favor, selecione um Grupo e um Tópico.")
        return

    passos = faq_data.get(grupo, {}).get(topico, [])
    if not passos:
        return  

    for widget in solucao_frame.winfo_children():
        widget.destroy()

    for idx, passo in enumerate(passos):
        var = ctk.StringVar(value="Não concluído")
        check = ctk.CTkCheckBox(solucao_frame, text=passo, variable=var, onvalue="Concluído", offvalue="Não concluído", state="normal")
        check.pack(anchor="w", padx=10, pady=5, ipadx=10, ipady=5)
        solucao_vars.append((check, var))

def atualizar_topicos(opcao_grupo):
    topicos = list(faq_data.get(opcao_grupo, {}).keys())
    topico_selecionado.set("")
    menu_topico.configure(values=topicos)

def exibir_mensagem(estado):
    if estado == "Concluído":
        resposta_label.configure(text="Obrigado, Chat BRA agradece")
    else:
        resposta_label.configure(text="Me chame no wpp")

def marcar_como_soluconado(indice):
    checkbox, var = solucao_vars[indice]
    var.set("Concluído")
    checkbox.configure(state="disabled")
    exibir_mensagem("Concluído")
    ultimo_checkbox.set(indice)

def marcar_todas_como_soluconadas():
    for idx, (checkbox, var) in enumerate(solucao_vars):
        if idx == ultimo_checkbox.get():
            var.set("Concluído")
            checkbox.configure(state="disabled")
    exibir_mensagem("Concluído")

def marcar_todas_como_nao_soluconadas():
    for checkbox, var in solucao_vars:
        var.set("Não concluído")
        checkbox.configure(state="disabled")
    
    grupo = grupo_selecionado.get()
    subgrupo = topico_selecionado.get()
    checkboxes_marcados = [check.cget('text') for check, var in solucao_vars if var.get() == "Não concluído"]
    
    mensagem_wpp = f"Breno, não consegui solucionar o problema {grupo} {subgrupo}, tentei {', '.join(checkboxes_marcados)}"
    
    numero_whatsapp = os.getenv("WHATSAPP_NUMBER")

    url = f"https://wa.me/{numero_whatsapp}?text={mensagem_wpp}"
    webbrowser.open(url) 
    exibir_mensagem("Não concluído")

def mostrar_resposta(resposta):
    resposta_label.config(text=resposta)

app = ctk.CTk()
app.title("Dúvidas Frequentes (FAQ)")
app.geometry("600x650")

titulo = ctk.CTkLabel(app, text="Dúvidas Frequentes (FAQ)", font=("Arial", 18, "bold"))
titulo.pack(pady=15)

grupo_selecionado = ctk.StringVar()
ctk.CTkLabel(app, text="Selecione um Grupo:", font=("Arial", 12)).pack(pady=5)
menu_grupo = ctk.CTkOptionMenu(app, variable=grupo_selecionado, values=list(faq_data.keys()), command=atualizar_topicos)
menu_grupo.pack(pady=10)

topico_selecionado = ctk.StringVar()
ctk.CTkLabel(app, text="Selecione um Tópico:", font=("Arial", 12)).pack(pady=5)
menu_topico = ctk.CTkOptionMenu(app, variable=topico_selecionado, values=[])
menu_topico.pack(pady=10)

botao_exibir = ctk.CTkButton(app, text="Exibir Informações", command=mostrar_faq)
botao_exibir.pack(pady=10)

solucao_frame = ctk.CTkFrame(app)
solucao_frame.pack(pady=10, padx=20, fill="both")
solucao_frame.pack(fill="both", expand=True)

resposta_label = ctk.CTkLabel(app, text="", font=("Arial", 12, "bold"))
resposta_label.pack(pady=5)

solucao_vars = []
ultimo_checkbox = ctk.IntVar(value=-1)

botao_marcar_todas_soluconadas = ctk.CTkButton(app, text="Solucionado", command=marcar_todas_como_soluconadas)
botao_marcar_todas_soluconadas.pack(pady=10)

botao_marcar_todas_nao_soluconadas = ctk.CTkButton(app, text="Não Solucionado", command=marcar_todas_como_nao_soluconadas)
botao_marcar_todas_nao_soluconadas.pack(pady=10)

app.mainloop()
