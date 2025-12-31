import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **基底**

    ベクトル空間 $V$のベクトルの組（**集合**）

    $$
    \{v_1, v_2, \cdots, v_n\}
    $$

    が、$V$の**基底**であるとは、


    * $V$を張る（$V$の任意のベクトルを$v_1, v_2, \cdots, v_n$の一次結合で表せる）

    * $v_1, v_2, \cdots, v_n$が一次独立である

    の両方を満たすことである。

    > **ベクトル空間$V$のすべてのベクトルを、ただ一通りに表せる最小限の材料セットのこと**

    基底の構成要素を、**基底ベクトル**という。

    ###**次元**
    ベクトル空間$V$の基底に含まれるベクトルの個数を、$V$の**次元**といい、$\text{dim}V$と表す。

    ただし、零ベクトル空間$V = \{\mathbb{O}\}$の次元は$\text{dim}V = 0$ と定める。


    **✅ 次元の一意性定理（線形代数の最重要定理の一つ）**
    > **任意のベクトル空間$V$の次元 $\text{dim}V$は、基底の取り方によらず一定**

    ### 零ベクトル空間
    零ベクトルだけからなる空間

    > **$n$次元ベクトル空間$V$において、$n$個の一次独立なベクトルの組は、$V$の基底となる**

    ベクトル空間の次元が分かっている場合の基底の判定に使用できる。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **例題20-1**
    ベクトルの組

    $$
    \boldsymbol{e_1} =
    \begin{bmatrix}
    1 \\ 0
    \end{bmatrix}, \quad
    \boldsymbol{e_2} =
    \begin{bmatrix}
    0 \\ 1
    \end{bmatrix}
    $$

    は$\mathbb{R^2}$の基底になることを示せ。

    ---

    (1)

    $$
    \mathbb{R^2}の任意のベクトル
    \begin{bmatrix}
    a \\ b
    \end{bmatrix}
    $$

    は、次のように$\boldsymbol{e_1}$と$\boldsymbol{e_2}$の一次結合で表せる。

    $$
    \begin{bmatrix}
    a \\ b
    \end{bmatrix} =
    \begin{bmatrix}
    a \\ 0
    \end{bmatrix} +
    \begin{bmatrix}
    0 \\ b
    \end{bmatrix} =
    a\boldsymbol{e_1} + b\boldsymbol{e_2}
    $$

    (2)

    $$
    E = \begin{bmatrix}
    \boldsymbol{e_1} &  \boldsymbol{e_2}
    \end{bmatrix} =
    \begin{bmatrix}
    1 &  0 \\
    0 & 1
    \end{bmatrix}
    $$

    $\text{det}E = 1\;(\neq 0)$であるから、$\boldsymbol{e_1}$と$\boldsymbol{e_2}$は一次独立である。

    (1), (2)より、$\boldsymbol{e_1}$と$\boldsymbol{e_2}$は、$\mathbb{R^2}$の基底となる。$\square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題20-3**
    次のベクトルの組が、$\mathbb{R^3}$の基底になる実数$a,b$の条件を求めよ。

    $$
    \boldsymbol{a_1} = \begin{bmatrix}1 \\ 1\\ 1 \end{bmatrix}, \quad
    \boldsymbol{a_2} = \begin{bmatrix}1 \\ a\\ a^2 \end{bmatrix}, \quad
    \boldsymbol{a_3} = \begin{bmatrix}1 \\ b\\ b^2 \end{bmatrix}
    $$


    <!-- ---

    $\text{dim}(\mathbb{R^3})=3$であるから、3つベクトル$\boldsymbol{a_1},\boldsymbol{a_2}, \boldsymbol{a_3}$が一次独立であれば、$\{\boldsymbol{a_1}, \boldsymbol{a_2}, \boldsymbol{a_3} \}$は$\mathbb{R^3}$の基底になる。

    ここで、

    $$
    A
    = \begin{bmatrix}
    \boldsymbol{a_1} & \boldsymbol{a_2} & \boldsymbol{a_3}
    \end{bmatrix} =
    \begin{bmatrix}
    1 & 1 & 1 \\
    1 & a & b \\
    1 & a^2 & b^2 \\
    \end{bmatrix}
    $$

    とする。$A$の行基本変形と列基本変形を行うと、

    ↑※行・列の基本変形ではなく、detAの余因子展開を行うべき！

    $$
    \begin{aligned}
    & \begin{bmatrix}
    1 & 1 & 1 \\
    1 & a & b \\
    0 & a^2 & b^2 \\
    \end{bmatrix}
    \\
    \\ \;\xrightarrow{\text{第1行}\times (-1) + \text{第2行}}\;
    &
    \begin{bmatrix}
    1 & 1 & 1 \\
    0 & a-1 & b-1 \\
    0 & a^2 & b^2 \\
    \end{bmatrix}
    \\
    \\ \;\xrightarrow{\text{第1行}\times (-1) + \text{第3行}}\;
    &
    \begin{bmatrix}
    1 & 1 & 1 \\
    0 & a-1 & b-1 \\
    0 & a^2-1 & b^2-1 \\
    \end{bmatrix}
    \\
    \\ \;\xrightarrow{\text{第1列}\times (-1) + \text{第2列}}\;
    &
    \begin{bmatrix}
    1 & 0 & 1 \\
    0 & a-1 & b-1 \\
    0 & a^2-1 & b^2-1 \\
    \end{bmatrix}
    \\
    \\ \;\xrightarrow{\text{第1列}\times (-1) + \text{第3列}}\;
    &
    \begin{bmatrix}
    1 & 0 & 0 \\
    0 & a-1 & b-1 \\
    0 & a^2-1 & b^2-1 \\
    \end{bmatrix}
    \end{aligned}
    $$

    これより


    ↓※detAを計算するならば、Aの行の基本変形か列の基本変形か、どちらか一方に統一するのが鉄則！


    $$
    \begin{aligned}
    \text{det}A &=
    \begin{array}{|ccc|}
    1 & 0 & 0 \\
    0 & a-1 & b-1 \\
    0 & a^2-1 & b^2-1 \\
    \end{array}\\ &=
    \begin{array}{|cc|}
    a-1 & b-1 \\
    a^2-1 & b^2-1 \\
    \end{array} \\ &=(a-1)(b^2-1) - (b-1)(a^2-1) \\
    &= (a-1)(b+1)(b-1) - (b-1)(a+1)(a-1) \\
    &= (a-1)(b-1)(a+b+2) \tag{*}
    \end{aligned}
    $$

    $\text{det}A \neq 0$ ならば、$\boldsymbol{a_1}, \boldsymbol{a_2}, \boldsymbol{a_3}$は一次独立である。

    このとき、$\{\boldsymbol{a_1}, \boldsymbol{a_2}, \boldsymbol{a_3}\}$は$\mathbb{R^3}$の基底となる。

    そのための条件は、(\*)より、$a \neq 1, b \neq 1, a+b \neq -2$である。$\square$ -->

    ---
    ### 模範解答

    $\boldsymbol{a_1},\boldsymbol{a_2}, \boldsymbol{a_3}$が $\mathbb{R}^3$ の基底となる条件を求める。

    $\dim\mathbb{R}^3=3$ より，
    3本のベクトルが一次独立であれば基底となる。

    列ベクトルを並べて

    $$
    A=
    \begin{bmatrix}
    1 & 1 & 1 \\
    1 & a & b \\
    1 & a^2 & b^2
    \end{bmatrix}
    $$

    とおく。

    $\det A$を**余因子展開**すると、

    $$
    \begin{aligned}
    \det A
    &=
    \begin{vmatrix}
    1 & 1 & 1 \\
    1 & a & b \\
    1 & a^2 & b^2
    \end{vmatrix}
    \\
    &=
    1\begin{vmatrix} a & b \\ a^2 & b^2 \end{vmatrix}
    1\begin{vmatrix} 1 & b \\ 1 & b^2 \end{vmatrix}
    +
    1\begin{vmatrix} 1 & a \\ 1 & a^2 \end{vmatrix}
    \\
    &=
    (ab^2 - ba^2) - (b^2 - b) + (a^2 - a)
    \\
    &=
    ab(b-a) - (b^2-b) + (a^2-a)
    \\
    &=
    (b-a)(ab - (a+b) + 1)
    \\
    &=
    (b-a)(a-1)(b-1)
    \end{aligned}
    $$

    ゆえに

    $$
    \det A = (a-1)(b-1)(b-a)
    $$

    である。
    したがって

    $$
    \det A \neq 0
    \iff
    a\neq1,\ b\neq1,\ a\neq b
    $$

    このとき
    ${\boldsymbol{a}_1,\boldsymbol{a}_2,\boldsymbol{a}_3}$ は
    $\mathbb{R}^3$ の基底である。
    $\square$









    <!-- ベクトル空間$V$の要素$\boldsymbol{v_1}, \boldsymbol{v_2}, \cdots \boldsymbol{v_n}$ -->
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 補足
    **ヴァンデルモンドの行列**

    $$
    \det
    \begin{bmatrix}
    1 & 1 & 1 \\
    1 & a & b \\
    1 & a^2 & b^2
    \end{bmatrix} =
    \prod_{i<j}(x_j-x_i)=
    (a-1)(b-1)(b-a)
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**生成される部分空間**

    ベクトル空間$V$の中のベクトルの組

    $$
    \boldsymbol{v}_1,\boldsymbol{v}_2,\dots,\boldsymbol{v}_k \in V
    $$

    に対して、

    $$
    \mathrm{span}\{\boldsymbol{v}_1,\dots,\boldsymbol{v}_k\} =
    \left\{
    c_1\boldsymbol{v}_1+\cdots+c_k\boldsymbol{v}_k
    \;\middle|\;
    c_1,\dots,c_k\in\mathbb{R}
    \right\} = \Big\{\sum_{i=1}^k c_i \boldsymbol{v}_i | \; c_i \in \mathbb{R}\Big\}
    $$

    を**$\boldsymbol{v}_1,\dots,\boldsymbol{v}_k$ が生成する$V$の部分空間（あるいは「張る部分空間」**という。

    > 与えられたベクトルの組から、一次結合によって作れるすべてのベクトルの集合
    >
    > 「そのベクトルたちを材料にして、作れる範囲全部」

    * 係数は自由（実数全部）
    * 足してもよい
    * スカラー倍してもよい

    **そうしてできる最小のベクトル空間が「生成される部分空間」**


    生成される部分空間とは
    「与えたベクトルで表現できる世界の全体」

    そして：

    * 表現できる世界が全体 → 基底
    * 表現できる世界が一部 → 部分空間

    ---
    #### 例1：$\mathbb{R}^2$

    $$
    \boldsymbol{v}= \begin{bmatrix}1\\2\end{bmatrix}, \quad
    \mathrm{span}\{\boldsymbol{v}\} =
    \left\{
    t\begin{bmatrix}1\\2\end{bmatrix}
    \mid t\in\mathbb{R}
    \right\}
    $$

    → 原点を通る1本の直線

    ####例2：$\mathbb{R}^2$ の2ベクトル

    $$
    \boldsymbol{e}_1=\begin{bmatrix}1 \\ 0\end{bmatrix},\;
    \boldsymbol{e}_2=\begin{bmatrix}0 \\ 1\end{bmatrix}, \;
    \mathrm{span}\{\boldsymbol{e}_1,\boldsymbol{e}_2\} = \mathbb{R}^2
    $$

    → 平面全体

    ####例3：一次従属な場合

    $$
    \boldsymbol{v}_1=\begin{bmatrix}1 \\ 1\end{bmatrix},\;
    \boldsymbol{v}_2=\begin{bmatrix}2 \\ 2\end{bmatrix}, \;
    \mathrm{span}\{\boldsymbol{v}_1,\boldsymbol{v}_2\} =
    \mathrm{span}\{\boldsymbol{v}_1\}
    $$

    $\boldsymbol{v_1} = 2\boldsymbol{v_2}$

    → 2本あっても、作れるのは1次元
    """)
    return


if __name__ == "__main__":
    app.run()
