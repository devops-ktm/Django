# Use official Python image
FROM python:3.13.3

# Set working directory inside the container
WORKDIR /app

# Copy current folder contents into /app in the container
COPY . /app

# Install Django
RUN pip install --no-cache-dir django

# Expose Django's default port
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
