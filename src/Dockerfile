# Debian Base Image with Python 3.11
FROM python:3.11-bullseye

# Environment variables
ENV PYTHONBUFFERED=1
ENV DJANGO_SETTINGS_MODULE="django_west.settings"

# Copy sources
COPY . /app


# Install Pyton libraries
RUN python -m pip install --no-cache-dir -r /app/requirements.txt 

# Filepath location in Docker container
WORKDIR /app

# Expose Django port
EXPOSE 8080

ENTRYPOINT ["python", "django_west/manage.py", "runserver", "0.0.0.0:8080"]

