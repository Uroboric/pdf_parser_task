# PDF Parser + Tests(Pytest)
[![run_tests](https://github.com/Uroboric/pdf_parser_task/actions/workflows/run_tests.yaml/badge.svg)](https://github.com/Uroboric/pdf_parser_task/actions/workflows/run_tests.yaml)
<p align="center">
<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--I3ObjKUU--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/82ljfvkp9q34w3uqhsx5.png" width="100%" height="auto" alt="Docker Logo">
</p>

## Getting started and run tests localy

To make it easy for you to get started, here's a list of recommended next steps.

### Clone project
```
git clone https://github.com/Uroboric/pdf_parser_task.git
```
### Preliminarily install zbar library
### Install dependencies
```
pip install -r requirements.txt
```

### Changing the file path in 
```
1.parser.py
2.conftest.py
3.test_parser.py
``` 
to the absolute path of pdf file on your local machine.

### Run tests 
```
cd tests
pytest -s -vv
```
