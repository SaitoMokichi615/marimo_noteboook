import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from math import comb
    return comb, mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題103**
    袋の中に白玉10個、黒玉60個が入っている。

    この袋の中から1玉ずつ取り出して調べて戻すという試行を40回行うとき、

    白玉が何回取り出される確率が最も大きいか。

    ---

    袋の中の70個の玉の中から白玉を取り出す確率は、$\dfrac{10}{70} = \dfrac{1}{7}$

    40回の試行の中で取り出した白玉の総数を確率変数$X$とすると、

    $$
    X \sim \mathrm{Bin}\left(40, \frac{1}{7}\right)
    $$

    ゆえに、

    $$
    P(X=k) = \binom{40}{k} \left(\frac{1}{7} \right)^{k}\left(\frac{6}{7} \right)^{40-k}
    $$

    $P(X=k)$を最大にする$k$(最頻値)を求めるには、$P(X=k+1)$と$P(X=k)$の*比*を調べればよい。

    すなわち、

    $$
    \frac{P(X=k+1)}{P(X=k)} > 1
    $$

    を満たす最大の$k$を求めればよい。


    $$
    \begin{aligned}
    \dfrac{P(X=k+1)}{P(X=k)} &= \dfrac{\dbinom{40}{k+1} \left(\dfrac{1}{7} \right)^{k+1}\left(\dfrac{6}{7} \right)^{40-k-1}}{\dbinom{40}{k} \left(\dfrac{1}{7} \right)^{k}\left(\dfrac{6}{7} \right)^{40-k}}\\
    &= \dfrac{\left(\dfrac{40!}{(k+1)!(40-k-1)!}\right) \dfrac{1}{7}}{\left(\dfrac{40!}{k!(40-k)!}\right)\dfrac{6}{7}}\\
    &= \left(\dfrac{40!}{(k+1)!(40-k-1)!}\right)\left(\dfrac{6\cdot 40!}{k!(40-k)!}\right)^{-1}\\
    &= \left(\dfrac{40!}{(k+1)!(40-k-1)!}\right)\left(\dfrac{k!(40-k)!}{6\cdot 40!}\right)\\
    &= \dfrac{40-k}{6(k+1)} > 1
    \end{aligned}
    $$

    これより、

    $$
    \begin{aligned}
    6k +6  &< 40 -k \\
    7k &< 34 \\
    k &< \frac{34}{7} \simeq 4.86
    \end{aligned}
    $$

    ゆえに、

    $$
    0 \le k \le 4 のとき、P(X=k+1) > P(X=k)
    $$

    すなわち、

    $$
    P(X=0) < P(X=1) < \dots < P(X=4) < P(X=5)
    $$



    $$
    5 \le k \le 39 のとき、P(X=k+1) < P(X=k)
    $$

    すなわち、

    $$
    P(X=5) > P(X=6) > \dots > P(X=39) > P(X=40)
    $$

    これより、$P(X=k)$を最大するのは$k=5$である。

    したがって、白玉が5回取り出される確率が最大である（最頻値である）。 $\; \square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 補足

    試行回数$n$, 成功確率$p$、試行が成功した回数を確率変数$X$で表すと、

    $$
    X \sim \mathrm{Bin}\left(n, p\right)
    $$

    $$
    P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}
    $$

    ここで、

    $$
    \begin{aligned}
    \dbinom{n}{k} &= \frac{{}_nP_k}{k!}  \\
    &= \frac{n!}{k!(n-k)!} \\
    &= \frac{n!}{k!(n-k)(n-k-1)!}
    \end{aligned} \tag{*}
    $$



    $$
    \begin{aligned}
    \dbinom{n}{k+1} &=  \frac{{}_nP_{k+1}}{(k+1)!} \\
    & = \frac{n!}{(k+1)!(n-k-1)!} \\
    & = \frac{n!}{k!(k+1)(n-k-1)!} \\
    & = \frac{n!(n-k)}{k!(k+1)(n-k)(n-k-1)!} \\
    & = \frac{n-k}{k+1}\binom{n}{k}
    \end{aligned} \tag{**}
    $$

    (\*), (\**)より、

    $$
    \begin{aligned}
    \dfrac{P(X=k+1)}{P(X=k)} &= \dfrac{\dbinom{n}{k+1} p^{k+1}\left(1-p \right)^{n-k-1}}{\dbinom{n}{k} p^{k}\left(1-p \right)^{n-k}}\\
    &= \dfrac{n-k}{k+1}\cdot\frac{p}{1-p}
    \end{aligned}
    $$

    $\dfrac{P(X=k+1)}{P(X=k)} > 1$ ならば、確率は増加中。

    $\dfrac{P(X=k+1)}{P(X=k)} < 1$ ならば、確率は減少中。

    増加・減少の境界は、$\dfrac{n-k}{k+1}\cdot\dfrac{p}{1-p}=1$

    $$
    \begin{aligned}
    &\dfrac{n-k}{k+1}\cdot\dfrac{p}{1-p} > 1 \\
    \rightarrow \;&\dfrac{n-k}{k+1} > \dfrac{1-p}{p} \\
    \rightarrow \;&p(n-k)> (k+1)(1-p) \\
    \rightarrow \;&pn-pk> k - pk + 1 -p \\
    \rightarrow \;&pn-p-1> k\\
    \rightarrow \;&k < (n+1)p-1 \\
    \end{aligned}
    $$

    これより、

    * $k < (n+1)p-1$では増加
    * $k > (n+1)p-1$では減少

    増加から減少に切り替わる点が最大なので、

    $$
    \boxed{(n+1)p-1 < k \le (n+1)p}
    $$

    を満たす$k$が最頻値となる。
    <!-- n=40, k=3
    (n-k)! = 37! = 37(36!) =
    (n-k-1)! = 36! -->
    """)
    return


@app.cell
def _(comb, np, plt):
    # パラメータ
    n = 40
    p = 1 / 7

    # k の範囲
    k = np.arange(0, n + 1)

    # 二項分布の確率
    prob = np.array([
        comb(n, ki) * (p ** ki) * ((1 - p) ** (n - ki))
        for ki in k
    ])

    # プロット
    plt.figure()
    plt.bar(k, prob)
    plt.xlabel("k (number of white balls)")
    plt.ylabel("P(X = k)")
    plt.title("Binomial Distribution: Bin(40, 1/7)")
    plt.show()

    return


if __name__ == "__main__":
    app.run()
