# Free-Geek 



A scheduling application, built for [Free Geek] (https://www.freegeek.org/), to manage and track volunteer shifts.  

A [Code for Good] (http://codeforgood.io/) project. 

We abide by the [Free Geek volunteer Code of Conduct] (https://www.freegeek.org/sites/default/files/2017-09/FreeGeek_CodeOfConduct.pdf )

## Requirements

- Docker 
- Python 3 
- Pip (bundled with Python 3.4 and above) 



## Getting Started


#### First time setup

- Clone the repo
- Checkout the develop branch 
- Install docker-compose
- Run the following:

``` 
docker-compose build
docker-compose up

```

- In a seperate shell tab run the following: 

```
docker-compose run web python manage.py migrate auth
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

- Visit the site at localhost:8000 
- Visit localhost:8000/admin to view database entries 




#### Continuing work


- Run the following:

```
docker-compose up

```

- Visit the site at localhost:8000 
- Visit localhost:8000/admin to view database entries 
	

## Contributing

**branch off of and make pull requests to DEVELOP, not master.**


## Documentation
