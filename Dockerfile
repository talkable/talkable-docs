FROM python:3.13-alpine3.21

# Install dependencies
WORKDIR /docs
ADD requirements.txt /docs
RUN python3 -m pip install -r requirements.txt
