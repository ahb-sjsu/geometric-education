# Front Matter

---

## Title Page

**Geometric Education: Learning, Assessment, and the Topology of Understanding**

Andrew H. Bond
Senior Member, IEEE
Department of Computer Science
San Jose State University

Book 9 of the Geometric Series

*San Jose, 2026*

---

## Series Foreword

This is the ninth volume in the Geometric Series.

The series began with a simple observation: across domains --- ethics, law, economics, cognition, medicine, communication --- the standard methodology compresses multi-dimensional structure into scalar numbers and then wonders why the numbers behave badly. GDP does not capture economic wellbeing. IQ does not capture intelligence. BLEU does not capture translation quality. QALYs do not capture patient health. Binary verdicts do not capture legal reasoning. The pattern is universal and the diagnosis is the same: scalar reduction destroys geometric structure, and the destruction is irreversible.

*Geometric Methods in Computational Modeling* (Book 1) assembled the mathematical toolkit: Riemannian geometry, hyperbolic embeddings, persistent homology, SPD manifolds, gauge theory. *Geometric Reasoning* (Book 2) developed the parent framework --- the heuristic field formalism, geodesic deviation, the four failure modes, gauge invariance, and the Scalar Irrecoverability Theorem that unifies them. Books 3 through 8 --- *Geometric Ethics*, *Geometric Economics*, *Geometric Law*, *Geometric Cognition*, *Geometric Communication*, and *Geometric Medicine* --- extended the instantiation to morality, markets, courts, minds, language, and clinical care.

This book turns to education. The domain is, in some ways, the most consequential home for the geometric framework. Every other domain in the series concerns the evaluation of *things* --- the quality of a translation, the justice of a verdict, the appropriateness of a clinical decision. Education concerns the evaluation of *persons*. When we compress the multi-dimensional state of a learner into a grade point average, we are not merely losing information about a product or a process. We are losing information about a human being --- a student whose strengths, weaknesses, potential, and trajectory are reduced to a number that will follow them through admissions decisions, job applications, scholarship competitions, and self-concept for the rest of their lives.

The stakes of scalar reduction are higher in education than in any other domain in the series, because the scalar is attached to a person, and the person knows it.

What distinguishes this volume from the others is the ubiquity of its subject. Not everyone encounters the legal system. Not everyone needs clinical care at the level where QALY limitations matter. But nearly everyone goes to school. Nearly everyone receives grades. Nearly everyone has internalized the scalar representation of their own learning --- has thought of themselves as a "3.5 student" or a "B+ student" or a "1200 SAT scorer" --- and nearly everyone has felt, at some point, the gap between what they know and what their transcript says they know. The geometric framework makes that gap precise. It gives it a name (the Scalar Irrecoverability Theorem), a measure (the GPA Irrecoverability Theorem), and a remedy (the learner manifold). The gap is not a feeling. It is a mathematical fact, and it has mathematical consequences.

---

## Preface

### The GPA Trap

In the fall of 2024, I sat in my office at San Jose State University and read two graduate school application files. Both applicants had completed undergraduate engineering degrees. Both had submitted transcripts, test scores, recommendation letters, and personal statements. Both had GPAs of 3.5.

The first applicant had attended a well-funded suburban high school with Advanced Placement courses, arrived at college with a year of transfer credit, studied in a quiet apartment paid for by parents, and optimized every course selection for GPA maintenance. The transcript was clean: a steady progression of A-minuses with strategic withdrawals from any course that threatened the average. The recommendations praised the student's consistency and reliability.

The second applicant had attended an under-resourced urban school with no AP courses, arrived at college with a placement test that put them in remedial mathematics, worked twenty hours a week at an auto repair shop, and discovered a passion for engineering through a professor who recognized that the student's mechanical intuition --- the ability to diagnose engine problems by sound, to estimate tolerances by feel, to build solutions from available parts --- was precisely the kind of understanding that engineering education claims to develop. The transcript was uneven: C-pluses in early formal mathematics courses, then a sharp upward trajectory as the student built formal knowledge on top of procedural expertise. The recommendations described a student who understood engineering in a way that transcripts could not capture.

The GPAs were identical. The learner states were orthogonal.

I knew this. Every faculty member who reads applications knows this. The graduate admissions committee discusses it every year: "The GPA doesn't tell the whole story." But we use the GPA anyway, because we do not have a better number, and the admissions process requires numbers. We acknowledge that the GPA is a lossy compression of a multi-dimensional reality, and then we use the lossy compression to make life-changing decisions about the people whose reality has been compressed.

This contradiction has bothered me for years. It bothered me as a teacher assigning grades that I knew misrepresented student understanding. It bothered me as a researcher developing evaluation metrics that compressed quality into scalars. It bothered me as a faculty member on committees that used scalar rankings to sort human beings into categories of deserving and undeserving.

The geometric framework I had developed across the series --- the Scalar Irrecoverability Theorem, the heuristic field formalism, the gauge invariance principle, the Bond Index --- gave me the mathematical vocabulary to say precisely what was wrong. A GPA is a contraction of a multi-dimensional learner tensor to a scalar. The contraction is lossy. The loss is irrecoverable. The contraction-optimal learning path diverges from the actual learning geodesic. And the divergence is not random noise --- it is systematic bias against students whose strengths are concentrated on dimensions that the grading system does not measure.

This is not a metaphor. It is the GPA Irrecoverability Theorem, proved in Chapter 5. It is the Assessment Gauge Invariance Theorem, proved in Chapter 9. It is the Standardized Testing Gauge Violation Theorem, proved in Chapter 14. And it is the Educational Bond Index, defined in Chapter 13 and computed from data that every university already collects.

This book is the account of those theorems and the framework that produces them. The central claim is stark: education has geometric structure, and scalar assessment destroys it. The structure is not metaphorical. It is the literal geometry of the space in which learning takes place --- a six-dimensional learner manifold whose coordinates include domain knowledge, procedural skill, metacognitive awareness, motivation, transfer ability, and creativity. Learning is geodesic traversal on this manifold. Teaching is heuristic field guidance. Assessment is forced contraction. And the gap between what a student knows and what their transcript says they know is the Scalar Irrecoverability Theorem made flesh.

### Who This Book Is For

This book is written for three audiences, and it asks something different of each.

For **educators, curriculum designers, and assessment professionals**, the book offers a geometric alternative to scalar evaluation. If you have ever assigned a grade that you knew misrepresented a student's understanding --- if you have ever felt the gap between what you saw in the classroom and what you wrote on the report card --- the geometric framework explains *why* that gap exists and provides mathematical tools for measuring it. The mathematics is self-contained (Appendix A covers the prerequisites), but the reader who has encountered rubric design, learning objectives, and item response theory will find the terrain more familiar.

For **educational researchers and psychometricians**, the book offers a unifying framework for phenomena that have been studied in isolation: the unreliability of grades, the gauge variance of standardized tests, the difficulty of transfer learning, the persistence of achievement gaps despite intervention, and the moral distress of teaching. These are not separate problems. They are manifestations of a single geometric fact --- the irrecoverability of scalar contraction --- and the framework provides the common language to study them as such.

For **mathematicians, physicists, and computer scientists** curious about applications of differential geometry, gauge theory, and algebraic topology to the human sciences, the book provides a worked example of what it means to take the geometric metaphor seriously --- not as a vague analogy between "learning space" and actual manifolds, but as a literal claim about the mathematical structure of understanding, supported by formalism and falsifiable prediction.

The book assumes basic linear algebra and probability. It does not assume differential geometry, topology, or gauge theory --- these are developed from first principles in Chapter 4 and Appendix A. It does assume intellectual seriousness: the reader should be prepared to follow a mathematical argument across three pages and an educational argument across three centuries.

### A Note on Scope

This book does not solve education. It does not produce a grading algorithm, a test replacement, or an admissions formula. What it does is establish that education --- from kindergarten to graduate school --- has mathematical structure that current assessment methods ignore, and it builds the tools to analyze that structure. The results are formal: the GPA Irrecoverability Theorem, the Assessment Gauge Invariance condition, the Transfer Holonomy measure, the Educational Bond Index. These are mathematical objects with definitions, proofs, and falsifiable predictions. They are not slogans.

The book also does not pretend that geometry is the final word. Chapter 18 is honest about what the framework cannot yet explain, and the open questions listed there are genuine --- they are problems I do not know how to solve. The frontier is real, and acknowledging it is more useful than pretending it does not exist.

### A Note on Alex

A single thread runs through every chapter of this book: the educational trajectory of Alex Rivera, a first-generation college student from a working-class family in East San Jose. Alex is a composite --- drawn from students I have known, taught, and failed to serve adequately over two decades of university teaching. Alex's trajectory through the educational system illustrates, chapter by chapter, what the geometric framework reveals: that the gap between what Alex knows and what Alex's transcript shows is not a personal failing but a structural feature of a system designed to produce scalars from tensors. Alex's story is not a case study. It is the theorem, embodied.

---

## Acknowledgments

A book that attempts to geometrize all of education is necessarily an act of intellectual overreach, and the debts incurred in the attempt are correspondingly large.

The geometric framework that underpins this book was developed across the Geometric Series, and I am grateful to the colleagues and collaborators who shaped each volume. The heuristic field formalism, the Scalar Irrecoverability Theorem, and the gauge invariance framework originate in *Geometric Reasoning*; the Bond Index originates in *Geometric Ethics*; the moral injury analysis originates in *Geometric Medicine*; the parallel transport model of transfer originates in *Geometric Communication*; and the cognitive manifold construction originates in *Geometric Cognition*. This book inherits from all of them.

The educational content of the book draws on twenty years of teaching at San Jose State University --- a public university that serves precisely the student population whose geometric structure the book describes. The students of SJSU, many of them first-generation, many of them navigating the educational manifold without the inherited heuristic field that this book formalizes, are the reason the book exists. They deserve assessment systems that see them as they are, not as their GPAs say they are.

I am particularly grateful to colleagues in the School of Education at SJSU, who patiently explained Bloom's taxonomy, Vygotsky's ZPD, Shulman's pedagogical content knowledge, and Freire's critical pedagogy to a computer scientist who insisted on translating everything into differential geometry. Any mathematical violence done to their ideas is mine, not theirs.

The psychometric literature on assessment validity, reliability, and fairness --- from Cronbach and Meehl through Messick to Kane --- provided essential grounding for the gauge invariance framework of Chapter 9. I am grateful to the measurement community for building the empirical foundations on which the geometric reinterpretation rests.

Institutional support came from the Department of Computer Science at San Jose State University, the College of Science, and the SJSU Research Foundation. The LMS data analysis described in Chapter 16 was conducted under IRB protocol #2025-034 with de-identified Canvas interaction data from consenting participants.

The series editors and early readers of the manuscript --- including colleagues at the IEEE Computational Intelligence Society, workshop participants at NeurIPS 2025 and AERA 2026, and anonymous reviewers of the component papers --- improved the book immeasurably through their criticism. The errors that remain are proof that I did not always listen.

Finally, and most directly: to every student who has ever received a grade they knew was wrong --- a number that said less than they learned, measured less than they understood, and valued less than they were. This book is for you. The grade was not your fault. It was a theorem.

Andrew H. Bond
San Jose, California
March 2026
