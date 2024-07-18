# İHA Kiralama

## Kurulum

Projeyi çalıştırmak için aşağıdaki adımları izleyiniz.

### Gereksinimler

- Python 3.x
- Django 5.x
- PostgreSQL
- Diğer gereksinimler proje içerisinde requirements.txt içerisinde bulunmaktadır

### Kurulum Adımları

1. **Proje Klonlama ve Çalıştırma**

   ```bash
    git clone https://github.com/kamilsimsek/iha-kiralama.git
    cd iha-kiralama
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
Tarayıcınızda http://localhost:8000 adresine giderek projeyi görüntüleyebilirsiniz.


2. **Docker Setup**

    ```bash
    docker compose build
    docker-compose up
    python manage.py test rental.tests  

3. **Unit Test**

    ```bash
    python manage.py test rental.tests  
