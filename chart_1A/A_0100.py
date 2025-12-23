import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import math
    import matplotlib.pyplot as plt
    return math, mo, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題100 (1)**
    袋の中に赤玉3個、白玉2個、黒玉1個が入っている。
    この袋から玉を3個取り出すとき、その中に含まれる赤玉の期待値を求めよ。

    ---
    この袋から取り出す赤玉の個数は確率変数$X \in \{0, 1, 2, 3\}$で表すことが出来、$X$は超幾何分布に従う。

    #### 解答1
    袋の中の6つの玉の中から、3つの玉を選んで取り出す取り出し方は、$\dbinom{6}{3}=20(通り)$

    袋から玉を3個取り出すとき、その中に赤玉が$x個\;(x=0, 1, 2, 3)$含まれる確率を$p_k$とすると、

    $$
    \begin{aligned}
    p_0 = P(X=0) &= \frac{\dbinom{3}{0}\dbinom{3}{3}}{20} = \frac{1}{20} \\
    p_1 = P(X=1) &= \frac{\dbinom{3}{1}\dbinom{3}{2}}{20} =\frac{9}{20}\\
    p_2 = P(X=2) &= \frac{\dbinom{3}{2}\dbinom{3}{1}}{20} =\frac{9}{20}\\
    p_3 = P(X=3) &= \frac{\dbinom{3}{3}\dbinom{3}{0}}{20} = \frac{1}{20} \\
    \end{aligned}
    $$

    求める期待値は、

    $$
    \begin{aligned}
    E(X) &= \sum_{x=1}^{4}xp_k \\
    &= 0 \cdot \frac{1}{20} + 1 \cdot \frac{9}{20} + 2 \cdot \frac{9}{20} + 3 \cdot \frac{1}{20}  \\
    &= \frac{30}{20} = \frac{3}{2} \;\square
    \end{aligned}
    $$

    ---
    #### 解答2
    抽出個数$n=3$、赤玉の総数$K=3$、玉の個数は$N=6$であるから、
    求める期待値は、

    $$
    E(X) = n \cdot \frac{K}{N} = 3 \cdot \frac{3}{6} = \frac{3}{2} \; \square
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題100 (2)**
    1から6までの整数が1つずつ書かれたカードが6枚ある。この中から4枚のカードを無作為に取り出して得られる4つの整数のうち最大のものを$X$とする。$X$の期待値を求めよ。

    ---
    カードを無作為に取り出して得られる4つの整数の最大値は、確率変数$X \in \{4, 5, 6\}$で表すことが出来る。

    6枚のカードから4枚のカードを取り出す方法は、$\dbinom{6}{4} = 15(通り)$


    $X=6$の場合、他3枚を1から5のカードから取り出せばよいので、

    $$
    P(X=6) = \frac{\dbinom{1}{1}\dbinom{5}{3}}{15} = \frac{10}{15}
    $$


    $X=5$の場合、他3枚を1から4のカードから取り出せばよいので、

    $$
    P(X=5) = \frac{\dbinom{1}{1}\dbinom{4}{3}}{15} = \frac{4}{15}
    $$


    $X=4$の場合、他3枚を1から3のカードから取り出せばよいので、

    $$
    P(X=4) = \frac{\dbinom{1}{1}\dbinom{3}{3}}{15} = \frac{1}{15}
    $$

    求める期待値は、

    $$
    \begin{aligned}
    E(X) &= 6 \cdot \frac{10}{15} + 5 \cdot\frac{4}{15} + 4 \cdot \frac{1}{15} \\
    &= \frac{84}{15} = \frac{28}{5} \;\square
    \end{aligned}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 補足
    問題100(2)の分布は超幾何分布か？

    ❌ 超幾何分布ではない
    ✔ 順序統計量（最大値）の分布

    なぜ超幾何分布ではないのか？

    超幾何分布は：

    * 「成功 / 失敗」の 2値
    * 「成功の個数」を数える分布

    例：
    * 赤玉が何個か
    * 当たりが何枚か

    今回数えているのは 「成功の個数」ではない。


    「4枚の中の最大値」すなわち、大小関係という**「順序情報」**を扱っている

    今回の$X$は、母集団 $\{1,2,3,4,5,6\}$から4個抽出したときの最大値
    これは確率論では

    $$
    X = \max\{1, 2, 3, 4, 5, 6\}
    $$

    と書かれ、**順序統計量**とよばれる。
    """)
    return


@app.cell(hide_code=True)
def _(math, plt):
    # パラメータ
    N_1 = 6   # 全体
    K_1 = 3   # 赤玉
    n_1 = 3   # 抽出数

    def comb(n, r):
        return math.comb(n, r)

    # 確率分布
    x_vals_1 = range(0, n_1 + 1)
    probs_1 = [
        comb(K_1, k) * comb(N_1 - K_1, n_1 - k) / comb(N_1, n_1)
        for k in x_vals_1
    ]

    # 図示
    plt.bar(x_vals_1, probs_1)
    plt.xlabel("Number of red balls")
    plt.ylabel("Probability")
    plt.title("Hypergeometric Distribution (Problem 100-1)")
    plt.xticks(x_vals_1)
    plt.show()

    return (comb,)


@app.cell(hide_code=True)
def _(comb, plt):
    # パラメータ
    N_2 = 6   # 最大値
    n_2 = 4   # 抽出数

    # X が取りうる値
    x_vals_2 = range(n_2, N_2 + 1)

    # 確率分布（最大値）
    probs_2 = [
        comb(x - 1, n_2 - 1) / comb(N_2, n_2)
        for x in x_vals_2
    ]

    # 図示
    plt.bar(x_vals_2, probs_2)
    plt.xlabel("Maximum value")
    plt.ylabel("Probability")
    plt.title("Distribution of Maximum (Problem 100-2)")
    plt.xticks(x_vals_2)
    plt.show()

    return


if __name__ == "__main__":
    app.run()
