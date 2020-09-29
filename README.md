**Activate the virtual environment**

```
source blockchain-env/bin/activate for Linux systems
source blockchain-env/scripts/activate for Windows systems
```

**Install all packages**
```
pip install -r requirements.txt
```

**Run the tests**
Make sure to activate the virtual environment.

```
python -m pytest backend/tests
```

**Run the application and API**
Make sure to activate the virtual environment.

```
python -m backend.app
```

**Run a peer instance**
Make sure to activate the virtual environment.

```
export PEER=True && python -m backend.app       for Linux/Bash Systems
env:PEER = 'True'; python -m backend.app        for Windows Powershell
```
