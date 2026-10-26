# 先行研究と採否 — No.42 v0.2

初回調査: 2026-10-26 / 追加照合: 2026-10-27。以下は範囲を限定した調査であり、網羅的な新規性証明ではない。

## 初期案の扱い

| 初期案 | 先に確認した既存研究・障害 | 採否 |
| --- | --- | --- |
| ARC有限証明書長 | 固定仮説集合から例で規則を特定する量はteaching dimensionなどに接続する。計算トレースの正しさと出題意図への一致は別。 | 広い主張では不採用。具体的な変換クラスの別の不変量へ絞った。 |
| Research Failure Taxonomy | Fei et al., arXiv:2608.14905 は100研究課題・800軌跡を対象に45失敗パターンを整理している。 | 「分類そのものが未開拓」という根拠では不採用。 |
| Boundary Exactification Principle | 境界付きグラフの同値類、protrusion replacement、有限整数指数などの既存理論がある。 | 一般的な名前だけでは不採用。新しいモデル固有の定理が必要。 |

固定仮説集合の必要性は、次の初等的な議論でも分かる。有限訓練集合に
含まれないテスト入力x*があるとき、訓練例に一致する写像fを取り、x*
だけで値を変えた写像gを作れる。仮説集合を制限しなければ、両者を
訓練例から区別できない。ARCの人間の事前知識を否定する主張ではない。

Goldman–Kearns のteaching dimensionはこの種の固定クラスでの識別を
扱う既存概念である。ARCという応用名を付けただけで新しい量とはしない。

## 今回の候補に近い一次資料

1. Xiaoyu Li, *Learning a Group Element from Its Action: Galois Correspondences,
   Optimal ERM, and an Abel–Ruffini Threshold for the Natarajan Dimension*,
   arXiv:2610.18154v1, 2026-10-13.
   <https://arxiv.org/html/2610.18154v1>

   群の学習と古典的不変量を結び付け、Natarajan cubeも扱う最接近資料。
   本文と公式提出ソースを確認。小qの計算は重複する。全qの本分類は
   確認範囲で見つからないが、提出物に探索コード・結果データは含まれず、
   報告された追加探索との全件照合は未完。

2. Vedran Krčadinac, Mario Osvin Pavčević, Kristijan Tabak,
   *Three-dimensional Hadamard matrices of Paley type*,
   Finite Fields and Their Applications 92 (2023), 102306;
   arXiv:2305.12415v2.
   <https://arxiv.org/html/2305.12415v2>

   §2、特にLemma 2.2を確認。三点の二次指標がPSL作用で保存される
   ことは既知。今回の三点判定の背後にある量を新発見とはしない。

3. Koji Momihara, Sho Suda, *Upper bounds on the size of transitive
   subtournaments in digraphs*, arXiv:1605.02469.
   <https://arxiv.org/abs/1605.02469>

   メタデータ・要旨とPDFの表2を確認。Paley tournamentにおける
   推移的部分トーナメントの大小は既存研究の対象である。
   今回のq=7,11の障害自体は新しいトーナメント現象ではない。

4. Sally A. Goldman, Michael J. Kearns, *On the Complexity of Teaching*,
   WUCS-92-28 (1992); Journal of Computer and System Sciences 50 (1995), 20–31.
   <https://repository.library.washu.edu/cse_research/591/>

   著者機関リポジトリの要旨・書誌を確認。定義の既存性に用いた。
   本文の全定理の照合は未実施。

5. Yanlin Fei et al., *How Do Agents Fail on AutoResearch: End-to-End Diagnostic
   Evaluation on 100 Real-World Frontier Research Tasks*, arXiv:2608.14905v3.
   <https://arxiv.org/html/2608.14905v3>

6. Bart M. P. Jansen, Jules J. H. M. Wulms, *Lower Bounds for Protrusion
   Replacement by Counting Equivalence Classes*, IPEC 2016, 17:1–17:12.
   <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.IPEC.2016.17>

7. Scott Hudson, arXiv:2607.20295 (2026), Chapter 4。
   <https://arxiv.org/pdf/2607.20295>

8. Devillers et al., *Linear dimension of group actions*, arXiv:2512.16079v1。
   <https://arxiv.org/html/2512.16079v1>

9. Gill–Lodà–Spiga, *On the height and relational complexity of a finite
   permutation group*, arXiv:2005.03942v2; Nagoya Math. J. 246 (2022), 372–411。
   <https://arxiv.org/abs/2005.03942>

追加3資料との定義・定理の比較はCITATION_CHECK_JA.mdを参照。

## 既知と候補の境界

既知として除外するもの:

- Natarajan次元そのもの、teaching dimension、群作用のbaseとの関係。
- 三点で射影変換が決まること、PSLの二重推移性、PGLの鋭三重推移性。
- 行列式の平方類、三点の二次指標、Paleyグラフ・トーナメントの標準性質。
- 初期例の計算値が先行論文と重複していること。

候補として監査に残すもの:

- 自然な射影直線作用に限定した、全ての素数冪に対するNatarajan次元の
  一つの例外表による完全分類。
- 正規化した二択3-cubeの必要十分条件から、奇数qの二つの剰余類を
  それぞれPaleyグラフの四角形と推移的五点トーナメントへ落とす論証。

これは「既知の材料から得た具体的な分類結果」の候補である。
材料が既知であることと分類が既出であることは同じではないが、分類が
既知定理の即時の帰結に過ぎない可能性も排除できていない。

## 使用した検索語の例

"ARC" "teaching dimension";
"abstraction and reasoning corpus" "verification" "ambiguity";
"research failure" taxonomy;
"finite integer index" "boundaried graphs";
"teaching dimension" "permutations" "group";
"Natarajan dimension" "PSL(2";
"Natarajan" "projective transformations";
"Natarajan" "Paley";
"PSL" "Boolean cubes";
"permutation group" "cube dimension";
"Paley two-graph" "octahedron";
"Paley" "monochromatic subcubes".

検索は2種類の検索サービスで実施し、採用する技術的根拠は一次資料へ
戻って確認した。検索結果ゼロを未発見の証明とはしていない。

## 未完了

Liの公式提出ソースは確認したが、報告された探索コードや詳細結果は
取得できていない。全引用先、有限群・二重推移群の古い別用語、
Paley two-graphの部分配置に関する文献、自作No.1–41全文との網羅的な
重複照合は未完了。著者への問い合わせも行っていない。

判定: REFERENCES=PARTIAL / NOVELTY=INCONCLUSIVE。
