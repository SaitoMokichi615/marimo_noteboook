import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


@app.cell
def _(mo):
    mo.md(r"""
    ###**固有値の数値解法**

    (1) 最大固有値を1個だけ欲しい
        → べき乗法

    (2) 全固有値が欲しい
        → QR法

    (3) QR法を高速・安定にしたい
        → ハウスホルダー変換
        → ヤコビ法（対称行列専用）
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**べき乗法**
    * 固有値の定義がそのままアルゴリズムになる
    * 数学的意味が直感的
    * 実装が一番簡単

    ###アイディア

    適当な初期ベクトル$\boldsymbol{x_0}$に対して、

    $$
    \boldsymbol{x_{k+1}} = \frac{A\boldsymbol{x_k}}{\|A\boldsymbol{x_k}\|}
    $$

    を繰り返す。

    そうすると、**最大絶対値の固有値の固有ベクトルに収束**

    ###何が分かる？
    * 「なぜ最大固有値だけ出てくるか」
    * 「固有値＝伸び率」
    * 「収束率は固有値の比で決まる」

    ###学ぶべき理由

    ✔ 固有値の幾何的意味

    ✔ 数値誤差と収束の感覚

    ✔ Markov連鎖・PageRankと直結
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**QR法**

    QR法は、

    $$
    A_k = Q_kR_k, \; A_{k+1} = R_kQ_k
    $$

    を繰り返す方法。

    $$
    A_{k+1} = {}^tQ_kA_kQ_k
    $$

    という**相似変換の繰り返し**。

    👉 **固有値を変えずに、対角化へ近づけている**



    * 「対角化は座標変換」という理解が完成する
    * べき乗法が 全固有値版 に進化したものだと分かる
    * 理論と実装の橋渡しになる
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**ハウスホルダー変換（QR法の裏方）**

    ##役割##
    QR分解を安定・高速に行うための道具。

    $$
    H = I - 2\frac{\boldsymbol{u}{}^t\boldsymbol{u}}{{}^t\boldsymbol{u}\boldsymbol{u}}
    $$

    👉 **直交変換なので数値的に超安定**

    初心者の立ち位置

    * 「仕組みを完全理解」より
    * 「なぜ使われるか」を理解する
    * 実装はライブラリ任せでOK
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**ヤコビ法（対象行列専用）**

    ###特徴
    * 非対角成分を**1個ずつ潰す**
    * 対象行列に対して非常に直感的

    ### 長所
    * 数学的に分かりやすい
    * 「直交変換で対角化」を可視化しやすい

    ### 短所
    * 大規模行列では遅い
    """)
    return


@app.cell
def _(np):
    # 対称行列（収束が分かりやすい）
    A = np.array([
        [4, -1, 1],
        [-1, 4, -1],
        [1, -1, 4]
    ], dtype=float)
    A
    return (A,)


@app.cell
def _():
    return


@app.cell
def _(A, np):
    # 真の固有値（比較用）
    eigvals, eigvecs = np.linalg.eig(A)
    idx = np.argsort(-np.abs(eigvals))
    eigvals = eigvals[idx]

    lambda1 = eigvals[0]
    lambda2 = eigvals[1]
    ratio = abs(lambda2 / lambda1)

    lambda1, lambda2, ratio
    return lambda1, ratio


@app.cell
def _(A, lambda1, np, ratio):
    steps = 30
    mu_history = []

    # 初期ベクトル
    np.random.seed(0)
    x = np.random.rand(3)
    x /= np.linalg.norm(x)
    x

    # べき乗法
    for k in range(steps):
        x = A @ x
        x /= np.linalg.norm(x)

        mu = x @ A @ x
        mu_history.append(mu)

    mu_history = np.array(mu_history)

    # 最大固有値の推定（レイリー商）
    # lambda_max = x @ A @ x
    print(mu_history)

    # 理論収束曲線
    k = np.arange(steps)
    theoretical = abs(lambda1) * ratio**k
    return k, mu_history, theoretical, x


@app.cell
def _(k, lambda1, mu_history, plt, theoretical):
    # 可視化
    plt.figure()
    plt.semilogy(k, abs(mu_history - lambda1), label="|μ_k - λ1|")
    plt.semilogy(k, theoretical, "--", label="|λ2/λ1|^k (theory)")
    plt.xlabel("iteration k")
    plt.ylabel("error (log scale)")
    plt.legend()
    plt.grid(True)
    plt.show()
    return


@app.cell
def _(x):
    x
    return


if __name__ == "__main__":
    app.run()
