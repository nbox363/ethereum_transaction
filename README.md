# Ethereum transaction

It's an app that has been created as a test-task for "Финтех" company


# Install 

```bash
$ git clone https://github.com/nbox363/ethereum_transaction.git
$ cd ethereum_transaction
```

Create a virtualenv and activate it:
```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

Install pip packages:
```bash
$ pip install -r requirements.txt
```

# Run
```bash
$ flask init-db
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ flask run
```

Visit http://127.0.0.1:5000/
