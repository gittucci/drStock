# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Atualiza o pip e o setuptools para as versões mais recentes e instala o Cython
RUN pip3 install --upgrade pip
RUN pip3 install httpx

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY ./app /app

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8007", "--reload"]