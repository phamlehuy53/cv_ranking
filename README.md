## Rank CV by extracted fields

---

## Features

- Checking valid Vietnamese phone number
- Find out university,college,... and graduated grade

---

## Requirements

- https://github.com/nlp-uoregon/trankit
- https://github.com/seatgeek/fuzzywuzzy
- https://github.com/trungtv/pyvi
---
## Usage

```python
python main.py --help
usage: main.py [-h] [-d | -f] [-o | -v]

optional arguments:
  -h, --help     show this help message and exit
  -d, --dir      Path to direcotry contain CVs
  -f, --fpath    Path to CV file
  -o, --output   Path to output csv
  -v, --verbose  Print to stdout
```

### Run with file

```python
python main.py -f _C__Users_admin_Downloads_dieninfo.html_1615456033471.txt -o score_cv.csv
```

### Run with directory

```python
python main.py -d cv_samples/ -o score_cv.csv 
```

