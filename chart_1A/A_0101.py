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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題101 (1)**
    1個のサイコロを投げて、1の目が出ると100円、6の目が出ると200円をそれぞれ支払い、それ以外の時は150円もらうことを約束した人は、得をするか？損をするか？

    ---

    サイコロの各出目$\{1, 2, 3, 5, 6, 6\}$は互い排反で同様に確からしいので、各目が出る確率は、

    $$
    P(\text{出目}=k) = \frac{1}{6} \quad (k=1, 2, \dots, 6)
    $$

    このときの金銭の収支を確率変数$X$とすると、

    $$
    X = \begin{cases}
    -100 &(\text{出目}1)\\
    150 &(\text{出目}2,3,4,5)\\
    200 &(\text{出目}6)
    \end{cases}
    $$

    となり、

    $$
    P(X=-100) =  \frac{1}{6}, \quad
    P(X=150) = \frac{4}{6}, \quad
    P(X=-200) = \frac{1}{6}
    $$

    となる。

    求める期待値は、

    $$
    \begin{aligned}
    E(X) &= (-100)\cdot\frac{1}{6} + 150\cdot\frac{4}{6} +(-200)\cdot\frac{1}{6} \\
    &= \frac{-100+600-200}{6} \\
    &= 50
    \end{aligned}
    $$

    期待値が正であるため、この約束をした人は**平均的に得をする**　$\square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題101 (2)**
    1個のサイコロを5回投げて、1または6の目が出る回数が$k$回の時、$k$百円もらえるというゲームがあり、参加料は200円である。

    このゲームに参加することは得であるか？損であるか？

    ---

    サイコロの各出目$\{1, 2, 3, 4, 5, 6\}$は互いに排反で同様に確からしく、各目が出る確率は$\dfrac{1}{6}$である。



    1回の試行で1または6が出る確率(成功確率)は、$\dfrac{1}{3}$である。

    5回の試行において、成功回数を確率変数$K$とすると、$K$は**二項分布に従い、**

    $$
    K\sim\mathrm{Bin}\left(5, \;\frac{1}{3}\right)
    $$

    と表すことが出来る。


    ゲームの収支を確率変数$X$とすると、

    $$
    X = 100K -200
    $$

    である。

    ---

    ### 解答1

    二項分布の確率は、

    $$
    P(K=k) = \binom{5}{k}\left(\frac{1}{3}\right)^k\left(\frac{2}{3}\right)^{5-k}
    $$

    であるから、

    $$
    \begin{aligned}
    P(K=0) &= \binom{5}{0}\left(\frac{1}{3}\right)^0\left(\frac{2}{3}\right)^{5} = \frac{32}{243} \\
    P(K=1) &= \binom{5}{1}\left(\frac{1}{3}\right)^1\left(\frac{2}{3}\right)^{4} = \frac{80}{243} \\
    P(K=2) &= \binom{5}{2}\left(\frac{1}{3}\right)^2\left(\frac{2}{3}\right)^{3} = \frac{80}{243} \\
    P(K=3) &= \binom{5}{3}\left(\frac{1}{3}\right)^2\left(\frac{2}{3}\right)^{3} = \frac{40}{243} \\
    P(K=4) &= \binom{5}{4}\left(\frac{1}{3}\right)^2\left(\frac{2}{3}\right)^{3} = \frac{10}{243} \\
    P(K=5) &= \binom{5}{5}\left(\frac{1}{3}\right)^2\left(\frac{2}{3}\right)^{3} = \frac{1}{243} \\
    \end{aligned}
    $$

    求める期待値は、

    $$
    \begin{aligned}
    E(X) &= \frac{(-200)\times32 + (-100)\times80 + 100\times40 + 200\times10 + 300\times1}{243} \\
    &= \frac{-6400-8000+4000+2000+300}{243} \\
    &=\frac{-8100}{243} = -\frac{100}{3}
    \end{aligned}
    $$

    ---

    ### 解答2
    二項分布の期待値

    $$
    E(K) = 5\times \frac{1}{3}
    $$

    より、

    $$
    \begin{aligned}
    E(X) &= 100E(K) -200 \\
    &= 100\cdot\frac{5}{3} - 200 \\
    &= \frac{500-600}{3} \\
    &= -\frac{100}{3}
    \end{aligned}
    $$

    となる。

    ---
    よって期待値は負であり、このゲームに参加するのは損である。 $\square$
    """)
    return


@app.cell(hide_code=True)
def _(comb, np, plt):
    # パラメータ
    n = 5
    p = 1/3

    # K と X の値
    K = np.arange(0, n+1)
    X = 100*K - 200

    # 二項分布
    prob = np.array([
        comb(n, k) * (p**k) * ((1-p)**(n-k))
        for k in K
    ])

    # 期待値
    EX = np.sum(X * prob)


    # 描画
    plt.bar(X, prob, width=8)
    plt.axvline(
        EX,
        linewidth=3,      # 線を太く
        color="red",      # 赤色
        linestyle="--",   # 破線（好みで）
        label=f"期待値 E(X) = {EX:.2f}"
    )

    plt.xlabel("収支 X（円）")
    plt.ylabel("確率")
    plt.title("ゲームの収支の確率分布")
    plt.legend()          # ラベル表示\
    plt.show()
    return


if __name__ == "__main__":
    app.run()
