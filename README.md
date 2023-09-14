# data located at docs/source/json-data
- docs/source/json-data/meetups.json
- docs/source/json-data/speakers.json

# installation
```bash
python3.11 -m venv .venv
. .venv/bin/activate

poetry install
pre-commit install
```

# generate/update rst and build html docs
```bash
generate-rst  # whenever you have new data, run this command and commit
cd docs
make html  # index.html is generated in docs/build/html
```
