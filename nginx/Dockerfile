FROM ubuntu:24.04

RUN apt update && apt install -y build-essential wget cmake git libpcre3-dev zlib1g-dev

# 1) Descargar y compilar OpenSSL 3.5
RUN wget https://www.openssl.org/source/openssl-3.5.0.tar.gz \
 && tar xzf openssl-3.5.0.tar.gz \
 && cd openssl-3.5.0 \
 && ./Configure --prefix=/opt/openssl-3.5 shared && make -j4 && make install

ENV PATH="/opt/openssl-3.5/bin:$PATH" LD_LIBRARY_PATH="/opt/openssl-3.5/lib"

# 2) Descargar y compilar Nginx apuntando a OpenSSL 3.5
RUN wget http://nginx.org/download/nginx-1.27.4.tar.gz \
 && tar xzf nginx-1.27.4.tar.gz \
 && cd nginx-1.27.4 \
 && ./configure --prefix=/opt/nginx \
      --with-http_ssl_module \
      --with-http_v2_module \
      --with-openssl=../openssl-3.5.0 \
      --with-cc-opt="-I/opt/openssl-3.5/include" \
      --with-ld-opt="-L/opt/openssl-3.5/lib" \
 && make -j4 && make install

COPY nginx.conf /opt/nginx/conf/nginx.conf

EXPOSE 8443

CMD ["/opt/nginx/sbin/nginx", "-g", "daemon off;"]
