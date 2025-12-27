import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from math import comb
    plt.rcParams["font.family"] = "Meiryo" 
    return comb, mo, np, plt


@app.cell
def _(mo):
    mo.md(r"""
    ### **問題102**
    標的に命中する確率が$\dfrac{2}{3}$の射撃選手が$n$回撃つ時、

    (1)一発も命中しない確率を求めよ。

    (2)少なくとも一発命中する確率が0.99より大きくなるのは、$n$がいくつ以上の時か。

    ---

    (1)
    命中回数を確率変数$X$とすると、

    $$
    X \sim \mathrm{Bin}\left(n, \frac{2}{3}\right)
    $$

    である。

    よって、一発も命中しない確率は

    $$
    \begin{aligned}
    P(X=0) &= \binom{0}{n}\left(\frac{2}{3}\right)^0\left(\frac{1}{3}\right)^n \\
    &= \frac{1}{3^n} \; \square
    \end{aligned}
    $$

    (2)
    少なくとも一発命中する確率は、


    $$
    \begin{aligned}
    P(X \ge 1) &= 1 - P(X=0 ) \\
    &= 1 - \frac{1}{3^n}
    \end{aligned}
    $$

    これが0.99より大きくなるには、

    $$
    \begin{aligned}
     \;\frac{1}{3^n} &< 0.01 \\
     \rightarrow \; n &> 2\log_3 10
    \end{aligned}
    $$

    となればよい。

    ここで、

    $$
    3^2 = 9, \quad 3^3 = 27
    $$

    であるから、

    $$
    \begin{aligned}
    9 &< 10 < 27 \\
    \rightarrow 2 &< \log_3 10 < 3\\
    \rightarrow 4 &< 2\log_3 10 < 6\\
    \end{aligned}
    $$


    $$
    2 \log_3 9 < 2 \log_3 10 < 2 \log_3 27
    $$


    $$
    0.01 = \frac{1}{100} = \frac{81}{8100} = \frac{243}{24300}
    $$

    $$
    \frac{1}{3^4} = \frac{1}{81} = \frac{100}{8100} > 0.01
    $$

    $$
    \frac{1}{3^5} = \frac{1}{243} = \frac{100}{24300} < 0.01
    $$


    したがって、$n \ge 5$のとき、$P(X \ge 1) > 0.99$ となる。　$\square$
    """)
    return


@app.cell
def _(mo):
    n_input = mo.ui.slider(start=1, stop=40, step=1, label="試行回数")
    n_input
    return (n_input,)


@app.cell(hide_code=True)
def _(comb, n_input, np, plt):
    # パラメータ
    n = n_input.value          # 試行回数（必要に応じて変更）
    p = 2 / 3      # 命中確率

    # 確率変数の取りうる値
    k = np.arange(0, n + 1)

    # 二項分布の確率
    prob = np.array([
        comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
        for i in k
    ])

    # プロット
    plt.figure()
    plt.bar(k, prob)
    plt.xlabel("命中回数 k")
    plt.ylabel("P(X = k)")
    plt.title(f"Binomial Distribution: n={n}, p={p}")
    plt.xticks(k)
    plt.show()
    return


if __name__ == "__main__":
    app.run()
