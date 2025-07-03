# Używamy oficjalnego, lekkiego obrazu Pythona
FROM python:3.11-slim

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy wszystkie pliki z projektu Django do kontenera
COPY . /app

# Instalujemy zależności
RUN pip install --upgrade pip \
 && pip install gunicorn django psycopg2-binary

# Otwieramy port 8080 (nasłuch Gunicorna)
EXPOSE 8080

# Domyślna komenda – uruchamiamy serwer Gunicorn na porcie 8080
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8080"]
