echo "BUILD START"
python -m pip install -r requirements.txt
python manage.py collecstatic --noinput --clear
echo "BUILD END"