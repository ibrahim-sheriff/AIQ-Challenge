"""
Created by: Ibrahim Sherif
Date: 2023-01-20

This script handles APIs for fetching needed images
"""
from enum import Enum
from io import BytesIO

import cv2
from fastapi import FastAPI
from fastapi.responses import Response
from PIL import Image

from dataloader import DataLoader

app = FastAPI()
data_loader = DataLoader('img_new.csv')

class OpenCVColorMap(str, Enum):
    """
    Enum class to handle OpenCV colormap choices
    """
    HOT = "hot"
    OCEAN = "ocean"


@app.get("/")
async def root():
    """
    Hello world root path for testing purposes

    Returns:
        dict[str, str]: hello world response
    """
    return {"message": "Hello World"}


@app.get("/get_frame")
async def get_frame(min_depth: float, max_depth: float, color_map: OpenCVColorMap):
    """
    This API is used to fetch a slice of data image based on the depth choosen
    and color map needed

    Args:
        min_depth (float): minimum depth
        max_depth (float): maximum depth
        color_map (OpenCVColorMap): color map needed from predefined values

    Raises:
        HTTPException: If color map is out of the given choices

    Returns:
        img: returns an image in png format
    """
    # select slice of image needed based on depth
    mask = (data_loader.depth >= min_depth) & (data_loader.depth <= max_depth)
    img = data_loader.image[mask]

    # choose color_map
    available_color_maps = {
        OpenCVColorMap.HOT: cv2.COLORMAP_HOT,
        OpenCVColorMap.OCEAN: cv2.COLORMAP_OCEAN,
    }
    color_map = available_color_maps[color_map]

    # apply color map and change it to RGB format
    img = cv2.applyColorMap(img, color_map)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # save image to an in-memory bytes buffer
    with BytesIO() as buf:
        img = Image.fromarray(img)
        img.save(buf, format='PNG')
        img = buf.getvalue()

    headers = {'Content-Disposition': 'inline; filename="slice.png"'}
    return Response(img , headers=headers, media_type='image/png')
