# 追加文献との照合 v0.2

確認日: 2026-10-27。一次資料で確認した箇所と、そこから言える範囲を記す。

## Liの提出ソース

対象: arXiv:2610.18154v1。公式srcから取得した提出アーカイブは32ファイル。
TeX、文献、図、提出設定から成り、独立した探索プログラムや結果データは
このアーカイブには含まれていない。ファイル一覧とハッシュを
evidence/li_source_inventory.json に記録した。第三者のソース本文は再配布しない。

関連する本文・付録を読み、Paley、q=11/13の明記、外部コードへのリンクも
検索した。全q分類は確認した範囲で見つからなかった。ただし、小qを含む
追加探索の詳細結果が得られていないため、既出性を否定できない。

## Hudson (2026), arXiv:2607.20295

Scott Hudson, *A Paper on Calculating the Height and Relational Complexity of
the Primitive Actions of PSL_2(q) and PGL_2(q)*, July 2026.
<https://arxiv.org/pdf/2607.20295>

Theorem 1.0.1–1.0.2、Chapter 4を確認。Borel作用は射影直線への自然作用。
ここでheightは最大独立集合の大きさ、relational complexityは部分タプルの
軌道整合が全タプルへ延びるのに必要な部分タプル長である。

該当する自然作用について、Theorem 4.3.8がheight、Theorem 4.4.5が
奇数qのrelational complexityを与える。q=11,13はともにheight=3、RC=4。
他のprimitive actionまで全て同じ値であるという主張ではない。

対してNo.42ではq=11でNatarajan次元2、q=13で3。この二例から、
heightとRCの二つの数値だけではNo.42の量は決定しないと分かる。
これは本分類の新規性を証明するものではない。

## Linear dimension of group actions

Alice Devillers, Michael Giudici, Daniel R. Hawtin, Lukas Klawuhn, Luke Morgan,
arXiv:2512.16079v1 (2025-12-18).
<https://arxiv.org/html/2512.16079v1>

§1の定義、Theorem 1.5を確認。linear dimensionは、群作用を保つ単射で
点集合をベクトル空間に埋め込むときの最小ベクトル空間次元。
Natarajanの二択配置の次元と同一視しない。対象群が重なるため比較に含める。

## base・independenceの既存用語

Nick Gill, Bianca Lodà, Pablo Spiga, *On the height and relational complexity
of a finite permutation group*, arXiv:2005.03942v2; Nagoya Mathematical Journal
246 (2022), 372–411, DOI 10.1017/nmj.2021.6.
<https://arxiv.org/abs/2005.03942>

§1.1の定義、式(1.1)–(1.2)を確認。base size、最大minimal base size、
height、最長irredundant base length、RCを区別して扱う必要がある。
これらを新しい名前に置き換えた主張はしない。

| 量 | 問うこと |
| --- | --- |
| base size b | 点を固定することで変換を一意にする最小点数 |
| height H | どの点も他の点の固定からは強制されない集合の最大サイズ |
| relational complexity RC | 対応する部分タプルの軌道整合から全体の軌道整合が従う閾値 |
| linear dimension | 群作用を保つ単射埋込みに必要なベクトル空間次元 |
| Natarajan dimension | 各点の二択ラベルの全組合せが実現できる点数の最大値 |

## 確認の限界

Liの探索コードを実行した、全補助データを読んだ、古典文献を網羅した、
とは主張しない。古い用語での同値結果、Paley two-graphの部分配置、
全引用先までの照合は未完。REFERENCES=PARTIAL / NOVELTY=INCONCLUSIVE。
