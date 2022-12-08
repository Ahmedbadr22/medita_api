# medita_api

## How to run the api ?
### Install Requirments

## Database configuration 
1. Install MySQL Server & Workbench
2. make you server user name = root
3. make your server password = 48259665a
4. create database called 'medita_db'


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

## Endpoints
Base url = "127.0.0.1"

### Authentication apis
authentication/user-register [name='normal_user_registration']
authentication/admin-register [name='superuser_registration']
authentication/doctor-register [name='superuser_registration']
authentication/login [name='obtain_token']
authentication/token/refresh [name='token_refresh']
authentication/token/varify [name='token_varify']
authentication/token/block [name='token_block']

### clinic apis
clinic/add-banner
clinic/add-speciality
clinic/add-favorite-doctor
clinic/add-review
clinic/add-hospital
clinic/add-doctor
clinic/list-banners
clinic/list-specialities
clinic/list-favorite-doctors
clinic/list-reviews
clinic/list-hospitals
clinic/list-doctors
