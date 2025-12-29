import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import sympy as sp
    return mo, sp


@app.cell
def _(mo):
    mo.md(r"""
    ###**表現行列**

    ベクトル空間$U, W$の線形写像$T:U \rightarrow W$について考える。

    $U$の基底$\{\boldsymbol{u_1}, \boldsymbol{u_2}, \dots , \boldsymbol{u_n}\}$と$W$の基底$\{\boldsymbol{w_1}, \boldsymbol{w_2}, \dots , \boldsymbol{w_m}\}$を取る。

    このとき、$T(\boldsymbol{u_1})$は$W$の要素のため、

    $$
    T(\boldsymbol{u_1}) = \sum_{i=1}^m{a_{i1} \boldsymbol{w_i}} \quad (a_{i1} \in \mathbb{R})
    $$

    と書ける。

    同様に、


    $$
    \begin{aligned}
    & T(\boldsymbol{u_2}) = \sum_{i=1}^m{a_{i2} \boldsymbol{w_i}} \quad (a_{i2} \in \mathbb{R}) \\
    & \vdots \\
    & T(\boldsymbol{u_n}) = \sum_{i=1}^m{a_{in} \boldsymbol{w_i}} \quad (a_{in} \in \mathbb{R}) \\
    \end{aligned}
    $$

    行列の形で整理すると、

    $$
    \begin{bmatrix}
    T(\boldsymbol{u_1}), & T(\boldsymbol{u_2}), & \dots &, T(\boldsymbol{u_n})
    \end{bmatrix}=
    \begin{bmatrix}
    \boldsymbol{w_1}, & \boldsymbol{w_2}, & \dots, & \boldsymbol{w_m}
    \end{bmatrix}
    \begin{bmatrix}
    a_{11} &  & \dots &a_{1m} \\
    \vdots &  &  & \vdots \\
    a_{n1} &  & \dots & a_{nm} \\
    \end{bmatrix}
    $$

    となる。

    上記の行列

    $$
    \begin{bmatrix}
    a_{11} &  & \dots &a_{1m} \\
    \vdots &  &  & \vdots \\
    a_{n1} &  & \dots & a_{nm} \\
    \end{bmatrix}
    $$

    を、$U$の基底$\{\boldsymbol{u_1}, \boldsymbol{u_2}, \dots , \boldsymbol{u_n}\}$と$W$の基底$\{\boldsymbol{w_1}, \boldsymbol{w_2}, \dots , \boldsymbol{w_m}\}$に関する**表現行列**という。
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ###**例題23-1**

    線形写像$T:\mathbb{R^3}\rightarrow \mathbb{R^2}$を次のように定義する。

    $$
    T(\boldsymbol{x}) = \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}\boldsymbol{x}　\quad (\boldsymbol{x} \in \mathbb{R^2})
    $$

    このとき、次の基底に関する$T$の表現行列を求めよ。

    ---

    (1)
    * $\mathbb{R^3}$の基底:

    $$
    \left\{
    \boldsymbol{e_1} = \begin{bmatrix}1 \\ 0 \\ 0 \end{bmatrix}, \;
    \boldsymbol{e_2} = \begin{bmatrix}0 \\ 1 \\ 0 \end{bmatrix}, \;
    \boldsymbol{e_3} = \begin{bmatrix}0 \\ 0 \\ 1 \end{bmatrix} \;
    \right\}
    $$

    * $\mathbb{R^2}$の基底:

    $$
    \left\{
    \boldsymbol{e'_1} = \begin{bmatrix}1 \\ 0 \end{bmatrix}, \;
    \boldsymbol{e'_2} = \begin{bmatrix}0 \\ 1 \end{bmatrix} \;
    \right\}
    $$

    ---

    $$
    \begin{aligned}
    T(\boldsymbol{e_1}) &=  \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}\boldsymbol{e_1} \\
    &= \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}
    \begin{bmatrix}1 \\ 0 \\0 \end{bmatrix} \\
    &= \begin{bmatrix}1 \\ 1 \end{bmatrix} = \boldsymbol{e'_1} + \boldsymbol{e'_2}
    \end{aligned}
    $$

    $$
    \begin{aligned}
    T(\boldsymbol{e_2}) &=  \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}\boldsymbol{e_2} \\
    &= \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}
    \begin{bmatrix}0 \\ 1 \\0 \end{bmatrix} \\
    &= \begin{bmatrix}4 \\ -1 \end{bmatrix} = 4\boldsymbol{e'_1} - \boldsymbol{e'_2}
    \end{aligned}
    $$

    $$
    \begin{aligned}
    T(\boldsymbol{e_3}) &=  \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}\boldsymbol{e_3} \\
    &= \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}
    \begin{bmatrix}0 \\ 0 \\1 \end{bmatrix} \\
    &= \begin{bmatrix}1 \\ 2 \end{bmatrix} = \boldsymbol{e'_1} + 2\boldsymbol{e'_2}
    \end{aligned}
    $$

    これより、

    $$
    \begin{aligned}
    \begin{bmatrix}T(\boldsymbol{e_1}), & T(\boldsymbol{e_2}), & T(\boldsymbol{e_3})\end{bmatrix}
    &=
    \begin{bmatrix}
    \boldsymbol{e'_1} + \boldsymbol{e'_2}, & 4\boldsymbol{e'_1} - \boldsymbol{e'_2}, & \boldsymbol{e'_1} + 2\boldsymbol{e'_2} \\
    \end{bmatrix} \\
    &= \begin{bmatrix}\boldsymbol{e'_1}, & \boldsymbol{e'_2}\end{bmatrix}
    \begin{bmatrix} 1  & 4 & 1 \\ 1 & -1 & 2
    \end{bmatrix}
    \end{aligned}
    $$

    <!-- よって、$T$に関する表現行列は、 -->
    よって、基底$\{\boldsymbol{e_1}, \boldsymbol{e_2}, \boldsymbol{e_3}\}$と基底$\{\boldsymbol{e'_1}, \boldsymbol{e'_2}\}$に関する表現行列は、

    $$
    \begin{bmatrix} 1  & 4 & 1 \\ 1 & -1 & 2 \end{bmatrix} \; \square
    $$

    ---

    (2)
    * $\mathbb{R^3}$の基底:

    $$
    \left\{
    \boldsymbol{a_1} = \begin{bmatrix}1 \\ 1 \\ 0 \end{bmatrix}, \;
    \boldsymbol{a_2} = \begin{bmatrix}1 \\ 0 \\ 1 \end{bmatrix}, \;
    \boldsymbol{a_3} = \begin{bmatrix}0 \\ 1 \\ 1 \end{bmatrix} \;
    \right\}
    $$

    * $\mathbb{R^2}$の基底:

    $$
    \left\{
    \boldsymbol{b_1} = \begin{bmatrix}1 \\ 1 \end{bmatrix}, \;
    \boldsymbol{b_2} = \begin{bmatrix}1 \\ 0 \end{bmatrix} \;
    \right\}
    $$

    ---

    $$
    \begin{aligned}
    T(\boldsymbol{a_1}) &=  \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}\boldsymbol{a_1} \\
    &= \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}
    \begin{bmatrix}1 \\ 1 \\0 \end{bmatrix} \\
    &= \begin{bmatrix}5 \\ 0 \end{bmatrix} = 5\boldsymbol{b_2}
    \end{aligned}
    $$

    $$
    \begin{aligned}
    T(\boldsymbol{a_2}) &=  \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}\boldsymbol{a_2} \\
    &= \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}
    \begin{bmatrix}1 \\ 0 \\1 \end{bmatrix} \\
    &= \begin{bmatrix}2 \\ 3 \end{bmatrix} = 3\boldsymbol{b_1} - \boldsymbol{b_2}
    \end{aligned}
    $$

    $$
    \begin{aligned}
    T(\boldsymbol{a_3}) &=  \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}\boldsymbol{a_3} \\
    &= \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}
    \begin{bmatrix}0 \\ 1 \\1 \end{bmatrix} \\
    &= \begin{bmatrix}5 \\ 1 \end{bmatrix} = \boldsymbol{b_1} + 4 \boldsymbol{b_2}
    \end{aligned}
    $$


    これより、

    $$
    \begin{aligned}
    \begin{bmatrix}T(\boldsymbol{a_1}), & T(\boldsymbol{a_2}), & T(\boldsymbol{a_3})\end{bmatrix}
    &=
    \begin{bmatrix}
    \boldsymbol5 \boldsymbol{b_2}, & 3\boldsymbol{b_1} - \boldsymbol{b_2}, & \boldsymbol{b_1} +4 \boldsymbol{b_2} \\
    \end{bmatrix} \\
    &= \begin{bmatrix}\boldsymbol{b_1}, & \boldsymbol{b_2}\end{bmatrix}
    \begin{bmatrix} 0  & 3 & 1 \\ 5 & -1 & 4
    \end{bmatrix}
    \end{aligned}
    $$

    <!-- よって、$T$に関する表現行列は、
    -->
    よって、基底$\{\boldsymbol{a_1}, \boldsymbol{a_2}, \boldsymbol{a_3}\}$と基底$\{\boldsymbol{b_1}, \boldsymbol{b_2}\}$に関する表現行列は、

    $$
    \begin{bmatrix} 0  & 3 & 1 \\ 5 & -1 & 4
    \end{bmatrix} \; \square
    $$

    ---

    (1)の表現行列は、$T$を定義した行列と同じ。

    これは標準基底の場合、必ず成立する。$A$を$m \times n$行列とするとき、

    線形写像

    $$
    T: \mathbb{R^m} \rightarrow \mathbb{R^n} \;(A \mapsto A \boldsymbol{x})
    $$

    に対して、

    $\mathbb{R^n}$の標準基底$\{\boldsymbol{e_1}, \boldsymbol{e_2}, \dots , \boldsymbol{e_n}\}$と$\mathbb{R^m}$の標準基底$\{\boldsymbol{e'_1}, \boldsymbol{e'_2}, \dots , \boldsymbol{e_m}\}$を取ると、
    <!-- $T$の表現行列は$A$自身となる。 -->
    標準基底$\{\boldsymbol{e_1}, \boldsymbol{e_2}, \dots , \boldsymbol{e_n}\}$と標準基底$\{\boldsymbol{e'_1}, \boldsymbol{e'_2}, \dots , \boldsymbol{e_m}\}$に関する表現行列は$A$自身となる。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**問題23-1**


    線形写像$T:\mathbb{R^3}\rightarrow \mathbb{R^2}$を次のように定義する。

    $$
    T(\boldsymbol{x}) = \begin{bmatrix}1 & 1 & 0 \\ 0 & 2 & 3  \end{bmatrix}\boldsymbol{x}　\quad (\boldsymbol{x} \in \mathbb{R^3})
    $$

    このとき、次の基底に関する$T$の表現行列を求めよ。

    ---

    * $\mathbb{R^3}$の基底:

    $$
    \left\{
    \boldsymbol{a_1} = \begin{bmatrix}1 \\ 0 \\ 0 \end{bmatrix}, \;
    \boldsymbol{a_2} = \begin{bmatrix}0 \\ 2 \\ 1 \end{bmatrix}, \;
    \boldsymbol{a_3} = \begin{bmatrix}1 \\ 1 \\ 1 \end{bmatrix} \;
    \right\}
    $$

    * $\mathbb{R^2}$の基底:

    $$
    \left\{
    \boldsymbol{b_1} = \begin{bmatrix}1 \\ 0 \end{bmatrix}, \;
    \boldsymbol{b_2} = \begin{bmatrix}1 \\ 1 \end{bmatrix} \;
    \right\}
    $$


    ---

    $$
    \begin{aligned}
    T(\boldsymbol{a_1}) &=  \begin{bmatrix}1 & 1 & 0 \\ 0 & 2 & 3
    \end{bmatrix}\boldsymbol{a_1} \\
    &= \begin{bmatrix}1 & 1 & 0 \\ 0 & 2 & 3 \end{bmatrix}
    \begin{bmatrix}1 \\ 0 \\0 \end{bmatrix} \\
    &= \begin{bmatrix}1 \\ 0 \end{bmatrix} = \boldsymbol{b_1}
    \end{aligned}
    $$

    $$
    \begin{aligned}
    T(\boldsymbol{a_2}) &=  \begin{bmatrix}1 & 1 & 0 \\ 0 & 2 & 3 \end{bmatrix}\boldsymbol{a_2} \\
    &= \begin{bmatrix}1 & 1 & 0 \\ 0 & 2 & 3  \end{bmatrix}
    \begin{bmatrix}0 \\ 2 \\1 \end{bmatrix} \\
    &= \begin{bmatrix}2 \\ 7 \end{bmatrix} = -5\boldsymbol{b_1} +7 \boldsymbol{b_2}
    \end{aligned}
    $$

    $$
    \begin{aligned}
    T(\boldsymbol{a_3}) &=  \begin{bmatrix}1 & 1 & 0 \\ 0 & 2 & 3 \end{bmatrix}\boldsymbol{a_3} \\
    &= \begin{bmatrix}1 & 1 & 0 \\ 0 & 2 & 3   \end{bmatrix}
    \begin{bmatrix}1 \\ 1 \\1 \end{bmatrix} \\
    &= \begin{bmatrix}2 \\ 5 \end{bmatrix} = -3\boldsymbol{b_1} + 5 \boldsymbol{b_2}
    \end{aligned}
    $$


    これより、


    $$
    \begin{aligned}
    \begin{bmatrix}T(\boldsymbol{a_1}), & T(\boldsymbol{a_2}), & T(\boldsymbol{a_3})\end{bmatrix}
    &=
    \begin{bmatrix}
    \boldsymbol{b_1,} &
    -5\boldsymbol{b_1} +7 \boldsymbol{b_2}, &
    -3\boldsymbol{b_1} + 5 \boldsymbol{b_2} \\
    \end{bmatrix} \\
    &= \begin{bmatrix}\boldsymbol{b_1}, & \boldsymbol{b_2}\end{bmatrix}
    \begin{bmatrix} 1  & -5 & -3 \\ 0 & 7 & 5
    \end{bmatrix}
    \end{aligned}
    $$

    <!-- よって、$T$に関する表現行列は、 -->
    よって、基底$\{\boldsymbol{a_1}, \boldsymbol{a_2}, \boldsymbol{a_3}\}$と基底$\{\boldsymbol{b_1}, \boldsymbol{b_2}\}$に関する表現行列は、


    $$
    \begin{bmatrix} 1  & -5 & -3 \\ 0 & 7 & 5
    \end{bmatrix} \; \square
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**基底変換**
    ベクトル空間$U, W$の間の線形写像$T:U\rightarrow W$を考える。

    $U$の基底$\{\boldsymbol{u_1}, \boldsymbol{u_2}, \dots, \boldsymbol{u_n}\}$と$W$の基底$\{\boldsymbol{w_1}, \boldsymbol{w_2}, \dots, \boldsymbol{w_m}\}$に関する$T$の表現行列$A$は、

    $$
    \boxed{
    \begin{bmatrix}
    T(\boldsymbol{u_1}), (T(\boldsymbol{u_2}), \dots, (T(\boldsymbol{u_n})
    \end{bmatrix}=
    \begin{bmatrix}\boldsymbol{w_1}, \boldsymbol{w_2}, \dots, \boldsymbol{w_m}\end{bmatrix}A　\tag{1.}
    }
    $$

    を満たす行列である。


    $U$の別の基底$\{\boldsymbol{u'_1}, \boldsymbol{u'_2}, \dots, \boldsymbol{u'_n}\}$と$W$の別の基底$\{\boldsymbol{w'_1}, \boldsymbol{w'_2}, \dots, \boldsymbol{w'_m}\}$に関する$T$の表現行列$B$は、

    $$
    \boxed{
    \begin{bmatrix}T(\boldsymbol{u'_1}), (T(\boldsymbol{u'_2}), \dots, (T(\boldsymbol{u'_n})\end{bmatrix} = \begin{bmatrix}\boldsymbol{w'_1}, \boldsymbol{w'_2}, \dots, \boldsymbol{w'_m}\end{bmatrix}B \tag{2.}
    }
    $$

    を満たす行列である。


    $$
    \boldsymbol{u'_i} = p_{1i}\boldsymbol{u_1} + p_{2i}\boldsymbol{u_2} + \cdots  + p_{ni}\boldsymbol{u_n}
    $$

    と表せるため、

    $$
    \begin{aligned}
    \begin{bmatrix}
    \boldsymbol{u'_1},\boldsymbol{u'_2},\dots, \boldsymbol{u'_n}
    \end{bmatrix} &=
    \begin{bmatrix}
    (p_{11}\boldsymbol{u_1}  + \dots  + p_{1n}\boldsymbol{u_n}),
    (p_{21}\boldsymbol{u_2}  + \dots  + p_{2n}\boldsymbol{u_n}),\dots
    (p_{n1}\boldsymbol{u_n}  + \dots  + p_{nn}\boldsymbol{u_n})
    \end{bmatrix}\\
    &=
    \begin{bmatrix}
    \boldsymbol{u_1}, & \boldsymbol{u_2},
    \dots
    \boldsymbol{u_n}
    \end{bmatrix}
    \begin{bmatrix}
    p_{11} & \dots & p_{1n} \\
    \vdots &  &  \vdots \\
    p_{n1} & \dots & p_{nn} \\
    \end{bmatrix}
    \end{aligned} \tag{3.}
    $$

    式(\3.)の行列


    $$
    P = \begin{bmatrix}
    p_{11} & \dots & p_{1n} \\
    \vdots &  &  \vdots \\
    p_{n1} & \dots & p_{nn} \\
    \end{bmatrix}
    $$

    を基底$\{\boldsymbol{u_1}, \boldsymbol{u_2}, \dots, \boldsymbol{u_n}\},\;$に関する**基底変換行列**という。

    すなわち、

    $$
    \boxed{
    \begin{bmatrix}
    \boldsymbol{u'_1}, & \boldsymbol{u'_2},
    \dots
    \boldsymbol{u'_n}
    \end{bmatrix} =
    \begin{bmatrix}
    \boldsymbol{u_1}, & \boldsymbol{u_2},
    \dots
    \boldsymbol{u_n}
    \end{bmatrix}P \tag{3'.}
    }
    $$

    ---

    $$
    \boxed{
    \begin{bmatrix}
    \boldsymbol{w'_1}, \boldsymbol{w'_2}, \dots, \boldsymbol{w'_m}
    \end{bmatrix} =
    \begin{bmatrix}
    \boldsymbol{w_1}, \boldsymbol{w_2}, \dots, \boldsymbol{w_m}
    \end{bmatrix}Q  \tag{4.}
    }
    $$

    を考える。

    (3.)の両辺に線形写像$T$を施すと、

    $$
    \begin{aligned}
    \begin{bmatrix}
    T(\boldsymbol{u'_1}), T(\boldsymbol{u'_2}), \dots, T(\boldsymbol{u'_n})
    \end{bmatrix} &=
    \begin{bmatrix}
    T(\boldsymbol{u_1}), T(\boldsymbol{u_2}), \dots, T(\boldsymbol{u_n})
    \end{bmatrix}P \\
    &=\begin{bmatrix}\boldsymbol{w_1}, \boldsymbol{w_2}, \dots, \boldsymbol{w_m}\end{bmatrix}AP \tag{5.}
    \end{aligned}
    $$

    一方、(2.), (4.)より、

    $$
    \begin{aligned}
    \begin{bmatrix}
    T(\boldsymbol{u'_1}), T(\boldsymbol{u'_2}), \dots, T(\boldsymbol{u'_n})
    \end{bmatrix} &=
    \begin{bmatrix}\boldsymbol{w'_1}, \boldsymbol{w'_2}, \dots, \boldsymbol{w'_m}\end{bmatrix}B\\
    &=\begin{bmatrix}
    \boldsymbol{w_1}, \boldsymbol{w_2}, \dots, \boldsymbol{w_m}
    \end{bmatrix}BQ \\
     \tag{6.}
    \end{aligned}
    $$

    (5.) - (6.)より、

    $$
    \begin{bmatrix}
    \boldsymbol{w_1}, \boldsymbol{w_2}, \dots, \boldsymbol{w_m}
    \end{bmatrix}(AP-BQ) = \begin{matrix}\mathbb{O_W}, \mathbb{O_W}, \dots , \mathbb{O_W}\end{matrix} \tag{7.}
    $$

    $\boldsymbol{w_1}, \boldsymbol{w_2}, \dots, \boldsymbol{w_m}$は一次独立であるから、(7.)より、

    $AP = BQ$

    よって、

    $$
    \boxed{
    B = Q^{-1}AP
    }
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ##  各行列が「何をしているか」

    ### 🔹 行列 $A$

    * **旧基底**

      * 定義域：$\{\boldsymbol{u_1},\dots,\boldsymbol{u_n}\}$
      * 値域：$\{\boldsymbol{w_1},\dots,\boldsymbol{w_m}\}$

    に関する **線形写像$T$の表現行列**

    ---

    ### 🔹 行列 $P$（定義域側の基底変換）

    $$
    \begin{bmatrix}
    \boldsymbol{u'_1} & \cdots & \boldsymbol{u'_n}
    \end{bmatrix}=
    \begin{bmatrix}
    \boldsymbol{u_1} & \cdots & \boldsymbol{u_n}
    \end{bmatrix}
    P
    $$

    👉

    * **新基底を旧基底で表す行列**
    * 「**座標を新 → 旧に直す**」役割

    ---

    ### 🔹 行列 $Q$（値域側の基底変換）

    $$
    \begin{bmatrix}
    \boldsymbol{w'_1} & \cdots & \boldsymbol{w'_m}
    \end{bmatrix}=
    \begin{bmatrix}
    \boldsymbol{w_1} & \cdots & \boldsymbol{w_m}
    \end{bmatrix}
    Q
    $$

    👉

    * **新基底を旧基底で表す行列**
    * 値域側の基底変換

    ---

    ## なぜ $B = Q^{-1}AP$ になるのか（意味）

    図で考えると理解しやすいです。

    ```
    [u']座標
       ↓ P（新→旧）
    [u ]座標
       ↓ A（線形写像T）
    [w ]座標
       ↓ Q^{-1}（旧→新）
    [w']座標
    ```

    つまり：

    1. 新基底の入力ベクトルを
       **旧基底に変換** $P$
    2. 旧基底で線形写像を作用 $A$
    3. 出力を
       **新基底に戻す**$Q^{-1}$

    これを1つの行列で表したものが **$B$**

    $$
    \boxed{
    B = Q^{-1}AP
    }
    $$

    ---

    ## 4️重要な直感的まとめ

    ### 🔑 表現行列は「基底依存」

    * 線形写像 $T$ そのものは変わらない
    * でも
      **「どの基底で測るか」** によって
      行列表現は変わる

    ---

    ### 🔑 基底変換の本質

    > **同じ写像を、違う座標系で見ているだけ**

    ---

    ## よくある混乱ポイント（超重要）

    | 混乱            | 正しい理解                |
    | ------------- | -------------------- |
    | $P$ は新→旧？旧→新？ | **新基底を旧基底で表す**       |
    | 左からか右からか      | **右から（列ベクトル）**       |
    | 逆行列の位置        | 値域側は **左に $Q^{-1}$** |

    ---

    ##  一言で言うと

    > **基底変換とは「座標の通訳」を行列で書いているだけ**
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ###**例題23-1(別解）**

    線形写像$T:\mathbb{R^3}\rightarrow \mathbb{R^2}$を次のように定義する。

    $$
    T(\boldsymbol{x}) = \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix}\boldsymbol{x}　\quad (\boldsymbol{x} \in \mathbb{R^2})
    $$

    このとき、次の基底に関する$T$の表現行列を求めよ。

    ---

    (1)
    * $\mathbb{R^3}$の基底:

    $$
    \left\{
    \boldsymbol{e_1} = \begin{bmatrix}1 \\ 0 \\ 0 \end{bmatrix}, \;
    \boldsymbol{e_2} = \begin{bmatrix}0 \\ 1 \\ 0 \end{bmatrix}, \;
    \boldsymbol{e_3} = \begin{bmatrix}0 \\ 0 \\ 1 \end{bmatrix} \;
    \right\}
    $$

    * $\mathbb{R^2}$の基底:

    $$
    \left\{
    \boldsymbol{e'_1} = \begin{bmatrix}1 \\ 0 \end{bmatrix}, \;
    \boldsymbol{e'_2} = \begin{bmatrix}0 \\ 1 \end{bmatrix} \;
    \right\}
    $$

    ---
    (2)
    * $\mathbb{R^3}$の基底:

    $$
    \left\{
    \boldsymbol{a_1} = \begin{bmatrix}1 \\ 1 \\ 0 \end{bmatrix}, \;
    \boldsymbol{a_2} = \begin{bmatrix}1 \\ 0 \\ 1 \end{bmatrix}, \;
    \boldsymbol{a_3} = \begin{bmatrix}0 \\ 1 \\ 1 \end{bmatrix} \;
    \right\}
    $$

    * $\mathbb{R^2}$の基底:

    $$
    \left\{
    \boldsymbol{b_1} = \begin{bmatrix}1 \\ 1 \end{bmatrix}, \;
    \boldsymbol{b_2} = \begin{bmatrix}1 \\ 0 \end{bmatrix} \;
    \right\}
    $$


    ---
    (1)の基底は標準基底である。ゆえに表現行列$A$は、$T$を定義した行列と同じ。

    すなわち、

    $$
    A = \begin{bmatrix}1 & 4 & 1 \\ 1 & -1 & 2  \end{bmatrix} \square
    $$

    (2)の別解

    $$
    \begin{bmatrix}
    \boldsymbol{a_1}, & \boldsymbol{a_2} & \boldsymbol{a_3}
    \end{bmatrix} =
    \begin{bmatrix}
    \boldsymbol{e_1}, & \boldsymbol{e_2} & \boldsymbol{e_3}
    \end{bmatrix}
    \begin{bmatrix}
    1 & 1 & 0 \\
    1 & 0 & 1 \\
    0 & 1 & 1
    \end{bmatrix}
    $$

    $$
    \begin{bmatrix}
    \boldsymbol{b_1}, & \boldsymbol{b_2}
    \end{bmatrix} =
    \begin{bmatrix}
    \boldsymbol{e'_1}, & \boldsymbol{e'_2}
    \end{bmatrix}
    \begin{bmatrix}
    1 & 1 \\
    1 & 0 \\
    \end{bmatrix}
    $$

    ここで

    $$
    P = \begin{bmatrix}
    1 & 1 & 0 \\
    1 & 0 & 1 \\
    0 & 1 & 1
    \end{bmatrix}
    ,\;Q = \begin{bmatrix}
    1 & 1 \\
    1 & 0 \\
    \end{bmatrix}
    $$

    とおくと、


    $$
    Q^{-1}=\begin{bmatrix}
    0 & 1 \\
    1 & -1 \\
    \end{bmatrix}
    $$

    よって、基底$\{\boldsymbol{a_1}, \boldsymbol{a_2}, \boldsymbol{a_3}\}$を基底$\{\boldsymbol{b_1}, \boldsymbol{b_2}\}$に関する$T$の表現行列は、

    $$
    \begin{aligned}
    Q^{-1}AP &= \begin{bmatrix}
    0 & 1 \\
    1 & -1 \\
    \end{bmatrix}
    \begin{bmatrix}
    1 & 4 & 1 \\
    1 & -1 & 2
    \end{bmatrix}
    \begin{bmatrix}
    1 & 1 & 0 \\
    1 & 0 & 1 \\
    0 & 1 & 1
    \end{bmatrix}\\ &=
    \begin{bmatrix}
    1 & -1 & 2 \\
    0 & 5 & -1
    \end{bmatrix}
    \begin{bmatrix}
    1 & 1 & 0 \\
    1 & 0 & 1 \\
    0 & 1 & 1
    \end{bmatrix}\\ &=
    \begin{bmatrix}
    0 & 3 & 1 \\
    5 & -1 & 4
    \end{bmatrix}
    \end{aligned} \square
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ###**線形変換**

    ベクトル空間$U$から$U$自身への線形写像$T:U \rightarrow U$を**線形変換**という。

    線形変換$T:U \rightarrow U$と$U$の基底$\{\boldsymbol{u_1},\boldsymbol{u_2}, \dots , \boldsymbol{u_n}\}$に対して、

    $$
    \begin{bmatrix}
    T(\boldsymbol{u_1}), & T(\boldsymbol{u_2}), \dots , T(\boldsymbol{u_n})
    \end{bmatrix} =
    \begin{bmatrix}
    \boldsymbol{u_1}, & \boldsymbol{u_2}, \dots , \boldsymbol{u_n}
    \end{bmatrix}A
    $$

    を満たす行列$A$を、**「基底$\{\boldsymbol{u_1},\boldsymbol{u_2}, \dots , \boldsymbol{u_n}  \}$に関する線形変換$T$の表現行列」**という。

    ---

    $U$の別の基底$\{\boldsymbol{u'_1},\boldsymbol{u'_2}, \dots , \boldsymbol{u'_n}\}$に関する$T$の表現行列を$B$とする。つまり、

    $$
    \begin{bmatrix}
    T(\boldsymbol{u'_1}), & T(\boldsymbol{u'_2}), \dots , T(\boldsymbol{u'_n})
    \end{bmatrix} =
    \begin{bmatrix}
    \boldsymbol{u'_1}, & \boldsymbol{u'_2}, \dots , \boldsymbol{u'_n}
    \end{bmatrix}B
    $$

    が成立する。

    また、

    $$
    \begin{bmatrix}\boldsymbol{u'_1},&\boldsymbol{u'_2},\dots , \boldsymbol{u'_n}\end{bmatrix}
     = \begin{bmatrix}
    \boldsymbol{u_1}, & \boldsymbol{u_2}, \dots , \boldsymbol{u_n}
    \end{bmatrix}P
    $$

    を満たす行列$P$を取る。

    このとき

    $$
    B = P^{-1}AP
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**例題23-2**
    線形変換$T:\mathbb{R^2}\rightarrow\mathbb{R^2}$を

    $$
    T(\boldsymbol{x}) = \begin{bmatrix}1 & -2 \\ 3 & -2\end{bmatrix}
    $$

    で定義する。

    このとき、基底

    $$
    \left\{\boldsymbol{u_1}=\begin{bmatrix}0 \\ 1 \end{bmatrix},\; \boldsymbol{u_2} = \begin{bmatrix}1 \\ 2 \end{bmatrix}\right\}
    $$

    に関する$T$の表現行列$B$を求めよ。

    ---

    $\mathbb{R^2}$の標準基底

    $$
    \left\{\boldsymbol{e_1} = \begin{bmatrix}1 \\ 0\end{bmatrix},\; \boldsymbol{e_2} = \begin{bmatrix}0 \\ 1\end{bmatrix}\right\}
    $$

    に関する$T$の表現行列$A$は、$T$を定義した行列と同じである。

    すなわち、

    $$
    A = \begin{bmatrix}1 & -2 \\ 3 & -2\end{bmatrix}
    $$

    $$
    \begin{bmatrix}
    \boldsymbol{u_1}, \boldsymbol{u_2}
    \end{bmatrix} =
    \begin{bmatrix}
    \boldsymbol{e_1}, \boldsymbol{e_2}
    \end{bmatrix}
    \begin{bmatrix}
    0 & 1\\
    1 & 2
    \end{bmatrix}
    $$

    である。

    $$
    P  =\begin{bmatrix}
    0 & 1\\
    1 & 2
    \end{bmatrix}
    $$

    とすると、

    $$
    P^{-1} = \begin{bmatrix}
    -2 & 1\\
    1 & 0
    \end{bmatrix}
    $$

    求める表現行列は

    $$
    \begin{aligned}
    B &= P^{-1}AP \\
    &= \begin{bmatrix}
    -2 & 1\\
    1 & 0
    \end{bmatrix}
    \begin{bmatrix}
    1 & -2 \\
    3 & -2
    \end{bmatrix}
    \begin{bmatrix}
    0 & 1\\
    1 & 2
    \end{bmatrix} \\
    &=
    \begin{bmatrix}
    1 & 2 \\
    1 & -2
    \end{bmatrix}
    \begin{bmatrix}
    0 & 1\\
    1 & 2
    \end{bmatrix} \\
    &= \begin{bmatrix}
    2 & 5\\
    -2 & -3
    \end{bmatrix} \square
    \end{aligned}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**例題23-3**
    多項式ベクトル空間$\mathbb{R}[x]_2$の線形変換$T$を

    $$
    T(ｆ) = f'(x) + f(1)x^2
    $$

    で定義する。


    (1)基底$\{1, x, x^2\}$に関する$T$の表現行列$A$を求めよ。

    (2)基底$\{1, 1+x, 1+x+x^2\}$に関する$T$の表現行列$B$を求めよ。


    ---
    (1)
    $\mathbb{R}[x]_2 = ax^2 + bx + c \;|\; a,b,c in \mathbb{R}$

    * $f(x) = 1$について、

    $f'(x)=0, f(1) = 1$であるから、$T(f) = T(1) = x^2$

    * $f(x) = x$について、

    $f'(x)=1, f(1) = 1$であるから、$T(f) = T(x) = 1 + x^2$

    * $f(x) = x^2$について、

    $f'(x)=2x, f(1) = 1$であるから、$T(f) = T(x^2) = 2x + x^2$

    これより、

    $$
    \begin{aligned}
    \begin{bmatrix}T(1),& T(x), & T(x^2)\end{bmatrix} &=
    \begin{bmatrix}x^2, & 1+x^2, & 2x + x^2 \end{bmatrix}\\ &=
    \begin{bmatrix}1, & x, & x^2\end{bmatrix}
    \begin{bmatrix}
    0 & 1 & 0 \\
    0 & 0 & 2 \\
    1 & 1 & 1 \\
    \end{bmatrix}\\&=
    \begin{bmatrix}1, & x, & x^2\end{bmatrix}A
    \end{aligned}
    $$

    よって、求める表現行列は

    $$
    A = \begin{bmatrix}
    0 & 1 & 0 \\
    0 & 0 & 2 \\
    1 & 1 & 1 \\
    \end{bmatrix} \square
    $$


    ---
    (2)

    $$
    \begin{bmatrix}
    1, & 1+x, & 1+x+x^2
    \end{bmatrix} =
    \begin{bmatrix}
    1, &x, &x^2
    \end{bmatrix}
    \begin{bmatrix}
    1 & 1 & 1\\
    0 & 1 & 1 \\
    0 & 0 & 1
    \end{bmatrix}
    $$

    $$
    P = \begin{bmatrix}
    1 & 1 & 1\\
    0 & 1 & 1 \\
    0 & 0 & 1
    \end{bmatrix}
    $$

    とすると、$\det{P} = 1$

    掃き出し法で逆行列$P^{-1}$を求めると、


    $$
    \begin{aligned}
    & \left[
    \begin{array}{ccc|ccc}
    1 & 1 & 1 & 1 & 0 & 0\\
    0 & 1 & 1 & 0 & 1 & 0\\
    0 & 0 & 1 & 0 & 0 & 1 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第1行} \leftarrow \text{第2行}\times (-1) + \text{第1行}}\;
    & \left[
    \begin{array}{ccc|ccc}
    1 & 0 & 0 & 1 & -1 & 0\\
    0 & 1 & 1 & 0 & 1 & 0\\
    0 & 0 & 1 & 0 & 0 & 1 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第2行} \leftarrow \text{第3行}\times (-1) + \text{第2行}}\;
    & \left[
    \begin{array}{ccc|ccc}
    1 & 0 & 0 & 1 & -1 & 0\\
    0 & 1 & 0 & 0 & 1 & -1\\
    0 & 0 & 1 & 0 & 0 & 1 \\
    \end{array}
    \right]
    \end{aligned}
    $$

    よって、

    $$
    P^{-1} = \begin{bmatrix}
    1 & -1 & 0\\
    0 & 1 & -1 \\
    0 & 0 & 1
    \end{bmatrix}
    $$

    よって、求める表現行列は

    $$
    \begin{aligned}
    B &= P^{-1}AP \\
    &= \begin{bmatrix}
    1 & -1 & 0\\
    0 & 1 & -1 \\
    0 & 0 & 1
    \end{bmatrix}
    \begin{bmatrix}
    0 & 1 & 0 \\
    0 & 0 & 2 \\
    1 & 1 & 1 \\
    \end{bmatrix}
    \begin{bmatrix}
    1 & 1 & 1\\
    0 & 1 & 1 \\
    0 & 0 & 1
    \end{bmatrix} \\
    &=
    \begin{bmatrix}
    0 & 1 & -2 \\
    -1 & -1 & 1 \\
    1 & 1 & 1 \\
    \end{bmatrix}
    \begin{bmatrix}
    1 & 1 & 1\\
    0 & 1 & 1 \\
    0 & 0 & 1
    \end{bmatrix} \\
    &= \begin{bmatrix}
    0 & 1 & -1\\
    -1 & -2 & -1 \\
    1 & 2 & 3
    \end{bmatrix} \square
    \end{aligned}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###補足

    **掃き出し法で逆行列が求まる理由**は：

    > 行基本変形は
    > **「左から可逆行列を掛ける操作」**であり、
    >
    > 単位行列を $P$ に変形する操作を
    > 同時に右側に適用すると、
    >
    > それが $P^{-1}$ になるから

    ---

    ### 行基本変形の正体

    行基本変形はすべて次の形で書けます：

    $$
    \text{（行基本変形）} \quad
    A ;\longmapsto; E A
    $$

    ここで：

    * $E$：**基本行列（elementary matrix）**
    * $E$ は必ず **可逆**

    ---

    ### 例

    * 行の入れ替え
    * 定数倍
    * 他の行の倍を足す

    すべて
    $
    E \times A
    $
    として書ける

    ---

    ### 掃き出し法でやっていること

    あなたがやった操作は：

    $$
    [P \mid I]
    ;\xrightarrow{\text{行基本変形}};
    [I \mid ?]
    $$

    これは数学的に

    $$
    E_k \cdots E_2 E_1
    \begin{bmatrix}
    P & I
    \end{bmatrix}=
    \begin{bmatrix}
    I & E_k \cdots E_2 E_1
    \end{bmatrix}
    $$

    を意味します。

    ---

    ### なぜ右側が逆行列になるのか

    左側が単位行列になったということは：

    $$
    E_k \cdots E_2 E_1 P = I
    $$

    つまり

    $$
    (E_k \cdots E_2 E_1) = P^{-1}
    $$

    したがって右側は：

    $$
    I ;\longmapsto; P^{-1}
    $$

    ---

    ### 式で一行で書くと

    $$
    \boxed{
    [E P \mid E I] = [I \mid P^{-1}]
    }
    \quad\text{（ただし }E=P^{-1}\text{）}
    $$

    ---

    ### 直感的な理解（かなり重要）

    ### 掃き出し法とは？

    > **「$P$ に左から何を掛けたら単位行列になるか」**
    > を実際に探している作業

    その「何」が **逆行列**

    ---

    ### なぜ連立方程式とも同じ方法で解けるのか

    連立方程式：

    $$
    Ax=b
    $$

    掃き出し法は：

    $$
    [A\mid b] \to [I\mid x]
    $$

    逆行列の場合：

    $$
    [P\mid I] \to [I\mid P^{-1}]
    $$

    👉 **同じ操作**

    ---

    ### 例との対応

    あなたの $P$ は：

    * 上三角
    * 対角成分がすべて 1
    * よって可逆

    行基本変形は

    $$
    E_2 E_1 P = I
    \Rightarrow
    P^{-1}=E_2 E_1
    $$

    ---

    ### 一言でまとめると

    > **掃き出し法とは
    > 「逆行列を実際に構成している過程」**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**問題23-3**
    線形変換$T:\mathbb{R^2}\rightarrow\mathbb{R^2}$を

    $$
    \begin{bmatrix}
    3 & -1 \\
    -2 & -1
    \end{bmatrix}\boldsymbol{x}
    $$

    で定義する。

    このとき、基底

    $$
    \left\{\boldsymbol{u_1} = \begin{bmatrix}3 \\1\end{bmatrix},\; \boldsymbol{u_2} = \begin{bmatrix}2 \\1\end{bmatrix}\right\}
    $$

    に関する$T$の表現行列$B$を求めよ。

    ---

    $\mathbb{R^2}$の標準基底

    $$
    \left\{\boldsymbol{e_1} = \begin{bmatrix}1 \\0\end{bmatrix},\; \boldsymbol{e_2} = \begin{bmatrix}0 \\1\end{bmatrix}\right\}
    $$

    に関する表現行列$A$は、$T$を定義した行列と同じである。

    ゆえに、

    $$
    A = \begin{bmatrix}
    3 & -1 \\
    -2 & -1
    \end{bmatrix}
    $$

    また、

    $$
    \begin{aligned}
    \begin{bmatrix}
    \boldsymbol{u_1}, & \boldsymbol{u_2}
    \end{bmatrix} =
    \begin{bmatrix}
    \boldsymbol{e_1}, & \boldsymbol{e_2}
    \end{bmatrix}
    \begin{bmatrix}
    3 & 2 \\
    1 & 1
    \end{bmatrix}
    \end{aligned}
    $$

    より、

    $$
    P = \begin{bmatrix}
    3 & 2 \\
    1 & 1
    \end{bmatrix}
    $$

    とすると、

    $$
    P^{-1} = \begin{bmatrix}
    1 & -2 \\
    -1 & 3
    \end{bmatrix}
    $$

    よって、求める表現行列は

    $$
    \begin{aligned}
    B &= P^{-1}AP \\
    &= \begin{bmatrix}
    1 & -2 \\
    -1 & 3
    \end{bmatrix}
    \begin{bmatrix}
    3 & -1 \\
    -2 & -1
    \end{bmatrix}
    \begin{bmatrix}
    3 & 2 \\
    1 & 1
    \end{bmatrix}\\
    &=
    \begin{bmatrix}
    7 & 1 \\
    -9 & -2
    \end{bmatrix}
    \begin{bmatrix}
    3 & 2 \\
    1 & 1
    \end{bmatrix}\\
    &=
    \begin{bmatrix}
    22 & 15 \\
    -29 & -20
    \end{bmatrix} \square
    \end{aligned}
    $$
    """)
    return


@app.cell
def _(sp):
    A = sp.Matrix([
        [3, -1],
        [-2, -1]
    ])

    P = sp.Matrix([
        [3, 2],
        [1, 1]
    ])

    P_inv = P.inv()

    A, P, P_inv
    return A, P, P_inv


@app.cell
def _(A, P, P_inv):
    B = P_inv * A * P
    B
    return


if __name__ == "__main__":
    app.run()
