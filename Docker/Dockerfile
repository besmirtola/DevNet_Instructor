FROM python
RUN pip install flask
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY web_app_flask.py /home/myapp/
EXPOSE 8081
CMD python3 /home/myapp/web_app_flask.py
