# links_cutter

Check how it works here: https://long-links-cutter.herokuapp.com/ or download app on your computer.

#### Requirements 

1. Python 3.8
2. Others packeges in file requirements.txt

#### First run

Create virtualenv:
    
    python -m venv myvenv
    cd myvenv/Scripts/activate
            
Pull repo:
    
    git clone https://github.com/PatrycjaModelska/Microblog.git
            
Install requirement packeges:
    
    pip install -r requirements.txt
            
Create superuser:
    
    python manage.py createsuperuser
            
Migrete data to database:
    
    python manage.py makemigrations
    python manage.py migrate
            
Run server:
    
    python mamage.py runserver
