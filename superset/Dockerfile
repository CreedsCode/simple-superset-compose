FROM apache/superset:4.1.1

USER root

COPY --chmod=777 superset_config.py /app/
ENV SUPERSET_CONFIG_PATH /app/superset_config.py

USER superset
ENTRYPOINT [ "/usr/bin/run-server.sh" ]
