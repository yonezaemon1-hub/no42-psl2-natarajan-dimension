# 新規性の再点検 — 2026-10-27

結論: 全q分類の既出は今回確認した範囲では見つからなかった。
ただし、NOVELTY=INCONCLUSIVE、REFERENCES=PARTIALを維持する。
新しい用語や既知の構成を新発見として扱わない。

## 重点的に読み直した範囲

Li, arXiv:2610.18154v1の公式提出ソースのうち、
`sections/3d_natarajan.tex`と`sections/app_d_natarajan.tex`を全体として再読。
一般上界、可換な構成、matroid closureの下界、二次元のsquare判定、
計算記録を本分類に照合した。提出ソースのハッシュは既存の一覧に記録済み。

| 既存の内容 | No.42との関係 |
| --- | --- |
| 一般上界・ラベル数の議論 | 上界3や小体の処理は既知の原理による。新規性の根拠にしない。 |
| matroid closureに対する下界 | この自然作用のrank 3の場合は下界2を与える。2か3かの全q判定までは与えない。 |
| Natarajan squareの判定 | 二地点の二択に関する内容。三地点8通りの全q分類とは区別する。 |
| 小qの計算 | 重複する例がある。個々の値を新規と断言しない。 |
| 追加の探索記録 | 詳細データが提出物にないため、全件照合は未完。 |

## 直接の帰結として除外した部分

偶数qでPSL=PGLとなること、鋭三重推移性、ラベル数からの次元3は、
既知の事実から直接出る。二次指標の三点不変量、Paleyグラフと
トーナメントの標準性質も既知である。

候補に残しているのは、指定された自然作用についての全素数冪の
例外表と、奇数qのcube必要十分条件を通じたその証明である。
材料が既知であることは明示する。分類結果自体が既知の言い換えである
可能性は排除できていない。

## 別名・隣接分野

Natarajan dimension、permutation/group learning、projective line、
PSL(2,q)、Paley、Cartesian/Boolean cube、shatteringを組み合わせて、
2種類の検索サービスで再検索した。さらにbase size、height、
relational complexity、linear dimensionの定義と照合した。
検索の無ヒットを新規性の証明とはしない。

HudsonのBorel作用の結果、Gill–Lodà–Spigaの既存不変量、
Devillersらのlinear dimensionは比較対象として維持する。
全引用先、Paley two-graphの古い部分配置用語、未公開・未取得の
探索データまで網羅したという主張はしない。

## 公開時の表現

未査読プレプリント、NOVELTY INCONCLUSIVE、REFERENCES PARTIAL、
優先権主張なしをPDF・README・登録説明に明記する。
「独立監査」は第三者確認を意味せず、別セッションのAIによる
同じ作業の流れの再点検であると明記する。
