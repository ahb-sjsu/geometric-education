# Chapter 2: The Testing Industrial Complex

*Part I: The Problem*

---

> *"When a measure becomes a target, it ceases to be a good measure."*
> --- Charles Goodhart

> **THE INDUSTRY**
>
> *The standardized testing industry in the United States generates approximately $2.5 billion in annual revenue. The College Board --- a nonprofit in name, a monopoly in practice --- reported revenues exceeding $1.2 billion in 2023. The Educational Testing Service, which administers the GRE, TOEFL, and Praxis, reported over $1.5 billion. Pearson, which provides state standardized tests to dozens of states, is a publicly traded company with a market capitalization exceeding $8 billion. This is not an assessment system. It is an industry. And like every industry, it has interests that are not identical to the interests of the people it serves.*
>
> *This chapter examines the standardized testing industry through the geometric lens: each test is a projection from the learner manifold onto a low-dimensional subspace, and the projection is designed not to maximize educational insight but to maximize the properties that make a test commercially viable --- standardization, scalability, comparability, and legal defensibility. The geometric framework explains why these commercial constraints produce instruments that systematically destroy the dimensions of learning that matter most.*

---

## 2.1 The SAT as Forced Contraction

The SAT is the most consequential scalar contraction in American education. Approximately 2.2 million students take the SAT each year, and their scores --- three-digit numbers between 400 and 1600 --- serve as gatekeeping criteria for college admissions at thousands of institutions. The score follows the student through applications, scholarship decisions, and often into the first job interview. It is a number assigned at age seventeen that shapes the trajectory of a life.

The SAT's two-section structure (Evidence-Based Reading and Writing + Mathematics) is a projection from the learner manifold onto a two-dimensional subspace. The total score contracts this two-dimensional representation to a single number. The projection discards at least four of the six learner manifold dimensions described in Chapter 1.

### 2.1.1 What the SAT Measures

The SAT measures a specific combination of domain knowledge ($d_1$) and a narrow sub-dimension of procedural skill ($d_2$): the ability to recognize correct answers under time pressure in a multiple-choice format. This is a genuine cognitive capacity. It is not a trivial one. And it is not the same as understanding.

The distinction between recognition and construction is critical. A student who can identify the correct use of a semicolon when presented with four options is demonstrating recognition of a grammatical rule. A student who can deploy semicolons effectively in their own writing is demonstrating construction --- the ability to generate correct usage, not merely to recognize it. Recognition is necessary for construction but not sufficient. The SAT tests the necessary part and infers the sufficient part. The inference is unreliable.

The time pressure of the SAT introduces a further distortion. Under timed conditions, students must rely on pattern matching rather than deliberate reasoning. A student who can solve a problem in three minutes by careful analysis but not in ninety seconds by pattern recognition will perform poorly on the SAT --- not because they lack understanding but because they lack speed. Speed and understanding are distinct dimensions of the learner manifold, and the SAT's time constraint projects them onto a single axis: timed performance. The slow, careful thinker and the fast, shallow pattern-matcher may produce the same score.

### 2.1.2 What the SAT Discards

**Procedural skill beyond recognition ($d_2$).** The SAT does not ask students to build, create, design, repair, or construct. A student who can design a bridge, write a novel, code a program, repair an engine, or conduct an experiment demonstrates procedural skill that the SAT cannot see. The entire domain of "knowing how" --- as distinct from "knowing that" --- is invisible to the instrument.

**Metacognitive awareness ($d_3$).** The SAT provides no mechanism for expressing confidence, uncertainty, or self-correction. A student who knows what they do not know --- who can accurately assess their own understanding and adjust their study strategy accordingly --- has a capacity that predicts academic success far more reliably than SAT scores predict it. But the SAT cannot measure this capacity because it requires a binary response (right or wrong) with no room for calibrated uncertainty.

**Motivation and persistence ($d_4$).** The SAT is a single event: four hours on a Saturday morning. It does not measure the ability to sustain effort over weeks, to persist through difficulty, to recover from failure, or to maintain engagement with material that is initially boring. These are the capacities that predict degree completion, career success, and lifelong learning. They are invisible to the SAT.

**Transfer ability ($d_5$).** The SAT tests within-domain pattern matching: recognizing mathematical patterns in math problems, recognizing linguistic patterns in reading passages. It does not test the ability to carry knowledge across domains --- to apply mathematical reasoning to a historical question, or to bring literary analysis to bear on a scientific controversy. Transfer is the highest-value educational outcome and the one most thoroughly destroyed by the SAT's domain-segregated structure.

**Creativity ($d_6$).** The SAT has one right answer per question. There are no open-ended items, no opportunities for novel solutions, no reward for original thinking. A student who sees an unconventional but valid interpretation of a reading passage will be marked wrong. A student who devises an elegant but non-standard mathematical approach will be marked wrong if the answer does not match the key. Creativity is not merely unmeasured --- it is actively punished.

### 2.1.3 The Projection Geometry

The SAT can be modeled as a linear projection from $\mathbb{R}^6$ (the learner manifold) to $\mathbb{R}^1$ (the total score):

$$\text{SAT}(\mathbf{x}) = \mathbf{w}^T \mathbf{x} = w_1 d_1 + w_2 d_2 + w_3 d_3 + w_4 d_4 + w_5 d_5 + w_6 d_6$$

where the weight vector $\mathbf{w}$ encodes the SAT's effective sensitivity to each dimension. Based on the analysis above, the approximate weights are:

$$\mathbf{w}_{\text{SAT}} \approx (0.70, \; 0.15, \; 0.05, \; 0.05, \; 0.03, \; 0.02)$$

The SAT loads heavily on $d_1$ (domain knowledge, specifically recognition-type knowledge testable in multiple-choice format), moderately on a narrow band of $d_2$ (test-taking procedural skill), and negligibly on $d_3$ through $d_6$. The projection direction is dominated by $d_1$. The kernel of the projection --- the set of learner-state differences that are invisible to the SAT --- is a five-dimensional subspace containing most of $d_2$ through $d_6$.

The preimage of any SAT score is a five-dimensional hyperplane in the learner manifold. All learner states on this hyperplane produce the same SAT score. The number of qualitatively different learner profiles consistent with, say, a score of 1200 is immense. The SAT score does not distinguish between them.

## 2.2 Test Prep as Metric Gaming

The test preparation industry is worth approximately $10 billion annually in the United States.[^1] Companies like Kaplan, Princeton Review, and their digital successors promise SAT score improvements of 100--200 points through systematic preparation. The geometric framework explains exactly what they are doing --- and what they are not doing.

### 2.2.1 Movement Along the Fiber

Recall from Chapter 1 that the preimage of a SAT score is a five-dimensional fiber in the learner manifold. Test preparation moves the student along a direction that increases the projection value (the SAT score) without necessarily moving the student's base position on the manifold (their actual understanding).

A student who learns to eliminate obvious wrong answers (a test-taking strategy, not a content skill) moves along a direction that has high projection onto $\mathbf{w}_{\text{SAT}}$ but low magnitude on the actual dimensions of understanding. The student's SAT score increases. The student's learner state barely changes. This is motion along the fiber: the projection changes, the base point does not.

Formally, let $\Delta \mathbf{x}_{\text{prep}}$ be the change in learner state produced by test preparation. We can decompose it into components parallel and perpendicular to the projection direction:

$$\Delta \mathbf{x}_{\text{prep}} = \Delta \mathbf{x}_{\parallel} + \Delta \mathbf{x}_{\perp}$$

where $\Delta \mathbf{x}_{\parallel}$ is the component that changes the SAT score and $\Delta \mathbf{x}_{\perp}$ is the component that does not. Test preparation is designed to maximize $\|\Delta \mathbf{x}_{\parallel}\|$ relative to total effort. This means it preferentially develops the narrow skills that project onto the SAT (recognition speed, strategic elimination, format familiarity) while ignoring the broad skills that do not project onto the SAT (deep understanding, construction ability, transfer, creativity).

### 2.2.2 The Equity Dimension

The $10 billion test preparation industry is not equally accessible. A comprehensive SAT prep course from Kaplan or Princeton Review costs $1,000--$2,500. Private tutoring costs $100--$300 per hour. A student who receives 100 hours of private tutoring has invested $10,000--$30,000 in projection optimization.

The geometric framework makes the equity implication precise. Let $\Delta \text{SAT}_{\text{prep}}$ be the score improvement from test preparation. If prep is pure projection optimization (motion along the fiber with no change in base position), then:

$$\Delta \text{SAT}_{\text{prep}} = \mathbf{w}^T \Delta \mathbf{x}_{\text{prep}} \approx 100 \text{--} 200 \text{ points}$$

This improvement does not correspond to improved learning. It corresponds to improved projection. A student who gains 200 points through test prep has not learned more --- they have learned to project more favorably. The 200-point improvement is indistinguishable, on the SAT score, from a 200-point improvement earned through genuine learning.

The admissions office sees 1400. It does not know whether the 1400 reflects a learner state with $d_1 = 0.90$ (genuine high knowledge) or a learner state with $d_1 = 0.70$ plus $\Delta \mathbf{x}_{\text{prep}}$ (moderate knowledge, well-projected). The scalar makes these states identical. The prep industry profits from the indistinguishability.

The equity consequence: students with access to expensive test preparation can purchase projection improvement. Students without access cannot. The SAT score gap between high-SES and low-SES students reflects, in part, differential access to projection optimization --- not differential learning. This is the standardized testing gauge violation that Chapter 14 formalizes.

## 2.3 The Testing Ecosystem

The SAT is not an isolated instrument. It exists within an ecosystem of standardized tests that spans the entire educational trajectory, each performing a scalar contraction at a different stage.

### 2.3.1 K-12: The State Assessment Apparatus

The No Child Left Behind Act (2002) and its successor, the Every Student Succeeds Act (2015), mandated annual standardized testing in mathematics and reading for grades 3--8 and once in high school. The result was a massive expansion of the testing industry: state contracts for test development, administration, scoring, and reporting, worth hundreds of millions of dollars annually.

These tests perform scalar contraction at the institutional level: schools are evaluated by aggregate student scores, producing school-level scalars (percent proficient, average scale score, growth percentile) that determine funding, sanctions, and public reputation. The school-level scalar is a contraction of a contraction: student understanding is contracted to a test score, and student test scores are contracted to a school average. The double contraction destroys even more information than either contraction alone.

The consequence is predictable from the GPA Irrecoverability Theorem: schools optimize the scalar. "Teaching to the test" --- narrowing the curriculum to tested content, drilling test-taking strategies, reallocating time from untested subjects (art, music, physical education, social studies) to tested subjects (math, reading) --- is the institutional analogue of grade optimization by students. The school is following the projected gradient, maximizing the scalar at the expense of the manifold.

### 2.3.2 Graduate and Professional School: The GRE, MCAT, LSAT

The graduate admissions pipeline continues the scalar contraction. The GRE (Graduate Record Examination) produces three section scores that serve as screening criteria for graduate programs. The MCAT produces four section scores for medical school admissions. The LSAT produces a single score for law school admissions.

Each of these instruments makes the same trade: scalability and comparability in exchange for dimensional collapse. The GRE's Verbal Reasoning section cannot distinguish a student who reads deeply and thinks slowly from a student who reads superficially and thinks quickly --- both may produce the same score if their speed-accuracy trade-offs happen to balance. The MCAT's science sections cannot distinguish a student who memorized biochemistry pathways from a student who understands the underlying chemistry well enough to derive the pathways from first principles. The LSAT's logical reasoning section cannot distinguish a student who has been coached in LSAT-specific argument patterns from a student who reasons logically about novel arguments.

### 2.3.3 Professional Certification: The Bar, Boards, and Beyond

Beyond admission, scalar testing continues into professional certification. The bar examination determines who may practice law. Medical board examinations determine who may practice medicine. Professional engineering examinations determine who may certify designs. Each is a scalar contraction that reduces a multi-dimensional competence state to a binary outcome (pass/fail) or a scalar score.

The irony is that professional practice is irreducibly multi-dimensional. A lawyer must integrate legal knowledge, client communication, strategic judgment, ethical reasoning, and adversarial thinking. A physician must integrate clinical knowledge, diagnostic reasoning, communication skills, procedural competence, and ethical sensitivity. No scalar can capture these competencies. Yet the gatekeeping decisions --- who may practice --- are made on the basis of scalars.

## 2.4 The Business Model of Scalar Contraction

The standardized testing industry has a business model that depends structurally on scalar contraction. Understanding this business model is essential to understanding why the testing industry has resisted dimensional expansion despite decades of psychometric criticism.

### 2.4.1 Why Scalars Are Commercially Viable

A scalar test has four properties that make it commercially valuable:

**Standardization.** A scalar produces the same type of output (a number) for every student, enabling comparison across students, schools, states, and years. This comparability is the basis for the test's value proposition: it provides a "common yardstick" for educational achievement. The geometric framework reveals that the yardstick measures in one dimension while the phenomenon varies in six, but the yardstick's uniformity is what makes it commercially useful.

**Scalability.** A scalar test can be administered to millions of students simultaneously, scored by machine (or by low-cost human raters following a constrained rubric), and reported as a single number per student. Multi-dimensional assessment --- portfolios, performance tasks, exhibitions, oral examinations --- requires expert human judgment, time, and individual attention. These are expensive. Scalars are cheap.

**Legal defensibility.** A scalar test produces a clear rank ordering: Student A scored higher than Student B. This rank ordering provides legal cover for high-stakes decisions. An admissions office that rejects a student with a 1100 SAT score in favor of one with a 1300 can point to the number as justification. A multi-dimensional assessment that says "Student A is stronger on transfer but weaker on domain knowledge" does not produce a clear ordering and therefore does not provide the same legal protection.

**Metric capture.** Once a scalar becomes established as the measure of educational quality, it becomes difficult to replace --- not because it measures well, but because the entire decision-making infrastructure is built around it. Admissions offices have calibrated their expectations to SAT scores. Scholarship criteria reference GPA thresholds. Employers use GPA cutoffs for resume screening. Replacing the scalar requires not just a better measure but a redesign of every system that references the old one.

### 2.4.2 The Commercial Incentive Against Dimensional Expansion

The testing industry has strong commercial incentives to resist dimensional expansion. A multi-dimensional assessment is harder to administer, harder to score, harder to compare, harder to defend legally, and harder to build a $10 billion prep industry around. A vector of scores does not produce the clean rank ordering that admissions offices use for screening. A profile of competencies does not fit in the SAT score box on the Common Application.

The industry's resistance is not conspiratorial. It is structural. The College Board does not hold secret meetings to suppress multi-dimensional assessment. It responds to market incentives: colleges want a simple screening number, students want a clear target, and policymakers want a comparable metric. The demand is for scalars. The industry supplies scalars. The geometric damage is a byproduct of a commercial equilibrium, not a deliberate design.

But the fact that the damage is unintentional does not make it less real. The $10 billion test prep industry profits from the gap between projection optimization and actual learning. The admissions consulting industry profits from the gap between transcript engineering and actual achievement. The tutoring industry profits from the gap between test-taking skill and domain understanding. These gaps are geometric --- they exist because the scalar projection creates a space between the projected value and the manifold position --- and they are monetized by industries that help students navigate the gap.

## 2.5 The Psychometric Defense and Its Limits

The testing industry has a sophisticated psychometric defense of scalar assessment. The defense is technically sound within its own framework and geometrically inadequate from the manifold perspective. Understanding both the defense and its limits is essential for an honest assessment of where scalar testing stands.

### 2.5.1 Reliability

Psychometric reliability measures the consistency of a test: does the same student produce the same score on repeated testing? The SAT's test-retest reliability is approximately 0.87 for the total score, which is high by psychometric standards. The testing industry presents this as evidence that the SAT measures "something real."

The geometric framework agrees: the SAT measures something real. It measures the projection of the learner state onto the SAT's weighting vector with high consistency. But reliability is a property of the projection, not of the manifold. A bathroom scale that consistently measures weight is reliable even if weight is an inadequate measure of health. The SAT consistently measures SAT performance. The question is whether SAT performance captures educationally relevant information, and the GPA Irrecoverability Theorem says it captures some ($d_1$ recognition) while destroying the rest.

### 2.5.2 Validity

Psychometric validity is more complex. The traditional framework distinguishes content validity (does the test cover the right material?), criterion validity (does the test predict an external outcome?), and construct validity (does the test measure the intended theoretical construct?).

The SAT's criterion validity for predicting first-year college GPA is moderate: correlations in the range of $r = 0.50$--$0.60$ in recent meta-analyses. This means the SAT explains roughly 25--36% of the variance in first-year GPA. The testing industry presents this as evidence of predictive power.

The geometric framework offers a different interpretation. First-year college GPA is itself a scalar contraction of the learner manifold. Predicting one scalar from another scalar tells us about the alignment of two projection directions, not about the manifold. If the SAT projects along a direction dominated by $d_1$ and first-year GPA projects along a similar direction (also dominated by $d_1$, because college courses also test domain recall through exams), then the correlation is expected --- both projections are sensitive to the same dimension. The correlation does not validate the SAT as a measure of "college readiness." It validates the SAT as a measure of the dimension of learner variation that also dominates first-year grades. If first-year grades are themselves inadequate measures of learning (which the GPA Irrecoverability Theorem says they are), then predicting them well is predicting an inadequate measure well --- which is a modest achievement.

### 2.5.3 Fairness

Psychometric fairness analyzes whether a test treats different demographic groups equitably. The standard framework examines differential item functioning (DIF): does the probability of answering an item correctly, conditional on overall ability, differ by demographic group? If so, the item is flagged as potentially biased.

The geometric framework reinterprets DIF as a specific type of gauge violation: the item measures something different for different groups, even after controlling for the scalar ability estimate. But the geometric framework goes further: the scalar ability estimate itself ($\theta$, in item response theory) is a projection of the multi-dimensional learner state onto a single axis. Controlling for $\theta$ is controlling for the projected value, not for the full learner state. Two students with the same $\theta$ may have different learner tensors, and if those tensors differ along demographic lines (as the analysis in Section 1.3 suggests they do), then DIF analysis on $\theta$ will underestimate the extent of bias.

The deeper problem is that the test's projection direction itself --- the weighting vector $\mathbf{w}_{\text{SAT}}$ --- may be demographically biased, even if individual items are fair. If the weighting vector privileges $d_1$ (domain knowledge testable by multiple choice) over $d_2$ through $d_6$ (procedural skill, metacognition, motivation, transfer, creativity), and if the distribution of strengths across these dimensions differs by demographic group, then the test is structurally biased at the level of the projection, not at the level of the items. No amount of DIF analysis can detect this bias because DIF operates within the projection, not on the projection itself.

## 2.6 The Post-COVID Reckoning

The COVID-19 pandemic produced an unplanned natural experiment in standardized testing. When test centers closed in 2020, hundreds of colleges and universities adopted test-optional or test-blind admissions policies. The results challenged decades of testing industry assumptions.

### 2.6.1 What Happened

By 2024, approximately 80% of four-year institutions in the United States had adopted test-optional policies for at least one admissions cycle. The immediate effect was a sharp decline in the number of students submitting test scores: at many institutions, only 50--60% of applicants submitted scores, down from near-universal submission.

The demographic composition of the non-submitting group was predictable from the geometric framework: students from lower-SES backgrounds, first-generation students, students from under-resourced schools, and underrepresented minority students were disproportionately likely to withhold scores. These are the students whose strengths are concentrated on non-tested dimensions ($d_2$ through $d_6$) and whose test scores are depressed by gauge violations (differential access to test preparation, differential familiarity with test format, differential impact of testing conditions).

### 2.6.2 What the Data Showed

Several large-scale studies examined the academic performance of students admitted without test scores. The findings were consistent: students admitted without test scores performed comparably to students admitted with test scores, as measured by first-year GPA, retention rates, and four-year graduation rates.[^2]

The geometric interpretation is straightforward. If the SAT primarily measures $d_1$ (domain recognition), and if first-year GPA also primarily measures $d_1$ (domain recall on exams), then removing the SAT from the admissions equation and replacing it with other indicators (high school GPA, essays, recommendations --- which may capture more of $d_2$ through $d_6$) does not degrade the prediction of first-year GPA much, because other indicators also predict $d_1$. The SAT is a redundant projection in the same direction as other available signals.

But the more interesting finding is that non-submitting students --- the students whose SAT scores would have been low --- perform comparably on the outcome measures despite their predicted underperformance on the SAT. This is consistent with the geometric framework: these students occupy learner states that are distant from the SAT's projection direction but not from the directions that matter for academic success. Their strengths ($d_2$, $d_3$, $d_4$, $d_5$) compensate for their weakness on the tested dimension ($d_1$), and the compensation is visible in their college performance even though it was invisible to the SAT.

### 2.6.3 The Backlash

Despite the evidence, several elite institutions reinstated test requirements in 2024--2025 --- notably MIT, Dartmouth, and Yale. The stated reasons varied: MIT cited internal research showing that test scores added predictive power for STEM courses specifically (a plausible claim if STEM courses weight $d_1$ even more heavily than other courses); Dartmouth cited concerns about holistic review without quantitative anchors.

The geometric framework illuminates the backlash. The primary value of the SAT to elite admissions offices is not prediction. It is sorting. A scalar produces a rank order. A rank order enables screening: draw a line at 1400 and discard everyone below it. Without the scalar, every application must be read holistically --- which is more labor-intensive, more expensive, and more vulnerable to subjective bias. The testing industry's commercial proposition is, at bottom, a labor-saving device for admissions offices. The geometric adequacy of the device is secondary to its practical convenience.

## 2.7 Alex Takes the SAT

Alex takes the SAT on a Saturday morning in October. The testing center is a high school gymnasium twenty miles from home. Alex's mother drives because the family car needs a fuel pump replacement and Alex doesn't have time to fix it before the test. Alex arrives after a forty-minute drive, nervous, having slept poorly the night before because a younger sibling was sick.

The test begins. Alex reads the first passage --- an excerpt from a nineteenth-century novel --- and struggles with the vocabulary. Not because Alex cannot read, but because Alex's reading has been primarily technical: repair manuals, electronics documentation, YouTube tutorial transcripts. The SAT's reading passages are drawn from literary fiction, social science, and natural science --- domains where Alex's $d_1$ is weakest.

In the mathematics section, Alex encounters problems that are structurally similar to problems Alex solves every day in the repair shop --- proportions, spatial reasoning, rate calculations. But they are expressed in a notation that Alex's school did not emphasize, with formatting conventions that test preparation (which Alex could not afford) teaches explicitly. Alex solves several problems by first translating them into the language of practical mechanics, then solving them, then translating back. The translation adds time. The test is timed.

Alex scores 1180. Ethan, who took the same test after two years of private tutoring (Kaplan course plus 40 hours of one-on-one instruction), scores 1420.

The 240-point gap does not measure the difference in their understanding. It measures the difference in four things: (1) domain knowledge alignment with SAT content ($d_1$ for SAT-tested material --- Ethan higher); (2) format familiarity (Ethan has taken dozens of practice tests --- Alex has taken two, from a free online source); (3) access to projection optimization (Ethan's $30,000 of test prep versus Alex's zero); and (4) testing conditions (Ethan slept well in a quiet room and was driven to the test by a parent who cheerfully discussed test strategy in the car; Alex slept poorly and worried about the fuel pump on the drive).

Of these four factors, only the first --- domain knowledge alignment --- has any relationship to Alex's capacity for college-level work. The other three are gauge violations: they change the measured value without changing the underlying state. Alex's "true" SAT score --- the score that would be obtained in a gauge-invariant testing environment --- is unknowable from the data, but the direction of the bias is clear: the gauge violations uniformly depress Alex's score.

The admissions office sees 1180 and 1420. It does not see the gauge violations. It does not see the manifold. It sees two numbers, and it makes decisions accordingly.

## 2.8 The Alternative

The geometric framework does not argue that standardized testing is entirely without value. It argues that the value is narrow and the destruction is broad. The SAT measures one dimension of the learner manifold with moderate reliability. It destroys five dimensions in the process. The question is not "should we measure?" but "in what space should we measure?"

The alternative is multi-dimensional assessment designed from the start to satisfy gauge invariance --- the requirement that the measured learner state should not depend on who administers the test, in what format, in what language, under what conditions, or in what context. Chapter 9 develops the Assessment Gauge Invariance Theorem in full. Chapters 14 and 15 apply it to standardized testing and educational opportunity. The path from scalar to geometric assessment is long, but the first step is understanding that the current system does not measure what it claims to measure. This chapter has taken that step.

---

## Summary

This chapter has examined the standardized testing industry as an institutionalized system of scalar contraction. The SAT projects a six-dimensional learner state onto a one-dimensional score, discarding procedural skill, metacognitive awareness, motivation, transfer ability, and creativity. The $10 billion test preparation industry profits from the gap between projection optimization and actual learning. The psychometric defenses of standardized testing --- reliability, validity, fairness --- are technically sound within the scalar framework and geometrically inadequate from the manifold perspective. The post-COVID natural experiment in test-optional admissions provided evidence that SAT scores are partially redundant with other available signals and that students admitted without scores perform comparably on scalar outcomes. The geometric framework explains why: the SAT is a redundant projection along a direction that other indicators also capture, and its unique contribution is screening convenience rather than diagnostic insight.

---

[^1]: Exact figures for the test preparation industry are difficult to verify because many providers are privately held. The $10 billion estimate includes test prep courses, private tutoring, practice materials, and online preparation platforms. IBISWorld and MarketWatch have published estimates in this range.

[^2]: Belasco, A. S., Rosinger, K. O., & Hearn, J. C. (2015). The test-optional movement at America's selective liberal arts colleges. *Educational Evaluation and Policy Analysis*, 37(2), 206--223. More recent data from the Common Application (2023) confirms the trend: test-optional admits show negligible differences in first-year academic performance relative to test-submitting admits, controlling for other application variables.
