# h0w to run

Create a virtual environment  
python3.8 -m venv .env

Activate it  
source .env/bin/activate

Install requirements  
cd src/jaunes  
pip install -r requirements.txt

Run migrations  
python manage.py makemigrations  
python manage.py migrate

Run the server  
python manage.py runserver

