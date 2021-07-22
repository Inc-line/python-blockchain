# A Full Blockchain Network in Python
A complete Blockchain Network in Python. The network includes clique minting, wallet front-end, and peer nodes.


## Get the Network Started:

**1. Activate the virtual environment**
To ensure every system has the appropriate system requirements, please initialize the prepared environment using the following command:
```
source blockchain-env/bin/activate for Bash shell
source blockchain-env/scripts/activate for Powershell
```

**2. Install all packages**
If this is the first time running the application, you will need to install the necessary packages with the next command:
```
pip install -r requirements.txt
```

**3. Run the tests**
Before making any transactions on the network, go ahead and run the prepared test scripts with either of the following commands:
```
python -m pytest backend/tests
python -m backend.scripts.test_app
```

**4. Now run the application and API**
Once your environment has been established and the app tested, run the following command to start the Blockchain on the backend:
```
python -m backend.app
```

**5. Run a peer instance**
You can also initialize peer instances of the blockchain at this point. Peers will load in a random port as listed in the console. Run the next command for your console: 
```
export PEER=True && python -m backend.app       for Linux/Bash Systems
env:PEER = 'True'; python -m backend.app        for Windows Powershell
```
**6. Finally, run the frontend**
Go to the frontend directory:
```
npm run start
```

**7. Seed the backend with data**
You'll need data to see what it will do!
```
export SEED_DATA=True && python -m backend.app
```

There are some aspects of this blockchain that still need improving such as:

* Synchronization without the root node
* Catching up a blockchain that's fallen behind
* API Endpoints that read more information
* Transaction pool validating transactions
* Applications for non-miners
* Frontend functionality and styling


### Please feel free to access the google doc work log for this project by clicking [here.](https://docs.google.com/document/d/1NDz9RbvH1QTHhnqP4efmoL-OrwIBX3z1PTuugHb9ZXo/edit?usp=sharing) 
*Thanks for your support!*
