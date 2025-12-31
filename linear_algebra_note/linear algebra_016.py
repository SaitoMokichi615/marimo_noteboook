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
    ### **ベクトル空間と部分空間**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題 16-1**

    $2 \times 2$型行列全体を $M2(\mathbb{R})$ と表す。

    $M2(\mathbb{R})$は行列の通常の和とスカラー倍でベクトル空間となる (これは認める)。

    このとき, 次の集合 $W1$, $W2$ は $M2(\mathbb{R}))$ の部分空間かどうか判定せよ。

    $$
    W1 = \Big\{ \begin{bmatrix}
    a & b \\
    c & d
    \end{bmatrix}
    \in M2(\mathbb{R}) \; | \;a=d=0\Big\}, \quad
    W2 = \Big\{ \begin{bmatrix}
    a & b \\
    c & d
    \end{bmatrix}
    \in M2(\mathbb{R}) \; | \;a+d=2\Big\}
    $$

    ---

    任意に$A \in W_1$, $B \in W_1$, $C \in W_2$, $D \in W_2$をとる。

    $$
    A = \begin{bmatrix}
    0 & a_{12} \\
    a_{21} & 0
    \end{bmatrix}, \quad
    B = \begin{bmatrix}
    0 & b_{12} \\
    b_{21} & 0
    \end{bmatrix}, \quad
    C = \begin{bmatrix}
    c_{11} & c_{12} \\
    c_{21} & c_{22}
    \end{bmatrix}, \quad
    D = \begin{bmatrix}
    d_{11} & d_{12} \\
    d_{21} & d_{22}
    \end{bmatrix}
    $$

    とすると、

    $$
    \alpha A + \beta B = \begin{bmatrix}
    0 & \alpha a_{12} + \beta b_{12}\\
    \alpha a_{21} + \beta b_{21}& 0
    \end{bmatrix}, \quad
    $$

    定義より、$\alpha A+\beta B \in W_1$ であるから、$W_1$は$M2(\mathbb{R}))$のベクトル空間である。

    $$
    \alpha C + \beta D = \begin{bmatrix}
    \alpha c_{11} + \beta d_{11} & \alpha c{12} + \beta c_{12}\\
    \alpha c_{21} + \beta d_{21}& \alpha c{22} + \beta d_{22}
    \end{bmatrix}, \quad
    $$

    $\alpha C + \beta D$の$(1, 1)$成分と$(2, 2)$成分の和は、


    $$
    \alpha c_{11} + \beta d_{11} + \alpha c_{22} + \beta d_{22}
    = \alpha(c_{11}+c_{22}) + \beta (d_{11} + d_{11}) \tag{*}
    $$

    となる。

    任意の$\alpha$,$\beta$に対して、(*) = 2 は成立しない。
    よって任意の$C$,$D$ に対して、$C \in W_2$、$D \in W_2$ は成立しない。
    したがって、$W_2$は部分空間ではない。$\square$

    ---

    $C,D \in W_2$ とすると
    $c_{11}+c_{22}=2,\; d_{11}+d_{22}=2$
    よって

    $$
    \alpha C+\beta D \text{ の対角和 } = 2(\alpha+\beta)
    $$

    これは一般には 2 にならない。
    例えば $\alpha=\beta=1$ とすると 4 となる。
    よって $W_2$ は部分空間ではない。$\square$

    ---

    >部分空間かどうかは
    >「原点を通るかどうか」でほぼ決まる
    >
    >$a+d=2$ は
    >「原点を通らない平面」なので
    >直感的にも部分空間ではない。

    >部分空間でないことを示すには：
    >「ある具体的な例で壊れる」
    >を示せば十分。



    <!-- ✓ ✏
    例題 16-3
    V をベクトル空間とし, W1, W2 が V の部分空間とする. このとき, W1 ∩ W2 も V の部分
    空間であることを示せ. ✒ ✑
    (解答)
    W1 ∩ W2 が定理 16-3 の (i),(ii),(iii) を満たすことを確認すればよい.
    (i) W1 と W2 はどちらも V の部分空間なので, O ∈ W1 かつ O ∈ -->
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題 16-2**

    $V$ をベクトル空間とし, $W_1$, $W_2$ が $V$ の部分空間とする. このとき,

    $$
    W_3 = \{\boldsymbol{u} + \boldsymbol{v} | \boldsymbol{u} ∈ W_1,\quad \boldsymbol{v} ∈ W_2\}
    $$

    は $V$ の部分空間であることを示せ.


    <!-- 任意の2つの$\boldsymbol{w_1}, \boldsymbol{w_2} \in W3$と、任意のスカラー$\alpha, \beta \in K$に対して次式が成立すれば、$W3$は$V$の部分空間である。

    $$
    \alpha \boldsymbol{w_1} + \beta\boldsymbol{w_2} \in V \tag{1}
    $$

    ここで、

    $$
    \begin{aligned}
    \boldsymbol{w_1} &= \boldsymbol{u_1} + \boldsymbol{v_1} \quad(\boldsymbol{u_1} ∈ W_1,\quad \boldsymbol{v_1} ∈ W_2) \\
    \boldsymbol{w_2} &= \boldsymbol{u_2} + \boldsymbol{v_2} \quad(\boldsymbol{u_2} ∈ W_1,\quad \boldsymbol{v_2} ∈ W_2) \\
    \end{aligned}
    $$

    とおくと、

    $$
    \begin{aligned}
    \alpha \boldsymbol{w_1} + \beta\boldsymbol{w_2}
    &= \alpha ( \boldsymbol{v_1} + \boldsymbol{u_1} ) + \beta(\boldsymbol{v_2} + \boldsymbol{u_2}) \\
    &= \alpha\boldsymbol{v_1} + \alpha\boldsymbol{u_1} + \beta\boldsymbol{v_2} + \beta\boldsymbol{u_2} \\
    &= \alpha(\boldsymbol{v_1} +\boldsymbol{v_2}) + \beta(\boldsymbol{u_2} +\boldsymbol{u_2})
    \end{aligned}
    $$

    $W1$, $W2$ が $V$の部分空間であるから、

    $\alpha(\boldsymbol{v_1} +\boldsymbol{v_2}) \in V,\quad \beta(\boldsymbol{u_2} +\boldsymbol{u_2}) \in V$ であり、

    その和もまた$V$の元である。
    すなわち、

    $$
    \alpha(\boldsymbol{v_1} +\boldsymbol{v_2}) + \beta(\boldsymbol{u_2} +\boldsymbol{u_2}) \in V　\tag{2}
    $$

    (1)と(2)より、$W3$は$V$の部分空間である。 -->

    ---


    任意に
    $\boldsymbol{w_1},\boldsymbol{w_2}\in W_3\quad(\alpha,\beta\in K)$を取る。


    定義より、ある$\boldsymbol{u_1},\boldsymbol{u_2}\in W_1$,
    $\boldsymbol{v_1},\boldsymbol{v_2}\in W_2$が存在して

    $$
    \boldsymbol{w_1}=\boldsymbol{u_1}+\boldsymbol{v_1},\quad
    \boldsymbol{w_2}=\boldsymbol{u_2}+\boldsymbol{v_2}
    $$

    と書ける。

    このとき

    $$
    \begin{aligned}
    \alpha\boldsymbol{w_1}+\beta\boldsymbol{w_2}
    &= \alpha(\boldsymbol{u_1}+\boldsymbol{v_1}) + \beta(\boldsymbol{u_2}+\boldsymbol{v_2})\\
    &= (\alpha\boldsymbol{u_1}+\beta\boldsymbol{u_2}) + (\alpha\boldsymbol{v_1}+\beta\boldsymbol{v_2}) \\
    \end{aligned}
    $$

    ここで

    * $W_1$ は部分空間なので
      $\alpha\boldsymbol{u_1}+\beta\boldsymbol{u_2}\in W_1$
    * $W_2$ は部分空間なので
      $\alpha\boldsymbol{v_1}+\beta\boldsymbol{v_2}\in W_2$

    よって$\alpha\boldsymbol{w_1}+\beta\boldsymbol{w_2}\in W_3$となる。

    以上より $W_3$ は $V$ の部分空間である。$\square$


    > $W_3$ が部分空間かどうかは
    > 「$W_3$の元の和を取ってもまた $W_1$ の元 + $W_2$ の元と書けるか」で決まる






    <!--
    問題 16-3 V をベクトル空間とし, W1, W2 が V の部分空間とする. W1 ∪ W2 が V の部分空間
    ならば, W1 ⊂ W2 または W2 ⊂ W1 となることを示せ -->
    """)
    return


if __name__ == "__main__":
    app.run()
