import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import sympy as sy
    from sympy.stats import Die, P, E, density, sample, FiniteRV, given
    from sympy import Eq, simplify

    return Die, Eq, P, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## B.901
    A君が目をつぶってサイコロを2回振った。
    B君が結果を見て、さいころの目の和は5以下であったと教えた。
    最初に振ったサイコロの目が1であった確率$p$を求めよ。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    事象$E$、$F$ を次のようにおく。

    $$
    \left\{
    \begin{aligned}
    E &= 「最初に振ったサイコロの目が1」 \\
    F &= 「サイコロの目の和が5以下」
    \end{aligned}
    \right.
    $$

    このとき、求める確率$p$は、
    「$F$が起こったという条件のもとに、$E$が起こる確率」である。

    すなわち、

    $$
    p = P_F(E) = \frac{P(E\cap F)}{P(F)} \tag{1.}
    $$

    サイコロの目の出方は、$6^2 = 36$通りあり、これらは等確率で起こる。

    このうち、事象$F$ のような目の出方は、

    $(1,1), (1,2), (1,3), (1,4),$

    $(2,1), (2,2), (2,3),$
    $(3,1), (3,2),$
    $(4,1)$

    の10通り。

    $$
    P(F) = \frac{10}{36} \tag{2.}
    $$

    $E\cap F$のような目の出方は、4通り。
    ゆえに、

    $$
    P(E\cap F) = \frac{4}{36} \tag{3.}
    $$


    したがって、(1.)、(2.)、(3.)より、

    $$
    p =  \frac{2}{5}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pythonの代数計算ライブラリ、Sympyでも検算する。
    """)
    return


@app.cell
def _(Die, Eq, P):
    # # 1個目と2個目のサイコロ
    # D1 = Die('D1', 6)
    # D2 = Die('D2', 6)

    # E_event = (D1 == 1)
    # F_event = (D1 + D2 <= 5)

    # 2つの6面サイコロを定義
    X, Y = Die('X', 6), Die('Y', 6)

    # 事象F: 合計が5以下
    event_F = X + Y <= 5

    # 事象E: サイコロXが1
    event_E = Eq(X ,1)

    # 条件付き確率 P(A | B) を計算
    conditional_prob = P(event_E, given=event_F)
    conditional_prob
    return


if __name__ == "__main__":
    app.run()
