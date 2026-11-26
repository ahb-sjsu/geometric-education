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

3. **Appendix C, Section C.3: how the examiner test enters the composite score.** (partly repaired, see below)
   The examiner test is scored by kappa or an intraclass correlation, where higher is better and the threshold is 0.80 or 0.85. The other four are scored by an effect size, where lower is better. The formula divides each score by its threshold and does not say what is used for the examiner test. Also, an assessment that sits exactly at every threshold has a score of 0, and the band "0.80 or more is adequate" requires the mean ratio to be at most 0.2, which is stricter than passing all five tests. The table of Section C.4 lists 0.20 for context, where Section C.2.5 also sets 0.30 for subgroups.

4. **Chapter 18, Section 18.2: the predicted conservation law.** (repaired, see below)
   The section says the framework predicts that a conservation law exists because a symmetry exists, by Noether's theorem. Noether's theorem needs a continuous symmetry. The five gauge transformations of Chapter 9 are discrete swaps, and the section itself notes that the theorem concerns continuous symmetries. Geometric Ethics has withdrawn its own conservation law. The author would need to say whether a continuous family of re-descriptions is intended, or weaken "predicts" to "suggests".

5. **Chapter 14, Section 14.4: "interact multiplicatively" against the total.** (repaired, see below)
   The rows of the table sum to 320 to 710 points. The text says the violations interact multiplicatively and then gives a compound total of 300 to 500 points, which is below the plain sum. Chapter 15, Proposition 15.2 states a multiplicative lower bound for compound metric distortion with no proof, and illustrates it with "3 squared" for three sources.

6. **Chapter 2, Section 2.7: Ethan's test preparation.** (repaired, see below)
   Ethan's preparation is "a Kaplan course plus 40 hours of one-on-one instruction" and also "30,000 dollars of test prep". At the rates of Section 2.2.2 (a course at 1,000 to 2,500 dollars, tutoring at 100 to 300 dollars per hour) 40 hours and a course cost at most 14,500 dollars. The figure of 30,000 matches the 100 hours of Section 2.2.2. Alex's own preparation is "zero" in the same sentence, two free practice tests earlier in it, and "no test prep" in Section 14.8.

7. **Chapters 1 and 2: length of the SAT.**
   Section 1.2.2 calls it a three-hour event and Section 2.1.2 says four hours.

8. **Alex's Differential Equations course, across Chapters 6, 7, 8, 11 and 12.**
   Section 6.6 gives a C+ from the standard section and an A- in Professor Vasquez's section. Section 7.8 has Alex withdraw from the standard course, with the withdrawal on the transcript. Section 8.7 has Dr. Patel as Alex's professor and a C+ on an exam. Section 11.5 says no instructor connected the mathematics to the engine, while Sections 6.6 and 12.6 have Vasquez make exactly that connection. Section 9.6 has a C+ of 68 on a physics exam and Section 8.7 a C+ of 65.

9. **Chapter 17, Section 17.4: "stakes/dimension ratio".** (repaired, see below)
   The quantity is called a ratio, and the formula is a product of the stakes and the fraction of dimensions lost.

10. **Chapter 13 against Section 18.1: what routine data can support.** (repaired, see below)
    Chapter 13 says the index is computable from data that most institutions already collect. Section 18.1 says three of the six dimensions have weak or no projection onto standard LMS observables and may not be identifiable from that data.

11. **Empirical figures given without a source.** (repaired, see below)
    The SAT gauge-violation ranges of Section 9.4 and of Sections 14.2.1 and 14.4. The 1.5 to 2 extra semesters for first-generation students in Section 6.4.1. Inter-rater reliability "typically below 0.70" in Section 9.3.1. The estimate of 100 to 1000 distinct profiles per grade value in Section 5.2.1. "Approximately 80% of four-year institutions" in Section 2.6.1. "Abundantly confirmed by empirical observation" in Section 1.7.2. The author would need to supply a citation for each or mark it as an estimate.

12. **Footnotes with no marker in the text.** (repaired, see below)
    Chapter 1 (note 3), Chapter 3 (notes 1 to 5), and note 1 of Chapters 5, 6, 7, 10, 11, 12, 13, 15, 17 and 18 are defined at the end of the chapter and never referenced. Each needs a marker at the place the author intends.

13. **Planning files not edited.** (repaired, see below)
    `OUTLINE.md` still describes "identical GPA contractions" for the 3.5 Decomposition, gives Alex's gauge violation as about 150 points where Section 14.8 says 150 to 200, and narrates Alex's study as results. It is a plan, not a chapter, and was left alone.

## Found while drawing the figures (2026-11-26), not changed

These were noticed while the figures were drawn and are left for the author. No figure draws them.

1. (repaired, see below) Section 1.3 says "The students are orthogonal". The cosine between the two printed vectors is 0.91. The same sentence calls them "about as different as two learner states can be while producing the same GPA", while their distance is 0.78 and the diameter of the unit cube is the square root of 6, about 2.45.
2. (repaired, see below) G(Ethan) is 0.6715 exactly and is printed as 0.671; the separation is 0.0785 and is printed as 0.078. The figures show the printed values.
3. (repaired, see below) Section 2.2.1 says that along a fiber "the projection changes, the base point does not". Along a fiber the projection is unchanged by definition; the formal decomposition in the same section has it right.
4. (partly repaired, see below) Section 3.9.1 lists Scantron (1972) after Gardner (1983), and its section follows the 1983 one.
5. (repaired, see below) Proposition 4.1: Scenarios 1 and 3 list the same four dimensions, so "no proper subset suffices" holds only in the sense that each dimension appears in some scenario. The next sentence calls the proposition empirical.
6. (partly repaired, see below) Section 11.5 against Section 5.4.1: Alex's entry state plus the printed transfer increment exceeds the printed four-year state on d4, d5 and d6. Section 11.5 also says that c squared = 4mk decides between overdamped, underdamped and undamped; undamped is c = 0.
7. (partly repaired, see below) Chapter 12 says the AI tutor cannot observe physical skill (d2) in Section 12.1.2, and that it is helpful for procedural drill (d2) in Section 12.6, which also lists d1 among the dimensions it is less helpful for.
8. (repaired, see below) Definition 13.1 subtracts the learning deviation of the geodesic, which is zero by the definition of the deviation; Section 13.3.3 drops the term without comment.
9. (repaired, see below) The rows of the Section 9.4 table sum to 190 to 480; the text says 200 to 500.

## Figure placeholder

The one bracketed figure description, in Chapter 1, was taken out when the drawn Figure 1.1 went in, and is kept with a verdict in figures/PLACEHOLDERS.md.

## Repaired in the survey of 2026-11-26

Each item was checked against the current text first. "U" numbers refer to the list "Unresolved" above, "F" numbers to "Found while drawing the figures". No figure line, caption, or heading placed after a figure was edited. One repair (item 2) changes numbers that Figures 1.1 and 1.2 draw; this is said there.

1. **Chapter 1, Section 1.3 (`manuscript/part_i/ch01_gpa_trap.md`): "orthogonal" (F1).** "they are about as different as two learner states can be while producing the same GPA. The GPA is identical. The students are orthogonal." now reads: a large distance for two states with the same GPA, though two states in the unit cube can be as far as $\sqrt{6} \approx 2.45$ apart; the GPA is identical; the students are not: their profiles are nearly complementary, each strong where the other is weak, although the two vectors are not orthogonal (the cosine between them is 0.91). The cosine is computed from the two printed vectors (0.9117). "Nearly complementary" is Figure 1.1's own caption.

2. **Chapter 1, Sections 1.3 and 1.4.1 (same file): $G(\text{Ethan})$ (F2).** Ethan's line printed the addends $0.480 + 0.125 + 0.020 + 0.028 + 0.012 + 0.007$, which sum to 0.672, and then "$= 0.671$". The exact value from the printed weights and vector is 0.6715. The line now prints the exact addend 0.0275 and the total 0.6715, and Section 1.4.1's separation now reads $0.6715 - 0.593 = 0.0785$. Alex's line printed rounded addends (0.213, 0.023) that sum to 0.594 against the exact total 0.593; it now prints the exact addends 0.2125 and 0.0225, and the total 0.593 is unchanged. **Figures made stale:** Figure 1.1 draws the labels "0.078" and "Ethan 0.671", and its caption says "0.078 apart (0.593 and 0.671)"; Figure 1.2's caption and labels give Ethan as 0.671. Each should read 0.6715 and 0.0785 (0.672 and 0.079 at three places). `tools/figs_all.py` line 60 hard-codes 0.671 and 0.078.

3. **Chapter 1, Section 1.4.1: footnote 3 (U12).** The note on the covariance matrix now has a marker after "All of these questions require the full metric."

4. **Chapter 1, Section 1.7.2: "abundantly confirmed" (U11).** "This prediction is abundantly confirmed by empirical observation" now reads "consistent with common observation, though this chapter cites no study that tests it".

5. **Chapter 2, Section 2.2.1 (`manuscript/part_i/ch02_testing_industrial_complex.md`): the fiber (F3).** Section 2.2.1 defines the fiber as the preimage of a score, so motion along it leaves the score unchanged. "This is motion along the fiber: the projection changes, the base point does not" now reads "motion across the fibers, from one set of equal score to the next: the projection changes while the base point barely moves. (Motion along a fiber would leave the score unchanged.)" The heading of Section 2.2.1 ("Movement Along the Fiber", not placed after a figure) now reads "Movement Across the Fibers", and the same phrase is corrected in Section 2.2.2 and in Section 14.2.1 ("motion across the fibers"). The formal decomposition of Section 2.2.1 and Figure 2.1 already had it right and are unchanged.

6. **Chapter 2, Section 2.7: Ethan's test preparation (U6).** "Ethan's \$30,000 of test prep" now reads "Ethan's \$5,000--\$14,500 of test prep, a course and 40 hours of tutoring at the rates of Section 2.2.2". The figure is recomputed from Section 2.2.2 (a course at \$1,000--\$2,500, tutoring at \$100--\$300 an hour) and the 40 hours of Section 2.7. "Alex's zero" is unchanged: it is a sum of money, and Alex's two practice tests were free. Section 14.8's "no test prep" is also unchanged; it reads as no paid preparation, and the author may want to say so.

7. **Chapter 2, Section 2.6.1: test-optional figures (U11).** A sentence now says that the 80% of institutions and the 50--60% of applicants are estimates for which the chapter gives no source.

8. **Chapter 2: currency signs (checker, math balance).** Sixteen dollar signs in the chapter head, Sections 2.2, 2.2.2 and 2.4.2, the Summary and footnote 1 were bare, and the checker read them as unclosed formulas. They are now written `\$`.

9. **Chapter 3, Section 3.9.1 (`manuscript/part_i/ch03_history.md`): the table (F4, in part).** The table is in order of era, and its Scantron (1972) row stood after Gardner (1983). The two rows are swapped. Figure 3.1, which puts the rows in order of date, is unchanged and still right. The order of the sections (3.6 Gardner before 3.9 Scantron) is thematic and is left as it is.

10. **Chapter 3: footnotes 1 to 5 (U12).** Markers now stand at the first mention of each work: Dewey (1916) in Section 3.4 (note 5), Bloom (1956) in Section 3.5 (note 1), Gardner (1983) in Section 3.6 (note 2), Vygotsky's Zone of Proximal Development in Section 3.7 (note 3), and Freire (1968) in Section 3.8 (note 4).

11. **Chapter 4, Section 4.3 (`manuscript/part_ii/ch04_learner_manifold.md`): Proposition 4.1 (F5).** "The proposition is empirical: it is verified by checking each scenario against the dimensional decomposition" now says the proposition is checked by reading off the listed activations, that each of the six dimensions appears in at least one scenario so no proper subset covers them all (scenarios 1 and 3 list the same four), and that whether the listed activations are right is the empirical question. Figure 4.1's caption already says this.

12. **Chapter 6, Section 6.4.1 (`manuscript/part_ii/ch06_teaching_geodesic.md`): 1.5 to 2 semesters (U11).** "The additional path cost is measurable: first-generation students take, on average, 1.5 to 2 semesters longer" now reads "measurable in principle: first-generation students are estimated to take ... (this chapter gives no source for the figure)".

13. **Chapter 9 (`manuscript/part_iii/ch09_gauge_invariance.md`) (U11, F9).**
    - Section 9.3.1: "typically below 0.70" now reads "often below 0.70 ..., by an estimate for which this chapter gives no source".
    - Section 9.3.4: "Chronobiological effects on test performance are well-documented" now reads "widely reported, though this chapter gives no source for the effects that follow" (found while reading; the same kind of claim as those listed under U11).
    - Section 9.4: a paragraph under the table now says the point values are estimates, that the language and context effects are reported in standard deviations by the works cited in Sections 9.3.3 and 9.3.5 (Abedi, 2002; Steele and Aronson, 1995, both in the bibliography), and that their conversion to points and the format and time rows have no source. The total now reads "on these estimates, 190--480 points, on the order of 200--500 SAT points"; the rows sum to 190--480 (F9).
    - Summary: "Most educational assessments have gauge violations on the order of 0.5--1.0 standard deviations" now reads "On the estimates of Section 9.4, educational assessments can have ...".

14. **Chapter 11, Section 11.5 (`manuscript/part_iii/ch11_transfer_learning.md`): damping (F6, in part).** "The critical damping condition ($c^2 = 4mk$) is the condition that determines whether the ... vibration dies out quickly (overdamped), oscillates and fades (underdamped), or resonates indefinitely (undamped)" now says it is the boundary between dying out without oscillating (overdamped, $c^2 > 4mk$) and oscillating as it fades (underdamped, $c^2 < 4mk$), and that with no damping ($c = 0$) the vibration continues (undamped). Figure 11.2 and its caption say the same and are unchanged.

15. **Chapter 12 (`manuscript/part_iii/ch12_ai_education.md`) (F7, in part, and found while reading).**
    - Section 12.1.2: "or physical skill ($d_2$)" now reads "or physical skill (the hands-on part of $d_2$; symbolic procedures, the other part, it can see)". Section 12.6 has the tutor help with procedural drill ($d_2$); $d_2$ is "ability to execute and construct" (Section 1.3) and covers both.
    - Footnote 1: the No Escape Theorem was cited as *Geometric Ethics* (Bond, 2026b, Ch. 19) and said to "establish" its result. In *Geometric Ethics* (clone of 2026-11-26) it is Theorem 18.1 of Chapter 18, a conditional theorem; the footnote now cites Ch. 18, Theorem 18.1, and says it "states, on its four requirements". The footnote now has a marker after Theorem 12.1 (U12).
    - `manuscript/backmatter/index_framework.md`: the No Escape entry's "Series: GE Ch. 19" now reads "GE Ch. 18, Theorem 18.1 (a conditional theorem)".

16. **Chapter 13 (`manuscript/part_iv/ch13_educational_bond_index.md`) (U10, F8, and found while reading).**
    - The chapter head's "computed from data that every university already collects" now reads "to be computed largely from data that universities already collect (Section 18.1 states the limits of that data)". Section 13.3's "computable from data that most institutions already collect" now says it is meant to be, and adds that Section 18.1 notes that three of the six dimensions ($d_3$, $d_5$, $d_6$) have weak or no projection onto routine LMS data. The illustrative scenario of Section 13.5 is unchanged.
    - Definition 13.1: a sentence after it says the second term is zero, since the geodesic's learning deviation from itself vanishes, and that Section 13.3.3 computes the first term alone. The definition and Figure 13.1 are unchanged.
    - Footnote 1: "follows the general Bond Index from *Geometric Ethics* (Bond, 2026b, Ch. 16)" now reads "follows the clinical Bond Index of *Geometric Ethics* (Bond, 2026b, Ch. 21, Definition 21.10)" and adds that it shares a name with the Bond Index of *Geometric Ethics* (Ch. 18), which measures invariance under re-description, and is a different quantity. Definition 13.1 is the expected deviation a policy imposes on a population, the construction of Definition 21.10 there (checked in the *Geometric Ethics* clone of 2026-11-26); *Geometric Ethics* Chapter 16 is on moral uncertainty; and *Geometric Medicine*, Section 12.1, states the same distinction. The footnote now has a marker after Definition 13.1 (U12). The index entry "Bond Index, Educational" is corrected the same way.

17. **Chapter 14 (held back) (`manuscript/part_iv/ch14_standardized_testing.md`) (U5, U11).**
    - A dated note at the head of Section 14.2.1 says the point values of Sections 14.2.1, 14.3, 14.4 and 14.8 are the chapter's estimates with no source in the book, that the language and context effects are reported in standard deviations by Abedi (2002) and Steele and Aronson (1995), cited in Chapter 9, and that their conversion to points and every other range is an estimate: rough magnitudes, not measurements.
    - Section 14.3: "Research consistently finds 0.5--1.0 standard deviation effects" now reads "Effects of 0.5--1.0 standard deviation are reported ... (Abedi, 2002, cited in Section 9.3.3)", and "this corresponds to approximately 80--200 points" now reads "this chapter estimates the effect at approximately 80--200 points".
    - Section 14.4: "Assembling the evidence" now reads "Assembling the estimates". "The gauge violations are not independent: they interact multiplicatively" stood before a compound total of 300--500 points, below the plain sum of the table's rows, 320--710. Multiplicative interaction would put the compound above the sum, so the statement is false of the chapter's own numbers. The text now says the rows overlap (the SES row of Section 14.2.1 already contains format familiarity and test anxiety, which overlap with the format and context rows), that the rows sum to 320--710 points, and that because of the overlap the compound effect for one student is less than that sum; the total of 300--500 is kept and called a rough estimate. Section 14.8's 150--200 points for Alex (SES, format, context) is consistent with the overlap reading.
    - Section 14.8: a first sentence says Alex is the volume's composite student and the section's figures are illustrative.
    - Summary: "The gauge violation tensor has been estimated for the SAT, with total violations of 300--500 points" now adds "roughly and without a source for its point values" and "perhaps".
    - Proposition 15.2 ("not additive but multiplicative") concerns the metric distortion of Chapter 15, not score points, and is unchanged; see the open list.

18. **Chapter 17, Section 17.4 (`manuscript/part_v/ch17_feedback_general_theory.md`): "ratio" (U9).** The formula $\text{Stakes} \times (d - k)/d$ is a product. "proportional to the stakes/dimension ratio" now reads "grows with the stakes and with the fraction of dimensions the contraction loses"; "the stakes/dimension ratio as a measure" and "This ratio provides" now read "the stakes-dimension product" and "This product provides"; the table row of Section 17.7 and item (4) of the summary now say "product". The heading of Section 17.4 and Figure 17.1 (which says "severity measure") are unchanged.

19. **Chapter 18 (`manuscript/part_v/ch18_open_questions.md`) (U4, and found while reading).**
    - Section 18.2: the opening sentence now adds "and if that invariance is under a continuous group of transformations". "The geometric framework predicts that a conservation law exists (because a symmetry exists)" now reads "suggests that a conservation law may exist", and adds that Noether's theorem needs a continuous symmetry and the five gauge transformations of Chapter 9 are discrete swaps, so the suggestion holds only if a continuous family of re-descriptions is intended.
    - Footnote 1: "*Geometric Ethics* (Bond, 2026b, Ch. 30)" now reads "Ch. 29, "Open Problems"". In the *Geometric Ethics* clone of 2026-11-26, Chapter 29 is "Open Problems" and Chapter 30 is the conclusion. The footnote now has a marker at the end of the chapter's opening statement (U12).

20. **Footnote markers, other chapters (U12).** Chapter 5: note 1 (the GPA Irrecoverability Theorem as an instance of the Scalar Irrecoverability Theorem) after Theorem 5.2. Chapter 6: note 1 (Shulman, 1986) at "Lee Shulman's (1986)" in Section 6.1.2. Chapter 7: note 1 (A*) at "A* search" in Section 7.2. Chapter 10: note 1 (Cronbach's aptitude-treatment interaction) at the end of the paragraph of Section 10.1 that says the metric is student-dependent. Chapter 11: note 1 (Barnett and Ceci's taxonomy for far transfer) at "far transfer" in Section 11.2.2. Chapter 15: note 1 (educational opportunity) after the first sentence of Section 15.1. Chapter 17: note 1 (the feedback protocol) at the end of the chapter's opening statement. With items 3, 10, 15, 16 and 19, sixteen markers in all; every footnote of the volume now has one.

21. **Appendix C, Section C.4 (`manuscript/appendices/appendix_c_assessment.md`): thresholds (U3, in part).** The reporting table gave the examiner threshold as "0.80 (kappa)" and the context threshold as "0.20". Sections C.2.1 and C.2.5 set "$\kappa \geq 0.80$ or ICC $\geq 0.85$" and "0.20 overall, and 0.30 for any demographic subgroup". The table rows now read "0.80 (kappa) or 0.85 (ICC)" and "0.20 overall; 0.30 per subgroup".

22. **`front_matter.md`, Series Foreword (found while reading).** "*Geometric Reasoning* (Book 2) ... Books 3 through 8 --- *Geometric Ethics*, ..." now reads "(Book 3) ... Book 2 and Books 4 through 8 --- *Geometric Ethics*, ...". The README's series table lists Methods, Ethics, Reasoning in that order, and *Geometric Ethics* calls itself Book 2, Volume 2 of the series (its README). The same correction was made in *Geometric Medicine* on 2026-11-26.

23. **`OUTLINE.md` (U13, and the cross-references).** The 3.5 Decomposition's "identical GPA contractions" now reads "the same 3.5 GPA ... (the illustrative linear weighting of Chapter 1 separates them by only 0.0785)". Alex's gauge violation "approximately 150 points" and "true" score "approximately 1330" now read 150–200 and 1330–1380, as in Section 14.8, and are marked illustrative. Alex's Bond Index study and Alex's LMS study are introduced as illustrative scenarios with hypothetical results (Sections 13.5 and 16.4), "The result" is "The hypothetical result", and "The GPA Irrecoverability Theorem, confirmed empirically" now reads "This is what an empirical confirmation ... would look like". The stakes-dimension "ratio" is a product, as in item 18. The cross-references to *Geometric Ethics* now give the clinical Bond Index as Ch. 21, Def. 21.10 (and say the Bond Index of Ch. 18 is a different quantity) and the No Escape Theorem as Ch. 18, Theorem 18.1 (conditional), in the existing-material line, the "From Geometric Ethics" list, the Chapter 12 plan and the cross-reference table.

Re-verified and left as they are:
- **U11, Section 5.2.1.** The "$10^2$ to $10^3$ qualitatively distinct learner profiles" is already introduced as "A rough estimate".
- **F7, Section 12.6, $d_1$.** The tutor is called less helpful for conceptual understanding ($d_1$, $d_5$, $d_6$) and an $\varepsilon$-admissible heuristic on $d_1$ and $d_2$. These are different properties (helping close a distance against estimating it), and both can hold.

Mechanical check: `series_check.py` (erisml-lib), in the version of 2026-11-26 20:34 that recognizes a cross-reference to another work when the work is named next to it, run on this clone after the repairs with its temporary build: 2 hard defects, both "Chapter 14" (Sections 2.2.2 and 2.8), which point at the held-back chapter and resolve if it goes online; KaTeX 0 failures; 22 pages, no broken internal link. Run with Chapter 14 included (the build's exclusion lifted, without a build): 0 hard defects, and Chapter 14 adds no finding. The footnotes of Chapters 12 and 13 (items 15 and 16) name *Geometric Ethics* next to the number ("*Geometric Ethics*, Theorem 18.1 (Bond, 2026b, Ch. 18)", "*Geometric Ethics*, Definition 21.10 (Bond, 2026b, Ch. 21)"), the form the checker reads as a reference to another work. The spelling findings are names (Hart, Furst), abbreviations (LSAT), technical words (automatized, statics, surjective) and British spellings in figure captions (centre, characterisations), none a misspelling.

## Still open after the survey of 2026-11-26

Each item needs the author. What the author must supply is said for each.

1. **Admissibility in Chapter 6 (U1).** Unchanged; the author must choose repair (a) or (b) as set out under Unresolved, item 1. The choice also touches Sections 6.6 and 12.6 and the Chapter 6 summary.

2. **Theorem 11.1 (U2).** Unchanged; needs a restatement with a closed loop or a reference path, which is new mathematics.

3. **The composite score of Appendix C (U3, rest).** The author must say what enters the formula for the examiner test (a reliability, higher is better, not an effect size), and whether the bands are meant to be stricter than passing all five tests (an assessment exactly at every threshold scores 0, and "0.80 or more" needs a mean ratio of at most 0.2).

4. **Continuous re-descriptions (U4, rest).** Section 18.2 now says "suggests". The author must say whether a continuous family of re-descriptions is intended.

5. **Proposition 15.2 (U5, rest).** The multiplicative lower bound for compound metric distortion has no proof, and its "$3^2$" illustration is not derived. The author must supply a proof or mark it a posit. Chapter 14 no longer says the score violations interact multiplicatively.

6. **Length of the SAT (U7).** Unchanged. Section 1.2.2 says a three-hour event, Section 2.1.2 four hours on a Saturday morning. The volume does not settle which form of the test it describes (the paper SAT and the digital SAT differ in length); the author must say.

7. **Alex's Differential Equations course (U8).** Unchanged; the author must settle the instructor, grade and withdrawal across Sections 6.6, 7.8, 8.7, 9.6, 11.5 and 12.6.

8. **Alex's learner state (F6, rest).** Alex's entry state plus the transfer increment of Section 11.5 exceeds the four-year state of Section 5.4.1 on $d_4$, $d_5$ and $d_6$ (0.95, 0.95, 0.75 against 0.75, 0.85, 0.70). The author must change a vector or say that those dimensions later fall. Figures 5.2 and 15.1 draw the four-year state.

9. **Section order of Chapter 3 (F4, rest).** The sections run Dewey (1916), Bloom (1956), Gardner (1983), Vygotsky (1934/1978), Freire (1968), Scantron (1972). If the author wants them in order of date, the headings that Figures 3.1 and 3.2 are placed before would move.

10. **Figures 1.1 and 1.2 (from repair 2).** Their labels and captions give 0.671 and 0.078 where Section 1.3 now gives 0.6715 and 0.0785; they must be redrawn (and line 60 of `tools/figs_all.py` updated).

11. **Sources for the estimates.** The point values of Sections 9.4 and 14.2--14.4, the test-optional figures of Section 2.6.1, the semesters of Section 6.4.1, the reliability figure of Section 9.3.1 and the time effects of Section 9.3.4 are now labelled estimates or unsourced. If the author has sources, they can replace the labels. Also unsourced and not changed: the SAT's criterion validity "in recent meta-analyses" (Section 2.5.2).

Chapter 14 (held back). It was held back because its point estimates were unsourced and its compound total contradicted its own table. After item 17, every point value is labelled an estimate and says where the standard-deviation effects come from, and the compound total is consistent with the table (the rows overlap, so the compound is below their sum). The chapter has no figure placeholder, its one footnote has a marker, and the checker finds nothing in it. Putting it online would also resolve the two "Chapter 14" cross-references of Chapter 2.

## Cross-volume repairs (2026-11-26)

These apply the findings for this volume in the cross-volume survey of 2026-11-26 (Volume 9, and the series-wide patterns X1, X2, X3, X4, X5, X6 and S1), with the author's decisions on the items marked [AUTHOR] (rules G1 to G14). Each anchor was matched against the text as committed in bb4c0f8. No figure line, caption, or heading placed after a figure was edited.

1. **E1 (X4), `part_i/ch01_gpa_trap.md`, Section 1.5.** "the Scalar Irrecoverability Theorem, proved in *Geometric Reasoning* (Ch. 13)" now reads "stated as a conditional theorem in *Geometric Reasoning*, Theorem 13.1 (Chapter 13; restated in that book's Section 10.7)". *Geometric Reasoning* tags the theorem "[Conditional Theorem.]" (Section 13.6), and its Section 10.7 restates it. Rule G10 gives the form of the citation.

2. **E2, `part_iii/ch08_grading_moral_injury.md`, chapter head.** "the Moral Injury Accumulation Theorem from Geometric Medicine (Ch. 13--15)" now reads "the Moral Injury Accumulation Theorem, Geometric Medicine's Theorem 13.1 (Ch. 13)". The theorem is Theorem 13.1 of *Geometric Medicine*, in its Chapter 13. (The survey also noted that Chapter 14 of that volume was held back; it is now published, but the theorem is still in Chapter 13.)

3. **E3, same file, Section 8.1.** "In *Geometric Medicine*, moral injury is defined as the permanent alteration of the clinician's heuristic function by forced boundary crossings on the clinical decision complex" now reads "... is defined as a forced crossing of a moral boundary on the clinical decision complex (that book's Definition 13.1), and its accumulation is held to alter the clinician's heuristic function, irreversibly above a threshold (that book's Theorem 13.1)". Checked against *Geometric Medicine*, Definition 13.1 ("Moral Injury as Forced Boundary Crossing"), Theorem 13.1, and Section 13.7 (the theorem states that the alteration is irreversible above a clinician-specific threshold).

4. **E4, `part_iii/ch09_gauge_invariance.md`, Section 9.1.** "The Bias Invariance Principle (BIP) from *Geometric Reasoning* (Ch. 11)" now reads "The Bond Invariance Principle (BIP) from *Geometric Reasoning* (Ch. 8)". *Geometric Reasoning* states the Bond Invariance Principle in Section 8.2; Chapter 11 is on alignment.

5. **E5, `part_iii/ch12_ai_education.md`, footnote 1.** "is an instantiation of the general No Escape Theorem, *Geometric Ethics*, Theorem 18.1 (Bond, 2026b, Ch. 18), a conditional theorem there, which states, on its four requirements, that AI systems operating within a geometric ethical framework cannot escape the framework's structural constraints" now reads "is an analogue of the No Escape Theorem of *Geometric Ethics*, Theorem 18.1 (Bond, 2026b, Ch. 18), conditional there on four requirements. It borrows the name, not the mechanism." Theorem 12.1 rests on the manifold's prerequisite topology and on scalar irrecoverability; Theorem 18.1 of *Geometric Ethics* on canonicalization, grounded evaluation, audit and external verification. [AUTHOR], rule G10.

6. **E6 (X5), `part_iv/ch13_educational_bond_index.md`, footnote 1.** The survey of 2026-11-26 (item 16 above) had already cited the clinical Bond Index, *Geometric Ethics* Definition 21.10, and added that the Bond Index of *Geometric Ethics* (Ch. 18) is a different quantity; the footnote has a marker after Definition 13.1. The footnote now also cites *Geometric Medicine* (Bond, 2026h, Ch. 12), which develops the clinical Bond Index under the same name. The name is kept. [AUTHOR], rule G4.

7. **E7, `part_v/ch17_feedback_general_theory.md`, footnote 1.** "is described in *Geometric Reasoning* (Bond, 2026c, Ch. 16) and in the Series Outlines document" now reads "is described in the Series Outlines document (`SERIES_OUTLINES.md`, item 9, in the geometric-reasoning repository)". Chapter 16 of *Geometric Reasoning* does not describe the protocol; `SERIES_OUTLINES.md` does ("9. What the domain teaches the general theory (feedback to the parent)").

8. **E8, `part_v/ch18_open_questions.md`, footnote 1.** Already applied in the survey (item 19 above: Ch. 29, "Open Problems"). No change.

9. **E9 (X1).** *Geometric Methods in Computational Modeling* now reads *Geometric Methods: Computational Modeling* in `appendices/appendix_a_math.md`, the table of Appendix D (Section D.6), the README, `front_matter.md` (Series Foreword) and `backmatter/bibliography.md` (2026a).

10. **E10 (X2, X3), README, series table.** *Geometric Ethics* "Published (v1.23)" now reads "Published (v1.29)". The rows for *Geometric Economics*, *Geometric Communication* and *Geometric Medicine* take the build configuration's subtitles ("Decision Manifolds, Equilibria, and the Geometry of Markets"; "Language, Signal, and the Topology of Meaning"; "Clinical Reasoning, Triage, and the Ethics of Allocation"). A row for *Geometric Observation* (Volume 14) is added with "Draft": its README gives no status word and its Chapters 20 to 23 are outlines. The table has fourteen rows in series order; the other status words are unchanged. This README has no series map. [AUTHOR] parts decided by rules G7 (subtitles) and G8 (the Observation row).

11. **S1, README, license section.** "Every claim in this series carries a status label, such as `[proved]`, `[posited]` or `[open]`, graded against a claim ledger" now reads "Claims in this series carry status labels, such as `[proved]`, `[posited]` or `[open]` or a volume's own tags, graded against a claim ledger where the volume keeps one". This volume keeps no claim ledger and tags with its own labels. [AUTHOR], rule G8.

12. **Unpublished files (X6).** The Series Foreword already gives *Geometric Ethics* as Book 2 and *Geometric Reasoning* as Book 3 (item 22 above). The bibliography gives no book numbers, its subtitles are the build configuration's, and its entries match every key the text uses: 2026a Methods; 2026b Ethics (Chapters 12, 13 and 18, Appendix D); 2026c Reasoning (Chapters 5 and 7, Appendix D); 2026d to 2026h Economics, Law, Cognition, Communication and Medicine (Appendix D, and Chapter 13 for 2026h). Only the Methods title (item 9) was changed.

Lapsed: **E11**, the references to Chapter 14 in Chapters 1 and 2 while it was held back. Chapter 14 is now published (rule G6).

Not applied: no finding of this volume.

Figures and captions: none is made stale. `tools/figs_all.py` places a figure before the heading of Section 12.3, which is unchanged.

Mechanical check: `series_check.py` (erisml-lib) on this clone, with its temporary build: before these repairs 0 hard defects, after them 0 hard defects; KaTeX 1,093 snippets, 0 failures; 23 pages, no broken internal link. The references added here name the work next to the number ("*Geometric Reasoning*, Theorem 13.1", "Geometric Medicine's Theorem 13.1", "that book's Definition 13.1"), the form the checker reads as a reference to another work.
