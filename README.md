### Blog

#### Install with `virtual env`

##### Set up virtual environment

With `virtualenv`
```shell
virtualenv venv # create 'venv' folder
source venv/bin/activate # activate env
deactivate # deactivate env
```

or with `pyenv virtualenv`
```shell
pyenv virtualenv 3.11 venv
pyenv local venv
eval "$(pyenv init -)}" # create '.python-version' file 
eval "$(pyenv virutalenv-init -)}" # init venv automatically
```

##### Inside virtual environment
Install deps
```shell
poetry install
```

Run server
```shell
python3 run.py 
```