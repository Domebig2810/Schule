# Basisimage für Python-Anwendungen
FROM python:3.12-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Zuerst nur die Abhängigkeiten kopieren und installieren (Docker-Cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Anwendungscode kopieren
COPY main.py .

# Port, auf dem die App im Container lauscht
EXPOSE 5000

# Startbefehl des Containers: python main.py
CMD ["python", "main.py"]