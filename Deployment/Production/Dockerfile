FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir app
WORKDIR app
COPY requirements.txt .
RUN pip install -r requirements.txt && pip install gunicorn
COPY . .
CMD '/app/Deployment/Production/docker-entrypoint.sh'