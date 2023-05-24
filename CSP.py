import copy as cp
import numpy as np
from sklearn.base import TransformerMixin, BaseEstimator
from scipy import linalg


class CSP(TransformerMixin, BaseEstimator):

    def __init__(
        self,
        n_components=4,
    ):

        # Init default CSP
        if not isinstance(n_components, int):
            raise ValueError("n_components must be an integer.")
        self.n_components = n_components

    def _check_Xy(self, X, y=None):

        if not isinstance(X, np.ndarray):
            raise ValueError("X should be of type ndarray (got %s)." % type(X))
        if y is not None:
            if len(X) != len(y) or len(y) < 1:
                raise ValueError("X and y must have the same length.")
        if X.ndim < 3:
            raise ValueError("X must have at least 3 dimensions.")

    def fit(self, X, y):

        self._check_Xy(X, y)

        self._classes = np.unique(y)
        n_classes = len(self._classes)
        if n_classes < 2:
            raise ValueError("n_classes must be >= 2.")
        if n_classes > 2 and self.component_order == "alternate":
            raise ValueError(
                "component_order='alternate' requires two "
                "classes, but data contains {} classes; use "
                "component_order='mutual_info' "
                "instead.".format(n_classes)
            )