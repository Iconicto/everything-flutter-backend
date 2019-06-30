FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir app
WORKDIR app
COPY requirements.txt .
RUN pip install -r requirements.txt && pip install gunicorn
COPY . .
RUN ["chmod", "+x", "/app/Deployment/Production/docker-entrypoint.sh"]
CMD '/app/Deployment/Production/docker-entrypoint.sh'