# Exact Natarajan Dimension of the Natural PSL(2,q) Action

Research No.42, public preprint prepared as v1.0, 2026-10-27 (Japan).

Status: a user-supplied report of AI rechecking in another session of the same workflow reports MODEL/PROOF/COMPUTATION PASS.
This is not third-party independent confirmation or human peer review. The mathematical claim is unchanged from the audited candidate.
Novelty is INCONCLUSIVE; references remain PARTIAL. This is an unreviewed preprint. The statements below concern a
specific mathematical class, not unrestricted ARC tasks or their intended rules.

## 1. Model and candidate theorem

Let q be any prime power, let Omega = P^1(F_q) = F_q union {infinity}, and let
H_q consist of the permutations of Omega induced by PSL(2,q). Equivalently,
these are the fractional linear maps x -> (a*x+b)/(c*x+d) represented by
determinant-one matrices; projectively, an invertible matrix is eligible exactly
when its determinant is a nonzero square. In even characteristic all nonzero
elements are squares.

A set {x_1,...,x_m} is Natarajan-shattered if there are different labels
u_i != v_i at each point and all 2^m choices of these labels are realized by
members of H_q. Write N(q) for the largest m.

**Candidate theorem.**

| Prime power q | N(q) |
| --- | --- |
| 2 | 1 |
| 3, 4, 5, 7, 11 | 2 |
| Every other prime power | 3 |

For q >= 4, the usual teaching dimension is 3: three distinct correspondences
determine the map and two do not. This last fact is standard and is not the
claimed contribution. The candidate contribution is the displayed exact
Natarajan classification, subject to the prior-art qualifications below.

## 2. Elementary reductions

**Lemma 1 (disjoint output pairs).** In a class of injective maps, the label
pairs of a shattered set are pairwise disjoint. Otherwise the pattern choosing
the same label at two different inputs is not injective. Thus shattering m
points needs at least 2m available labels.

**Lemma 2 (upper bound).** N(q) <= 3. Two fractional linear maps agreeing on
three distinct inputs are identical. A hypothetical shattered set of size four
would have two realizers agreeing on three inputs and disagreeing on the fourth.

**Lemma 3 (small lower bound).** N(q) >= 2 for q >= 3. PSL(2,q) is 2-transitive
on the projective line, and the domain then has at least four labels. Choose
two disjoint label pairs and realize all four ordered choices.

Here is a direct proof of 2-transitivity, so this argument does not depend on a
classification theorem. Translations are represented by determinant-one
matrices, and x -> -1/x is also so represented. They make the action transitive.
The stabilizer of infinity contains all translations and is transitive on the
remaining points. This proves 2-transitivity.

For q=2, Lemma 1 rules out dimension 2 and any moved point gives dimension 1.
For q=3,4 the projective line has fewer than six labels, so Lemmas 1 and 3
give dimension 2. These observations settle q=2,3,4.

In particular, q=3 already supplies four labels on the projective line, so
the 2-transitivity argument of Lemma 3 applies without a separate exception.

## 3. A complete normalized cube criterion for odd q

Assume q is odd. A 3-cube can be normalized to have input points
(infinity,0,1), and its first output at each input equal to that input.
Indeed, compose all realizers on the left by the inverse of the all-zero
realizer. Next conjugate the action by the unique PGL(2,q) map sending the
three inputs to (infinity,0,1). This conjugation preserves PSL(2,q), since
PSL is the kernel of the projective determinant-square-class homomorphism.

By Lemma 1 the output pairs must now be

    {infinity,a}, {0,b}, {1,c},

where a,b,c,0,1 are five different finite field elements. Let chi be the
quadratic character, with chi(0)=0. Such a cube exists exactly when

    chi(c) = chi(1-b) = chi(c-b) = 1,                         (1)
    chi(a) = chi(a-1) = chi(a-b) = chi(a-c).                (2)

**Proof of the criterion.** A map fixing infinity and sending 0 to y and 1 to z
is x -> (z-y)*x+y. It is in PSL exactly when chi(z-y)=1. Applying this to the
four choices y in {0,b}, z in {1,c} gives (1), including chi(1)=1.

The unique projective map sending (infinity,0,1) to (a,y,z) can be represented by

    [ a*(z-y)    y*(a-z) ]
    [   z-y        a-z  ].

Its determinant is (a-y)*(a-z)*(z-y). Given (1), its square class is positive
exactly when chi(a-y)=chi(a-z). The four choices of y,z give precisely (2).
All factors here are nonzero by distinctness. This proves necessity and
sufficiency, including all eight patterns.

The triple-character invariant behind this calculation is known; in
particular, see Krcadinac, Pavcevic and Tabak (2023), Lemma 2.2. We do not
claim that invariant, the normalization method, or the determinant test as new.

## 4. Character sums used in the two cases

For a finite field of odd order,

    sum_x chi(x) = 0,
    sum_x chi(x)*chi(x-t) = -1   for t != 0.                (3)

For completeness, scale x by t to reduce the second assertion to t=1.
The number of pairs (x,y) with y^2=x*(x-1) is q plus the character sum.
Writing U=2*x-1 and V=2*y changes the equation to U^2-V^2=1.
The bijection (U-V,U+V)=(r,r^(-1)), r != 0, gives q-1 pairs.
Thus the character sum is -1. The first assertion follows by multiplying
the nonzero field elements by a nonsquare.

We use also chi(-1)=1 for q=1 mod 4 and -1 for q=3 mod 4, the elementary
square-class fact in a finite field. The Paley structures below and their
parameters are standard; their use is made explicit to avoid renaming them.

## 5. q = 1 mod 4

Make the Paley graph on F_q by joining x,y when chi(y-x)=1. It is undirected.
Take the vertices S that are nonneighbors of 0, i.e. chi(x)=-1. There are
m=(q-1)/2 such vertices. The graph induced on S is k-regular with
k=(q-1)/4.

To check this parameter directly, for x in S expand

    1/4 * sum_y (1-chi(y))*(1+chi(y-x)).

Equation (3) gives (q+1)/4. The y=0 summand is zero, while the y=x summand
equals 1/2 and must be removed, leaving (q-1)/4 actual neighbors in S.

If q>=13, then k>=3 and m=2*k. A C4-free graph has at most one common neighbor
for each pair of vertices, so

    m * binom(k,2) <= binom(m,2),
    k*(k-1) <= 2*k-1.

This is false for every integer k>=3. Thus the graph induced on S contains
a four-cycle (not necessarily induced). For q=9 it is a 2-regular simple
graph on four vertices, so it too is a four-cycle.

Write the four-cycle bipartition as {u,u'} and {v,v'}. Its four cross edges
are present. Use the affine change h(t)=(t-u)/(v-u). Its multiplier is a
square, so it preserves all relevant quadratic characters. Set

    a=h(0), b=h(u'), c=h(v').

The four cross edges give (1); all four cycle vertices were nonneighbors of
0, which gives (2) with common character -1. The five finite labels are
different. Therefore N(q)=3 for every q=1 mod 4 with q>=9.

For q=5, any a has only two vertices with chi(a-x)=1 and two with value -1.
It cannot have four distinct other vertices with a common value, as required
by (2). Hence N(5)=2.

## 6. q = 3 mod 4

Make the Paley tournament on F_q with arc x -> y when chi(y-x)=1. The cube
criterion (1)-(2) is equivalent to this tournament containing a transitive
five-vertex subtournament.

For the forward direction, (1) directs all four edges from the pair {0,b}
to the pair {1,c}. Each pair has its own internal order, so the four vertices
form a transitive tournament. Equation (2) makes a either a source or a sink
relative to all four, giving a transitive five-set.

Conversely, order a transitive five-set as t1 -> t2 -> t3 -> t4 -> t5. Take
a0=t5, the first pair {u,u'}={t1,t2}, and the second pair {v,v'}={t3,t4}.
The square affine normalization h(t)=(t-u)/(v-u) sends u to 0 and v to 1.
Put a=h(a0), b=h(u'), c=h(v'). The cross arcs give (1) and the common sink
gives (2). Thus the equivalence is in both directions.

Every pair of vertices in the Paley tournament has exactly (q-3)/4 common
outneighbors. For example, after a translation and scaling, expansion of
the two positive-character indicators uses (3). The sum over all x before
removing the endpoints is (q-1)/4; the endpoint contributions add to 1/2
because chi(-1)=-1. The result is (q-3)/4, independently of the direction
of the chosen pair.

For q=7,11 this number is respectively 1,2. The first two vertices of a
transitive five-set would have three common outneighbors, which is impossible.
So N(7)=N(11)=2.

For every prime power q=3 mod 4 with q>=19, fix any arc u -> v. Its common
outneighbor set has at least four vertices. Every tournament on four vertices
has a transitive triple: some vertex has at least two outneighbors, which
are themselves joined by an arc. Such a triple, together with u,v, is a
transitive five-set. Consequently N(q)=3.

The only smaller prime powers congruent to 3 mod 4 are 3,7,11; the next is 19,
since 15 is not a prime power. The smaller cases have already been handled.
The tournament statements used here are standard
finite combinatorics, not a new result about Paley tournaments.

## 7. Even q

For even q, squaring permutes F_q^*, so PSL(2,q)=PGL(2,q). The group is sharply
3-transitive on the projective line: an ordered triple of distinct points
has a unique projective map to any other such triple.

If q>=8, choose three disjoint output pairs, possible because q+1>=9. Every
one of their eight choices is a distinct triple, so sharp 3-transitivity
realizes it. Thus N(q)=3. The smaller even prime powers 2,4 were settled
in Section 2. This completes the candidate proof for every prime power q.

## 8. What this proof does and does not establish

The theorem is a mathematical classification of the natural degree-(q+1)
action. It is not a classification of all actions or all coset cubes of the
abstract group PSL(2,q), nor of its Galois actions on entire fields.
Isomorphic abstract groups can act differently here: PSL(2,4) and PSL(2,5)
are both isomorphic to A5 but have degrees 5 and 6 in this theorem.

The proof is uniform in q; finite computations only check the implementation
and the fragile small cases. It does not infer an infinite theorem from a
finite sweep. No statement about ARC scores, consciousness, NAGI, unrestricted
program discovery, or the correctness of an intended ARC rule follows.

The closest retrieved group-learning paper (Li, arXiv:2610.18154v1) already
connects teaching to bases and treats Natarajan cubes. Its small computations
overlap this work. We have not located this exact all-q classification there;
that observation is not a proof of novelty. A fuller literature comparison remains necessary. AI rechecking in another session of the same workflow has reported no defects;
third-party independent confirmation and human peer review have not been performed.
