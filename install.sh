sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.7
python3 -m pip install virtualenv
virtualenv smarttracker --python=python3.7
source smarttracker/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install fastapi
python3 -m pip install "uvicorn[standard]"