# Use an official Python base image
FROM python

# Create working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy .env file
COPY .env .env

# Copy the app source code
COPY ./src /app/src

# Set working directory to the source folder
WORKDIR /app/src

# Expose FastAPI default port
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
