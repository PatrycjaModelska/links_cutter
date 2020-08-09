# links_cutter

See here and check how it works https://long-links-cutter.herokuapp.com/ or download app for your own computer.

#### Requirements 
    1. Python 3.8
    2. Others packeges in file requirements.txt

#### First run
    
    1. Create virtualenv:
    
            python -m venv myvenv
            cd myvenv/Scripts/activate
            
    2. Pull repo:
    
            git clone https://github.com/PatrycjaModelska/Microblog.git
            
    3. Install requirement packeges:
    
            pip install -r requirements.txt
            
    4. Create superuser:
    
            python manage.py createsuperuser
            
    5. Migrete data to database:
    
            python manage.py makemigrations
            python manage.py migrate
            
    6. Run server:
    
            python mamage.py runserver
