FROM python:3.10

USER root

RUN apt-get update && \
    apt-get install -y --reinstall ca-certificates && \
    apt-get -y install ffmpeg && \
    pip install --upgrade pip

RUN pip install ipykernel jupyter

ENV CUDA_HOME /usr/local/cuda
ENV PATH $CUDA_HOME/bin:$PATH
ENV LD_LIBRARY_PATH $CUDA_HOME/lib64:$LD_LIBRARY_PATH

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt