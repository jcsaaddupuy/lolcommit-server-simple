import multiprocessing

user = 'lolcommitss'
bind = "0.0.0.0:8080"


workers = multiprocessing.cpu_count() * 2 + 1


loglevel = "info"

logfile = "/var/log/lolcommitss-gunicorn.log"
pidfile = '/tmp/moviesidsdb-gunicorn.pid'

daemon = False
debug = False
timeout = 300
