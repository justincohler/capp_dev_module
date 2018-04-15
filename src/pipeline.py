"""
Pipeline is a generic ML pipeline containing basic functions for cleaning and processing a model.

Current Implementations:
    - K-Nearest-Neighbors

@author: Justin Cohler
"""
from abc import ABC, abstractmethod
import pandas as pd
import numpy as np

class Pipeline(ABC):
    """
    Pipeline is a generic ML pipeline containing basic functions for cleaning, processing, and evaluating a model.

    Current Implementations:
        - K-Nearest-Neighbors
    """

    def ingest(self, source):
        """Return a pandas dataframe of the data from a given source string."""
        return pd.read_csv(source)

    @abstractmethod
    def preprocess(self, data):
        """
        Return an updated df, filling missing values for all fields.

        (Uses mean to fill in missing values)
        """
        raise NotImplementedError
