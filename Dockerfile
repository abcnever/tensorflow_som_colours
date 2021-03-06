FROM python:3

# copy requirements.txt and pip install to utilize docker caching mechnism so
# we won't install all the packages over again whenever we modified the codes
COPY requirements.txt /som_app/

WORKDIR /som_app

RUN pip install -r requirements.txt

ENV FLASK_APP __init__.py
ENV FLASK_DEBUG 1
ENV MPLBACKEND agg

COPY . .

CMD ["python", "-u", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]
