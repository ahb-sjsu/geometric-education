# Chapter 16: Measuring the Learner Manifold from LMS Data

*Part V: Horizons*

---

> *"The theory is beautiful. Can we measure it?"*

> **THE EMPIRICS**
>
> *The framework's central empirical challenge: estimating the learner metric from observable data. Every student interaction with a Learning Management System generates trajectory data --- timestamps, click patterns, assignment submissions, quiz attempts, discussion forum posts. These are observations of the student's path on the learner manifold. This chapter proposes methods for inferring the manifold's metric from these observed trajectories and specifies six falsifiable predictions that would validate or refute the framework.*

---

## 16.1 Learning Management Systems as Trajectory Observers

Every student interaction with Canvas, Blackboard, Moodle, or any LMS generates a data record: a timestamp, an action type, a resource identifier, and (for submissions) a score. Over a semester, a single student generates thousands of data points --- a high-frequency trajectory through the digital learning environment.

The trajectory is a projection of the student's path on the learner manifold. It does not observe the manifold directly (it does not measure $d_1$ through $d_6$ at each point), but it observes consequences of the manifold position: which resources the student accesses (correlated with which dimensions the student is developing), how long the student spends on each resource (correlated with the local curvature --- high curvature means more time), which problems the student solves and which they skip (correlated with which regions of the manifold are accessible), and how the student's performance changes over time (correlated with the trajectory direction and velocity).

The empirical question is: can we infer the manifold's metric from these observed projections?

## 16.2 Proposed Methods

### 16.2.1 Trajectory Clustering

**Method.** Cluster students by their LMS interaction patterns using time-series similarity metrics (dynamic time warping, edit distance on activity sequences, or embedding-based similarity). Students who follow similar paths through the LMS are in similar regions of the manifold. The between-cluster distances estimate the manifold metric.

**What it measures.** Trajectory clustering identifies learner profiles: groups of students who navigate the learning environment similarly. These profiles correspond to different manifold positions. The number of distinct clusters estimates the effective dimensionality of the learner manifold in the observed data. The distances between clusters estimate the metric.

**Limitations.** Trajectory clustering captures the dimensions of the learner manifold that project onto LMS behavior. It is blind to dimensions that do not affect LMS interaction: $d_4$ (motivation) may not differ between students who interact similarly with the LMS but differ in their intrinsic versus extrinsic motivation. The clustering is a lower-dimensional projection of the manifold structure.

### 16.2.2 Multi-Dimensional Item Response Theory (MIRT)

**Method.** Fit a multi-dimensional IRT model to student response data (quiz scores, homework grades, exam results). MIRT estimates a vector $\boldsymbol{\theta} \in \mathbb{R}^k$ for each student, where $k$ is the number of latent dimensions.

**What it measures.** MIRT estimates are coordinates on the learner manifold. The estimated dimensions correspond to latent trait dimensions that underlie the observed response patterns. If the items span multiple dimensions of the learner manifold (some items measure $d_1$, others measure $d_2$, others measure $d_5$), the MIRT estimate is a multi-dimensional position estimate.

**Connection to the framework.** MIRT is already a manifold coordinate estimator --- the geometric framework provides the interpretation. The estimated $\boldsymbol{\theta}$ is a point on the learner manifold. The IRT item parameters define the coordinate system. The item information function (how much each item tells us about the student's position) is related to the metric: items with high information in a given region provide precise position estimates, corresponding to low uncertainty in the metric estimate.

### 16.2.3 Learning Curve Analysis

**Method.** Fit learning curves (performance vs. practice) to student data for each topic or skill. The shape of the learning curve contains information about local curvature.

**What it measures.** Steep learning curves indicate high curvature: the student's performance changes rapidly with practice, suggesting that the local metric is steep and the transition is costly but achievable. Flat learning curves indicate either low curvature (the student has already learned the material and additional practice produces diminishing returns) or a plateau (the student is at a local minimum from which further progress requires a different approach).

**Curvature estimation.** The second derivative of the learning curve is related to the local curvature of the manifold. Comparing learning curves across students estimates metric variation: if Student A has a steeper learning curve on Topic X than Student B, the metric is higher for Student A at that point on the manifold (the transition is more costly).

### 16.2.4 Knowledge Space Theory

**Method.** Apply Doignon and Falmagne's (1999) knowledge space theory to model the learner's knowledge state as a subset of a partially ordered set of skills. The knowledge space is a simplicial complex --- a discretized version of the learner manifold.

**What it measures.** Knowledge space theory captures the prerequisite structure of the manifold: which knowledge states are accessible from which, and in what order. The partial ordering defines the connectivity of the manifold. The surmise relation (the prerequisite structure) defines the boundary architecture.

**Connection to the framework.** Knowledge space theory is a discrete approximation of the learner manifold. The geometric framework provides the continuous generalization: the knowledge space is a simplicial complex embedded in the continuous learner manifold, and the operations of knowledge space theory (learning, forgetting, assessment) are discrete approximations of manifold operations (geodesic traversal, metric contraction, position estimation).

## 16.3 The Falsifiable Prediction Suite

The geometric framework for education generates six falsifiable predictions, each with specific experimental designs.

### 16.3.1 GPA Non-Injectivity

**Prediction.** Given LMS trajectory data, students with identical GPAs can be separated into distinct clusters with statistically different learner profiles on $d_1$ through $d_6$.

**Experimental design.** Select a cohort of students with GPAs in a narrow band (e.g., 3.4--3.6). Cluster their LMS trajectories. Test whether the clusters have statistically different learning outcomes on assessments that target different dimensions (a procedural assessment for $d_2$, a transfer assessment for $d_5$, a metacognitive assessment for $d_3$).

**Falsification criterion.** If students with identical GPAs cannot be separated into distinct clusters, or if the clusters do not differ on non-$d_1$ dimensions, the prediction fails.

### 16.3.2 Format Gauge Violation

**Prediction.** Administering the same content assessment in multiple formats to the same students produces format-dependent scores exceeding test-retest noise.

**Experimental design.** Administer a content assessment in three formats (multiple choice, free response, oral exam) to the same students, counterbalanced for order. Compute the within-student variance across formats and compare to the within-format test-retest variance.

**Falsification criterion.** If the cross-format variance does not exceed the within-format variance, the prediction fails.

### 16.3.3 Transfer Holonomy

**Prediction.** Students who have traversed cross-domain paths in the curriculum (interdisciplinary courses, cross-listed electives) show higher $d_5$ (transfer) on post-course assessments than students who traversed within-domain paths of equal length.

**Experimental design.** Compare transfer assessment scores between students who took interdisciplinary electives and students who took single-domain electives, controlling for total credits, GPA, and demographic variables.

**Falsification criterion.** If interdisciplinary curriculum does not produce higher transfer scores, the prediction fails.

### 16.3.4 First-Generation Heuristic Deficit

**Prediction.** First-generation students show higher path cost (more credits to degree, more course changes, more late withdrawals) not because of lower ability but because of missing heuristic field values.

**Experimental design.** Compare time-to-degree, credits-to-degree, and course-change frequency between first-generation and continuing-generation students, controlling for GPA, SAT score, and high school preparation. The prediction is that the path-cost difference persists after controlling for ability indicators.

**Falsification criterion.** If first-generation students do not show excess path cost after controlling for ability, the prediction fails.

### 16.3.5 Metric Inequality

**Prediction.** Students from under-resourced backgrounds show steeper learning curves (higher curvature) on early assignments, consistent with higher metric distance for the same content transitions.

**Experimental design.** Compare learning curve slopes between students from well-resourced and under-resourced backgrounds in the same course, for the same content. The prediction is that under-resourced students have steeper initial curves (higher curvature) but converge to similar performance with sufficient practice.

**Falsification criterion.** If under-resourced students do not show steeper initial learning curves, the prediction fails.

### 16.3.6 Moral Injury in Teaching

**Prediction.** Teachers who assign grades they believe to be inaccurate show measurable stress responses (survey-based) that dissociate from workload-based burnout.

**Experimental design.** Survey teachers about grading stress (moral injury items) and workload stress (burnout items). Test whether the two constructs are statistically independent after controlling for total grading load.

**Falsification criterion.** If grading stress does not dissociate from workload stress, the prediction fails.

## 16.4 Alex's Study

Alex, now a doctoral student in education, designs a study using LMS data from three semesters of introductory engineering courses. The study tests Prediction 16.3.1 (GPA non-injectivity) and Prediction 16.3.4 (first-generation heuristic deficit).

The results confirm both predictions. Students with identical GPAs cluster into four distinct profiles with significantly different trajectories and different performance on dimension-specific assessments. First-generation students show 1.4 additional semesters to degree and 2.3x the course-change frequency of continuing-generation students, after controlling for GPA and SAT score.

The GPA Irrecoverability Theorem is confirmed empirically: the scalar cannot distinguish learner states that the trajectory data reveals as geometrically distant.

---

## Summary

This chapter has proposed four methods for estimating the learner metric from LMS data: trajectory clustering, multi-dimensional IRT, learning curve analysis, and knowledge space theory. Six falsifiable predictions are specified, each with an experimental design and falsification criterion. The predictions test the framework's core claims: GPA non-injectivity, format gauge violation, transfer holonomy, first-generation heuristic deficit, metric inequality, and moral injury in teaching. The predictions are empirically testable with data that most educational institutions already collect.

---

[^1]: Doignon, J.-P., & Falmagne, J.-C. (1999). *Knowledge Spaces*. Springer.
