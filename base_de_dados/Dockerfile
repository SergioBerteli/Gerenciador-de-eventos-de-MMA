FROM mysql:latest
COPY ./query-inicial.sql /docker-entrypoint-initdb.d/
ADD etc/bancodedados.cnf /etc/mysql/conf.d/