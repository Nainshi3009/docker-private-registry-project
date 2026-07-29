FROM python:3.13
WORKDIR /containerr
COPY . .
RUN pip install -r req.txt
EXPOSE 6000
CMD ["python", "app.py"]
