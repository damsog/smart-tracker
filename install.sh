sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.7
python3.7 -m pip install virtualenv
python3.7 -m virtualenv smarttracker
source smarttracker/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install fastapi
python3 -m pip install "uvicorn[standard]"
python3 -m pip install prisma
prisma generate
prisma migrate dev --name init