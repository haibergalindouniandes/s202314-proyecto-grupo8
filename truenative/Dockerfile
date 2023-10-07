FROM python:3.10 AS base
LABEL author="h.galindos@uniandes.edu.co"
RUN apt-get update && apt-get install -y
RUN apt-get install telnet -y
RUN pip install --upgrade pip
RUN pip install pipenv

FROM base AS app
WORKDIR /home/appuser/app
COPY ["Pipfile", "Pipfile.lock", "./"]
COPY src/. /home/appuser/app

FROM app AS release
EXPOSE 3000

FROM release AS dev
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
RUN pipenv install --system --deploy --dev
CMD ["python", "main.py"]

FROM release AS prod
RUN pipenv install --system --deploy
CMD ["gunicorn", "--bind", ":3000", "main:app"]