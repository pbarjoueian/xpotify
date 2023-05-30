# docker/app/Dockerfile
FROM python:3.8

LABEL maintainer="Peyman Barjoueian p.barjoueian@gmail.com"

# Define the user [will create it later]
ARG USER=django
ARG USER_GROUP=django

# Define user related ENVs
ENV HOME=/home/$USER
ENV APP_HOME=$HOME/webapp
ENV LOG_PATH=$HOME/web/logs

# Create directory for the app user & create the app user
RUN mkdir -p $APP_HOME; \
    mkdir -p $LOG_PATH; \
    mkdir -p "$APP_HOME/files"; \
    groupadd $USER_GROUP; \
    useradd -g $USER_GROUP $USER;

# Change workdir to app dir
WORKDIR ${APP_HOME}

# Run OS dependencies before switching the user
RUN apt-get update; \
    apt-get upgrade; \
    apt-get install python3-gdal -y

# Exposing the project port
EXPOSE 8000 8080

# Copy requirements files
COPY Pipfile $APP_HOME

# Install python dependecies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir pipenv \
    && pipenv install --skip-lock --system --deploy \
    && pipenv --clear

# Copy project source files
COPY . ${APP_HOME}
COPY --chmod=755 docker/app/entrypoint.sh /entrypoint.sh

# chown/chmod all the files to the app user
RUN chown -R $USER:$USER_GROUP $APP_HOME
RUN chown -R $USER:$USER_GROUP $LOG_PATH
RUN chown -R $USER:$USER_GROUP $APP_HOME/files
RUN chmod -R 755 $LOG_PATH

# Switch user
USER $USER

ENTRYPOINT ["sh", "/entrypoint.sh"]
CMD ["uwsgi", "--ini", "uwsgi.ini"]
