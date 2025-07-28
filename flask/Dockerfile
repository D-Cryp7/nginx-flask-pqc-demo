FROM ubuntu:24.04

RUN apt update && apt install -y build-essential autoconf libtool pkg-config git \
    python3 python3-pip python3-dev libffi-dev ca-certificates

# Instalar wolfSSL con ML-KEM y ML-DSA
RUN git clone https://github.com/wolfSSL/wolfssl.git /tmp/wolfssl \
 && cd /tmp/wolfssl \
 && ./autogen.sh || true \
 && ./configure --enable-dilithium --enable-kyber \
 && make -j"$(nproc)" && make install && ldconfig

# Instalar binding Python
RUN pip install wolfcrypt flask gunicorn --break-system-packages

WORKDIR /app
COPY app.py crypto.py /app/
EXPOSE 8000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
