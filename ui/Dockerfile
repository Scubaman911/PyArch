# ================================= Jupyter-Pyspark ============================
FROM jupyter/pyspark-notebook as notebook

WORKDIR /nb

USER jup_user

CMD ["jupyter", "lab", "--port=8008", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--ServerApp.token=''"]
