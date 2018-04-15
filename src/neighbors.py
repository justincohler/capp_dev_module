"""
Neighbors is a basic ML pipeline implementation using a K-Nearest-Neighbors model.

@author: Justin Cohler
"""
from capp_demo.src.pipeline import Pipeline
from abc import ABCMeta
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class Neighbors(Pipeline):
    """Implement ML pipeline using a K-Nearest-Neighbors model."""

    def __init__(self):
        """Set up k-nearest-neighbor specific globals."""
        super().__init__()

    def preprocess(self, data):
        """
        Return an updated df, filling missing values for all fields.

        (Uses mean to fill in missing values)
        """
        return data.fillna(data.mean())
