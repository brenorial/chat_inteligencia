# Use a imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o código para o container
COPY sistema_ia.py /app/sistema_ia.py

# Define o comando padrão ao iniciar o container
CMD ["python", "sistema_ia.py"]
