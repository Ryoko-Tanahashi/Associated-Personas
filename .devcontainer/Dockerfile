# ベースイメージはPython 3.10
FROM python:3.10

# rootユーザーを使用
USER root

# 必要なパッケージをインストール
RUN apt-get update && \
    apt-get install -y --reinstall ca-certificates && \
    # apt-get -y install software-properties-common && \
    apt-get -y install ffmpeg && \
    pip install --upgrade pip

# 基本的なPythonパッケージをインストール
RUN pip install ipykernel jupyter

ENV CUDA_HOME /usr/local/cuda
ENV PATH $CUDA_HOME/bin:$PATH
ENV LD_LIBRARY_PATH $CUDA_HOME/lib64:$LD_LIBRARY_PATH

# requirements.txtをコンテナにコピーし、依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt