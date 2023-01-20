# drill-image-api
This repo is for a simple API to handle fetching of images in oil and gas domain

## Description
This is a simple project to learn about how to use FastAPI to make APIs that handle images


## Prerequisites and Installation

This project requires 
- ```python >= 3.9```
- ```pip```
- ```virtualenv``` package

Create virtual environment using venv
```bash
python -m venv .venv
```

Activate the virtual environment created
```
source .venv/bin/activate
```

Install needed dependencies from requirements file
```
pip install -r requirements.txt
```

## Usage
1- Start FastAPI app
```bash
uvicorn api:app --reload
```

2- FastAPI app documentation to test the API from the browser
```
http://127.0.0.1:8000/docs
```

## Resources
[OpenCV Colormap](https://learnopencv.com/applycolormap-for-pseudocoloring-in-opencv-c-python/)

[Get image in FastAPI #1](https://stackoverflow.com/questions/71595635/render-numpy-array-in-fastapi)

[Get image in FastAPI #2](https://stackoverflow.com/questions/66265511/how-to-return-image-and-json-in-one-response-in-fastapi)

[Get image in FastAPI #3](https://stackoverflow.com/questions/55873174/how-do-i-return-an-image-in-fastapi)

