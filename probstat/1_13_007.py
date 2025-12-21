import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams["font.family"] = "Meiryo" 
    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **超幾何分布**
    有限個のものの中から、重複なしで抽出する。
    * 全体の個数$N$
    * 成功（当たり）の個数$K$
    * 失敗（外れ）の個数$N-K$
    * 抽出回数$n$

    $$
    X = 「n回引いた中に含まれる成功の個数」
    $$

    は** 超幾何分布 **に従う。
    超幾何分布の確率質量関数は、

    $$
    P(X=x) = \frac{\dbinom{K}{x}\dbinom{N-K}{n-x}}{\dbinom{N}{n}}
    $$

    #### 式の意味
    分子
    * $\dbinom{K}{x}$ :当たり$K$本から$x$本選ぶ
    * $\dbinom{N-K}{n-x}$ :外れ$N-K$本から$n-k$本選ぶ。

    分母
    * $\dbinom{N}{n}$ :全体から$n$本選ぶ。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 定義域
    $$
    \max(0, n-(N-K)) \le x \leq \min(n, K)
    $$

    * 全体の個数$N$
    * 成功（当たり）の個数$K$
    * 失敗（外れ）の個数$N-K$
    * 抽出回数$n$
    * 抽出された成功の個数$x$

    #### 右側の不等式
    $x \leq \min(n, K)$
    * 成功は**最大でも抽出回数$n$回まで**
    * そもそも成功は**全体で$K$個**しかない

    #### 左側の不等式
    $x \geq \max(0, n-(N-K))$
    * 失敗（外れ）の個数$N-K$
    * 抽出回数$n$

    もし$n > N-K$ ならば、すなわち**抽出回数が失敗回数より多い**ならば、最低でも抽出回数から失敗回数を引いた不足分は必ず成功する。その成功回数が$n-(N-K)$となる。

    もし$n \leq N-K$ならば、**全部の抽出が失敗である**可能性もある。つまり、最低の成功回数は$0$となる。
    """)
    return


@app.cell
def _(mo):
    N_input = mo.ui.slider(10, 100, value=10, label="全体:N")
    N_input
    return (N_input,)


@app.cell
def _(N_input):
    # パラメータ
    N = N_input.value        # 全体
    return (N,)


@app.cell
def _(N, mo):
    K_input = mo.ui.slider(0, N, value=2, label="成功:K")
    n_input = mo.ui.slider(0, N, value=8, label="抽出回数:n")
    mo.vstack([K_input, n_input])

    return K_input, n_input


@app.cell
def _(K_input, n_input):
    # パラメータ
    K = K_input.value         # 成功
    n = n_input.value        # 抽出回数
    return K, n


@app.cell(hide_code=True)
def _(K, N, n, xmax, xmin):
    # print(f"全体N:{N}, 成功K:{K}, 失敗N-K:{N-K}, 抽出回数:n:{n}")
    # check = n > N-K
    # str_min = ""
    # str_max = ""

    # if check:
    #     str_max = "max関数はn-(N-K)を出力"
    #     str_min = "min関数はKを出力"
    # else:
    #     str_max = "max関数は0を出力" 
    #     str_min = "min関数はnを出力"

    # print(f"n > N-K(抽出回数>失敗)?:{check}")
    # print(f"xmin=max(0, n-(N-K)):{xmin} {str_max}")
    # print(f"xmax=min(n, K):{xmax} {str_min}")

    # print(f"{xmin}<=x<={xmax}")

    print(f"全体N:{N}, 成功K:{K}, 失敗N-K:{N-K}, 抽出回数n:{n}")

    check = n > (N - K)

    if check:
        xmin_reason = "失敗が足りないため xmin = n-(N-K)"
    else:
        xmin_reason = "失敗だけで足りるため xmin = 0"

    if n < K:
        xmax_reason = "抽出回数が少ないため xmax = n"
    else:
        xmax_reason = "成功数が少ないため xmax = K"

    print(f"n > N-K (抽出回数 > 失敗数)?: {check}")
    print(f"xmin = max(0, n-(N-K)) = {xmin}  ← {xmin_reason}")
    print(f"xmax = min(n, K) = {xmax}  ← {xmax_reason}")

    print(f"定義域: {xmin} ≤ x ≤ {xmax}")

    return


@app.cell(hide_code=True)
def _(K, N, n, np, plt):


    # 定義域の計算
    xmin = max(0, n - (N - K))
    xmax = min(n, K)

    # x の候補（0〜n）
    x_vals = np.arange(0, n + 1)

    # 可能かどうか（1 = 可能, 0 = 不可能）
    possible = [(xmin <= x <= xmax) for x in x_vals]

    # プロット
    plt.figure()
    plt.bar(x_vals, possible)
    plt.xticks(x_vals)
    plt.yticks([0,1])
    plt.xlabel("x（抽出された成功の個数）")
    plt.ylabel("成功の可能があるかどうか")
    plt.title("超幾何分布の定義域")
    plt.show()

    return xmax, xmin


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 図の意味
    * 高さ 1：その$x$は**起こり得る**

    * 高さ 0：その$x$は**絶対に起こらない**
    """)
    return


@app.cell(hide_code=True)
def _(K, N, n, plt):
    labels = [f"成功 K={K}", f"失敗 N-K={N-K}", f"抽出 n={n}"]
    values = [K, N-K, n]

    plt.figure()
    plt.bar(labels, values)
    plt.ylabel("個数")
    plt.title(f"超幾何分布の構造(全体N={N})")
    plt.show()

    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 補足
    $\max(0, n-(N-K))$は、$0$と$n-(N-K)$のうち、**大きい方を返す**。

    $\min(n, K)$は、$n$と$K$のうち、**小さい方を返す**。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 超幾何分布の期待値と分散

    $$
    E(X) = n \cdot \frac{K}{N}
    $$

    $$
    V(X) = n \cdot \frac{K(N-K)}{N^2} \cdot \frac{N-n}{N-1}
    $$

    上記は**非復元抽出法**の場合の期待値と分散である。

    **復元抽出法**の場合、成功確率$\dfrac{K}{N}$は一定のため、$p$と表すことが出来る。

    よって

    $$
    \begin{aligned}
    E(X) &= n p \\
    V(X) &= n \cdot \frac{K}{N}\frac{(N-K)}{N} \cdot \frac{N-n}{N-1} \\
    &= np(1-p)\cdot \frac{N-n}{N-1} \\
    \end{aligned}
    $$

    $N$が無限に大きい場合、

    $$
    V(X) = np(1-p)\cdot \frac{1-\dfrac{n}{N}}{1-\dfrac{1}{N}} \xrightarrow{N\to\infty}  np(1-p)
    $$

    となり、二項分布の期待値と分散は等しくなる。
    すなわち、非復元抽出法で$N$が無限に大きい場合、超幾何分布は二項分布に近似できる。

    ### 二項分布との対比

    |    | 超幾何分布 | 二項分布     |
    | -- | ----- | -------- |
    | 抽出 | 非復元   | 復元       |
    | 確率 | 毎回変わる | 一定       |
    | 分布 | 有限母集団 | 無限 or 独立 |
    """)
    return


if __name__ == "__main__":
    app.run()
