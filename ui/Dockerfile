# ================================= Jupyter-Pyspark ============================
FROM jupyter/pyspark-notebook as notebook

WORKDIR /nb

COPY notebooks ./nb_vol
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
USER root
RUN chmod +x /usr/bin/tini
USER jovyan
ENTRYPOINT ["/usr/bin/tini", "--"]

EXPOSE 8888
CMD ["jupyter", "lab", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--ServerApp.token=''"]
