FROM python:3

ADD ./ /som_app

WORKDIR /som_app

ENV FLASK_APP __init__.py
ENV FLASK_DEBUG 1

# RUN pip install flask flask_cors flask_caching numpy webcolors matplotlib tensorflow
RUN pip install -r requirements.txt

CMD ["python", "-u", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]
