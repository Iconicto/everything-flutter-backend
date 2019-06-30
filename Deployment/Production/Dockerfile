FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir app
WORKDIR app
COPY requirements.txt .
RUN pip install -r requirements.txt && pip install gunicorn
COPY . .
ENTRYPOINT ['/app/Deployment/Production/docker-entrypoint.sh']
CMD ['gunicorn', 'EverythingFlutter.wsgi', '-b', '0.0.0.0:8000']