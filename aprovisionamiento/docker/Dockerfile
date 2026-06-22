FROM debian:13
 
RUN apt-get update && apt-get install -y \
    apache2 \
    python3 \
    ansible \
    curl \
    git \
    python3-pytest \
    python3-requests \
    && apt-get clean

EXPOSE 8083

CMD apache2ctl -D FOREGROUND

