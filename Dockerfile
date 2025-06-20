# Dockerfile

# 1. Base image
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy dependencies file
COPY req.txt .

# 4. Install dependencies
RUN pip install --upgrade pip \
 && pip install -r req.txt

# 5. Copy the entire app
COPY . .

# 6. Expose the port
EXPOSE 8000

# 7. Run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
