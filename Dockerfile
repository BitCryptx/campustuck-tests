FROM python:3.9-slim

# Chromium aur WebDriver install karna
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Work directory set karna
WORKDIR /app

# Requirements install karna
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Saara code container mein copy karna
COPY . .

# Pytest ke zariye tests run karna
CMD ["pytest", "-v", "test_app.py"]