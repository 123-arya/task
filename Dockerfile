FROM python:3.12-slim

RUN useradd -m docker

WORKDIR /webapp

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R docker:docker /webapp

USER docker

CMD ["python3","app.py"]
