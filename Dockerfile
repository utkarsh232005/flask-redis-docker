# Step 1: Base Image
FROM python:3.9-slim

# Step 2: Set Working Directory
WORKDIR /app

# Step 3: Copy Requirements
COPY requirements.txt .

# Step 4: Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy Application Code
COPY . .

# Step 6: Expose Port
EXPOSE 5000

# Step 7: Define Entrypoint
CMD ["python", "app.py"]