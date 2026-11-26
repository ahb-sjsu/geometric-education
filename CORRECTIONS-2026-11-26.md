# Corrections to Geometric Education, 2026-11-26

These corrections were made on 2026-11-26 at the author's direction after a review of the series.

## Reconciled

1. **Chapter 1, Sections 1.3 and 1.4.1 (`manuscript/part_i/ch01_gpa_trap.md`): distance between Alex and Ethan.**
   The text gave the Euclidean distance between the two learner states as about 0.77, in three places. It now gives 0.78. The coordinate differences printed in the same sentence are 0.35, 0.35, 0.30, 0.25, 0.35 and 0.30. Their squares sum to 0.61, and the square root of 0.61 is 0.781.

2. **Chapter 1, Section 1.4.1 (same file): the two projections.**
   The text said that on the GPA line the two students are at the same point, with |G(Alex) - G(Ethan)| = 0. Section 1.3 computes G(Alex) = 0.593 and G(Ethan) = 0.671 with the printed weights, and says itself that Ethan's projected score is higher on that weighting. The sentence now says that both transcripts read 3.5 and that the illustrative linear weighting of Section 1.3 separates the two by 0.671 - 0.593 = 0.078. The two statements (the students' actual grade point averages are both 3.5; the illustrative linear model does not give equal values) are now both stated and related. The vectors and the weights were not changed.

3. **Chapter 5, Sections 5.4.1 and 5.7 (`manuscript/part_ii/ch05_assessment_contraction.md`) and Chapter 15, Section 15.7 (`manuscript/part_iv/ch15_geometry_opportunity.md`): norms of the four-year states.**
   The text gave the norms as about 1.34 for Ethan and 1.87 for Alex. It now gives 1.33 and 1.93. The printed vectors are (0.90, 0.55, 0.40, 0.50, 0.40, 0.30) and (0.70, 0.90, 0.80, 0.75, 0.85, 0.70). Their squares sum to 1.7725 and 3.715, with square roots 1.331 and 1.927. The comparison the text draws (Alex is further from the origin) is unchanged.

4. **Chapter 9, Section 9.6 (`manuscript/part_iii/ch09_gauge_invariance.md`): attribution of the 30-point gap.**
   One paragraph attributed the gap between the two assessments to three transformations that changed together (format, time, context). The next said the format transformation alone accounts for it. The second sentence now says the format entry is about 0.30 if the whole shift is attributed to format, and that the pair of assessments bounds the three entries together and does not separate them. This is the weaker of the two statements.

5. **Chapter 14, Summary (`manuscript/part_iv/ch14_standardized_testing.md`): total gauge violation.**
   The summary said 200 to 500 points for multiply-disadvantaged students. Section 14.4 of the same chapter says 300 to 500 points. The summary now says 300 to 500. (The figure of 200 to 500 in Section 9.4 is the sum of a different table, without the SES row, and was left as it is: its rows sum to 190 to 480.)

6. **Chapter 14, Section 14.5 (same file): the test-optional evidence.**
   The text said that low-SES students admitted without scores perform comparably to high-SES students admitted with high scores. Section 2.6.2, which this passage cites, and its source report only that students admitted without scores perform comparably to students admitted with scores, and Section 2.6.1 says that the students who withheld scores were disproportionately of lower socioeconomic status. The sentence now says what Chapter 2 says. The following sentence was changed from "low-SES admits" to "admits without scores" to match.

7. **Appendix C, Section C.3 (`manuscript/appendices/appendix_c_assessment.md`): composite score.**
   The formula used the signed effect size d_k. The thresholds of Section C.2 are all stated for the absolute value, and with a negative effect size the formula gives a score above 1, outside the stated range of 0 to 1. The formula and the sentence under it now use |d_k|.

8. **Chapter 16, Section 16.2.4 (`manuscript/part_v/ch16_measuring_manifold.md`): footnote marker.**
   The chapter's footnote 1 (Doignon and Falmagne, 1999) had no marker in the text. The marker was added where the work is cited.

## Marked as illustrative or simulated

1. **Chapter 13, Section 13.5 (`manuscript/part_iv/ch13_educational_bond_index.md`).**
   The section narrates a study by Alex, the volume's composite student, and said "The GPA Irrecoverability Theorem, confirmed empirically" and called the decomposition "a finding". A first sentence now says the section is an illustrative scenario, that the study and its numbers are hypothetical, and that no such study has been run (Section 18.5). "Confirmed empirically" now reads "illustrated in Alex's hypothetical data", and "a finding" now reads "a hypothetical finding". The numbers (2.1, and the shares of 45, 30, 15 and 10 percent) are unchanged.

2. **Chapter 13, Summary (same file).**
   The summary said the chapter had "defined, computed, and applied" the index. It now says the chapter has defined the index, set out its computation, and illustrated its application with a hypothetical study. This agrees with Section 18.5 and with the README's status note of 2026-07-14.

3. **Chapter 16, Section 16.4 (`manuscript/part_v/ch16_measuring_manifold.md`).**
   The section said "The results confirm both predictions" and "The GPA Irrecoverability Theorem is confirmed empirically". Section 18.1 says the predictions of Section 16.3 have not been tested. A first sentence now says the section is an illustrative scenario with hypothetical results. The two sentences now read "In the scenario, the hypothetical results agree with both predictions" and "This is what an empirical confirmation of the GPA Irrecoverability Theorem would look like". The numbers (1.4 semesters, 2.3x) are unchanged.

4. **Chapter 14, chapter head, Section 14.1 and Summary (`manuscript/part_iv/ch14_standardized_testing.md`).**
   The chapter said it "proves" Theorem 14.1 and that "the proof is empirical". The support given is a set of estimated score effects, most without a source, and the README classes the volume as posited. The chapter head now says "states", Section 14.1 says "The case for it is empirical: it consists of arguing that", and the summary says "has stated and argued for". The theorem statement and the estimates are unchanged.

## Withdrawn or updated

1. **Chapter 17, Section 17.6 (`manuscript/part_v/ch17_feedback_general_theory.md`): the D4 group.**
   The last sentence of the section said the general theory "inherited the D4 symmetry group from ethics". Geometric Ethics withdrew D4 as the group of the four Hohfeldian positions in its version 1.25: the correlative and the negation commute and generate the Klein four-group V4, of order 4, and there is no quarter-turn. The sentence now names the Klein four-group V4 of the Hohfeldian positions, and a dated note at the head of the section records the change. This is the only mention of the group in the volume. No theorem, definition or prediction of this volume uses a quarter-turn or a group of order 8, so nothing is marked withdrawn.

No other result that Geometric Ethics has withdrawn or refuted (Conservation of Harm, the SU(2) gauge prediction, hysteresis) is cited in this volume. Section 18.2 asks what conservation law the assessment invariance would imply; see Unresolved, item 4.

## Unresolved

Each of these needs the author. The text was left as it is.

1. **Chapter 6, Sections 6.2.1 to 6.2.3 (`manuscript/part_ii/ch06_teaching_geodesic.md`): admissibility, inequality against prose.**
   Definition 6.2 calls the heuristic admissible when h_T(x) is at most the true distance to the goal. That is the standard condition for A* (Appendix A.8, Theorem 7.1), and Theorem 6.1 needs it. Under it the teacher may judge the student closer to understanding than the student is, and never further. The prose says the opposite: the admissible teacher "may think the student is further from understanding than they actually are" and "never thinks the student understands when they do not". Section 6.2.3 writes the inadmissible case as h_T > d + epsilon and describes it as overestimating readiness, which would be h_T below d. The same section calls "frustration deflation", an estimate that is too pessimistic and so above d, admissible. There are two consistent repairs and they differ in substance. (a) Keep the A* definition and Theorem 6.1, and change the educational reading: the admissible teacher is the one whose estimate is a lower bound on the remaining work. (b) Keep the educational reading (the safe teacher never judges a student ready too early, h_T at least d), give that property its own name, and withdraw the claim that Theorem 6.1 applies to it. The same choice touches Section 6.6, Section 12.6 and the Chapter 6 summary.

2. **Chapter 11, Theorem 11.1 (`manuscript/part_iii/ch11_transfer_learning.md`): closed-curve integral on an open path.**
   Definition 11.1 takes a path from one domain to another and writes the holonomy as k' - k, a difference of vectors at two different points. Theorem 11.1 writes the holonomy as an integral of the connection form around a closed curve and bounds it by the area the path encloses. An open path encloses no area. A correct statement needs either a closed loop (out by one route and back by another, which is what part 3 of the theorem compares) or a reference path that closes the curve. This is a restatement that needs real mathematics.

3. **Appendix C, Section C.3: how the examiner test enters the composite score.**
   The examiner test is scored by kappa or an intraclass correlation, where higher is better and the threshold is 0.80 or 0.85. The other four are scored by an effect size, where lower is better. The formula divides each score by its threshold and does not say what is used for the examiner test. Also, an assessment that sits exactly at every threshold has a score of 0, and the band "0.80 or more is adequate" requires the mean ratio to be at most 0.2, which is stricter than passing all five tests. The table of Section C.4 lists 0.20 for context, where Section C.2.5 also sets 0.30 for subgroups.

4. **Chapter 18, Section 18.2: the predicted conservation law.**
   The section says the framework predicts that a conservation law exists because a symmetry exists, by Noether's theorem. Noether's theorem needs a continuous symmetry. The five gauge transformations of Chapter 9 are discrete swaps, and the section itself notes that the theorem concerns continuous symmetries. Geometric Ethics has withdrawn its own conservation law. The author would need to say whether a continuous family of re-descriptions is intended, or weaken "predicts" to "suggests".

5. **Chapter 14, Section 14.4: "interact multiplicatively" against the total.**
   The rows of the table sum to 320 to 710 points. The text says the violations interact multiplicatively and then gives a compound total of 300 to 500 points, which is below the plain sum. Chapter 15, Proposition 15.2 states a multiplicative lower bound for compound metric distortion with no proof, and illustrates it with "3 squared" for three sources.

6. **Chapter 2, Section 2.7: Ethan's test preparation.**
   Ethan's preparation is "a Kaplan course plus 40 hours of one-on-one instruction" and also "30,000 dollars of test prep". At the rates of Section 2.2.2 (a course at 1,000 to 2,500 dollars, tutoring at 100 to 300 dollars per hour) 40 hours and a course cost at most 14,500 dollars. The figure of 30,000 matches the 100 hours of Section 2.2.2. Alex's own preparation is "zero" in the same sentence, two free practice tests earlier in it, and "no test prep" in Section 14.8.

7. **Chapters 1 and 2: length of the SAT.**
   Section 1.2.2 calls it a three-hour event and Section 2.1.2 says four hours.

8. **Alex's Differential Equations course, across Chapters 6, 7, 8, 11 and 12.**
   Section 6.6 gives a C+ from the standard section and an A- in Professor Vasquez's section. Section 7.8 has Alex withdraw from the standard course, with the withdrawal on the transcript. Section 8.7 has Dr. Patel as Alex's professor and a C+ on an exam. Section 11.5 says no instructor connected the mathematics to the engine, while Sections 6.6 and 12.6 have Vasquez make exactly that connection. Section 9.6 has a C+ of 68 on a physics exam and Section 8.7 a C+ of 65.

9. **Chapter 17, Section 17.4: "stakes/dimension ratio".**
   The quantity is called a ratio, and the formula is a product of the stakes and the fraction of dimensions lost.

10. **Chapter 13 against Section 18.1: what routine data can support.**
    Chapter 13 says the index is computable from data that most institutions already collect. Section 18.1 says three of the six dimensions have weak or no projection onto standard LMS observables and may not be identifiable from that data.

11. **Empirical figures given without a source.**
    The SAT gauge-violation ranges of Section 9.4 and of Sections 14.2.1 and 14.4. The 1.5 to 2 extra semesters for first-generation students in Section 6.4.1. Inter-rater reliability "typically below 0.70" in Section 9.3.1. The estimate of 100 to 1000 distinct profiles per grade value in Section 5.2.1. "Approximately 80% of four-year institutions" in Section 2.6.1. "Abundantly confirmed by empirical observation" in Section 1.7.2. The author would need to supply a citation for each or mark it as an estimate.

12. **Footnotes with no marker in the text.**
    Chapter 1 (note 3), Chapter 3 (notes 1 to 5), and note 1 of Chapters 5, 6, 7, 10, 11, 12, 13, 15, 17 and 18 are defined at the end of the chapter and never referenced. Each needs a marker at the place the author intends.

13. **Planning files not edited.**
    `OUTLINE.md` still describes "identical GPA contractions" for the 3.5 Decomposition, gives Alex's gauge violation as about 150 points where Section 14.8 says 150 to 200, and narrates Alex's study as results. It is a plan, not a chapter, and was left alone.

## Found while drawing the figures (2026-11-26), not changed

These were noticed while the figures were drawn and are left for the author. No figure draws them.

1. Section 1.3 says "The students are orthogonal". The cosine between the two printed vectors is 0.91. The same sentence calls them "about as different as two learner states can be while producing the same GPA", while their distance is 0.78 and the diameter of the unit cube is the square root of 6, about 2.45.
2. G(Ethan) is 0.6715 exactly and is printed as 0.671; the separation is 0.0785 and is printed as 0.078. The figures show the printed values.
3. Section 2.2.1 says that along a fiber "the projection changes, the base point does not". Along a fiber the projection is unchanged by definition; the formal decomposition in the same section has it right.
4. Section 3.9.1 lists Scantron (1972) after Gardner (1983), and its section follows the 1983 one.
5. Proposition 4.1: Scenarios 1 and 3 list the same four dimensions, so "no proper subset suffices" holds only in the sense that each dimension appears in some scenario. The next sentence calls the proposition empirical.
6. Section 11.5 against Section 5.4.1: Alex's entry state plus the printed transfer increment exceeds the printed four-year state on d4, d5 and d6. Section 11.5 also says that c squared = 4mk decides between overdamped, underdamped and undamped; undamped is c = 0.
7. Chapter 12 says the AI tutor cannot observe physical skill (d2) in Section 12.1.2, and that it is helpful for procedural drill (d2) in Section 12.6, which also lists d1 among the dimensions it is less helpful for.
8. Definition 13.1 subtracts the learning deviation of the geodesic, which is zero by the definition of the deviation; Section 13.3.3 drops the term without comment.
9. The rows of the Section 9.4 table sum to 190 to 480; the text says 200 to 500.

## Figure placeholder

The one bracketed figure description, in Chapter 1, was taken out when the drawn Figure 1.1 went in, and is kept with a verdict in figures/PLACEHOLDERS.md.
