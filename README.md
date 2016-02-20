# home_work
home_work


virtualenv virtenv
source virtenv/bin/activate
pip install -r docs/requirements.txt


python manage.py syncdb
python manage.py migrate


