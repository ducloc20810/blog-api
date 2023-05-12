# Blog

An amazing and interesting blog

## Installation

### Set up virtual environment

With `virtualenv`
```shell
virtualenv venv 
source venv/bin/activate 
deactivate
```

or with `pyenv virtualenv`
```shell
pyenv virtualenv 3.11 venv
pyenv local venv
pyenv init - 
pyenv virutalenv-init -
```

### Inside virtual environment
Install deps
```shell
poetry install
```

Run server
```shell
python3 run.py 
```