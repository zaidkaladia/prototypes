FROM python:3.13

# Make a directory for our app
WORKDIR /api/

# Adding requirements file to current directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy our source code
COPY ./src/ .

EXPOSE 4000

# Run the application
CMD ["python", "./app.py"]