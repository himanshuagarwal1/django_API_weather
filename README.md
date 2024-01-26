

## Running with Docker

- A sample Dockerfile and a docker-compose is provided to run the application in an isolated environment
- Make sure you have `docker` and `docker-compose` installed and that the Docker daemon is running
- Build and run the container: `docker-compose up`
- Start making some requests: `http://localhost:8000/`

## Running with a virtual environment

- To run the application in a virtual Python environment, follow these instructions. This example will create a virtual Python environment for 3.9.6
- Check you have the pyenv version you need: `pyenv versions`
- You should see 3.9.6
- If you do not have the correct version of Python, install it like this: `pyenv install 3.9.6`
- On command line do this: `~/.pyenv/versions/3.9.6/bin/python -m venv env`
- This creates a folder called env. Then do this to activate the virtual environment: `source env/bin/activate`
- Lastly do this to check that you are now on the correct Python version: `python --version`
- You can install the dependencies with `pip install -r requirements.txt`

- You can then run the app with `python manage.py runserver 0.0.0.0:8000` in the root directory

## Running with a on CMD without any virtualization


- Clone repository.
- install Python
- You can install the dependencies with `pip install -r requirements.txt`

- You can then run the app with `python manage.py runserver ` in the root directory
## Project Structure Notes

- There are one django app installed weather
- Django is used as a RESTful API, no html rendering is required

Project structure:
```
.
├── README.md
├── manage.py
├── requirements.txt
|── test.py
└── techtest(App Folder)
```
POST http://localhost:8000/

REQUEST
```json
{
	"city_name": "berlin",
   "lang" : "de",
}
```
RESPONSE
```json
   
{
   "city": "Berlin", 
   "temperature": {"temp": 7.02, "feels_like": 2.08, "temp_min": 6.57, "temp_max": 7.77, "pressure": 1007, "humidity": 81}, 
   "wind": {"speed": 10.8, "deg": 290}, 
   "description": "Bedeckt"
}
```

# I don't have GIT installed in on my persoanl computer so there is no GIT history plus this test was very small and straight forward so I didn't use Aasyncio

