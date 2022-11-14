# FastApi template with SQLAlchemy

### Quickly start:
#### You need to create ```.env``` file in ```./settings``` folder and add there this value:

```
CONN_STRING=mysql+aiomysql://{username}:{password}@{host}:{port}/{database}
```

#### Also you need to replace ```username``` and *others* values 

### That`s It! Run this commands in the root directory 

```console
$ > pip3 install -r requirements.txt
$ > uvicorn app:app
```

### There are also Others Opportunities here: 
- APScheduler
- Logger
- JSONConfig -> [docs here](https://github.com/enveloss/py_json_config)