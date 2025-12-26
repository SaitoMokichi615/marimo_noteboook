import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


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


if __name__ == "__main__":
    app.run()
