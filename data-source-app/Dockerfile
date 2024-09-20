# simple BASE-Image
FROM python:3.10.11

# working directory for te container
WORKDIR /fx_data_source

# Install requirements
COPY ./req.txt  /fx_data_source/req.txt
RUN pip install --no-cache-dir --upgrade -r /fx_data_source/req.txt

# Run "API-APP"
COPY ./app /fx_data_source/app
CMD ["uvicorn", "app.poc_data_source:app", "--host", "0.0.0.0", "--port", "80"]
# NOTE: we might want to change the port-cfg depending on the deployment
#       on the individual k8s-clusters (Arno's cluster, Catena cluster, SFH ...) 