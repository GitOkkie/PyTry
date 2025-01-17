In this directory, run:
```
python3 -m venv venv
```

This will create an evironment where you can install python packages 
without messing with the os configuration.

To enable access to these packages, `cd` into this directory and run:
```
source venv/bin/activate
```

Now if your project needs <module>, you can do stuff like:
```
pip install <module>
```

