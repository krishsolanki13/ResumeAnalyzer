# # # Step 1: Use an official Python runtime as a parent image
# # FROM python:3.13-alpine
# FROM python:3.9-alpine


# # Step 2: Set the working directory
# WORKDIR /app

# # Step 3: Copy the current directory contents into the container at /app
# COPY . /app

# # Step 4: Install build dependencies
# RUN apk add --no-cache build-base

# # Step 5: Install any dependencies that are in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Step 6: Expose port 8501 for Streamlit
# EXPOSE 8501

# # Step 7: Run the application
# CMD ["streamlit", "run", "main.py"]



# Step 1: Use an official Python runtime as a parent image (use python:3.9-slim for more tools)
FROM python:3.9-slim

# Step 2: Set the working directory
WORKDIR /app
ENV PYTHONPATH=/app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Step 5: Upgrade pip to ensure we are using the latest version
RUN pip install --upgrade pip

# Step 6: Install any dependencies that are in requirements.txt
# Use --prefer-binary to prioritize pre-built binaries and avoid source compilation for pyarrow
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Step 7: Expose port 8501 for Streamlit
EXPOSE 8501

# Step 8: Run the application
CMD ["streamlit", "run", "frontend/main.py"]
