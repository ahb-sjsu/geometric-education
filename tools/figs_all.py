"""Figures for Geometric Education, Chapters 1 to 13 and 15 to 17 (2026-11-26).

Chapter 14 is not published and Chapter 18 has no figure. Alex and Ethan are composite
students: every figure drawn from their numbers says "illustrative". The studies of
Sections 13.5 and 16.4 are hypothetical and are labelled so. No figure uses a number on the
"Unresolved" list of CORRECTIONS-2026-11-26.md.
"""

import heapq
import itertools
import math

from figkit import BORDER, BOX, CRITICAL, GRID, INK, INK2, INK3, SERIES, SURFACE, Axes, Canvas, legend, reg

CH = {
    1: "manuscript/part_i/ch01_gpa_trap.md",
    2: "manuscript/part_i/ch02_testing_industrial_complex.md",
    3: "manuscript/part_i/ch03_history.md",
    4: "manuscript/part_ii/ch04_learner_manifold.md",
    5: "manuscript/part_ii/ch05_assessment_contraction.md",
    6: "manuscript/part_ii/ch06_teaching_geodesic.md",
    7: "manuscript/part_ii/ch07_curriculum_pathfinding.md",
    8: "manuscript/part_iii/ch08_grading_moral_injury.md",
    9: "manuscript/part_iii/ch09_gauge_invariance.md",
    10: "manuscript/part_iii/ch10_personalized_learning.md",
    11: "manuscript/part_iii/ch11_transfer_learning.md",
    12: "manuscript/part_iii/ch12_ai_education.md",
    13: "manuscript/part_iv/ch13_educational_bond_index.md",
    15: "manuscript/part_iv/ch15_geometry_opportunity.md",
    16: "manuscript/part_v/ch16_measuring_manifold.md",
    17: "manuscript/part_v/ch17_feedback_general_theory.md",
}

DIMS = ["d1 domain knowledge", "d2 procedural skill", "d3 metacognition", "d4 motivation", "d5 transfer",
        "d6 creativity"]

# Printed vectors. Section 1.3 (entry) and Section 5.4.1 (after four years).
ALEX0 = (0.45, 0.85, 0.70, 0.80, 0.75, 0.65)
ETHAN0 = (0.80, 0.50, 0.40, 0.55, 0.40, 0.35)
ALEX4 = (0.70, 0.90, 0.80, 0.75, 0.85, 0.70)
ETHAN4 = (0.90, 0.55, 0.40, 0.50, 0.40, 0.30)
W_GPA = (0.60, 0.25, 0.05, 0.05, 0.03, 0.02)   # Section 1.3
W_SAT = (0.70, 0.15, 0.05, 0.05, 0.03, 0.02)   # Section 2.1.3


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(a):
    return math.sqrt(dot(a, a))


# The corrected values of CORRECTIONS-2026-11-26.md, recomputed from the printed vectors.
DIST = norm([a - b for a, b in zip(ALEX0, ETHAN0)])
G_ALEX, G_ETHAN = dot(W_GPA, ALEX0), dot(W_GPA, ETHAN0)
N_ALEX4, N_ETHAN4 = norm(ALEX4), norm(ETHAN4)
assert abs(DIST ** 2 - 0.61) < 1e-9 and f"{DIST:.2f}" == "0.78"
assert abs(G_ALEX - 0.593) < 1e-9 and abs(G_ETHAN - 0.6715) < 1e-9      # the chapter prints 0.593 and 0.671
assert abs(G_ETHAN - 0.671) < 6e-4 and abs((0.671 - 0.593) - 0.078) < 1e-12
assert abs(N_ALEX4 ** 2 - 3.715) < 1e-9 and f"{N_ALEX4:.2f}" == "1.93"
assert abs(N_ETHAN4 ** 2 - 1.7725) < 1e-9 and f"{N_ETHAN4:.2f}" == "1.33"
assert abs(sum(W_GPA) - 1) < 1e-12 and abs(sum(W_SAT) - 1) < 1e-12


def poly(c, pts, fill, opacity=0.15, stroke="none", width=1.5, dash=None):
    d = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
    da = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<polygon points="{d}" fill="{fill}" fill-opacity="{opacity}" stroke="{stroke}" stroke-width="{width}" '
          f'stroke-linejoin="round"{da}/>')


def frame(c, x, y, w, h, stroke=BORDER, fill="none", opacity=1.0, dash=None, r=6, width=1):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{r}" fill="{fill}" '
          f'fill-opacity="{opacity}" stroke="{stroke}" stroke-width="{width}"{da}/>')


def ring(c, x, y, r=4.5, stroke=INK2):
    c.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{SURFACE}" stroke="{stroke}" stroke-width="1.8"/>')


def note(c, s, y=None):
    c.text(16, (y if y is not None else c.h - 10), s, 10.5, "start", INK3, italic=True)


# ------------------------------------------------------------------ chapter 1
def fig_01_1():
    p = reg(CH[1], "1.1",
            "The 3.5 Decomposition, drawn from the two learner vectors of Section 1.3; Alex and Ethan are "
            "illustrative composite students. Each axis of the radar plot is one of the six dimensions, from 0 at "
            "the centre to 1 at the rim. The two shapes are nearly complementary, and the two states are 0.78 "
            "apart in six dimensions. The illustrative linear weighting G of Section 1.3 places them 0.078 apart "
            "(0.593 and 0.671), and both transcripts read 3.5.",
            "## 1.4 What the Contraction Destroys")
    c = Canvas(720, 440, "Two profiles of different shape, one number on the transcript")
    cx, cy, R = 220, 238, 128
    ang = [math.radians(-90 + 60 * i) for i in range(6)]
    for rr in (0.25, 0.5, 0.75, 1.0):
        poly(c, [(cx + R * rr * math.cos(a), cy + R * rr * math.sin(a)) for a in ang], "none", 0, GRID, 1)
    for a in ang:
        c.line(cx, cy, cx + R * math.cos(a), cy + R * math.sin(a), GRID, 1)
    for vec, col, name in ((ETHAN0, SERIES[1], "Ethan"), (ALEX0, SERIES[0], "Alex")):
        pts = [(cx + R * v * math.cos(a), cy + R * v * math.sin(a)) for v, a in zip(vec, ang)]
        poly(c, pts, col, 0.16, col, 2)
        for (x, y), v, d in zip(pts, vec, DIMS):
            c.dot(x, y, col, 3.5, title=f"{name}, {d}: {v:.2f}")
    for rr in (0.5, 1.0):
        am, rm = math.radians(-120), R * rr * math.cos(math.radians(30))
        c.text(cx + rm * math.cos(am) - 5, cy + rm * math.sin(am) - 3, f"{rr:g}", 9.5, "end", INK3)
    labs = [(0, -12, "middle"), (10, 0, "start"), (10, 8, "start"), (0, 20, "middle"), (-10, 8, "end"), (-10, 0, "end")]
    short = ["d1 domain knowledge", "d2 procedural skill", "d3 metacognition", "d4 motivation", "d5 transfer",
             "d6 creativity"]
    for a, (dx, dy, anc), s in zip(ang, labs, short):
        c.text(cx + R * math.cos(a) + dx, cy + R * math.sin(a) + dy + 4, s, 11, anc, INK2)
    legend(c, 60, 52, [("Alex", SERIES[0]), ("Ethan", SERIES[1])])
    # right panel: the two separations on one scale
    x0, w = 476, 220
    c.text(x0, 92, "In six dimensions", 12, "start", INK, "600")
    c.hrect(x0, 102, w * DIST, 16, SERIES[2], title=f"distance between the two states {DIST:.2f}")
    c.text(x0 + w * DIST + 8, 114, "0.78", 11, "start", INK)
    c.text(x0, 136, "distance between the two states", 10.5, "start", INK2)
    c.text(x0, 180, "After the contraction G", 12, "start", INK, "600")
    c.hrect(x0, 190, w * 0.078, 16, SERIES[2], title="separation of the two projected values 0.078")
    c.text(x0 + w * 0.078 + 8, 202, "0.078", 11, "start", INK)
    c.text(x0, 224, "separation of the two projected values", 10.5, "start", INK2)
    ly = 290
    c.line(x0, ly, x0 + w, ly, INK3, 1.5)
    for v in (0, 0.5, 1):
        c.line(x0 + w * v, ly - 4, x0 + w * v, ly + 4, INK3, 1.5)
        c.text(x0 + w * v, ly + 18, f"{v:g}", 10.5, "middle", INK2)
    c.dot(x0 + w * G_ALEX, ly, SERIES[0], 4, title="G(Alex) = 0.593")
    c.dot(x0 + w * 0.671, ly, SERIES[1], 4, title="G(Ethan) = 0.671")
    c.text(x0 + w * G_ALEX - 8, ly - 12, "Alex 0.593", 10.5, "end", INK)
    c.text(x0 + w * 0.671 + 8, ly - 12, "Ethan 0.671", 10.5, "start", INK)
    c.text(x0, ly + 40, "the line of G, same scale as the bars", 10.5, "start", INK2)
    c.text(x0, 372, "Both transcripts read GPA 3.5", 12, "start", INK, "600")
    note(c, "illustrative composite students; vectors and weights from Section 1.3")
    c.save(p)


def fig_01_2():
    p = reg(CH[1], "1.2",
            "Where the projected value comes from, for the illustrative weighting G of Section 1.3. The top bar is the "
            "weight on each dimension. The two lower bars split G for Alex (0.593) and for Ethan (0.671) into the "
            "six products of weight and coordinate. Domain knowledge and procedural skill supply almost all of each "
            "total, and the four remaining dimensions, where the two illustrative students differ most, supply little.",
            "### 1.4.2 Symmetry Structure: What Transformations Preserve")
    c = Canvas(720, 340, "Four of the six dimensions barely reach the projected value")
    x0, w = 150, 500
    rows = [("weights of G", W_GPA, "1.00"),
            ("Alex", tuple(a * b for a, b in zip(W_GPA, ALEX0)), "0.593"),
            ("Ethan", tuple(a * b for a, b in zip(W_GPA, ETHAN0)), "0.671")]
    printed = {"Alex": (0.270, 0.213, 0.035, 0.040, 0.023, 0.013), "Ethan": (0.480, 0.125, 0.020, 0.028, 0.012, 0.007)}
    for name, vals in printed.items():
        mine = rows[1][1] if name == "Alex" else rows[2][1]
        assert all(abs(a - b) < 6e-4 for a, b in zip(mine, vals))
    for v in (0, 0.25, 0.5, 0.75, 1.0):
        c.line(x0 + w * v, 76, x0 + w * v, 268, GRID, 1)
        c.text(x0 + w * v, 286, f"{v:g}", 11, "middle", INK2)
    for r, (name, vals, total) in enumerate(rows):
        y = 92 + 62 * r
        c.text(x0 - 12, y + 17, name, 12, "end", INK, "600" if r else "normal")
        acc = 0.0
        for j, v in enumerate(vals):
            xa, xb = x0 + w * acc, x0 + w * (acc + v)
            c.add(f'<rect x="{xa + 1:.2f}" y="{y:.2f}" width="{max(xb - xa - 2, 0.6):.2f}" height="26" rx="2" '
                  f'fill="{SERIES[j]}"><title>{name}, {DIMS[j]}: {v:.3f}</title></rect>')
            if v >= 0.1:
                shown = f"{v:.2f}" if r == 0 else f"{printed[name][j]:.3f}"
                c.text((xa + xb) / 2, y + 17, shown, 10.5, "middle", SURFACE, "600")
            acc += v
        c.text(x0 + w * acc + 8, y + 17, ("sum " if r == 0 else "G = ") + total, 11, "start", INK)
    c.text(x0 + w / 2, 306, "weight (top bar); weight × coordinate (lower bars)", 11.5, "middle", INK2)
    legend(c, x0, 56, [(f"d{j + 1}", SERIES[j]) for j in range(6)])
    note(c, "illustrative composite students; Section 1.3")
    c.save(p)


# ------------------------------------------------------------------ chapter 2
def fig_02_1():
    w1, w2 = W_SAT[0], W_SAT[1]
    wn = math.hypot(w1, w2)
    u = (w1 / wn, w2 / wn)
    start, dx = (0.42, 0.30), (0.20, 0.26)
    s = dx[0] * u[0] + dx[1] * u[1]
    par = (s * u[0], s * u[1])
    perp = (dx[0] - par[0], dx[1] - par[1])
    assert abs(perp[0] * w1 + perp[1] * w2) < 1e-12
    p = reg(CH[2], "2.1",
            "The projection geometry of Section 2.1.3. Left: the weight vector the chapter posits for the SAT. "
            "Right: the plane of d1 and d2 with the other four dimensions held fixed, where the thin lines are "
            "sets of equal score for the weights 0.70 and 0.15. A change in the learner state (the one drawn is "
            "illustrative) splits into a part along the weight direction, which changes the score, and a part "
            "along a line of equal score, which does not.",
            "### 2.2.2 The Equity Dimension")
    c = Canvas(720, 400, "The score reads one direction; movement across it is invisible")
    ax = Axes(c, 60, 70, 250, 250, (0, 6), (0, 0.8), [], [0, 0.2, 0.4, 0.6, 0.8], "", "weight in the SAT projection")
    for i, v in enumerate(W_SAT):
        x = ax.X(i + 0.5) - 12
        c.rect(x, ax.Y(v), 24, ax.Y(0) - ax.Y(v), SERIES[0], title=f"{DIMS[i]}: weight {v:.2f}")
        c.text(x + 12, ax.Y(v) - 6, f"{v:.2f}", 10.5, "middle", INK)
        c.text(x + 12, ax.Y(0) + 16, f"d{i + 1}", 11, "middle", INK2)
    c.text(60 + 125, 356, "dimension of the learner state", 11.5, "middle", INK2)
    bx = Axes(c, 420, 70, 250, 250, (0, 1), (0, 1), [0, 0.5, 1], [0, 0.5, 1], "d1 domain knowledge", "d2 procedural skill")
    c.line(420, 70, 420, 320, GRID, 1)
    for k in range(1, 8):
        cval = 0.1 * k
        pts = []
        for d2 in (0.0, 1.0):
            d1 = (cval - w2 * d2) / w1
            pts.append((d1, d2))
        (xa, ya), (xb, yb) = pts
        if xb < 0:
            ya2 = (cval - 0) / w2
            xb, yb = 0.0, ya2
        if xa > 1:
            continue
        c.line(bx.X(xa), bx.Y(ya), bx.X(xb), bx.Y(yb), "#3d5a78", 1.2)
    P = lambda q: (bx.X(q[0]), bx.Y(q[1]))
    a0 = P(start)
    a1 = P((start[0] + par[0], start[1] + par[1]))
    a2 = P((start[0] + dx[0], start[1] + dx[1]))
    c.arrow(a0[0], a0[1], a2[0], a2[1], INK, 2)
    c.arrow(a0[0], a0[1], a1[0], a1[1], SERIES[1], 2.5)
    c.arrow(a1[0], a1[1], a2[0], a2[1], SERIES[2], 2.5)
    c.dot(a0[0], a0[1], INK, 3.5)
    c.text(a0[0] - 8, a0[1] - 34, "change in", 10.5, "end", INK)
    c.text(a0[0] - 8, a0[1] - 21, "learner state", 10.5, "end", INK)
    legend(c, 420, 52, [("changes the score", SERIES[1])])
    legend(c, 560, 52, [("does not", SERIES[2])])
    c.text(668, 88, "lines of", 10.5, "end", INK3, italic=True)
    c.text(668, 101, "equal score", 10.5, "end", INK3, italic=True)
    note(c, "weights from Section 2.1.3; the displacement is illustrative, drawn with equal scales on both axes")
    c.save(p)


# ------------------------------------------------------------------ chapter 3
def fig_03_1():
    # Section 3.9.1 table, in order of date. (name, date, scored low, scored high, named, scalability)
    eras = [("Socratic", "400 BCE", 6, 6, None, "none (1:1)"),
            ("Medieval", "500 CE", 3, 4, None, "low (1:few)"),
            ("Prussian", "1800", 1, 2, None, "moderate"),
            ("Bloom", "1956", 1, 1, 6, "high"),
            ("Scantron", "1972", 1, 1, None, "very high"),
            ("Gardner", "1983", 1, 1, 8, "high")]
    p = reg(CH[3], "3.1",
            "The trade-off of Section 3.9.1, with the rows of the chapter's table put in order of date. Solid "
            "bars are the number of dimensions the assessment scores, as the table gives it (a lighter top marks "
            "a range, and 'all 6' is drawn as 6); dashed outlines are dimensions a tradition named and did not "
            "score. The line under each era is the scalability the table assigns. These are the chapter's "
            "characterisations, not measurements.",
            "## 3.10 The Standards Movement: Institutionalizing the Contraction (1990s--2000s)")
    c = Canvas(720, 420, "As assessment scaled up, the dimensions it scored fell to one")
    ax = Axes(c, 70, 64, 620, 240, (0, 6), (0, 8.6), [], [0, 2, 4, 6, 8], "", "dimensions")
    for i, (name, date, lo, hi, named, scal) in enumerate(eras):
        xm = ax.X(i + 0.5)
        if named:
            frame(c, xm - 16, ax.Y(named), 32, ax.Y(0) - ax.Y(named), INK3, dash="4 3", r=3, width=1.3)
            c.text(xm, ax.Y(named) - 6, f"{named} named", 10.5, "middle", INK2)
        if hi > lo:
            c.rect(xm - 12, ax.Y(hi), 24, ax.Y(0) - ax.Y(hi), SERIES[0], opacity=0.4, title=f"{name}: up to {hi}")
            c.rect(xm - 12, ax.Y(lo), 24, ax.Y(0) - ax.Y(lo), SERIES[0], 0, title=f"{name}: at least {lo}")
            lab = f"{lo} to {hi}"
        else:
            c.rect(xm - 12, ax.Y(hi), 24, ax.Y(0) - ax.Y(hi), SERIES[0], title=f"{name}: {hi} scored")
            lab = f"{hi}"
        if named:
            c.text(xm + 22, ax.Y(hi) + 4, f"{lab} scored", 10.5, "start", INK)
        else:
            c.text(xm, ax.Y(hi) - 6, lab, 10.5, "middle", INK)
        c.text(xm, ax.Y(0) + 17, name, 11.5, "middle", INK, "600")
        c.text(xm, ax.Y(0) + 32, date, 10.5, "middle", INK2)
        c.text(xm, ax.Y(0) + 56, scal, 10.5, "middle", INK2)
    c.text(62, ax.Y(0) + 56, "scales:", 10.5, "end", INK3, italic=True)
    legend(c, 70, 50, [("dimensions scored", SERIES[0])])
    c.line(236, 46, 262, 46, INK3, 1.3, dash="4 3")
    c.text(268, 51, "dimensions named, not scored", 11.5, "start", INK2)
    note(c, "from the table of Section 3.9.1; characterisations the chapter makes, not measured values")
    c.save(p)


def fig_03_2():
    p = reg(CH[3], "3.2",
            "The example of Section 3.7.2. Two students perform at 0.50 on domain knowledge when working alone, so a "
            "scalar assessment gives both the same value. With support, Student A reaches 0.70 and Student B reaches "
            "0.55. The band between the two marks is the zone of proximal development, which the scalar does not "
            "record. The horizontal axis is performance on d1, from 0 to 1.",
            "## 3.8 Freire's Critical Pedagogy: The Political Geometry (1968)")
    c = Canvas(720, 300, "Same score alone, different reach with support")
    ax = Axes(c, 150, 70, 500, 150, (0, 1), (0, 2), [0, 0.25, 0.5, 0.75, 1.0], [], "performance on d1 (domain knowledge)", "")
    for v in (0, 0.25, 0.5, 0.75, 1.0):
        c.line(ax.X(v), 70, ax.X(v), 220, GRID, 1)
    for i, (name, alone, helped) in enumerate((("Student A", 0.50, 0.70), ("Student B", 0.50, 0.55))):
        y = 112 + 66 * i
        c.text(138, y + 4, name, 12, "end", INK, "600")
        c.add(f'<rect x="{ax.X(alone):.2f}" y="{y - 11:.2f}" width="{ax.X(helped) - ax.X(alone):.2f}" height="22" rx="4" '
              f'fill="{SERIES[1]}" fill-opacity="0.35"><title>{name}: zone from {alone} to {helped}</title></rect>')
        c.dot(ax.X(alone), y, SERIES[0], 5, title=f"{name} alone {alone}")
        c.dot(ax.X(helped), y, SERIES[1], 5, title=f"{name} with support {helped}")
        c.text(ax.X(alone) - 11, y + 4, f"{alone:.2f}", 11, "end", INK)
        c.text(ax.X(helped) + 11, y + 4, f"{helped:.2f}", 11, "start", INK)
    legend(c, 150, 52, [("alone", SERIES[0]), ("with support", SERIES[1])])
    c.text(650, 56, "band: zone of proximal development", 10.5, "end", INK3, italic=True)
    note(c, "values from Section 3.7.2")
    c.save(p)


# ------------------------------------------------------------------ chapter 4
def fig_04_1():
    scen = [("1  novel engineering problem", (1, 2, 5, 6)),
            ("2  sees a gap, seeks help", (1, 3, 4)),
            ("3  original integrative project", (1, 2, 5, 6)),
            ("4  persists through a problem set", (2, 3, 4)),
            ("5  explains by cross-domain analogy", (1, 2, 3, 5)),
            ("6  surprising creative solution", (2, 5, 6))]
    assert min(len(s) for _, s in scen) >= 3                      # "at least three dimensions"
    assert set().union(*[set(s) for _, s in scen]) == {1, 2, 3, 4, 5, 6}  # every dimension is used
    col = [sum(1 for _, s in scen if d in s) for d in range(1, 7)]
    p = reg(CH[4], "4.1",
            "The six scenarios of Proposition 4.1 against the six dimensions. A filled mark means the proposition "
            "lists that dimension as activated. Every scenario activates at least three dimensions, and each dimension "
            "is activated by at least two scenarios, so no dimension can be dropped without losing part of some "
            "scenario. The counts at the right and at the bottom are row and column totals.",
            "## 4.4 The Learner Metric")
    c = Canvas(720, 400, "Every scenario needs three dimensions or more; none is unused")
    x0, y0, dx, dy = 300, 96, 58, 38
    short = ["d1", "d2", "d3", "d4", "d5", "d6"]
    names = ["knowledge", "procedure", "metacog.", "motivation", "transfer", "creativity"]
    for j in range(6):
        c.text(x0 + dx * j, 62, short[j], 12, "middle", INK, "600")
        c.text(x0 + dx * j, 77, names[j], 10, "middle", INK2)
    for i, (name, s) in enumerate(scen):
        y = y0 + dy * i + 12
        c.line(40, y + 19, x0 + dx * 5 + 70, y + 19, GRID, 1)
        c.text(40, y + 4, name, 11.5, "start", INK2)
        for j in range(6):
            x = x0 + dx * j
            if j + 1 in s:
                c.dot(x, y, SERIES[0], 7, title=f"scenario {i + 1} activates {DIMS[j]}")
            else:
                c.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2" fill="{GRID}" stroke="{INK3}" stroke-width="0.6"/>')
        c.text(x0 + dx * 5 + 52, y + 4, str(len(s)), 12, "middle", INK, "600")
    yb = y0 + dy * 6 + 14
    for j in range(6):
        c.text(x0 + dx * j, yb, str(col[j]), 12, "middle", INK, "600")
    c.text(40, yb, "scenarios that activate the dimension", 11, "start", INK3, italic=True)
    c.text(x0 + dx * 5 + 52, 77, "count", 10, "middle", INK3, italic=True)
    note(c, "Proposition 4.1; scenarios 1 and 3 list the same four dimensions")
    c.save(p)


def fig_04_2():
    p = reg(CH[4], "4.2",
            "A schematic of Definition 4.4 and Section 4.8, in two of the six dimensions, with illustrative "
            "thresholds and no data. A goal region is the set of states at or above a minimum vector, so it is a "
            "corner-shaped region and not a point, and different stakeholders set different minimum vectors. "
            "Graduate P lies in the university's region and outside the employer's and the student's own. "
            "Graduate Q lies in all three.",
            "## 4.9 The Heuristic Field")
    c = Canvas(720, 420, "A goal is a region, and each stakeholder draws a different one")
    ax = Axes(c, 90, 56, 300, 300, (0, 1), (0, 1), [0, 0.5, 1], [0, 0.5, 1], "", "one dimension of the learner state")
    c.text(240, 390, "another dimension of the learner state", 11.5, "middle", INK2)
    c.line(90, 56, 90, 356, GRID, 1)
    corners = [("university: degree requirements", (0.58, 0.28), SERIES[0]),
               ("employer: job competencies", (0.36, 0.62), SERIES[1]),
               ("student: own objectives", (0.50, 0.48), SERIES[2])]
    for name, (a, b), col in corners:
        frame(c, ax.X(a), ax.Y(1), ax.X(1) - ax.X(a), ax.Y(b) - ax.Y(1), col, col, 0.13, r=0, width=1.6)
        c.dot(ax.X(a), ax.Y(b), col, 3.5, title=f"minimum vector, {name}")
    P, Q = (0.86, 0.38), (0.72, 0.82)
    for (a, b), lab in ((P, "P"), (Q, "Q")):
        c.dot(ax.X(a), ax.Y(b), INK, 5)
        c.text(ax.X(a) + 10, ax.Y(b) + 4, lab, 12, "start", INK, "600")
    for (a, b), lab in ((P, "P"), (Q, "Q")):
        inside = [n.split(":")[0] for n, (ca, cb), _ in corners if a >= ca and b >= cb]
        assert len(inside) == (1 if lab == "P" else 3)
    x0 = 450
    c.text(x0, 92, "Goal region = all states at or", 11.5, "start", INK2)
    c.text(x0, 108, "above a minimum vector (the corner)", 11.5, "start", INK2)
    for i, (name, _, col) in enumerate(corners):
        c.add(f'<rect x="{x0}" y="{133 + 26 * i}" width="12" height="12" rx="3" fill="{col}"/>')
        c.text(x0 + 18, 143 + 26 * i, name, 11.5, "start", INK2)
    c.text(x0, 236, "P", 12, "start", INK, "600")
    c.text(x0 + 16, 236, "degree earned; outside the", 11.5, "start", INK2)
    c.text(x0 + 16, 252, "other two regions", 11.5, "start", INK2)
    c.text(x0, 282, "Q", 12, "start", INK, "600")
    c.text(x0 + 16, 282, "inside all three regions", 11.5, "start", INK2)
    note(c, "schematic; two of six dimensions; thresholds are illustrative")
    c.save(p)


# ------------------------------------------------------------------ chapter 5
def fig_05_1():
    w1, w2 = W_GPA[0], W_GPA[1]
    X, Y = (0.50, 0.40), (0.35, 0.76)
    cx_, cy_ = w1 * X[0] + w2 * X[1], w1 * Y[0] + w2 * Y[1]
    assert abs(cx_ - cy_) < 1e-12 and abs(cx_ - 0.40) < 1e-12
    p = reg(CH[5], "5.1",
            "Theorems 5.1 and 5.2 in the smallest case, two dimensions and one score. The plane is d1 against d2 with "
            "the other four dimensions held fixed, and the lines are level sets of a linear score with the weights "
            "0.60 and 0.25 of Section 1.3. The states x and y are different points on one level set, so the score sends "
            "both to the same value c. No rule that starts from c alone can return x for one student and y for the "
            "other.",
            "## 5.3 Irrecoverability")
    c = Canvas(720, 400, "A whole line of different states arrives at one score")
    ax = Axes(c, 80, 62, 270, 270, (0, 1), (0, 1), [0, 0.5, 1], [0, 0.5, 1], "d1 domain knowledge", "d2 procedural skill")
    c.line(80, 62, 80, 332, GRID, 1)

    def seg(cval):
        pts = []
        for d2 in (0.0, 1.0):
            d1 = (cval - w2 * d2) / w1
            if 0 <= d1 <= 1:
                pts.append((d1, d2))
        for d1 in (0.0, 1.0):
            d2 = (cval - w1 * d1) / w2
            if 0 < d2 < 1:
                pts.append((d1, d2))
        return sorted(pts)

    for k in range(1, 9):
        cval = 0.1 * k
        s = seg(cval)
        if len(s) == 2:
            hot = abs(cval - 0.4) < 1e-9
            c.line(ax.X(s[0][0]), ax.Y(s[0][1]), ax.X(s[1][0]), ax.Y(s[1][1]), SERIES[0] if hot else "#3d5a78",
                   2.5 if hot else 1.2)
    # the score axis at the right
    sx, top, bot = 560, 62, 332
    c.line(sx, top, sx, bot, INK3, 1.5)
    SY = lambda v: bot - (bot - top) * v / 0.85
    for v in (0, 0.2, 0.4, 0.6, 0.8):
        c.line(sx - 4, SY(v), sx + 4, SY(v), INK3, 1.5)
        c.text(sx + 12, SY(v) + 4, f"{v:g}", 11, "start", INK2)
    c.text(sx, top - 12, "score", 11.5, "middle", INK2)
    for q, lab, off in ((X, "x", (10, 16)), (Y, "y", (10, -8))):
        px, py = ax.X(q[0]), ax.Y(q[1])
        c.arrow(px, py, sx - 9, SY(0.4), INK3, 1.2)
    for q, lab, off in ((X, "x", (10, 16)), (Y, "y", (10, -8))):
        px, py = ax.X(q[0]), ax.Y(q[1])
        c.dot(px, py, SERIES[1], 5, title=f"state {lab} = ({q[0]}, {q[1]}), score 0.40")
        c.text(px + off[0], py + off[1], lab, 13, "start", INK, "600", italic=True)
    c.dot(sx, SY(0.4), SERIES[0], 5, title="c = 0.40")
    c.text(sx + 34, SY(0.4) + 4, "= c, for x and for y", 11.5, "start", INK)
    c.text(sx - 2, 366, "one number for every state on the line", 11, "middle", INK2)
    c.text(350, 54, "lines: level sets of the score", 10.5, "end", INK3, italic=True)
    note(c, "two of six dimensions; weights 0.60 and 0.25 from Section 1.3; x = (0.50, 0.40), y = (0.35, 0.76)")
    c.save(p)


def fig_05_2():
    p = reg(CH[5], "5.2",
            "The two trajectories of Section 5.4.1, dimension by dimension, for Alex and Ethan, who are "
            "illustrative composite students. Open marks are the states at entry (Section 1.3) and filled marks "
            "are the states after four years. Ethan moves mainly along d1 and Alex moves on five of the six "
            "dimensions. The chapter gives Ethan a GPA of 3.7 and Alex 3.2, and the norms of the four-year states "
            "are 1.33 and 1.93.",
            "## 5.5 Corollaries")
    c = Canvas(720, 400, "The higher GPA goes with the state that moved on one dimension")
    panels = [("Alex", ALEX0, ALEX4, "GPA 3.2, norm of the state 1.93", 150, SERIES[0]),
              ("Ethan", ETHAN0, ETHAN4, "GPA 3.7, norm of the state 1.33", 446, SERIES[1])]
    for name, v0, v4, sub, x0, col in panels:
        w = 190
        c.text(x0, 78, name, 13, "start", INK, "600")
        c.text(x0 + 46, 78, sub, 11, "start", INK2)
        for v in (0, 0.5, 1.0):
            c.line(x0 + w * v, 92, x0 + w * v, 322, GRID, 1)
            c.text(x0 + w * v, 340, f"{v:g}", 11, "middle", INK2)
        for i in range(6):
            y = 112 + 38 * i
            xa, xb = x0 + w * v0[i], x0 + w * v4[i]
            if abs(xb - xa) > 0.5:
                c.line(xa, y, xb, y, col, 2.5)
            ring(c, xa, y, 4.5, INK2)
            c.dot(xb, y, col, 4.5, title=f"{name}, {DIMS[i]}: {v0[i]:.2f} to {v4[i]:.2f}")
            c.text(x0 + w + 12, y + 4, f"{v0[i]:.2f} → {v4[i]:.2f}", 10.5, "start", INK)
    for i in range(6):
        c.text(134, 116 + 38 * i, DIMS[i], 11, "end", INK2)
    ring(c, 156, 47, 4.5, INK2)
    c.text(168, 51, "at entry", 11.5, "start", INK2)
    c.add(f'<circle cx="246" cy="47" r="4.5" fill="{INK2}"/>')
    c.text(258, 51, "after four years", 11.5, "start", INK2)
    c.text(360, 362, "coordinate on each dimension, 0 to 1", 11.5, "middle", INK2)
    note(c, "illustrative composite students; vectors from Sections 1.3 and 5.4.1")
    c.save(p)


# ------------------------------------------------------------------ chapter 6
def _grid_search(W, H, walls, start, goal, guided):
    h = (lambda q: abs(q[0] - goal[0]) + abs(q[1] - goal[1])) if guided else (lambda q: 0)
    cnt = itertools.count()
    openq = [(h(start), 0, next(cnt), start)]
    g = {start: 0}
    parent = {}
    closed = []
    seen = set()
    while openq:
        f, negg, _, q = heapq.heappop(openq)
        if q in seen:
            continue
        seen.add(q)
        if q == goal:
            break
        closed.append(q)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n = (q[0] + dx, q[1] + dy)
            if not (0 <= n[0] < W and 0 <= n[1] < H) or n in walls:
                continue
            ng = g[q] + 1
            if ng < g.get(n, 1e9):
                g[n] = ng
                parent[n] = q
                heapq.heappush(openq, (ng + h(n), -ng if guided else 0, next(cnt), n))
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return closed, path[::-1]


def fig_06_1():
    W, H = 21, 13
    walls = {(10, y) for y in range(2, 11)} | {(x, 2) for x in range(6, 10)} | {(x, 10) for x in range(6, 10)}
    start, goal = (2, 6), (18, 6)
    blind, pb = _grid_search(W, H, walls, start, goal, False)
    guide, pg = _grid_search(W, H, walls, start, goal, True)
    free = W * H - len(walls)
    assert len(pb) == len(pg) and len(blind) > len(guide)
    p = reg(CH[6], "6.1",
            f"The search-theory fact that Section 6.4.1 cites, on a small grid with a wall; a schematic, with "
            f"counts that belong to this grid and are not educational data. Both searches find a path of the same "
            f"length, {len(pb) - 1} steps. With no estimate of the remaining cost (h = 0) the search examines "
            f"{len(blind)} of the {free} open cells before it reaches the goal. Guided by an estimate of the "
            f"remaining cost (here the grid distance to the goal with the wall ignored) it examines {len(guide)}.",
            "## 6.5 The Four Heuristic Failure Modes in Teaching")
    c = Canvas(720, 400, "Without an estimate of what remains, the search looks everywhere")
    cs = 14
    for (x0, title, closed, path, col) in ((48, "No heuristic: h = 0", blind, pb, SERIES[1]),
                                           (378, "Guided by an estimate of the remaining cost", guide, pg, SERIES[0])):
        y0 = 92
        c.text(x0, 78, title, 12, "start", INK, "600")
        cl = set(closed)
        for x in range(W):
            for y in range(H):
                q = (x, y)
                fill, op = (INK3, 0.9) if q in walls else ((col, 0.5) if q in cl else (GRID, 0.6))
                c.add(f'<rect x="{x0 + cs * x + 0.75:.2f}" y="{y0 + cs * y + 0.75:.2f}" width="{cs - 1.5}" '
                      f'height="{cs - 1.5}" rx="2" fill="{fill}" fill-opacity="{op}"/>')
        c.polyline([(x0 + cs * (x + 0.5), y0 + cs * (y + 0.5)) for x, y in path], INK, 2)
        c.dot(x0 + cs * (start[0] + 0.5), y0 + cs * (start[1] + 0.5), INK, 4, title="start")
        c.dot(x0 + cs * (goal[0] + 0.5), y0 + cs * (goal[1] + 0.5), CRITICAL, 4, title="goal")
        c.text(x0, y0 + cs * H + 22, f"{len(closed)} of {free} open cells examined", 11.5, "start", INK)
        c.text(x0, y0 + cs * H + 39, f"path found: {len(path) - 1} steps", 11.5, "start", INK2)
    y = 352
    c.add(f'<rect x="48" y="{y - 9}" width="12" height="12" rx="3" fill="{INK3}"/>')
    c.text(66, y + 1, "wall", 11.5, "start", INK2)
    c.add(f'<circle cx="118" cy="{y - 3}" r="4" fill="{INK}"/>')
    c.text(128, y + 1, "start", 11.5, "start", INK2)
    c.add(f'<circle cx="184" cy="{y - 3}" r="4" fill="{CRITICAL}"/>')
    c.text(194, y + 1, "goal", 11.5, "start", INK2)
    c.line(244, y - 3, 266, y - 3, INK, 2)
    c.text(274, y + 1, "path found", 11.5, "start", INK2)
    c.text(368, y + 1, "shaded cells: examined before the goal was reached", 11.5, "start", INK2)
    note(c, "schematic of Section 6.4.1; unit cost per step on a 21 by 13 grid")
    c.save(p)


# ------------------------------------------------------------------ chapter 7
def fig_07_1():
    N, G0, thr = 6, 1.5, 2.0
    grades = [(4.0, SERIES[0]), (3.0, SERIES[1]), (2.5, SERIES[2])]

    def cum(g, n):
        return (N * G0 + n * g) / (N + n)

    def first(g):
        return next(n for n in range(1, 40) if cum(g, n) >= thr - 1e-12)

    assert [first(g) for g, _ in grades] == [2, 3, 6]
    p = reg(CH[7], "7.1",
            "The recursive GPA trap of Section 7.7, computed from the cumulative average with illustrative "
            "starting values. A student has six semesters at an average of 1.5 and needs 2.0, the graduation "
            "minimum the section uses as its example. The curves give the cumulative GPA after further semesters "
            "of equal weight at 4.0, 3.0 and 2.5. The threshold is reached after 2, 3 and 6 semesters, and each "
            "added semester moves the average less than the one before.",
            "## 7.8 Alex and the Advisor")
    c = Canvas(720, 400, "A cumulative average is slow to move, and slower each semester")
    ax = Axes(c, 70, 60, 520, 270, (0, 8), (1.4, 3.0), list(range(9)), [1.5, 2.0, 2.5, 3.0],
              "further semesters at the stated grade average", "cumulative GPA")
    c.line(ax.x0, ax.Y(thr), ax.x0 + ax.w, ax.Y(thr), INK3, 1.5, dash="4 4")
    c.text(ax.x0 + ax.w, ax.Y(thr) + 16, "required 2.0", 10.5, "end", INK2, italic=True)
    for g, col in grades:
        pts = [(ax.X(n), ax.Y(cum(g, n))) for n in range(9)]
        c.polyline(pts, col, 2)
        nf = first(g)
        for n in range(9):
            c.dot(pts[n][0], pts[n][1], col, 5.5 if n == nf else 3.5, title=f"at {g}: after {n} semesters {cum(g, n):.2f}")
        c.text(pts[-1][0] + 10, pts[-1][1] + 4, f"all at {g:.1f}: {cum(g, 8):.2f}", 11, "start", INK2)
    c.text(ax.X(0) + 8, ax.Y(1.5) + 18, "six semesters at 1.5", 10.5, "start", INK2)
    c.text(70, 46, "large marks: first semester at or above 2.0", 11, "start", INK3, italic=True)
    note(c, "cumulative GPA = (6 × 1.5 + n × g) / (6 + n); illustrative starting values")
    c.save(p)


# ------------------------------------------------------------------ chapter 8
def fig_08_1():
    p = reg(CH[8], "8.1",
            "A schematic of Definition 8.1, in two of the six dimensions, with illustrative positions. The line "
            "is the set of learner states that receive one grade, and the open mark is the state an observer "
            "would infer from that grade alone, written ψ(G(x)) in the definition. Three students receive the "
            "grade. The moral injury increment the definition assigns to each grading event is the length of the "
            "arrow from the inferred state to the student's actual state, so it is smallest for student 1 and "
            "largest for student 3.",
            "## 8.3 The Moral Injury Accumulation Theorem for Education")
    c = Canvas(720, 380, "The increment is the gap between the state and what the grade says")
    a, b = (120, 320), (430, 70)

    def at(t):
        return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)

    c.line(a[0], a[1], b[0], b[1], SERIES[0], 2.5)
    c.text(b[0] + 10, b[1] + 2, "states that receive the same grade", 11, "start", INK2)
    psi = at(0.36)
    studs = [(0.43, "student 1"), (0.62, "student 2"), (0.92, "student 3")]
    for t, name in studs:
        q = at(t)
        off = 16 + 14 * studs.index((t, name))
        nx, ny = 250 / 398.2, 310 / 398.2  # unit normal to the line, pointing down-right
        s0 = (psi[0] + nx * off, psi[1] + ny * off)
        s1 = (q[0] + nx * off, q[1] + ny * off)
        c.line(psi[0], psi[1], s0[0], s0[1], GRID, 1)
        c.line(q[0], q[1], s1[0], s1[1], GRID, 1)
        c.arrow(s0[0], s0[1], s1[0], s1[1], SERIES[1], 2)
    for t, name in studs:
        q = at(t)
        c.dot(q[0], q[1], INK, 5, title=name)
        c.text(q[0] - 12, q[1] - 6, name, 11.5, "end", INK)
    ring(c, psi[0], psi[1], 6, INK)
    c.text(psi[0] - 14, psi[1] - 4, "ψ(G(x)): the state the", 11.5, "end", INK)
    c.text(psi[0] - 14, psi[1] + 11, "grade alone suggests", 11.5, "end", INK)
    x0 = 478
    c.text(x0, 150, "ΔMI = ‖ x − ψ(G(x)) ‖", 13, "start", INK, "600")
    c.text(x0, 172, "one arrow per graded student:", 11.5, "start", INK2)
    c.text(x0, 188, "the longer the arrow, the more", 11.5, "start", INK2)
    c.text(x0, 204, "the grade leaves out", 11.5, "start", INK2)
    c.add(f'<rect x="{x0}" y="226" width="12" height="12" rx="3" fill="{SERIES[1]}"/>')
    c.text(x0 + 18, 236, "increment for that student", 11.5, "start", INK2)
    c.text(x0, 270, "The career total of Theorem 8.1", 11.5, "start", INK2)
    c.text(x0, 286, "adds these over every student", 11.5, "start", INK2)
    c.text(x0, 302, "and every assessment event.", 11.5, "start", INK2)
    note(c, "schematic of Definition 8.1; two of six dimensions; positions are illustrative")
    c.save(p)


# ------------------------------------------------------------------ chapter 9
def fig_09_1():
    fmts = [("multiple choice", (1,)), ("free response", (1, 2)), ("oral examination", (1, 2, 3)),
            ("portfolio", (1, 2, 3, 4, 5, 6))]
    assert [len(s) for _, s in fmts] == [1, 2, 3, 6]
    p = reg(CH[9], "9.1",
            "The format swap of Section 9.3.2 as the chapter describes it; the cells restate the text and are not "
            "measurements. Each row is an assessment format and each column a dimension of the learner state. A "
            "filled cell means the chapter says that format projects onto that dimension. The same content read "
            "through a different format reaches a different set of dimensions, which is why the chapter posits "
            "that the score changes with the format.",
            "### 9.3.3 Language Swap")
    c = Canvas(720, 320, "Each format reads a different part of the same learner state")
    x0, y0, dx, dy = 220, 92, 66, 46
    names = ["knowledge", "procedure", "metacog.", "motivation", "transfer", "creativity"]
    for j in range(6):
        c.text(x0 + dx * j + 27, 62, f"d{j + 1}", 12, "middle", INK, "600")
        c.text(x0 + dx * j + 27, 77, names[j], 10, "middle", INK2)
    for i, (name, s) in enumerate(fmts):
        y = y0 + dy * i
        c.text(x0 - 16, y + 21, name, 12, "end", INK)
        for j in range(6):
            on = j + 1 in s
            frame(c, x0 + dx * j, y, 54, 32, SERIES[0] if on else BORDER, SERIES[0] if on else "none",
                  0.85 if on else 0, r=5)
        c.text(x0 + dx * 6 + 6, y + 21, f"{len(s)} of 6", 11.5, "start", INK2)
    c.text(x0 + dx * 6 + 6, 77, "reached", 10, "start", INK3, italic=True)
    note(c, "Section 9.3.2; the oral examination reaches d3 through the interaction, as the chapter puts it")
    c.save(p)


# ------------------------------------------------------------------ chapter 10
def _cheapest_path(cost, start, goal, nx, ny, hstep):
    moves = [(dx, dy) for dx in range(-5, 6) for dy in range(-5, 6) if (dx, dy) != (0, 0) and math.gcd(dx, dy) == 1]
    dist = {start: 0.0}
    parent = {}
    pq = [(0.0, start)]
    done = set()
    while pq:
        d, q = heapq.heappop(pq)
        if q in done:
            continue
        done.add(q)
        if q == goal:
            break
        for dx, dy in moves:
            n = (q[0] + dx, q[1] + dy)
            if not (0 <= n[0] < nx and 0 <= n[1] < ny):
                continue
            mean = sum(cost((q[0] + dx * f) * hstep, (q[1] + dy * f) * hstep) for f in (0.1, 0.3, 0.5, 0.7, 0.9)) / 5
            nd = d + mean * math.hypot(dx, dy) * hstep
            if nd < dist.get(n, 1e18):
                dist[n] = nd
                parent[n] = q
                heapq.heappush(pq, (nd, n))
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return [(x * hstep, y * hstep) for x, y in path[::-1]], dist[goal]


def fig_10_1():
    hstep, nx, ny = 0.1, 91, 51
    sx, sy, amp, edge = 1.7, 0.9, 6.0, 1.2

    def bump(cy):
        return lambda x, y: 1 + amp * math.exp(-(((x - 4.5) / sx) ** 2 + ((y - cy) / sy) ** 2) ** 2)

    costA, costB = bump(2.0), bump(3.0)       # A: spatial learner, formal route costly; B: the reverse
    start, goal = (8, 25), (82, 25)
    pathA, dA = _cheapest_path(costA, start, goal, nx, ny, hstep)
    pathB, dB = _cheapest_path(costB, start, goal, nx, ny, hstep)
    straight = lambda cost: sum(cost(0.8 + 0.1 * (i + 0.5), 2.5) * 0.1 for i in range(74))
    assert abs(dA - dB) < 1e-6 and straight(costA) > dA and straight(costB) > dB
    assert max(y for _, y in pathA) > 3.1 and min(y for _, y in pathB) < 1.9
    p = reg(CH[10], "10.1",
            "The two learners of Section 10.1.1 as a computed illustration with illustrative cost fields; start "
            "and goal are the same. The cost of each step is close to 1 outside the shaded regions and rises "
            "steeply inside them: the region through formal manipulation is costly for the spatial learner, and "
            "the region through geometric visualization is costly for the symbolic learner. The solid curves are "
            "the least-cost paths under the two cost fields. The dashed line is the single path a uniform metric "
            "assumes, and it is the least-cost path for neither learner.",
            "## 10.2 One-Size-Fits-All as the Uniform Metric Assumption")
    c = Canvas(720, 420, "Same start, same goal, different least-cost path for each learner")
    S, x0, yb = 60, 90, 372
    X = lambda x: x0 + S * x
    Y = lambda y: yb - S * y
    frame(c, X(0), Y(5), S * 9, S * 5, GRID, "none", r=4)
    c.ellipse(X(4.5), Y(2.0), S * sx * edge, S * sy * edge, 0, SERIES[0], SERIES[0], 1.5, 0.16, title="costly for the spatial learner")
    c.ellipse(X(4.5), Y(3.0), S * sx * edge, S * sy * edge, 0, SERIES[1], SERIES[1], 1.5, 0.16, title="costly for the symbolic learner")
    c.line(X(0.8), Y(2.5), X(8.2), Y(2.5), INK3, 1.5, dash="5 5")
    c.polyline([(X(x), Y(y)) for x, y in pathA], SERIES[0], 2.5, title="least-cost path, spatial learner")
    c.polyline([(X(x), Y(y)) for x, y in pathB], SERIES[1], 2.5, title="least-cost path, symbolic learner")
    c.dot(X(0.8), Y(2.5), INK, 5, title="start")
    c.dot(X(8.2), Y(2.5), INK, 5, title="goal")
    c.text(X(0.8), Y(2.5) + 22, "start", 11.5, "middle", INK)
    c.text(X(8.2), Y(2.5) + 22, "goal", 11.5, "middle", INK)
    c.text(X(4.5), Y(4.72), "geometric visualization: costly for the symbolic learner", 11, "middle", INK2)
    c.text(X(4.5), Y(0.2), "formal manipulation: costly for the spatial learner", 11, "middle", INK2)
    legend(c, 90, 52, [("spatial learner", SERIES[0]), ("symbolic learner", SERIES[1])])
    c.line(382, 48, 408, 48, INK3, 1.5, dash="5 5")
    c.text(416, 53, "the one path a uniform metric assumes", 11.5, "start", INK2)
    note(c, "computed illustration of Section 10.1.1; the cost fields are illustrative, not estimated from data")
    c.save(p)


# ------------------------------------------------------------------ chapter 11
def fig_11_1():
    lonB = math.radians(60)

    def transport(path, v):
        for q in path[1:]:
            d = dot(v, q)
            v = tuple(a - d * b for a, b in zip(v, q))
            n = norm(v)
            v = tuple(a / n for a in v)
        return v

    def meridian(lon, n=6000):
        return [(math.sin(t) * math.cos(lon), math.sin(t) * math.sin(lon), math.cos(t))
                for t in [math.pi / 2 * i / n for i in range(n + 1)]]

    def equator(l0, l1, n=6000):
        return [(math.cos(s), math.sin(s), 0.0) for s in [l0 + (l1 - l0) * i / n for i in range(n + 1)]]

    v0 = (1.0, 0.0, 0.0)
    r1 = meridian(lonB)
    r2a, r2b = meridian(0.0), equator(0.0, lonB)
    e1 = transport(r1, v0)
    e2 = transport(r2b, transport(r2a, v0))
    angle = math.degrees(math.acos(max(-1, min(1, dot(e1, e2)))))
    assert abs(angle - 60) < 0.01, angle
    p = reg(CH[11], "11.1",
            "Path dependence of parallel transport, the property Section 11.3 attributes to knowledge transfer, "
            "computed on a sphere that stands in for a curved learner manifold; a schematic, not a measurement of "
            "any learner. One vector starts at the top. Carried straight down one meridian (route 1) and carried "
            "down another meridian and then along the equator (route 2), it arrives at the same point turned by "
            "60 degrees, the angle between the meridians. On a flat surface the two arrivals would agree.",
            "## 11.4 Teaching for Transfer")
    c = Canvas(720, 420, "On a curved surface, what arrives depends on the route taken")
    view = (math.cos(math.radians(30)) , math.sin(math.radians(30)), 0.62)
    vn = norm(view)
    view = tuple(a / vn for a in view)
    xs = (-view[1], view[0], 0.0)
    xn = norm(xs)
    xs = tuple(a / xn for a in xs)
    ys = (view[1] * xs[2] - view[2] * xs[1], view[2] * xs[0] - view[0] * xs[2], view[0] * xs[1] - view[1] * xs[0])
    cx, cy, R = 230, 232, 158
    P = lambda q: (cx + R * dot(q, xs), cy - R * dot(q, ys))
    c.add(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{BOX}" fill-opacity="0.45" stroke="{BORDER}" stroke-width="1.2"/>')
    for lon in range(-60, 121, 30):
        pts = [P(q) for q in meridian(math.radians(lon), 60) if dot(q, view) > 0]
        if len(pts) > 1:
            c.polyline(pts, GRID, 1)
    eq = [P(q) for q in equator(math.radians(-60), math.radians(120), 120) if dot(q, view) > 0]
    c.polyline(eq, GRID, 1)
    c.polyline([P(q) for q in r1[::60]], SERIES[0], 2.5, title="route 1")
    c.polyline([P(q) for q in (r2a + r2b)[::60]], SERIES[1], 2.5, title="route 2")

    def vec(path, frac_list, col, v):
        n = len(path) - 1
        for f in frac_list:
            k = int(round(f * n))
            w = transport(path[:k + 1], v)
            q = path[k]
            a, b = P(q), P(tuple(q[i] + 0.3 * w[i] for i in range(3)))
            c.arrow(a[0], a[1], b[0], b[1], col, 2)
        return transport(path, v)

    vec(r1, (0.4, 0.75, 1.0), SERIES[0], v0)
    vmid = vec(r2a, (0.4, 0.75), SERIES[1], v0)
    vec(r2b, (0.0, 0.5, 1.0), SERIES[1], vmid)
    a, b = P(r1[0]), P(tuple(r1[0][i] + 0.3 * v0[i] for i in range(3)))
    c.arrow(a[0], a[1], b[0], b[1], INK, 2.5)
    for q, lab, off, anc in ((r1[0], "start", (10, -8), "start"), (r1[-1], "arrival", (14, 8), "start")):
        x, y = P(q)
        c.dot(x, y, INK, 4.5)
        c.text(x + off[0], y + off[1], lab, 12, anc, INK, "600")
    x0 = 450
    c.add(f'<rect x="{x0}" y="100" width="12" height="12" rx="3" fill="{SERIES[0]}"/>')
    c.text(x0 + 18, 110, "route 1: straight down one meridian", 11.5, "start", INK2)
    c.add(f'<rect x="{x0}" y="130" width="12" height="12" rx="3" fill="{SERIES[1]}"/>')
    c.text(x0 + 18, 140, "route 2: down another meridian,", 11.5, "start", INK2)
    c.text(x0 + 18, 156, "then along the equator", 11.5, "start", INK2)
    c.text(x0, 200, "The arrows are one vector, carried", 11.5, "start", INK2)
    c.text(x0, 216, "without turning it relative to the", 11.5, "start", INK2)
    c.text(x0, 232, "surface.", 11.5, "start", INK2)
    c.text(x0, 268, "At arrival the two copies differ", 11.5, "start", INK)
    c.text(x0, 284, f"by {angle:.0f}°, the angle between the", 11.5, "start", INK)
    c.text(x0, 300, "two meridians.", 11.5, "start", INK)
    note(c, "schematic; exact on the unit sphere; no learner data")
    c.save(p)


def fig_11_2():
    m, k = 1.0, 1.0
    ccrit = 2 * math.sqrt(m * k)
    assert abs(ccrit ** 2 - 4 * m * k) < 1e-12

    def x(cdamp, t):
        if cdamp == 0:
            return math.cos(t)
        disc = cdamp * cdamp - 4 * m * k
        if abs(disc) < 1e-12:
            r = -cdamp / (2 * m)
            return math.exp(r * t) * (1 - r * t)
        if disc < 0:
            om = math.sqrt(-disc) / (2 * m)
            a = cdamp / (2 * m)
            return math.exp(-a * t) * (math.cos(om * t) + a / om * math.sin(om * t))
        r1 = (-cdamp + math.sqrt(disc)) / (2 * m)
        r2 = (-cdamp - math.sqrt(disc)) / (2 * m)
        return (r2 * math.exp(r1 * t) - r1 * math.exp(r2 * t)) / (r2 - r1)

    cases = [(0.0, "c = 0: undamped", INK3), (0.3, "c = 0.3: underdamped", SERIES[0]),
             (2.0, "c = 2: critical, c² = 4mk", SERIES[1]), (6.0, "c = 6: overdamped", SERIES[2])]
    for cd, _, _ in cases:
        assert abs(x(cd, 0) - 1) < 1e-12
        h = 1e-4   # the curve satisfies m x'' + c x' + k x = 0
        for t in (1.0, 4.0):
            xdd = (x(cd, t + h) - 2 * x(cd, t) + x(cd, t - h)) / h ** 2
            xd = (x(cd, t + h) - x(cd, t - h)) / (2 * h)
            assert abs(m * xdd + cd * xd + k * x(cd, t)) < 1e-5
    p = reg(CH[11], "11.2",
            "The equation Alex recognizes in Section 11.5, m x'' + c x' + k x = 0, solved for four illustrative "
            "values of the damping c with m = 1, k = 1, starting at x = 1 at rest. The horizontal axis is time "
            "and the vertical axis is displacement. With no damping the oscillation continues. Below the critical "
            "value c² = 4mk the motion oscillates and fades, at the critical value it returns without "
            "oscillating, and above it the return is slower.",
            "## Summary")
    c = Canvas(720, 400, "One equation, the regimes a mechanic finds by adding damping")
    ax = Axes(c, 70, 60, 470, 270, (0, 20), (-1.1, 1.1), [0, 5, 10, 15, 20], [-1, -0.5, 0, 0.5, 1], "time", "displacement x")
    ends = {0.0: -18, 0.3: 0, 2.0: 14, 6.0: -10}
    for cd, name, col in cases:
        pts = [(ax.X(t), ax.Y(x(cd, t))) for t in [20 * i / 400 for i in range(401)]]
        if cd == 0:
            for (x1, y1), (x2, y2) in zip(pts[:-1:2], pts[1::2]):
                c.line(x1, y1, x2, y2, col, 1.4)
        else:
            c.polyline(pts, col, 2.2, title=name)
    yl = 96
    for cd, name, col in cases:
        c.add(f'<rect x="556" y="{yl - 10}" width="12" height="12" rx="3" fill="{col}"/>')
        c.text(574, yl, name.split(": ")[0], 11.5, "start", INK, "600")
        c.text(574, yl + 15, name.split(": ")[1], 11, "start", INK2)
        yl += 46
    note(c, "computed from the equation of Section 11.5 with m = 1, k = 1, x(0) = 1, x'(0) = 0; illustrative values")
    c.save(p)


# ------------------------------------------------------------------ chapter 12
def fig_12_1():
    p = reg(CH[12], "12.1",
            "A schematic of Section 12.2.1 that restates the chapter's argument and reports no measurement. A "
            "human grader and an automated grader perform the same contraction of a six-dimensional learner state "
            "to one grade. In the chapter's account the human grader can feel the gap between the state and the "
            "grade, and in some teachers that discomfort becomes pressure to change the assessment. The automated "
            "grader produces the grade with no such signal, so the loop back to the assessment is absent.",
            "## 12.3 The No Escape Theorem for Educational AI")
    c = Canvas(720, 380, "Automated grading keeps the contraction and drops the signal")
    rows = [("Human grader", 92, True), ("Automated grader", 242, False)]
    for name, y, human in rows:
        c.text(24, y - 12, name, 12.5, "start", INK, "600")
        c.box(24, y, 150, 50, "learner state", "six dimensions")
        c.box(214, y, 130, 50, "grade", "one number")
        c.arrow(176, y + 25, 210, y + 25, INK2, 1.6)
        c.arrow(346, y + 25, 380, y + 25, INK2, 1.6)
        if human:
            c.box(384, y, 150, 50, "grader feels the gap", "moral injury", stroke=SERIES[1])
            c.box(574, y, 126, 50, "pressure to", "improve assessment", stroke=SERIES[1])
            c.arrow(536, y + 25, 570, y + 25, SERIES[1], 1.8)
            # the loop back to the grade
            c.line(637, y + 50, 637, y + 78, SERIES[1], 1.8)
            c.line(637, y + 78, 279, y + 78, SERIES[1], 1.8)
            c.arrow(279, y + 78, 279, y + 53, SERIES[1], 1.8)
            c.text(458, y + 94, "in some teachers: better assessments, comments, fuller reporting", 11, "middle", INK2)
        else:
            frame(c, 384, y, 150, 50, INK3, "none", dash="5 4")
            c.text(459, y + 22, "no signal", 12, "middle", INK2, "600")
            c.text(459, y + 38, "no discomfort", 10.5, "middle", INK3)
            frame(c, 574, y, 126, 50, INK3, "none", dash="5 4")
            c.text(637, y + 22, "no pressure", 12, "middle", INK2, "600")
            c.text(637, y + 38, "to change", 10.5, "middle", INK3)
            c.text(459, y + 76, "the same contraction, faster and at scale, with no loop back", 11, "middle", INK2)
    note(c, "schematic of Section 12.2.1")
    c.save(p)


# ------------------------------------------------------------------ chapter 13
def fig_13_1():
    p = reg(CH[13], "13.1",
            "A schematic of the quantity inside the Educational Bond Index (Definition 13.1 and Section 13.3.3), "
            "with illustrative paths and no data. The geodesic is the least-cost path from the student's starting "
            "state to the goal region, and the other curve is the path the institution's policy leaves open. The "
            "learning deviation is the distance between the two paths added up along the way, drawn as the shaded "
            "area. The index is its average over a student population.",
            "## 13.2 What the Bond Index Detects")
    c = Canvas(720, 400, "Learning deviation: the gap between the open path and the geodesic")
    a, b = (90, 310), (560, 150)

    def geo(t):
        x = a[0] + (b[0] - a[0]) * t
        y = a[1] + (b[1] - a[1]) * t - 26 * math.sin(math.pi * t)
        return x, y

    def act(t):
        gx, gy = geo(t)
        off = 92 * math.sin(math.pi * t) ** 0.8 + 16 * math.sin(3 * math.pi * t) * math.sin(math.pi * t)
        return gx + 0.32 * off, gy + off * 0.95

    ts = [i / 100 for i in range(101)]
    G = [geo(t) for t in ts]
    A = [act(t) for t in ts]
    poly(c, G + A[::-1], SERIES[1], 0.16)
    for t in (0.15, 0.3, 0.45, 0.6, 0.75, 0.88):
        g, q = geo(t), act(t)
        c.line(g[0], g[1], q[0], q[1], SERIES[1], 1.2, dash="3 3")
    c.ellipse(b[0] + 52, b[1] - 6, 70, 52, -15, SERIES[2], SERIES[2], 1.5, 0.14, title="goal region")
    c.text(b[0] + 58, b[1] - 12, "goal region", 11.5, "middle", INK)
    c.polyline(G, SERIES[0], 2.5, title="geodesic")
    c.polyline(A, SERIES[1], 2.5, title="policy-constrained path")
    c.dot(a[0], a[1], INK, 5, title="starting state")
    c.text(a[0] - 4, a[1] + 50, "student's starting state", 11.5, "start", INK)
    g5 = geo(0.5)
    c.text(g5[0] - 20, g5[1] - 14, "geodesic", 11.5, "end", INK)
    q5 = act(0.62)
    c.text(q5[0] + 14, q5[1] + 22, "path open under the policy", 11.5, "start", INK)
    c.text(90, 88, "LD = distance between the two paths, added along the way (shaded)", 11.5, "start", INK2)
    c.text(90, 106, "BI = average LD over the student population", 11.5, "start", INK2)
    legend(c, 90, 52, [("geodesic", SERIES[0]), ("policy-constrained path", SERIES[1])])
    note(c, "schematic of Definition 13.1; illustrative paths, no data")
    c.save(p)


def fig_13_2():
    shares = [("heuristic", 45), ("metric", 30), ("access", 15), ("residual", 10)]
    assert sum(v for _, v in shares) == 100
    p = reg(CH[13], "13.2",
            "The hypothetical scenario of Section 13.5, in which no study has been run and every number is invented "
            "for illustration. Top: in the scenario the Bond Index of first-generation students is 2.1 times that of "
            "continuing-generation students, drawn with the continuing-generation value as 1. Bottom: the shares "
            "into which the scenario decomposes the index, 45 percent heuristic, 30 percent metric, 15 percent access "
            "and 10 percent residual.",
            "## Summary")
    c = Canvas(720, 380, "Hypothetical scenario: what a Bond Index report would look like")
    x0, w = 210, 400
    c.text(24, 70, "Bond Index, relative (hypothetical)", 12, "start", INK, "600")
    for v in (0, 0.5, 1, 1.5, 2, 2.5):
        c.line(x0 + w * v / 2.5, 84, x0 + w * v / 2.5, 158, GRID, 1)
        c.text(x0 + w * v / 2.5, 174, f"{v:g}", 11, "middle", INK2)
    for i, (name, v) in enumerate((("continuing-generation", 1.0), ("first-generation", 2.1))):
        y = 92 + 34 * i
        c.text(x0 - 12, y + 15, name, 11.5, "end", INK2)
        c.hrect(x0, y, w * v / 2.5, 22, SERIES[0] if i == 0 else SERIES[1], title=f"{name}: {v} (hypothetical)")
        c.text(x0 + w * v / 2.5 + 8, y + 15, "1 (reference)" if i == 0 else "2.1 ×", 11, "start", INK)
    c.text(24, 226, "Shares of the index in the scenario (hypothetical)", 12, "start", INK, "600")
    acc = 0
    for j, (name, v) in enumerate(shares):
        xa, xb = x0 + w * acc / 100, x0 + w * (acc + v) / 100
        c.add(f'<rect x="{xa + 1:.2f}" y="246" width="{xb - xa - 2:.2f}" height="30" rx="3" fill="{SERIES[j + 2]}">'
              f'<title>{name}: {v} percent (hypothetical)</title></rect>')
        c.text((xa + xb) / 2, 266, f"{v}%", 11.5, "middle", SURFACE, "600")
        c.text((xa + xb) / 2, 296, name, 11, "middle", INK2)
        acc += v
    c.text(x0 - 12, 266, "first-generation", 11.5, "end", INK2)
    frame(c, 24, 318, 672, 30, CRITICAL, "none", r=6, width=1.2)
    c.text(360, 338, "Illustrative only: Section 13.5 is a hypothetical scenario and no such study has been run.", 11.5,
           "middle", INK)
    note(c, "numbers from the hypothetical scenario of Section 13.5")
    c.save(p)


# ------------------------------------------------------------------ chapter 15
def fig_15_1():
    nmax = math.sqrt(6)
    p = reg(CH[15], "15.1",
            "The two readings of the same graduation in Section 15.7, for Alex and Ethan, who are illustrative "
            "composite students. Left: the grade point averages the chapter gives, 3.2 and 3.7, on the 4.0 scale. "
            "Right: the distance of each four-year state from the origin of the six-dimensional space, 1.93 and "
            "1.33, recomputed from the vectors printed in Section 5.4.1; the largest possible value is the square "
            "root of 6, about 2.45. The two readings order the two students oppositely.",
            "## Summary")
    assert abs(nmax - 2.449) < 1e-3
    c = Canvas(720, 380, "GPA and six-dimensional state order the two graduates oppositely")
    panels = [("Grade point average", 60, (0, 4.0), [0, 1, 2, 3, 4], (("Alex", 3.2), ("Ethan", 3.7)), "of 4.0"),
              ("Distance of the state from the origin", 400, (0, 2.6), [0, 0.5, 1, 1.5, 2, 2.5],
               (("Alex", N_ALEX4), ("Ethan", N_ETHAN4)), None)]
    for title, x0, ylim, ticks, vals, _ in panels:
        ax = Axes(c, x0 + 30, 96, 230, 210, (0, 2), ylim, [], ticks, "", "")
        c.text(x0 + 30, 78, title, 12, "start", INK, "600")
        for i, (name, v) in enumerate(vals):
            xm = ax.X(i + 0.5)
            c.rect(xm - 12, ax.Y(v), 24, ax.Y(0) - ax.Y(v), SERIES[i], title=f"{name}: {v:.2f}")
            c.text(xm, ax.Y(v) - 7, f"{v:.1f}" if ylim[1] == 4.0 else f"{v:.2f}", 11.5, "middle", INK, "600")
            c.text(xm, ax.Y(0) + 18, name, 12, "middle", INK2)
        if ylim[1] != 4.0:
            c.line(ax.x0, ax.Y(nmax), ax.x0 + ax.w, ax.Y(nmax), INK3, 1.5, dash="4 4")
            c.text(ax.x0 + ax.w, ax.Y(nmax) + 15, "largest possible, √6", 10.5, "end", INK2, italic=True)
    c.text(205, 344, "Ethan ranks first", 11.5, "middle", INK)
    c.text(545, 344, "Alex ranks first", 11.5, "middle", INK)
    note(c, "illustrative composite students; GPAs from Section 15.7, norms from the vectors of Section 5.4.1")
    c.save(p)


# ------------------------------------------------------------------ chapter 16
def fig_16_1():
    skills = ["P", "C1", "C2", "L", "Q"]
    prereq = {"C1": "P", "C2": "C1", "Q": "L"}   # pre-calculus < Calculus I < Calculus II; linear algebra < quantum mechanics
    states = []
    for r in range(6):
        for sub in itertools.combinations(skills, r):
            if all(prereq[s] in sub for s in sub if s in prereq):
                states.append(frozenset(sub))
    assert len(states) == 12 and 2 ** len(skills) == 32
    p = reg(CH[16], "16.1",
            "A small illustrative knowledge space of the kind Section 16.2.4 describes, built from two "
            "prerequisite chains the book uses as examples: pre-calculus before Calculus I before Calculus II, "
            "and linear algebra before quantum mechanics. Each box is a knowledge state, a set of mastered skills "
            "that contains the prerequisites of everything in it; of the 32 subsets of the five skills, 12 are "
            "states. A line joins two states that differ by one skill, and learning moves upward along the lines. "
            "The highlighted route is one of the possible orders.",
            "## 16.3 The Falsifiable Prediction Suite")
    c = Canvas(720, 460, "Prerequisites leave 12 states of 32, joined by single steps")
    cx, yb, dx, dy = 250, 404, 82, 62

    def pos(i, j):
        return cx + (i - j) * dx, yb - (i + j) * dy

    def lab(i, j):
        s = ["P", "C1", "C2"][:i] + ["L", "Q"][:j]
        return " ".join(s) if s else "∅"

    route = [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2)]
    redges = set(zip(route[:-1], route[1:]))
    n_edges = 0
    for i in range(4):
        for j in range(3):
            for (i2, j2) in ((i + 1, j), (i, j + 1)):
                if i2 <= 3 and j2 <= 2:
                    n_edges += 1
                    hot = ((i, j), (i2, j2)) in redges
                    (x1, y1), (x2, y2) = pos(i, j), pos(i2, j2)
                    c.line(x1, y1, x2, y2, SERIES[1] if hot else INK3, 2.5 if hot else 1.2, opacity=1 if hot else 0.7)
    assert n_edges == 17
    for i in range(4):
        for j in range(3):
            x, y = pos(i, j)
            hot = (i, j) in route
            frame(c, x - 38, y - 12, 76, 24, SERIES[1] if hot else BORDER, BOX, 1.0, r=5, width=1.6 if hot else 1)
            c.text(x, y + 4, lab(i, j), 11, "middle", INK, "600" if hot else "normal")
    x0 = 566
    for k, s in enumerate(["P   pre-calculus", "C1  Calculus I", "C2  Calculus II", "L   linear algebra",
                           "Q   quantum mechanics"]):
        c.text(x0, 96 + 18 * k, s.split()[0], 11.5, "start", INK, "600")
        c.text(x0 + 26, 96 + 18 * k, " ".join(s.split()[1:]), 11.5, "start", INK2)
    c.text(x0, 208, "Not states: C2 without", 11, "start", INK2)
    c.text(x0, 224, "C1, or Q without L", 11, "start", INK2)
    c.line(x0, 254, x0 + 24, 254, SERIES[1], 2.5)
    c.text(x0 + 32, 258, "one learning order", 11, "start", INK2)
    c.text(40, 78, "all five skills", 11, "start", INK3, italic=True)
    c.text(40, yb + 6, "nothing mastered yet", 11, "start", INK3, italic=True)
    note(c, "illustrative example; prerequisite pairs from Sections 4.7 and 7.2")
    c.save(p)


# ------------------------------------------------------------------ chapter 17
def fig_17_1():
    frac = lambda d, k=1: (d - k) / d
    assert abs(frac(6) - 5 / 6) < 1e-12 and frac(1) == 0
    p = reg(CH[17], "17.1",
            "The severity measure Section 17.4 proposes, Severity = Stakes × (d − k) / d, where d is the number "
            "of input dimensions and k the number the output keeps; it is a proposal of the chapter and has not "
            "been measured. Left: the fraction of dimensions lost, (d − k) / d, for a scalar output (k = 1), "
            "which is 0 for a one-dimensional input and 5/6 for the six-dimensional learner state. Right: the "
            "four cases the section lists, placed by stakes and by input dimensions, with the verdict the section "
            "gives each.",
            "## 17.5 The Developmental Dimension: Growing Manifolds")
    c = Canvas(720, 400, "Contraction is worst at high stakes with many dimensions lost")
    ax = Axes(c, 64, 70, 250, 250, (0.5, 12.5), (0, 1), [1, 2, 4, 6, 8, 10, 12], [0, 0.25, 0.5, 0.75, 1.0],
              "input dimensions d", "fraction of dimensions lost, k = 1")
    c.polyline([(ax.X(d), ax.Y(frac(d))) for d in range(1, 13)], SERIES[0], 2)
    for d in range(1, 13):
        c.dot(ax.X(d), ax.Y(frac(d)), CRITICAL if d == 6 else SERIES[0], 5.5 if d == 6 else 3.5,
              title=f"d = {d}: {frac(d):.3f}")
    c.text(ax.X(6) + 6, ax.Y(frac(6)) + 22, "d = 6: 5/6 lost", 11, "start", INK)
    c.text(ax.X(1) + 10, ax.Y(0) - 8, "d = 1: nothing lost", 11, "start", INK2)
    gx, gy, gw, gh = 416, 84, 138, 104
    cells = [(0, 0, "driver's license test", "appropriate", False), (1, 0, "SAT score", "catastrophic", True),
             (0, 1, "a homework problem", "harmless", False), (1, 1, "classroom discussion", "tolerable", False)]
    for i, j, ex, verdict, hot in cells:
        x, y = gx + (gw + 8) * i, gy + (gh + 8) * j
        frame(c, x, y, gw, gh, CRITICAL if hot else BORDER, BOX, 0.9 if hot else 0.55, r=6, width=1.8 if hot else 1)
        c.text(x + gw / 2, y + 44, verdict, 13, "middle", INK, "600")
        c.text(x + gw / 2, y + 64, ex, 11, "middle", INK2)
    c.text(gx + gw / 2, gy - 10, "few input dimensions", 11, "middle", INK2)
    c.text(gx + gw + 8 + gw / 2, gy - 10, "many input dimensions", 11, "middle", INK2)
    c.text(gx - 14, gy + gh / 2, "high stakes", 11, "middle", INK2, rotate=-90)
    c.text(gx - 14, gy + gh + 8 + gh / 2, "low stakes", 11, "middle", INK2, rotate=-90)
    c.text(gx + gw + 4, 338, "Severity = Stakes × (d − k) / d", 12, "middle", INK, "600")
    note(c, "formula and the four cases from Section 17.4; a proposed measure, not a measured one")
    c.save(p)
