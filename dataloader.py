"""
Created by: Ibrahim Sherif
Date: 2023-01-20

This script handles dataloading of image in CSV files
"""
import numpy as np
import pandas as pd


class DataLoader:
    """
    Handles loading and preprocessing of image and depth in CSV format
    to numpy array format
    """
    __image__ = None
    __depth__ = None

    def __init__(self, file_path: str):

        img_df = pd.read_csv(file_path)

        depth = img_df.pop('depth').to_numpy()
        img_arr = img_df.to_numpy().astype(np.uint8)

        self.__image__ = img_arr
        self.__depth__ = depth

    @property
    def image(self) -> np.ndarray:
        """
        Getter function for image

        Returns:
            np.ndarray: loaded image
        """
        return self.__image__

    @property
    def depth(self) -> np.ndarray:
        """
        Getter function for depth array

        Returns:
            np.ndarray: depth array
        """
        return self.__depth__
