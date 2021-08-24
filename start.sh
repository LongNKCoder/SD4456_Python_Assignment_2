python -m venv ".venv"
. ./.venv/bin/activate
pip install -r ./assignment/requirements.txt
python ./assignment/manage.py migrate
cp ./assignment/backup/backupdb.sqlite3 ./assignment/db.sqlite3
python ./assignment/manage.py runserver 0.0.0.0:5000
