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
    ### 条件付確率
    ある試行にともなう2つの事象$A$,$B$に関し、$A$が起こったという状況の下で$B$が起こる確率を、**$A$が起こった時の$B$の起こる条件付確率**といい、**$P_A(B)$**で表す。

    ### 確率の乗法定理

    $$
    P(A\cap B) = P(A)\cdot P_A(B)
    $$

    これは、

    $$
    (AとBが同時に起きる確率) = (Aが起こる確率)\times(Aが起こった時のBの起こる確率)
    $$

    であることを示す。

    もし、$A$と$B$が**独立**ならば、$B$の起こる確率$P(B)$は$A$による影響を受けないため、

    $$
    P_A(B) = P(B)
    $$

    すなわち

    $$
    AとBが独立　\Leftrightarrow P(A \cap B) = P(A)\cdot P(B)
    $$


    $P(A)$と$P(A\cap B)$が既知ならば、条件付確率$P_A(B)$は、

    $$
    P_A(B) = \frac{P(A\cap B)}{P(A)} \quad (P(A) \neq 0)
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    「10本の中に2本の当たりが入っているくじを、甲、乙の2人がこの順に引く」

    という試行$T$を考察する。


    * 甲と乙が共に当たる確率$\;p$
    * 甲の当たりはずれによらず、乙が当たる確率$\;q$

    を求めよ。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$
    \left\{
    \begin{aligned}
    A &= 「甲が当たりを引く」 \\
    B &= 「乙が当たりを引く」
    \end{aligned}
    \right.
    $$

    とおくと、事象$A$が起きる確率$P(A)$は、

    $$
    P(A) = \frac{2}{10} = \frac{1}{5}　\tag{1}
    $$

    一方、乙が引くときには、くじが9本残っているが、その中で当たりのくじの本数は、甲が当たりを引いたか、外れたかで異なってくる。

    事象$A$が起こったとすると、乙は「9本中1本当たり」のくじを引くことになる。

    事象$A$が起こらなかったとすると、乙は「9本中2本当たり」のくじを引くことになる。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $A$が起きたときに$B$が起きた確率を$P_A(B)$、$A$が起きなかったときに$B$が起きた確率を$P_{\overline A}(B)$とすると、

    $$
    P_A(B) =  \frac{1}{9}, \quad P_{\overline A}(B) = \frac{2}{9} \tag{2}
    $$


    甲と乙が共に当たる確率$p$は、

    $$
    \begin{aligned}
    p &= P(A\cap B) \\
    &= P(A)\cdot P_B(A) \\
    &=\frac{1}{5} \cdot \frac{1}{9} = \frac{1}{45 } \tag{3}
    \end{aligned}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    甲の当たりはずれによらず、乙が当たる確率$q$は、事象$B$が起きる確率と等しい。

    また、事象$B$は2つの**排反事象**$A\cap B$と$\overline A \cap B$ の和事象である。

    ゆえに、

    $$
    \begin{aligned}
    q &= P(B) \\
    &= P(A\cap B) +  P(\overline A \cap B) \\
    &= P(A)\cdot P_a(B) +  P(\overline A)\cdot P_{\overline A}(B) \\
    &=\frac{1}{5} \cdot \frac{1}{9} + \frac{4}{5} \cdot \frac{2}{9} \\
    & = \frac{9}{45 } = \frac{1}{5} \tag{4}\\
    \end{aligned}
    $$

    (1)と(4)より、

    $$
    P(A) = P(B) = \frac{1}{5} \tag{5}
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    (5)より、事象$A$と事象$B$は等確率になる。

    * 乙は 甲の結果に影響されている（条件付き確率は変わる）
    * それでも最終的な確率は同じ

    この試行は本質的に

    > **10本のくじを無作為に並べ、
    > 上から順に引いている**

    のと同じである。

    * 当たりは2本
    * 外れは8本
    * 並び方はすべて等確率
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1回目,2回目,…,k回目に当たる確率の分布

    #### 確率分布

    任意の位置 $k=1,\dots,10$ について

    $$
    P(\text{k回目に当たり})=\frac{2}{10}=\frac{1}{5}
    $$

    つまり、

    * 横軸：引く順番（1〜10）
    * 縦軸：当たる確率

    をとると、**高さがすべて同じ棒グラフ**になる。

    これが
    「1回目に当たる確率＝2回目に当たる確率」
    の正体である（くじ引きの公平性）。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    数学的には：

    * 当たり 2 本が
    * 10 個の位置から
    * 重複なく選ばれる

    というモデルなので、

    * **超幾何分布**
    * 位置に注目すると **一様分布**

    になる。
    """)
    return


@app.cell
def _(np, plt):

    N = 10   # くじの本数
    K = 2    # 当たりの本数

    k = np.arange(1, N+1)
    p = np.full(N, K/N)  # 各位置で同じ確率

    plt.bar(k, p)
    plt.xlabel("何回目に引くか")
    plt.ylabel("当たる確率")
    plt.title("当たりが出る回数（位置）の分布")
    plt.show()

    return K, N


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###「最初に当たりが出る回数」の分布

    #### 数学的意味

    * 10本中2本が当たり
    * 無作為に並べて上から引く
    * **最初の当たりが k 回目に出る確率**

    これは **超幾何分布に基づく「初成功時刻」の分布**となる。

    #### 確率

    $$
    P(\text{最初の当たりが }k\text{回目}) =
    \frac{\binom{10-k}{1}}{\binom{10}{2}}
    \quad (k=1,\dots,9)
    $$
    """)
    return


@app.cell
def _(K, N, comb, np, plt):
    k_ = np.arange(1, N)  # 1〜9回目
    p_first = [comb(N - i, K - 1) / comb(N, K) for i in k_]

    plt.figure()
    plt.bar(k_, p_first)
    plt.xlabel("k 回目に最初の当たり")
    plt.ylabel("確率")
    plt.title("最初に当たりが出る回数の分布")
    plt.show()

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###「2人がともに当たる／片方だけ当たる」の分布

    #### 事象の整理

    * 甲・乙の2人が順に1本ずつ引く
    * 当たりは2本

    考える結果は3通り：

    | 状態 | 意味          |
    | -- | ----------- |
    | 0  | 誰も当たらない     |
    | 1  | どちらか1人だけ当たる |
    | 2  | 2人とも当たる     |

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 確率（超幾何分布）

    $$
    \begin{aligned}
    P(2) &= \frac{\binom{2}{2}\binom{8}{0}}{\binom{10}{2}} = \frac{1}{45} \\
    P(1) &= \frac{\binom{2}{1}\binom{8}{1}}{\binom{10}{2}} = \frac{16}{45} \\
    P(0) &= \frac{\binom{2}{0}\binom{8}{2}}{\binom{10}{2}} = \frac{28}{45} \\
    \end{aligned}
    $$
    """)
    return


@app.cell
def _(comb, plt):
    p_both = comb(2,2)*comb(8,0)/comb(10,2)
    p_one  = comb(2,1)*comb(8,1)/comb(10,2)
    p_none = comb(2,0)*comb(8,2)/comb(10,2)

    labels = ["誰も当たらない", "1人だけ当たる", "2人とも当たる"]
    probs = [p_none, p_one, p_both]

    plt.figure()
    plt.bar(labels, probs)
    plt.xlabel("結果")
    plt.ylabel("確率")
    plt.title("甲・乙の当たり方の分布")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
