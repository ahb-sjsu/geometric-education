# Appendix C: Assessment Gauge Invariance Test Battery

---

This appendix provides a practical instrument for testing the gauge invariance of educational assessments. The battery is designed for adoption by assessment designers, institutional researchers, and accreditation bodies.

## C.1 Purpose

The Assessment Gauge Invariance Test Battery (AGITB) determines whether an educational assessment is gauge-invariant --- whether the measured learner state is independent of who administers the test, in what format, in what language, at what time, and in what context. Assessments that fail gauge invariance measure the instrument as well as the student.

## C.2 Structure

The battery consists of five parallel assessments of the same content, each varying one gauge transformation while holding the others constant.

### C.2.1 Test 1: Examiner Invariance

**Design.** The same student work (essays, problem solutions, projects) is graded independently by two or more qualified examiners using the same rubric.

**Measure.** Inter-rater reliability (Cohen's kappa or intraclass correlation coefficient).

**Threshold.** $\kappa \geq 0.80$ or ICC $\geq 0.85$ indicates acceptable examiner invariance. Below these thresholds, the assessment is examiner-variant: the grade depends on who reads the work.

**Action if failed.** Improve rubric specificity, provide calibration training for graders, or switch to machine-scored items.

### C.2.2 Test 2: Format Invariance

**Design.** Administer the same content assessment to the same students in two or more formats: (a) selected response (multiple choice), (b) constructed response (free response), (c) performance task, (d) oral examination. Counterbalance order to control for practice effects.

**Measure.** Within-student cross-format correlation and mean score difference. Compute format effect size: $d_{\text{format}} = (\bar{X}_{\text{format A}} - \bar{X}_{\text{format B}}) / s_{\text{pooled}}$.

**Threshold.** $|d_{\text{format}}| < 0.20$ (small effect) indicates acceptable format invariance. Above 0.20, the assessment is format-variant: different formats measure different aspects of the learner state.

**Action if failed.** Report scores separately by format, or redesign the assessment to include multiple formats and compute an invariant composite.

### C.2.3 Test 3: Language Invariance

**Design.** For bilingual or multilingual students, administer the same content assessment in two languages (the student's strongest language and the assessment's standard language). Counterbalance order.

**Measure.** Within-student cross-language correlation and mean score difference. Compute language effect size: $d_{\text{language}} = (\bar{X}_{\text{L1}} - \bar{X}_{\text{L2}}) / s_{\text{pooled}}$.

**Threshold.** $|d_{\text{language}}| < 0.20$ for content assessments (mathematics, science). Above 0.20, the assessment measures language proficiency in addition to content understanding.

**Action if failed.** Provide assessment in the student's strongest language, or provide linguistic accommodations (glossaries, extended time, bilingual dictionaries).

### C.2.4 Test 4: Time Invariance

**Design.** Administer the same assessment (parallel form to control for item memory) at two different times: (a) morning vs. afternoon, (b) beginning vs. end of semester. Use within-student comparison.

**Measure.** Within-student test-retest reliability and mean score difference. Compute time effect size: $d_{\text{time}} = (\bar{X}_{\text{time A}} - \bar{X}_{\text{time B}}) / s_{\text{pooled}}$.

**Threshold.** $|d_{\text{time}}| < 0.15$ indicates acceptable time invariance. Above 0.15, the assessment is time-variant.

**Action if failed.** Provide flexible testing windows. Use power tests (untimed) rather than speed tests (timed). Allow students to choose testing time.

### C.2.5 Test 5: Context Invariance

**Design.** Administer the same assessment under two conditions: (a) high-stakes (described as "this test counts toward your grade") and (b) low-stakes (described as "this is a diagnostic exercise, not graded"). Use between-subjects design to avoid expectation carryover.

**Measure.** Between-groups effect size: $d_{\text{context}} = (\bar{X}_{\text{high-stakes}} - \bar{X}_{\text{low-stakes}}) / s_{\text{pooled}}$, stratified by demographic group to detect stereotype threat effects.

**Threshold.** $|d_{\text{context}}| < 0.20$ overall, and $|d_{\text{context}}| < 0.30$ for any demographic subgroup. Above these thresholds, the assessment is context-variant.

**Action if failed.** Reduce stakes (use portfolio-based assessment, multiple low-stakes assessments rather than single high-stakes exams). Minimize identity salience in testing environments.

## C.3 Composite Gauge Invariance Score

The overall gauge invariance of an assessment is summarized by the composite gauge invariance score:

$$\text{GIS} = 1 - \frac{1}{5}\sum_{k=1}^{5} \min(d_k / d_{\text{threshold},k}, \; 1.0)$$

where $d_k$ is the effect size for gauge transformation $k$ and $d_{\text{threshold},k}$ is the threshold for that transformation. GIS ranges from 0 (maximally gauge-variant) to 1 (perfectly gauge-invariant).

- GIS $\geq 0.80$: Assessment is adequately gauge-invariant for most purposes.
- GIS $0.60$--$0.80$: Assessment has moderate gauge violations; use with caution for high-stakes decisions.
- GIS $< 0.60$: Assessment has substantial gauge violations; not recommended for consequential decisions.

## C.4 Reporting Template

For each assessment evaluated with the AGITB, report:

| Gauge Transformation | Effect Size $d_k$ | Threshold | Pass/Fail | Action |
|---------------------|-------------------|-----------|-----------|--------|
| Examiner | | 0.80 (kappa) | | |
| Format | | 0.20 (Cohen's d) | | |
| Language | | 0.20 (Cohen's d) | | |
| Time | | 0.15 (Cohen's d) | | |
| Context | | 0.20 (Cohen's d) | | |
| **Composite GIS** | | **0.80** | | |

## C.5 Implementation Notes

- **Sample size.** Each test requires at least 50 students for adequate power to detect medium effect sizes. Test 3 (language) requires bilingual students and may have smaller available samples.
- **Ethics.** The AGITB involves administering multiple assessments to the same students, which imposes additional testing burden. IRB review is recommended. Low-stakes conditions should be genuinely low-stakes.
- **Frequency.** The AGITB should be administered at least once for each new assessment instrument and re-administered when the instrument or population changes significantly.

---

*The AGITB is designed for independent adoption. No license is required. Assessment designers who use the battery are encouraged to publish their results to build a comparative database of gauge invariance across instruments and institutions.*
