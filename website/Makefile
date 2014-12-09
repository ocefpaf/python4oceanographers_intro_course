.PHONY: clean gen serve

all: clean gen

cp_notebooks:
	mkdir -p content/notebooks
	rsync -ar ../notebooks/*.ipynb content/notebooks/

clean_notebooks:
	rm content/notebooks/*.ipynb

gen: cp_notebooks
	hyde gen

serve: clean gen
	hyde serve

clean: clean_notebooks
	rm -rf deploy

update: gen

publish:
	hyde gen -c production.yaml
	hyde publish -c production.yaml -p github
