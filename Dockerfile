# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.7-buster

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache

RUN mkdir -p /opt/app/TWT
RUN mkdir -p /opt/app/public
RUN mkdir -p /opt/app/TWT/public

COPY requirements.txt start-server.sh /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY our_secrets.py manage.py /opt/app/
COPY public /opt/app/public/
COPY public /opt/app/TWT/public/
COPY TWT /opt/app/TWT/
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]