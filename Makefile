ifeq ($(OS), Windows_NT)

VENV_DIR=venv

all: install build run

run:
	.\venv\Scripts\activate && pytest

install:
	if not exist "$(VENV_DIR)" python -m venv $(VENV_DIR)
	.\venv\Scripts\activate && python -m pip install --upgrade pip
	.\venv\Scripts\activate && python setup.py install

build:
	.\venv\Scripts\activate && python db_seed.py

clean:
	python reset_db.py
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist 
	if exist "./Ecommerce_Site_Testing.egg-info" rd /s /q Ecommerce_Site_Testing.egg-info 
	if exist "$(VENV_DIR)" rd /s /q $(VENV_DIR)

else

VENV_DIR=venv

all: install build run

run:
	. ./venv/bin/activate && python3 -m pytest

install:
	sudo apt install -y python3-venv
	if [ ! -d "$(VENV_DIR)" ]; then python3 -m venv $(VENV_DIR); fi
	chmod +x venv/bin/activate  
	. ./venv/bin/activate && python3 -m pip install --upgrade pip
	. ./venv/bin/activate && python3 setup.py install

build:
	. ./venv/bin/activate && python3 db_seed.py 
	. ./Credantials.sh

clean:
	python3 reset_db.py
	rm -rf build dist Ecommerce_Site_Testing.egg-info $(VENV_DIR)
	find . -iname "*.pyc" -delete

endif
