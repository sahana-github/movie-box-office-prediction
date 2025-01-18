# Use Python 3.10 or newer
FROM python:3.10-slim

WORKDIR /app

# Copy and install dependencies
COPY ../requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project files
COPY ../ .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
