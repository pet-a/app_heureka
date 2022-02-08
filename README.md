# Language detector FAST API app 

API for language detection, which uses ```gcld3``` Python library.
This app was created as a part of Heureka coding challenge. 

## Instalation 

This project uses [poetry](https://python-poetry.org/) dependency manager and conda enviroment manager.

Install the poetry with the command below and conda from [this](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) website first

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

after installing poetry and conda clone this Git repository and change directory to app_heureka

```
git clone https://github.com/pet-a/app_heureka.git
cd app_heureka
```

create enviroment using conda

```
conda create -n myenv python=3.8
```

and install all the dependencies using poetry

```
poetry install
```

## Run the project

After installing all the dependencies you can run the project with this command:
```
poetry run start
```
