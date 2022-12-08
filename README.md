# medita_api

## How to run the api ?
### Install Requirments

## Database configuration 
1. Install MySQL Server & Workbench
2. create database called 'medita_db'


## Enviroment Configuration
1. download python version 3.9.13
2. install virtual env python lib in your python version
> pip install virtualenv
3. clone the repository
4. move to the root dir
> cd medita_api
5. open the terminal and write this command
> virtualenv venv
6. after create the virtual enviroment run this command to activate it
> venv\Scripts\activate
7. the run this command
> pip install -r requirements.txt
8. migrate the database
> py manage.py migrate
9. then run this command 
> py manage.py run server

### Importent Step
Use Ngrok to deploy the api in the web to access it in the mobile app (Localhost didn't work with the local app development)
Now The server is open
