# Chapter 7: Curriculum as Pathfinding

*Part II: The Framework*

---

> *"A curriculum is a planned route through the territory of knowledge. The question is whether the planner has ever seen the territory."*
> --- Anonymous educator

> **THE PATH**
>
> *A curriculum is not a list of topics. It is a route on the learner manifold, with prerequisites as boundary conditions, course sequences as waypoints, and the degree as the goal region. This chapter formalizes curriculum design as pathfinding on the learner manifold --- specifically, as A* search through the knowledge space --- and derives the conditions under which a curriculum is optimal, near-optimal, or structurally deficient.*

---

## 7.1 The Curriculum as Path

**Definition 7.1 (Curriculum).** *A curriculum is a planned path $\gamma_C: [0, T] \to \mathcal{L}$ through the learner manifold, specified by a sequence of waypoints (courses) $\{c_1, c_2, \ldots, c_n\}$ and transitions (learning steps) between them. The start state is the incoming student's estimated position $\mathbf{x}_0$. The goal region is the set of learner states $G$ that satisfy the degree requirements.*

Each course $c_k$ is a segment of the path that moves the student from an estimated pre-state $\mathbf{x}_{k-1}$ to an estimated post-state $\mathbf{x}_k$. The movement is along specific dimensions: a calculus course moves the student primarily along $d_1$ (mathematical knowledge) and $d_2$ (computational skill); a design studio moves the student primarily along $d_2$ (procedural skill) and $d_6$ (creativity); a capstone project moves the student along $d_5$ (transfer) and $d_6$ (creativity) by requiring the integration of knowledge from multiple courses.

The curriculum path is not the same as the student's actual trajectory. The curriculum specifies the planned path. The student's actual trajectory depends on the student's starting position (which may differ from the assumed $\mathbf{x}_0$), the student's metric (which differs from the assumed uniform metric), and the quality of the teaching heuristic (which varies by instructor). The deviation between the curriculum path and the actual trajectory is the learning deviation --- the educational analogue of geodesic deviation from *Geometric Reasoning* (Ch. 4).

## 7.2 A* Through the Knowledge Space

Optimal curriculum design is pathfinding on the learner manifold. The mathematical framework is A* search, with the following components:

**Start state:** The incoming student's position $\mathbf{x}_0$ on the learner manifold. In practice, this is estimated from placement tests ($d_1$ only), prior transcripts ($d_1$ primarily), and self-reports (unreliable). The quality of the start-state estimate determines the quality of the pathfinding: if $\mathbf{x}_0$ is estimated poorly, the planned path begins from the wrong point on the manifold.

**Goal region:** The set of learner states $G$ that satisfy the degree requirements. $G$ is defined by minimum thresholds on certain dimensions: "Students must demonstrate competence in linear algebra" translates to $d_1(\text{linear algebra}) \geq \theta_1$. The goal region is large: many different combinations of courses satisfy the requirements, and the specific point reached in $G$ depends on the path taken.

**Edges:** Each course is an edge (or a sequence of edges) on the manifold. The edge from $\mathbf{x}_{k-1}$ to $\mathbf{x}_k$ has a cost $w(c_k)$ representing the educational cost of the course: time, effort, tuition, and the opportunity cost of not taking a different course. The cost depends on the student's position: a course is cheap if the student's current state is well-prepared for it (low curvature in the transition region) and expensive if the student is poorly prepared (high curvature).

**Heuristic:** The curriculum designer's estimate of the remaining cost from any intermediate state to the goal region. An experienced curriculum designer has a well-calibrated heuristic: "After completing the core sequence, most students need three more semesters to finish" is a heuristic estimate.

**Constraints:** Prerequisites are hard constraints: the edge from pre-calculus to Calculus II does not exist (the manifold is disconnected between these states --- the student cannot traverse the content without the intermediate states provided by Calculus I). Co-requisites are soft constraints: the edge from Physics to Physics Lab has lower cost if traversed simultaneously.

### 7.2.1 The Optimal Curriculum

**Theorem 7.1 (Optimal Curriculum).** *If the curriculum designer's heuristic is admissible (never overestimates remaining cost), A* search on the learner manifold produces the minimum-cost curriculum --- the path from $\mathbf{x}_0$ to $G$ that minimizes total educational cost.*

The optimal curriculum is the geodesic through the knowledge space, constrained by prerequisite boundaries. It is not necessarily the shortest path in terms of course count or time-to-degree; it is the path of minimum total educational cost, which includes the effort cost of each transition, weighted by the student's position-dependent metric.

For Alex, the optimal curriculum is different from the standard curriculum because Alex's metric is different from the assumed metric. The standard curriculum assumes a student with high $d_1$ and moderate $d_2$ (the profile of a well-prepared traditional student). Alex has the reverse profile. The optimal path for Alex passes through applied courses first (leveraging high $d_2$) and builds formal knowledge as needed (developing $d_1$ on top of $d_2$). The standard path goes the other way: formal courses first, applications later. For a student with Alex's metric, the standard path has higher total cost than the optimal path.

## 7.3 Prerequisites as Manifold Boundaries

**Proposition 7.2 (Prerequisite Necessity).** *A prerequisite is a claim about the manifold's connectivity: the region of the learner manifold accessible from "post-$c_j$" is connected to the content of $c_k$, but the region accessible from "pre-$c_j$" is not. The student who skips $c_j$ enters a region where the local metric is degenerate --- the tangent vectors needed to move in the content direction do not exist.*

This is not a mere inconvenience. It is a topological fact about the knowledge manifold. A student who enrolls in Calculus II without Calculus I is not facing a "challenge" or a "stretch" --- they are in a region of the manifold where the necessary directions of motion do not exist. The student cannot learn the material because the prerequisite structure of the domain creates manifold boundaries that cannot be crossed by effort alone.

The distinction between genuine prerequisites and institutional prerequisites is important:

**Genuine prerequisites** reflect the logical and conceptual structure of the domain. You cannot understand integration without limits because the definition uses limits. You cannot understand quantum mechanics without linear algebra because the formalism is expressed in linear algebra. These prerequisites are manifold boundaries: they reflect the actual connectivity of the knowledge space.

**Institutional prerequisites** reflect administrative decisions that may or may not correspond to genuine manifold boundaries. "Must complete English 101 before taking any course numbered above 200" may be a genuine prerequisite (writing skills are needed for 200-level courses) or an administrative convenience (the department wants to ensure enrollment in English 101). The geometric framework provides a diagnostic: if removing the prerequisite has no effect on student success in the subsequent course (controlling for other variables), the prerequisite is institutional rather than genuine.

## 7.4 Degree Requirements as Goal Regions

**Definition 7.2 (Degree Goal Region).** *The goal region for a degree is the set $G = \{\mathbf{x} \in \mathcal{L} : R(\mathbf{x}) \geq \theta_R\}$, where $R$ is the degree requirement function and $\theta_R$ is the threshold. The goal region is typically defined by: (1) a set of required courses (mandatory waypoints on the path), (2) a set of distribution requirements (minimum credits in specified domain areas), (3) a minimum GPA threshold, and (4) a total credit threshold.*

The goal region is large. Two students who satisfy the same degree requirements may occupy very different points in $G$: different electives, different depth-breadth trade-offs, different profiles of strengths and weaknesses. A student who takes all their electives in philosophy occupies a different point from a student who takes all their electives in statistics, even though both satisfy the requirements for a biology degree.

The GPA threshold within the goal region is a scalar boundary: it excludes learner states that satisfy all other requirements but have a GPA below the threshold. The geometric framework reveals this as a scalar filter applied to a multi-dimensional region: the filter removes states with low projection onto the GPA direction, regardless of their value on other dimensions. A student who satisfies all content requirements but has a 1.9 GPA is excluded from the goal region, even if their actual learner state (high $d_2$, $d_3$, $d_5$, $d_6$; low $d_1$ on exam-tested recall) is educationally valuable.

## 7.5 The Elective as Geodesic Freedom

Required courses constrain the path: they specify mandatory waypoints that the curriculum must pass through. Electives provide geodesic freedom: the student can explore regions of the manifold that the curriculum designer did not prescribe.

**Proposition 7.3 (Elective-Rich Curricula and Transfer).** *Curricula with more elective freedom produce learner states with higher $d_5$ (transfer) and $d_6$ (creativity) on average, because the student traverses more of the manifold and encounters more cross-domain connections. Curricula with less elective freedom produce states with higher $d_1$ (domain depth) at the cost of $d_5$ and $d_6$.*

This is the depth-breadth trade-off, geometrized. A narrow, deep curriculum is a path that stays in one region of the manifold and explores it thoroughly. A broad, shallow curriculum is a path that covers more of the manifold but explores each region less deeply. The optimal trade-off depends on the educational objective: a professional degree (medicine, law, engineering) requires depth in a specific domain; a liberal arts degree prioritizes breadth and transfer.

The geometric framework quantifies the trade-off. If the educational objective weights $d_5$ and $d_6$ highly (as liberal education does), the optimal curriculum has more elective freedom. If the objective weights $d_1$ and $d_2$ highly (as professional training does), the optimal curriculum has more required courses. The standard one-size-fits-all curriculum --- moderate requirements, moderate electives --- is a compromise that is optimal for no student and adequate for most.

## 7.6 The Hidden Curriculum as Implicit Metric

The "hidden curriculum" --- the unwritten norms, expectations, and cultural knowledge required for academic success --- is an implicit metric on the learner manifold. Students who arrive with the hidden curriculum already internalized (continuing-generation students, students from academic cultures) experience a different effective metric than those who must learn it on the fly.

Examples of hidden curriculum as metric values:

- **"Go to office hours"** reduces the cost of help-seeking from high (for students who do not know office hours exist or how they function) to low (for students who treat office hours as a normal part of academic life).
- **"Start the paper early"** reduces the cost of long writing assignments from high (for students who procrastinate until the night before) to moderate (for students who begin early and revise).
- **"Choose courses strategically"** reduces the cost of curriculum navigation from high (for students who select courses randomly or based on schedule convenience) to low (for students who optimize for learning, interest, and GPA).

These hidden curriculum elements are not on the official pathfinding map, but they affect the cost of every edge. A student who does not know about office hours pays a higher cost for every course that involves difficult material, because the student does not access the help that would reduce the curvature. A student who does not know about strategic course selection takes a higher-cost path through the curriculum, because each course selection is made without heuristic guidance.

The hidden curriculum is the intergenerationally transmitted heuristic field ($h_P$) discussed in Chapter 6. Its absence for first-generation students is measurable as excess path cost: more credits to degree, more course changes, more late withdrawals, more time spent on non-geodesic paths.

## 7.7 Local Minima and Prerequisite Traps

The learner manifold has local minima --- states from which the student cannot progress without external intervention.

**Definition 7.3 (Educational Local Minimum).** *A learner state $\mathbf{x}$ is a local minimum if the geodesic cost to the goal region from $\mathbf{x}$ is greater than the geodesic cost from some nearby state $\mathbf{y}$, but the cost of transitioning from $\mathbf{x}$ to $\mathbf{y}$ exceeds the student's available resources (time, effort, motivation).*

Examples:

- **The prerequisite trap.** A student who has taken a course sequence in the wrong order may arrive at a state from which the intended next course is inaccessible (the prerequisite is not met) and the prerequisite course is not offered until the next year. The student is stuck: they cannot move forward (prerequisite boundary) and the cost of waiting (a year of delay) is high.

- **The remediation loop.** A student placed into remedial courses may spend semesters in remediation, consuming financial aid and motivation, without ever reaching the credit-bearing courses that count toward the degree. Each remedial course moves the student slightly along $d_1$ (formal skills) but consumes resources that would otherwise support progress along $d_4$ (motivation) and the temporal dimension (time to degree). The remediation loop is a local minimum: the student is making progress on $d_1$ but the total cost of the path is increasing faster than the distance to the goal is decreasing.

- **The GPA trap (recursive).** A student whose GPA has fallen below the threshold for the goal region (e.g., minimum 2.0 for graduation) must raise the GPA to re-enter the goal region. But the GPA is a cumulative average: a low GPA accumulated over many semesters is resistant to improvement, because each new semester contributes only a small fraction of the total. The student must earn many credits at high grades to raise the average, and the courses that would raise the average most (easy courses with high expected grades) may not contribute to the degree requirements. The student is trapped between two gradients: the GPA gradient (take easy courses) and the degree gradient (take required courses). The optimal path for the degree is not the optimal path for the GPA. The student, rationally, follows the GPA gradient and delays the degree.

## 7.8 Alex and the Advisor

Alex's academic advisor uses a default curriculum plan: the same path for every engineering student, designed for the median student profile ($d_1 \approx 0.65$, $d_2 \approx 0.55$, uniform on other dimensions). The plan sequences courses in the traditional order: calculus, physics, differential equations, circuits, statics, dynamics, design.

Alex's actual position on the manifold ($d_1 \approx 0.45$, $d_2 \approx 0.85$) would benefit from a different path: an applied mathematics course that builds formal skills through engineering applications, a hands-on lab course early in the sequence (leveraging high $d_2$), and the theoretical courses later (building $d_1$ on top of the experiential foundation). This path is a different geodesic to the same goal region, with lower total cost given Alex's actual manifold position.

The advisor does not know this because the advising tool shows GPA (a scalar) and transcript (a list of courses taken, which records the path but not the learner state at each point). The advising tool does not show the learner tensor, the student's metric, or the position on the manifold. The advisor sees a 3.5 GPA and assumes a student near the median profile. The advisor assigns the default path.

Alex follows the default path and hits a wall in Differential Equations. The course is taught formally-first: definitions, theorems, solution techniques, then (briefly) applications. Alex's weak $d_1$ on formal notation makes the early weeks nearly impenetrable. Alex's strong $d_2$ on applied mathematics is unused until the final two weeks of the semester, when applications are covered. By then, Alex's $d_4$ (motivation) has declined significantly: weeks of struggling with formalism have eroded the persistence that Alex carried into college.

Professor Vasquez intervenes. Vasquez recognizes Alex's manifold position (high $d_2$, low formal $d_1$, high $d_5$) and reroutes Alex through an applied mathematics sequence: a different path to the same content, passing through applications first and building the formalism as needed. The total cost of this path, given Alex's metric, is substantially lower than the default path.

The rerouting costs Alex a semester: Alex withdraws from the standard Differential Equations course and takes the applied sequence starting the following semester. The withdrawal appears on the transcript. It lowers Alex's completion rate metric. It is, in the scalar accounting, a failure. On the manifold, it is a correction: a rerouting from a non-geodesic path to a path that is closer to Alex's actual geodesic.

---

## Summary

This chapter has formalized curriculum design as A* pathfinding on the learner manifold. The optimal curriculum is the minimum-cost path from the student's starting position to the degree goal region, constrained by prerequisite boundaries and guided by the curriculum designer's heuristic. Prerequisites are claims about the manifold's connectivity that can be genuine (reflecting the logical structure of knowledge) or institutional (reflecting administrative decisions). Degree requirements define a goal region that is large and multi-dimensional, but the GPA threshold within the goal region is a scalar filter that excludes educationally valuable states. Electives provide geodesic freedom that increases transfer and creativity. The hidden curriculum is an implicit metric that disadvantages students who must learn it on the fly. Educational local minima --- prerequisite traps, remediation loops, and GPA traps --- are states from which progress requires external intervention. The one-size-fits-all curriculum is a default path designed for a median student that is optimal for no one.

---

[^1]: The A* algorithm was introduced by Hart, Nilsson, and Raphael (1968) and is the basis for the pathfinding formalism in *Geometric Reasoning* (Bond, 2026c, Ch. 3). Its application to curriculum design is novel to this book.
