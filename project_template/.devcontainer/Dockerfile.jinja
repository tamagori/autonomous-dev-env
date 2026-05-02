# .devcontainer/Dockerfile
FROM ubuntu:22.04

# タイムゾーン等のインタラクティブなプロンプトを回避
ENV DEBIAN_FRONTEND=noninteractive

# 基本的なシステムツールとPythonビルド依存関係のインストール
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python3-openssl \
    && rm -rf /var/lib/apt/lists/*

# uvのインストール
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# uvのパスを通す
ENV PATH="/root/.local/bin:${PATH}"

# プロジェクトディレクトリをワーキングディレクトリに設定
WORKDIR /workspace

# デフォルトシェルをbashにする
ENV SHELL /bin/bash