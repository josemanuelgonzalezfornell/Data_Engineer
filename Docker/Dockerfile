# Obtenemos la imagen. Se intenta buscar la más pequeña posible con lo mínimo neccesario (en este caso lo suyo sería python) para que tarde lo menos posible
FROM tiangolo/uvicorn-gunicorn-fastapi

# copiamos requeriments a la raiz
COPY requeriments.txt .
# instalamos requeriments
RUN pip install -r requeriments.txt

# creamos una carpeta app
RUN mkdir -p app
# copiamos la carpeta app del local a app del contenedor
COPY ./app app

# Exponemos un puerto para liberarlo y decir por donde saldrá
EXPOSE 8080

# Ejecutamos el comando uvicorn... para ejecutar la app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

