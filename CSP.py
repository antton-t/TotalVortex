import copy as cp
import numpy as np
from sklearn.base import TransformerMixin, BaseEstimator
from scipy import linalg

# https://github.com/mne-tools/mne-python/blob/maint/1.4/mne/decoding/csp.py#L21-L621


class CSP(TransformerMixin, BaseEstimator):
    def __init__(
            self,
            n_components=4,
        ):
            if not isinstance(n_components, int):
                raise ValueError('n_components must be an integer.')
        
            self.n_components =  n_components
    
    def _compute_covariance_matrices(self, X, y):
        _, n_channels, _ = X.shape

        covs = []
        for cur_class in self.classes_:
            # Concatenate epochs before computing the covariance.
            x_class = X[y == cur_class]
            x_class = np.transpose(x_class, [1, 0, 2])
            x_class = x_class.reshape(n_channels, -1)
            cov_mat = np.cov(x_class)
            covs.append(cov_mat)

        return np.stack(covs)

    def fit(self, X, y):
        """Estimate the CSP decomposition on epochs."""

        self.classes_ = np.unique(y)

        # Compute the covariance matrices for each class
        covs = self._compute_covariance_matrices(X, y)

        # Perform eigenvalue decomposition on the average covariance matrix
        eigen_values, eigen_vectors = linalg.eigh(covs[0], covs.sum(0))

        # Sort the eigenvalues in descending order
        ix = np.argsort(np.abs(eigen_values - 0.5))[::-1]
        eigen_vectors = eigen_vectors[:, ix]

        # Store the CSP filters
        self.filters_ = eigen_vectors.T
        pick_filters = self.filters_[:self.n_components]

        # Apply CSP filtering to the input epochs
        X = np.asarray([np.dot(pick_filters, epoch) for epoch in X])

        # Logarithm of the variance of CSP-filtered signals
        X = np.log(np.mean(X ** 2, axis=2))

        return self

    def transform(self, X):
        pick_filters = self.filters_[:self.n_components]

        # Apply CSP filtering to the input epochs
        X = np.asarray([np.dot(pick_filters, epoch) for epoch in X])

        # Logarithm of the variance of CSP-filtered signals
        X = np.log(np.mean(X ** 2, axis=2))

        # Zero-mean and unit variance normalization
        X -= np.mean(X)
        X /= np.std(X)

        return X

    def fit_transform(self, X, y):
        # Fit CSP on the training data and apply CSP filtering
        self.fit(X, y)
        return self.transform(X)