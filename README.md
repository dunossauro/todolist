## TODO list

A simple integration using bottle to test JS request functions


### Structure
```
.
├── back_end.py     # Requests routes
├── front_end.py    # Templates/views routes
├── api.py          # Merge front and back routes
├── db.py           # Simple Sqlalchemy schema
├── static          # Path to put static files
│   └── requests.js
└── views            # Templates path
    └── home.tpl
```

## How to run that?

```
pip install -r requirements.txt
python3 api.py
```


## TODO
- Ajust bootstrap views
- Implement new js functions
