FROM python:3.12-alpine

# Set the working directory to /app (where manage.py is located)
WORKDIR /app

# Install dependencies required for psycopg2 and other packages
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev postgresql-dev

# Copy the manage.py file and the Backend directory


# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/Backend/requirements.txt

COPY ./manage.py /app/
COPY . /app/Backend

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]