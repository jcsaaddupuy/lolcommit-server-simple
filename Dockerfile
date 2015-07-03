FROM jcsaaddupuy/nginx-python


ADD docker/nginx/lolcommit-simple.conf /etc/nginx/sites-available/lolcommit-simple/lolcommit-simple.conf
RUN ln -s /etc/nginx/sites-available/lolcommit-simple /etc/nginx/sites-enabled/lolcommit-simple
RUN rm /etc/nginx/sites-enabled/default

ADD docker/supervisord/ /etc/supervisor/conf.d/


RUN useradd lolcommitss
RUN mkdir -p /home/lolcommitss && chown -R lolcommitss /home/lolcommitss
RUN mkdir -p /data && chown -R lolcommitss /data

VOLUME ["/data"]

ENV PYTHON_EGG_CACHE /home/lolcommitss/eggs

ADD . /home/lolcommitss
RUN cd /home/lolcommitss/  && python setup.py install

