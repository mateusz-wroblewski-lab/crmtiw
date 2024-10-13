FROM python:3.12-slim-bullseye

# Set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to that same code directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the Python project requirements
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000    

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
