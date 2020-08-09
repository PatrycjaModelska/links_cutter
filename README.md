# links_cutter

#### Requirements 
    1. Python 3.8
    2. Others packeges in file requirements.txt

### First run
    
    1. Create virtualenv:
            python -m venv myvenv
            cd myvenv/Scripts/activate
    3. Pull repo:
            git clone https://github.com/PatrycjaModelska/Microblog.git
    4. Requirements install:
            pip install -r requirements.txt
    5. Create superuser:
            python manage.py createsuperuser
    6. Migrete data to database:
            python manage.py makemigrations
            python manage.py migrate
    7. Run server:
            python mamage.py runserver
