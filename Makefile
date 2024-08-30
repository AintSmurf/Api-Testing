ifeq ($(OS), Windows_NT)

VENV_DIR=venv

run: activate
	pytest

install: activate
	python setup.py install

build: activate
	python db_seed.py

clean:
	python reset_db.py
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist 
	if exist "./Ecommerce_Site_Testing.egg-info" rd /s /q Ecommerce_Site_Testing.egg-info 
	if exist "$(VENV_DIR)" rd /s /q $(VENV_DIR)

create_venv:
	python -m venv $(VENV_DIR)

activate:
	$(VENV_DIR)\Scripts\activate

else

VENV_DIR=venv

run: activate
	pytest

install: activate
	python3 setup.py install

build: activate
	python3 db_seed.py 

clean:
	python3 reset_db.py
	rm -rf build dist Ecommerce_Site_Testing.egg-info $(VENV_DIR)
	
create_venv:
	python3 -m venv $(VENV_DIR)

activate:
	source $(VENV_DIR)/bin/activate

endif
