# Set the python version as a build-time argument
# with Python 3.12 as the default
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

# Set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to that same code directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python project requirements
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# set the Django default project name
ARG PROJ_NAME="crmtiw"

EXPOSE 8000    

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
