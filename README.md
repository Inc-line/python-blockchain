**Activate the virtual environment**

```
source blockchain-env/bin/activate for Bash shell
source blockchain-env/scripts/activate for Powershell
```

**Install all packages**
```
pip install -r requirements.txt
```

**Run the tests**
Make sure to activate the virtual environment.

```
python -m pytest backend/tests

python -m backend.scripts.test_app
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
**Run the frontend**
In the frontend directory:
```
npm run start
```

**Seed the backend with data**
Make sure to activate the virtual environment.
```
export SEED_DATA=True && python -m backend.app
```