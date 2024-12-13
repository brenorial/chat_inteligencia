import json
from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

# Carregar perguntas e respostas do FAQ em formato JSON
faq_data = {
    "1. PAINEL": {
        "1.1": {
            "pergunta": "Painel não dá imagem",
            "resposta": "CHECK\nProcessadora\nDisjuntor da sala de instrumentos\nDisjuntor do templo (escrito TELÃO)"
        },
        "1.2": {
            "pergunta": "Processadora não liga",
            "resposta": "Disjuntor sala de mídia (ligar todos os botões)\nFiltro de linha na parte inferior da mesa (deve estar ligado, aceso)\nSplitter HDMI em cima da processadora"
        }
    },
    "2. COMPUTADORES": {
        "2.1": {
            "pergunta": "PC não dá imagem",
            "resposta": "Apertar novamente botão de ligar CPU\nApertar novamente botão de ligar Monitor\nFiltro de linha na parte inferior da mesa (deve estar ligado, aceso)"
        },
        "2.2": {
            "pergunta": "PC não funciona mouse ou teclado",
            "resposta": "Trocar pilhas\nTirar e recolocar USB do mouse e teclado\nVerificar se ao colocar USB aparece \"Dispositivo não reconhecido\""
        },
        "2.3": {
            "pergunta": "Sem internet",
            "resposta": "Roteador ligado, apertar cabos de rede\nCaso roteador esteja piscando luzes ao mesmo tempo: tirar fonte, esperar 10 segundos e recolocar\nConectar celular ao Wifi MidiaIBMDC, para conferir se há rede\nRecolocar cabo de rede no servidor"
        }
    },
    "3. TELEVISÃO DE RETORNO": {
        "3.1": {
            "pergunta": "TV não liga",
            "resposta": "Disjuntor da Mídia (última alavanca da esquerda para direita)\nLigar no botão físico, localizado no centro, parte inferior da televisão\nVerificar se há alguma tomada desconectada na parte traseira da tv"
        },
        "3.2": {
            "pergunta": "Não aparece o mesmo da tela de retorno na sala",
            "resposta": "Colocar tv em HDMI 2\nConferir se cabo HDMI está conectado\nConferir HDMI próximo à processadora"
        }
    },
    "4. CÂMERA PTZ": {
        "4.1": {
            "pergunta": "Não liga",
            "resposta": "Disjuntor da Mídia (última alavanca da esquerda para direita)\nLigar cabo de força (desconectado a cada fim de culto)\nVerificar se há alguma tomada desconectada na parte traseira da tv"
        },
        "4.3": {
            "pergunta": "Não funciona controladora",
            "resposta": "Verifique os cabos de conexão da controladora e a alimentação."
        }
    },
    "5. Interface de Áudio": {
        "5.1": {
            "pergunta": "Não chega sinal na interface",
            "resposta": "Retirar e inserir o cabo USB A\nGirar botão de volume 2\nPedir para técnico abrir som da Live (Auxiliar 3)"
        }
    }
}

# Rota API para responder com as FAQs
@app.route('/api/faq', methods=['GET'])
def get_faq():
    return jsonify(faq_data)

# Rota principal que irá exibir a página com FAQs
@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FAQ Suporte</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; padding: 10px; background-color: #f4f4f4; }
            h1 { text-align: center; color: #333; }
            .faq-item { margin-bottom: 20px; }
            .faq-item h3 { color: #007BFF; }
            .faq-item pre { background-color: #e9ecef; padding: 10px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>FAQ Suporte - Dúvidas Frequentes</h1>
        {% for categoria, subcategorias in faq_data.items() %}
            <div class="categoria">
                <h2>{{ categoria }}</h2>
                {% for key, faq in subcategorias.items() %}
                    <div class="faq-item">
                        <h3>{{ faq['pergunta'] }}</h3>
                        <pre>{{ faq['resposta'] }}</pre>
                    </div>
                {% endfor %}
            </div>
        {% endfor %}
    </body>
    </html>
    """
    return render_template_string(html, faq_data=faq_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
