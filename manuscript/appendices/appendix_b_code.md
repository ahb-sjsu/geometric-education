# Appendix B: The Learner Manifold --- Code Walkthrough

---

This appendix provides Python implementations of the core computational objects in the geometric framework. All code is designed for reproducibility and requires only NumPy, SciPy, and scikit-learn.

## B.1 Learner State Representation

```python
import numpy as np
from dataclasses import dataclass

@dataclass
class LearnerState:
    """A point on the 6-dimensional learner manifold."""
    d1_domain_knowledge: float    # [0, 1]
    d2_procedural_skill: float    # [0, 1]
    d3_metacognition: float       # [0, 1]
    d4_motivation: float          # [0, 1]
    d5_transfer: float            # [0, 1]
    d6_creativity: float          # [0, 1]

    def to_vector(self) -> np.ndarray:
        return np.array([
            self.d1_domain_knowledge,
            self.d2_procedural_skill,
            self.d3_metacognition,
            self.d4_motivation,
            self.d5_transfer,
            self.d6_creativity
        ])

# Alex and Ethan from Chapter 1
alex = LearnerState(0.45, 0.85, 0.70, 0.80, 0.75, 0.65)
ethan = LearnerState(0.80, 0.50, 0.40, 0.55, 0.40, 0.35)
```

## B.2 GPA Contraction and Irrecoverability Demonstration

```python
def gpa_contraction(state: LearnerState,
                    weights: np.ndarray = None) -> float:
    """Contract a 6D learner state to a scalar GPA.

    Default weights reflect typical exam-dominated assessment:
    heavy on d1, moderate on d2, negligible on d3-d6.
    """
    if weights is None:
        weights = np.array([0.60, 0.25, 0.05, 0.05, 0.03, 0.02])
    return float(weights @ state.to_vector())

def demonstrate_irrecoverability(n_samples: int = 10000,
                                 target_gpa: float = 0.60,
                                 tolerance: float = 0.01):
    """Generate random learner states that produce the same GPA.

    Returns states in the level set G^{-1}(target_gpa +/- tolerance).
    """
    weights = np.array([0.60, 0.25, 0.05, 0.05, 0.03, 0.02])
    states = np.random.uniform(0, 1, size=(n_samples, 6))
    gpas = states @ weights
    mask = np.abs(gpas - target_gpa) < tolerance
    level_set = states[mask]
    return level_set  # Many distinct states, same GPA
```

## B.3 Metric Estimation from Learning Curves

```python
from scipy.optimize import curve_fit

def power_law(practice, a, b, c):
    """Power law learning curve: performance = c - a * practice^(-b)."""
    return c - a * np.power(practice + 1, -b)

def estimate_local_curvature(practice_data: np.ndarray,
                              performance_data: np.ndarray) -> float:
    """Estimate local curvature from learning curve shape.

    Higher curvature = steeper initial curve = harder transition.
    """
    popt, _ = curve_fit(power_law, practice_data, performance_data,
                        p0=[0.5, 0.5, 1.0], maxfev=5000)
    a, b, c = popt
    # Curvature proxy: the exponent b (higher = steeper = harder)
    return b
```

## B.4 Educational Bond Index Computation

```python
def compute_bond_index(actual_paths: np.ndarray,
                       geodesic_paths: np.ndarray,
                       sigma_inv: np.ndarray) -> float:
    """Compute the Educational Bond Index.

    Parameters
    ----------
    actual_paths : array of shape (n_students, n_timesteps, 6)
        Observed learning trajectories.
    geodesic_paths : array of shape (n_students, n_timesteps, 6)
        Computed optimal trajectories.
    sigma_inv : array of shape (6, 6)
        Inverse covariance matrix (precision matrix).

    Returns
    -------
    float
        Expected learning deviation (Bond Index).
    """
    n_students, n_steps, d = actual_paths.shape
    total_deviation = 0.0
    for s in range(n_students):
        path_deviation = 0.0
        for t in range(n_steps):
            diff = actual_paths[s, t] - geodesic_paths[s, t]
            # Mahalanobis distance at each timestep
            path_deviation += np.sqrt(diff @ sigma_inv @ diff)
        total_deviation += path_deviation / n_steps
    return total_deviation / n_students
```

## B.5 Gauge Violation Tensor Calculation

```python
def compute_gauge_violation_tensor(
    scores_original: np.ndarray,
    scores_transformed: np.ndarray,
    transformation_labels: list
) -> dict:
    """Compute gauge violation tensor V_ij.

    Parameters
    ----------
    scores_original : array of shape (n_students, n_score_dims)
    scores_transformed : array of shape (n_transforms, n_students, n_score_dims)
    transformation_labels : list of transformation names

    Returns
    -------
    dict mapping transformation name to mean score change vector
    """
    V = {}
    for i, label in enumerate(transformation_labels):
        diff = scores_transformed[i] - scores_original
        V[label] = np.mean(diff, axis=0)  # Mean change per score dimension
    return V
```

## B.6 Trajectory Clustering for Profile Identification

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster_learner_trajectories(
    trajectory_features: np.ndarray,
    n_clusters: int = 4
) -> tuple:
    """Cluster students by trajectory features to identify learner profiles.

    Parameters
    ----------
    trajectory_features : array of shape (n_students, n_features)
        Features extracted from LMS interaction data.
    n_clusters : int
        Number of learner profiles to identify.

    Returns
    -------
    labels : array of cluster assignments
    centers : array of cluster centers (profile prototypes)
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(trajectory_features)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    centers = scaler.inverse_transform(kmeans.cluster_centers_)
    return labels, centers
```

---

*All code is available in the companion repository. For full documentation and extended examples, see the project website.*
