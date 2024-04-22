FROM python:3.9-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN apt-get update && \
    apt-get install -y netcat-openbsd
COPY . .

COPY wait-for.sh .
# Expose port 8000 to the outside world
EXPOSE 8000
#CMD python3 -m uvicorn app:app --reload --host 0.0.0.0 --port 80
# Command to run the FastAPI application
#RUN python3 -m uvicorn main:app --reload
# CMD [ "python", "-m", "uvicorn", "index:app", ,"--reload", "--host", "0.0.0.0", "--port", "8000"]
RUN chmod +x wait-for.sh
CMD ["uvicorn", "index:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]