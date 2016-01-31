API Example

It's a very simple API made with <a href="https://github.com/jespino/anillo/" target="_new">Anillo</a> and Python. To get ready with your environment:

* You need to copy <em>myapp.ini</em> and <em>pytest.ini</em> files outside the repository
* You need to export two env vars: MY_APP and MY_APP_TEST, pointing the previous files
* You need sqlite (usually it's in all Linux)
* I encourage you to use a virtualenv (with Python3!!!)
* You need to install <em>requirements.txt</em> and <em>requirements-server.txt</em>

Note: if you're not using postgres (not mandatory!), you don't need to install psycopg2 (which is in `requirements.txt`)

Once you've all of this, you can run the API locally directly with Anillo:
```
(myvenv) src/ $ python run.py serve --create-db --with-fixtures --no-hot-reload
```

Or, if you installed <em>requirements-server.txt</em>, you can run the application with Gunicorn:
```
(myvenv) src/ $ gunicorn -b 0.0.0.0:5005 --access-logfile - --error-logfile - --log-level debug 'wsgi:load_application("create-db", "with-fixtures")'
```

And you can run the tests:
```
(myvenv) src/ $ python run.py test
```
