# links_cutter


### Uruchomienie projektu 
    1. Wymagania sprzętowe:
    
            python 3.8
            
    2. Tworzenie środowiska w konsoli:
    
            python -m venv myvenv
            cd myvenv/Scripts/activate
            
    3. Ściąganie repozytorium:
    
            git clone https://github.com/PatrycjaModelska/Microblog.git
    
    4. Instalowanie wymaganych plików:
    
            pip install -r requirements.txt.
    
    5. Utworzenie superuser:
    
            python manage.py createsuperuser
    
    6. Migracja danych do tabel w bazie:
    
            python manage.py makemigrations
            python manage.py migrate
            
    7. Uruchomienie serwera:
    
            python mamage.py runserver
