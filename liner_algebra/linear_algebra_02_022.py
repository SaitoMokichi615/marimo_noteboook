import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from sympy import Matrix
    return Matrix, mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ベクトル空間$U$, $W$の間の写像$T:U\rightarrow W$が

    全ての$\boldsymbol{u}, \boldsymbol{u'} \in U, \alpha, \beta \in \mathbb{R}$に対して、

    $$
    T(\alpha\boldsymbol{u}+ \beta \boldsymbol{u'})=\alpha T(\boldsymbol{u}) + \beta T(\boldsymbol{u'})
    $$

    を満たすならば、写像$T$は**線形写像**である。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題22-1(1)**
    写像$T\;\mathbb{R^2}\rightarrow \mathbb{R}$を次のように定義する時、$T$は線形写像かどうか調べよ。

    ---

    $$
    T\left(\begin{bmatrix}x \\ y\end{bmatrix} \right) = x + y
    $$

    任意の$x,y, x', y', \alpha, \beta \in \mathbb{R}$について、

    $$
    \begin{aligned}
    T\left(\alpha\begin{bmatrix}x \\ y\end{bmatrix} +\beta \begin{bmatrix}x' \\ y' \end{bmatrix} \right) &=
    T\left(\begin{bmatrix}\alpha x + \beta x' \\ \alpha y + \beta y' \end{bmatrix}\right) \\
    &= (\alpha x + \beta x' ) + (\alpha y + \beta y') \\
    &= \alpha(x + y) + \beta(x' + y') \\
    &= \alpha T\left(\ \begin{bmatrix}x \\ y \end{bmatrix}\right) + \beta T\left(\ \begin{bmatrix}x' \\ y' \end{bmatrix}\right)
    \end{aligned}
    $$

    であるから、写像$T$は線形写像である。$\square$

    ---

    線形写像$T$は、行列を用いると

    $$
    T\left(\begin{bmatrix}x \\ y\end{bmatrix}\right) = \begin{bmatrix}1 & 1 \end{bmatrix}\begin{bmatrix}x \\ y \end{bmatrix}
    $$

    と表すことが出来る。
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題22-1(2)**
    写像$T:\;\mathbb{R^2}\rightarrow \mathbb{R}$を次のように定義する時、$T$は線形写像かどうか調べよ。

    ---

    <!-- $$
    T\left(\begin{bmatrix}x \\ y\end{bmatrix} \right) = x^2 + y^2
    $$

    $x=1, y=1$とすると、

    $$
    \begin{aligned}
    T\left(\begin{bmatrix}1 \\ 1\end{bmatrix} + \begin{bmatrix}1 \\ 1\end{bmatrix} \right) &= T\left(\begin{bmatrix}2 \\ 2\end{bmatrix} \right) \\ &= 2^2 + 2^2 = 8 \\
    \end{aligned} \tag{*}
    $$

    $$
    \begin{aligned}
    T\left(\begin{bmatrix}1 \\ 1\end{bmatrix}\right) + T\left(\begin{bmatrix}1 \\1 \end{bmatrix}\right)
    &= (1^2 + 1^2) + (1^2 + 1^2) = 4 \\
    \end{aligned} \tag{**}
    $$

    (\*),(\**)より、

    $$
    T\left(\begin{bmatrix}1 \\ 1\end{bmatrix} + \begin{bmatrix}1 \\ 1\end{bmatrix} \right) \neq T\left(\begin{bmatrix}1 \\ 1\end{bmatrix}\right) + T\left(\begin{bmatrix}1 \\1 \end{bmatrix}\right)
    $$

    であるから、写像$T$は線形写像ではない。$\square$ -->

    線形写像であるならば、任意の $\boldsymbol{u}, \boldsymbol{u'} \in \mathbb{R}^2$ に対して

    $$
    T\left(\boldsymbol{u}+\boldsymbol{u'}\right)=T(\boldsymbol{u})+T(\boldsymbol{u'})
    $$

    が成り立つ必要がある。

    ここで

    $$
    \boldsymbol{u}=\boldsymbol{u'}=\begin{bmatrix}1 \\ 1\end{bmatrix}
    $$

    とおくと，

    $$
    \begin{aligned}
    T(\boldsymbol{u}+\boldsymbol{u'})
    &= T\left(\begin{bmatrix}2 \\ 2\end{bmatrix}\right)
    = 2^2 + 2^2 = 8
    \end{aligned}
    $$

    一方，

    $$
    \begin{aligned}
    T(\boldsymbol{u})+T(\boldsymbol{u'})
    &= (1^2+1^2) + (1^2+1^2) = 4
    \end{aligned}
    $$

    よって

    $$
    T(\boldsymbol{u}+\boldsymbol{u'}) \neq T(\boldsymbol{u})+T(\boldsymbol{u'})
    $$

    である。

    したがって $T$ は線形写像ではない。$\square$


    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題22-2**
    写像$T\;\mathbb{R}[x]_n\rightarrow \mathbb{R}[x]_{n-1}$を次のように定義する時、$T$は線形写像かどうか調べよ。

    ただし、$\mathbb{R}[x]_n$は$n$次以下の実数係数多項式のなすベクトル空間である。

    $$
    T\left(f(x) \right) = f'(x)
    $$

    任意の$f(x), g(x) \in \mathbb{R}[x]_n$、任意の$\alpha, \beta \in \mathbb{R}$について、
    微分は線形性であるから、

    <!-- $$
    \begin{aligned}
    f(x) &= \sum_{k=0}^n a_kx^k \quad (a_k \in \mathbb{R}) \\
    g(x) &= \sum_{k=0}^n b_kx^k \quad (b_k \in \mathbb{R}) \\
    \end{aligned}
    $$

    であるから、

    $$
    \begin{aligned}
    f'(x) &= \sum_{k=0}^n ka_kx^{k-1} \\
    g'(x) &= \sum_{k=0}^n kb_kx^{k-1}
    \end{aligned}
    $$ -->



    $$
    \begin{aligned}
    T\left(\alpha f(x)+\beta g(x) \right) &=
    \left(\alpha f(x)+\beta g(x) \right)' \\
    &= \alpha f'(x)+\beta g'(x)  \\
    &= \alpha T\left(f(x)\right)+\beta T\left(g(x)\right)
    \end{aligned}
    $$

    よって、$T$は線形写像である。$\square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $m \times n$ 行列$A$について、写像$\mathbb{R^m}\rightarrow\mathbb{R}^n$を

    $$
    T(\boldsymbol{x})=A\boldsymbol{x}
    $$

    と定義すると、$T$は**線形写像**である。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $U, W$をベクトル空間とし、それぞれの零ベクトルを$\mathbb{O}_U, \mathbb{O}_W$とすると、

    線形写像$T:U \rightarrow W$について、次が成り立つ

    $$
    T(\mathbb{O}_U) =  \mathbb{O}_W \tag{*}
    $$

    ---
    $\mathbb{O}_U = \mathbb{O}_U + \mathbb{O}_U$であるから、

    $$
    \begin{aligned}
    T(\mathbb{O}_U) &= T(\mathbb{O}_U + \mathbb{O}_U)\\ &= T(\mathbb{O}_U) + T(\mathbb{O}_U)
    \end{aligned}
    $$

    両辺から$T(\mathbb{O}_U)$を引くと、$T(\mathbb{O}_U) \in W$であるから、
    $T(\mathbb{O}_U)-T(\mathbb{O}_U) = \mathbb{O}_W$

    よって(\*)を得る。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    線形写像$T: U \rightarrow W$について考える。

    ###**像**
    $W$の部分集合

    $$
    \text{Im}(T) \coloneqq \left\{T(x) \;| x \in U \right\}
    $$

    を$T$の**像(またはイメージ$T$)**と呼ぶ。

    $\dim\left(\text{Im}(T)\right)$を$T$の**階数**といい、$\text{rank}(T)$と表す。

    ###**核**
    $U$の部分集合

    $$
    \text{Ker}(T) \coloneqq \left\{x \in U \;| T(x) = \mathbb{O}_W \right\}
    $$

    を$T$の**核(またはカーネル$T$)**と呼ぶ。

    $\dim\left(\text{Ker}(T)\right)$を$T$の**退化次数**といい、$\text{null}(T)$と表す。

    | 観点    | 核         | 像        |
    | ----- | --------- | -------- |
    | 属する空間 | 入力側 (U)   | 出力側 (W)  |
    | 意味    | つぶれる方向    | 到達できる方向  |
    | 計算    | (Ax=0)    | (Ax) の全体 |
    | 幾何    | 原点に押し潰される | 写像後の広がり  |


    **線形写像は「核を潰し、像に射影する操作」**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**例題22-3**
    線形写像$T: \mathbb{R}^2 \rightarrow \mathbb{R}^2$ を次のように定義する。

    $$
    T\left(\begin{bmatrix} x \\ y \end{bmatrix}\right) = \begin{bmatrix} x \\ x \end{bmatrix}
    $$

    (1)核$\text{Ker}\left(T\right)$の1組の基底と退化次数$\text{null}(T)$を求めよ。

    (2)像$\text{Im}\left(T\right)$の1組の基底と階数$\text{rank}(T)$を求めよ。

    ---

    (1)

    $$
    \begin{aligned}
    \text{Ker}\left(T\right) &= \left\{ \begin{bmatrix} x \\ y \end{bmatrix} \in \mathbb{R^2} \Big | T\left(\begin{bmatrix} x \\ y \end{bmatrix} \right) = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \right\} \\
    &= \left\{ \begin{bmatrix} x \\ y \end{bmatrix} \in \mathbb{R^2} \Big | \begin{bmatrix} x \\ x \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \right\}\\
    &= \left\{ \begin{bmatrix} x \\ y \end{bmatrix} \in \mathbb{R^2} \Big | x=0 \right\}\\
    &= \left\{ y\begin{bmatrix} 0 \\ 1 \end{bmatrix} \in \mathbb{R^2} \Big | x=0 \right\}\\
    \end{aligned}
    $$

    これより、

    $$
    \left\{\begin{bmatrix} 0 \\ 1 \end{bmatrix}\right\}
    $$

    は$\text{Ker}\left(T\right)$の基底であり、

    $\text{null}(T) = \dim \left( \text{Ker}\left(T\right) \right) = 1 \; \square$

    ---

    (2)

    $$
    \begin{aligned}
    \text{Im}\left(T\right) &= \left\{T\left(\begin{bmatrix} x \\ y \end{bmatrix} \right) \;\Big| x,y \in \mathbb{R} \right\} \\
    &= \left\{\begin{bmatrix} x \\ x \end{bmatrix}  \;\Big| x,y \in \mathbb{R} \right\} \\
    &= \left\{x\begin{bmatrix} 1 \\ 1 \end{bmatrix}  \;\Big| x \in \mathbb{R} \right\}
    \end{aligned}
    $$

    これより、

    $$
    \left\{\begin{bmatrix} 1 \\ 1 \end{bmatrix}\right\}
    $$

    は$\text{Im}\left(T\right)$の基底であり、

    $\text{rank}(T) = \dim \left( \text{Im}\left(T\right) \right) = 1 \; \square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**例題22-4**
    線形写像$T: \mathbb{R}^4 \rightarrow \mathbb{R}^3$ を次のように定義する。

    $$
    T\left(\boldsymbol{x} \right) =
    \begin{bmatrix}
    2 & 4 & 3 & 1 \\
    0 & 0 & 1 & 1 \\
    1 & 2 & 1 & 0 \\
    \end{bmatrix}\boldsymbol{x}
    $$

    (1)核$\text{Ker}\left(T\right)$の1組の基底と退化次数$\text{null}(T)$を求めよ。

    (2)像$\text{Im}\left(T\right)$の1組の基底と階数$\text{rank}(T)$を求めよ。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    (1)
    (i)

    $$
    \begin{aligned}
    \text{Ker}\left(T\right) &= \left\{ \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} \in \mathbb{R^4} \;\Big |\; T\left(\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} \right) = \begin{bmatrix} 0 \\ 0 \\0 \\ 0\end{bmatrix} \right\} \\
    &= \left\{ \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} \in \mathbb{R^4} \;\Big |\; \begin{bmatrix}
    2 & 4 & 3 & 1 \\
    0 & 0 & 1 & 1 \\
    1 & 2 & 1 & 0 \\
    \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\0 \\ 0\end{bmatrix} \right\} \\
    \end{aligned}
    $$

    条件の係数行列を基本変形で簡略化すると、


    $$
    \begin{aligned}
    & \left[
    \begin{array}{cccc|c}
    2 & 4 & 3 & 1 &0\\
    0 & 0 & 1 & 1 &0\\
    1 & 2 & 1 & 0 &0\\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第1行} \leftarrow \text{第3行}\times (-2) + \text{第1行}}\;
    & \left[
    \begin{array}{cccc|c}
    0 & 0 & 1 & 1 &0\\
    0 & 0 & 1 & 1 &0\\
    1 & 2 & 1 & 0 &0\\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第1行} \leftarrow \text{第2行}\times (-1) + \text{第1行}}\;
    & \left[
    \begin{array}{cccc|c}
    0 & 0 & 0 & 0 &0\\
    0 & 0 & 1 & 1 &0\\
    1 & 2 & 1 & 0 &0\\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第1行}\leftrightarrow\text{第3行}}\;
    & \left[
    \begin{array}{cccc|c}
    1 & 2 & 1 & 0 &0\\
    0 & 0 & 1 & 1 &0\\
    0 & 0 & 0 & 0 &0\\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第1行} \leftarrow \text{第2行}\times (-1) + \text{第1行}}\;
    & \left[
    \begin{array}{cccc|c}
    1 & 2 & 0 & -1 &0\\
    0 & 0 & 1 & 1 &0\\
    0 & 0 & 0 & 0 &0\\
    \end{array}
    \right]
    \end{aligned}
    $$


    これより、

    $$
    \begin{aligned}
    \text{Ker}\left(T\right) &= \left\{ \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} \in \mathbb{R^4} \;\Big |\; \begin{aligned}x_1 + 2x_2 -x_4 = 0 \\ x_3 + x_4 = 0\end{aligned} \right\} \\
    \end{aligned}
    $$

    * 自由変数: $x_2, x_4$
    * 従属変数: $x_1 = -2x_2 + x_4, x_3 = -x_4$
    であるから、

    $$
    \begin{aligned}
    \text{Ker}\left(T\right) &= \left\{ \begin{bmatrix} -2x_2+x_4 \\ x_2 \\ -x_4 \\ x_4 \end{bmatrix}  \;\Big |\; \begin{aligned}x_2, x_4 \in \mathbb{R}\end{aligned} \right\} \\
    &= \left\{ x_2\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + x_4\begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix} \in \mathbb{R^4} \;\Big |\; \begin{aligned}x_2, x_4 \in \mathbb{R}\end{aligned} \right\}
    \end{aligned}
    $$

    これより、$\text{Ker}\left(T\right)$の任意の元は、

    $$
    \boldsymbol{u_1} = \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix},\; \boldsymbol{u_2} =\begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix}
    $$

    の一次結合で表すことが出来る（$\boldsymbol{u_1}, \boldsymbol{u_2}$は$\text{Ker}\left(T\right)$を生成する）

    ---

    (ii)
    $c_1\boldsymbol{u_1} + c_2\boldsymbol{u_2} = \mathbb{O}$とすると、

    $$
    c_1\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix}+c_2\begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}
    $$

    $$
    \begin{cases}
    -2c_1 + c_2 = 0 \\
    c_1 = 0 \\
    -c_2 = 0 \\
    c_2 = 0
    \end{cases}
    $$

    より、$c_1 = c_2 = 0$であるから、$\boldsymbol{u_1}, \boldsymbol{u_2}$は一次独立である。

    ---

    (i),(ii)より、$\boldsymbol{u_1}, \boldsymbol{u_2}$は$\text{Ker}(T)$の基底であり、

    $\text{null}(T) = \dim \left( \text{Ker}\left(T\right) \right) = 2 \; \square$


    ---
    ### 補足

    **重複している計算はどこか？**

    🔁 重複しているのは

    > (ii) で一次独立性を「連立方程式で再確認している部分」

    **実は、(i) の段階で一次独立性はすでに保証されている**

    #### 理由：

    * 自由変数が 2つ
    * 解空間が$\{x_2\boldsymbol{u_1} + x_4\boldsymbol{u_2} \}$と書けている

    👉 この時点で「$\boldsymbol{u_1}, \boldsymbol{u_2}$は一次独立かつ核を生成する」ことが理論的に自動で成立する。

    > 行列を階段形にして、$\text{自由変数の数} = \text{核の次元}$
    >
    > そのときに得られるベクトルは自動的に一次独立。

    つまり：

    > ガウス消去法
    >
    > → 解空間のパラメータ表示
    >
    > → その係数ベクトルは基底

    #### 簡略版

    これより連立方程式は

    $$
    \begin{cases}
    x_1 + 2x_2 - x_4 = 0 \\
    x_3 + x_4 = 0
    \end{cases}
    $$

    となる。

    自由変数を $x_2, x_4$ とすると，

    $$
    \begin{aligned}
    x_1 &= -2x_2 + x_4 \\
    x_3 &= -x_4
    \end{aligned}
    $$

    よって

    $$
    \text{Ker}(T)= \left\{
    x_2\begin{bmatrix}-2 \\ 1 \\ 0 \\0\end{bmatrix}+ x_4\begin{bmatrix}1\\0\\-1\\1\end{bmatrix}
    \;\Bigg|\;
    x_2,x_4\in\mathbb{R}
    \right\}
    $$

    したがって

    $\text{null}(T)=2$であり，

    $$
    \left\{
    \begin{bmatrix}-2\\1\\0\\0\end{bmatrix},
    \begin{bmatrix}1\\0\\-1\\1\end{bmatrix}
    \right\}
    $$

    は $\text{Ker}(T)$ の基底である。$\square$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    (2)

    (i)

    $$
    \begin{aligned}
    \text{Im}\left(T\right) &= \left\{T\left(\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} \right) \;\Bigg| x_1,x_2,x_3,x_4 \in \mathbb{R} \right\} \\
    &= \left\{\begin{bmatrix}
    2 & 4 & 3 & 1 \\
    0 & 0 & 1 & 1 \\
    1 & 2 & 1 & 0 \\
    \end{bmatrix}
    \begin{bmatrix}x_1 \\ x_2 \\ x_3 \\ x_4\end{bmatrix}
    \;\Bigg| x_1,x_2,x_3,x_4 \in \mathbb{R}
    \right\}\\
    &=\left\{\begin{bmatrix}
    2x_1 + 4x_2 + 3x_3+ x_4 \\
    x_3 + x_4 \\
    x_1 +2x_2 + x_3 \\
    \end{bmatrix}
    \;\Bigg| x_1,x_2,x_3,x_4 \in \mathbb{R}
    \right\}\\
    &=\left\{x_1\begin{bmatrix}
    2 \\0 \\ 1
    \end{bmatrix}+
    x_2\begin{bmatrix}
    4 \\0 \\ 2
    \end{bmatrix}+
    x_3\begin{bmatrix}
    3 \\1 \\ 1
    \end{bmatrix}+
    x_4\begin{bmatrix}
    1 \\1 \\ 0
    \end{bmatrix}
    \;\Bigg| x_1,x_2,x_3,x_4 \in \mathbb{R}
    \right\}
    \end{aligned}
    $$

    これより、$\text{Im}(T)$の任意の元は

    $$
    \boldsymbol{a_1} = \begin{bmatrix}
    2 \\0 \\ 1
    \end{bmatrix}, \;
    \boldsymbol{a_2} = \begin{bmatrix}
    4 \\0 \\ 2
    \end{bmatrix}, \;
    \boldsymbol{a_3} = \begin{bmatrix}
    3 \\1 \\ 1
    \end{bmatrix}, \;
    \boldsymbol{a_4} = \begin{bmatrix}
    1 \\1 \\ 0
    \end{bmatrix}
    $$

    の一次結合で表すことが出来る。

    （$\text{Im}(T)$は、$\boldsymbol{a_1}, \boldsymbol{a_2}, \boldsymbol{a_3}, \boldsymbol{a_4}$によって生成される。）

    ---

    (ii)

    $$
    c_1\boldsymbol{a_1} + c_2 \boldsymbol{a_2} + c_3\boldsymbol{a_3} + c_4\boldsymbol{a_4} = \mathbb{O} \tag{*}
    $$

    とすると、

    $$
    c_1\begin{bmatrix}
    2 \\0 \\ 1
    \end{bmatrix}+
    c_2\begin{bmatrix}
    4 \\0 \\ 2
    \end{bmatrix}+
    c_3\begin{bmatrix}
    3 \\1 \\ 1
    \end{bmatrix}+
    c_4\begin{bmatrix}
    1 \\1 \\ 0
    \end{bmatrix}=
    \begin{bmatrix}
    0 \\0 \\ 0
    \end{bmatrix}
    $$

    係数行列は、(1)と同様に簡略化できるため、

    $$
    \begin{aligned}
    & \left[
    \begin{array}{cccc|c}
    2 & 4 & 3 & 1 &0\\
    0 & 0 & 1 & 1 &0\\
    1 & 2 & 1 & 0 &0\\
    \end{array}
    \right] \rightarrow \left[
    \begin{array}{cccc|c}
    1 & 2 & 0 & -1 &0\\
    0 & 0 & 1 & 1 &0\\
    0 & 0 & 0 & 0 &0\\
    \end{array}
    \right]
    \end{aligned}
    $$

    となる。

    行基本変形後の係数行列において，第1列および第3列が**ピボット列**である。

    よって，元の行列の第1列，第3列に対応するベクトル

    $$
    \boldsymbol a_1=
    \begin{bmatrix}
    2\\0\\1
    \end{bmatrix},\quad
    \boldsymbol a_3=
    \begin{bmatrix}
    3\\1\\1
    \end{bmatrix}
    $$

    は一次独立である。

    <!--
    $$
    \text{Im}(T)=\operatorname{span}\{\boldsymbol a_1,\boldsymbol a_3\}
    $$

    が成り立つ。 -->

    ---

    (i),(ii)より、$\{\boldsymbol a_1,\boldsymbol a_3\}$は $\text{Im}(T)$ の基底であり，

    $\operatorname{rank}(T)=\dim(\text{Im}(T))=2
    \quad \square$



    <!-- $$
    \begin{cases}
    c_1 + 2c_2 -c_4 = 0\\
    c_3 + c_4 = 0
    \end{cases}
    $$

    * 自由変数: $c_2, c_4$
    * 従属変数: $c_1 = -2c_2 + c_4,\; c_3 = -c_4$

    $$ -->

    <!-- つまり

    $$
    c_1 \begin{bmatrix}1 \\ 0\end{bmatrix}+
    c_2 \begin{bmatrix}2 \\ 0\end{bmatrix}+
    c_3 \begin{bmatrix}0 \\ 1\end{bmatrix}+
    c_4 \begin{bmatrix}-1 \\ 1\end{bmatrix}=
    \begin{bmatrix}0 \\ 0\end{bmatrix}　\tag{**}
    $$

    $$
    \boldsymbol{b_1}  = \begin{bmatrix}1 \\ 0\end{bmatrix}, \;
    \boldsymbol{b_2}  \begin{bmatrix}2 \\ 0\end{bmatrix}, \;
    \boldsymbol{b_3}  \begin{bmatrix}0 \\ 1\end{bmatrix}, \;
    \boldsymbol{b_4}   \begin{bmatrix}-1 \\ 1\end{bmatrix}
    $$

    とすると、(**)は、

    $$
    c_1\boldsymbol{b_1} + c_2\boldsymbol{b_2} + c_3\boldsymbol{b_3} + c_4\boldsymbol{b_4} = \mathbb{O} \tag{***}
    $$

    **(\*)と(\*\*\*)の$c_1, c_2, c_3, c_4$は共通のため、**

    **$\boldsymbol{a_1}, \boldsymbol{a_2}, \boldsymbol{a_3}, \boldsymbol{a_4}$と$\boldsymbol{b_1},\boldsymbol{b_2}, \boldsymbol{b_3}, \boldsymbol{b_4}$の一次独立・一次従属の関係は共通である。**

    $\boldsymbol${b_1}と$\boldsymbol${b_3}は一次独立であり、

    $$
    \boldsymbol${b_2} = 2\boldsymbol{b_1}, \;\boldsymbol{b_4} + -\boldsymbol{b_1} + \boldsymbol{b_4}
    $$

    $\boldsymbol{b_1},\boldsymbol{b_2}, \boldsymbol{b_3}, \boldsymbol{b_4}$の一次独立なベクトルの最大個数は$r=2$であるから、

    $\boldsymbol{a_1},\boldsymbol{a_2}, \boldsymbol{a_3}, \boldsymbol{a_4}$の一次独立な最大個数も$r=2$である。

    $\boldsymbol${a_1}と$\boldsymbol${a_3}は一次独立であり、

    $$
    \boldsymbol${a_2} = 2\boldsymbol{a_1}, \;\boldsymbol{a_4} + -\boldsymbol{a_1} + \boldsymbol{a_4}
    $$
     -->


    <!--
    \begin{aligned}
    (-2c_2 + c_4)\begin{bmatrix}
    2 \\0 \\ 1
    \end{bmatrix}+
    c_2\begin{bmatrix}
    4 \\0 \\ 2
    \end{bmatrix}-c_4\begin{bmatrix}
    3 \\1 \\ 1
    \end{bmatrix}+
    c_4\begin{bmatrix}
    1 \\1 \\ 0
    \end{bmatrix}=
    \begin{bmatrix}
    0 \\0 \\ 0
    \end{bmatrix}
    &= c_2\begin{bmatrix}
    -4+2 \\
    \end{bmatrix}
    +c_4
    \begin{bmatrix}
    -4+2 \\
    \end{bmatrix}
    \end{aligned}
    $$ -->

    <!-- $$
    \left\{\begin{bmatrix} 1 \\ 1 \end{bmatrix}\right\}
    $$

    は$\text{Im}\left(T\right)$の基底であり、 -->

    <!-- $\text{rank}(T) = \dim \left( \text{Im}\left(T\right) \right) = 1 \; \square$ -->

    ---
    ### 補足


    * 核 (Ker)
    → 解集合そのもの
    → 「自由変数で表す」書き方が自然

    * 像 (Im)
    → 列ベクトルの張る部分空間
    → 「一次独立な列を抜き出す」のが自然
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ###**次元公式**

    ベクトル空間$U, W$の間の線形写像$T:U \rightarrow W$について、次のことが成り立つ。

    $$
    \dim({U}) = \text{null}(T) + \text{rank}(T)
    $$

    ---

    とても良いところに来ています。
    **次元公式は「計算公式」ではなく、「構造の公式」**です。
    意味を段階的に整理します。

    ---

    ## ① まず一言でいうと（核心）

    > **次元公式とは**
    > 「入力空間 $U$ の自由度は、
    > **潰れて消える自由度（核）**と
    > **出力として残る自由度（像）**に
    > ちょうど分解できる」という主張。

    ---

    ## ② 各項の意味を“役割”で見る

    ### 左辺：$\dim(U)$

    * **入力側の自由度の総数**
    * 「どれだけ独立に動かせるか」

    ---

    ### $\text{null}(T) = \dim(\text{Ker}(T))$

    * **入力しても出力がゼロになる方向の数**
    * 情報が **完全に失われる自由度**
    * 「見えない動き」

    ---

    ### $\text{rank}(T) = \dim(\text{Im}(T))$

    * **実際に出力として観測できる自由度**
    * 「見える動き」

    ---

    ## ③ 直感的な図（超重要）

    ```
    入力空間 U
    ┌──────────────────┐
    │                  │
    │   Ker(T)         │  ← 消える方向（null）
    │   （潰れる）     │
    │                  │
    ├──────────────────┤
    │                  │
    │   見える方向     │  ← Im(T) に対応（rank）
    │                  │
    └──────────────────┘
    ```

    👉 **$U$ の自由度は**

    * 「潰れる方向」＋「残る方向」
      に完全に分解できる。

    ---

    ## ④ なぜ「足してちょうど」になるのか？

    ### 決定的な事実

    線形写像$(T$ に対して：

    $$
    U / \text{Ker}(T) ;\cong; \text{Im}(T)
    $$

    （核で割ると像になる）

    👉

    * 核の分だけ情報を捨てて
    * 残った部分が像になる

    ---

    ### 次元で見ると

    $$
    \dim(U) - \dim(\text{Ker}(T)) = \dim(\text{Im}(T))
    $$

    これを並べ替えただけ：

    $$
    \dim(U) = \text{null}(T) + \text{rank}(T)
    $$

    ---

    ## ⑤ あなたの例題に当てはめると

    今回の写像

    $$
    T:\mathbb R^4 \to \mathbb R^3
    $$

    * 入力の自由度：4
    * 潰れる自由度：2（核）
    * 見える自由度：2（像）

    $$
    4 = 2 + 2
    $$

    👉 **「4次元の入力を、2次元分は捨て、2次元分だけ出力している」**

    ---

    ## ⑥ よくある誤解を正す

    ### ❌「rank は出力空間の次元」

    → **違う**

    * 出力空間 $W$ の次元とは無関係
    * 実際に届いている部分の次元

    ---

    ### ❌「null は余り」

    → **違う**

    * null は「構造的に消える方向」
    * ノイズや偶然ではない

    ---

    ## ⑦ 物理・情報的な比喩

    ### カメラで例えると

    * 入力 $U$：3D空間
    * 出力 $W$：2D画像
    * 核：奥行き方向（潰れる）
    * 像：平面上に映る情報

    $$
    3 = 1 + 2
    $$

    ---

    ## ⑧ まとめ（最重要）

    > **次元公式の意味**
    > 「線形写像は、
    > 入力空間の自由度を
    > **消える部分（核）**と
    > **残る部分（像）**に
    > 完全に分解する」

    これは線形代数の**背骨**です。

    ここまで理解できていれば、
    もはや「計算の線形代数」ではなく
    **構造の線形代数**に入っています。
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    **線形代数の文脈では**

    > **解集合 = 解空間**
    > と考えて **ほぼ問題ありません**。

    ただし、**いつでも同義で使ってよいわけではない**ので、
    その「使い分けの感覚」を整理します。

    ---

    ## ① 基本的な整理

    ### 解集合（solution set）

    * **方程式を満たす解全体の集合**
    * 一般に **集合論的な言い方**
    * 線形か非線形かは問わない

    例：

    $$
    x^2=1 \quad \Rightarrow \quad {1,-1}
    $$

    これは **解集合**だが、**空間ではない**

    ---

    ### 解空間（solution space）

    * 解集合が **ベクトル空間になっている場合**
    * 線形構造を強調した言い方

    👉
    **解集合 ⊃ 解空間**
    （解空間は「ベクトル空間になっている解集合」）

    ---

    ## ② 線形代数での決定的ポイント

    ### 同次線形方程式の場合

    $$
    A\boldsymbol{x}=\boldsymbol{0}
    $$

    * 解集合は必ず

      * 零ベクトルを含む
      * 加法・スカラー倍で閉じている
    * 👉 **必ずベクトル空間**

    したがって

    > **同次線形方程式の解集合 = 解空間**

    と呼んでよい。

    これはまさに：

    $$
    \text{Ker}(T)={\boldsymbol{x}\mid T(\boldsymbol{x})=\boldsymbol{0}}
    $$

    あなたが扱っている状況そのものです。

    ---

    ### 非同次線形方程式の場合

    $$
    A\boldsymbol{x}=\boldsymbol{b}\quad(\boldsymbol{b}\neq\boldsymbol{0})
    $$

    * 解集合は

      * 零ベクトルを含まない
      * 原点を通らない
    * 👉 **ベクトル空間ではない**

    この場合は：

    * ❌ 解空間とは呼ばない
    * ⭕ 解集合、あるいは
    * ⭕ アフィン部分空間

    と言う。

    ---

    ## ③ 教科書・答案での安全な使い分け

    | 状況        | 推奨表現        |
    | --------- | ----------- |
    | 同次線形方程式   | 解空間（または解集合） |
    | 核 Ker(T)  | 解空間         |
    | 非同次方程式    | 解集合         |
    | 一般論・厳密さ重視 | 解集合         |

    ---

    ## ④ あなたの文脈での結論

    今回ずっと扱っているのは

    * 核 $\text{Ker}(T)$
    * $A\boldsymbol{x}=\boldsymbol{0}$

    なので、

    > **解集合 = 解空間**

    と書いて **完全に正しい**です。

    むしろ

    > 「核は解空間である」

    と言えるレベルまで来ています。

    ---

    ## ⑤ 一言で覚えるなら

    > **線形・同次 → 解空間**
    > **非同次・非線形 → 解集合**

    この区別だけ覚えておけば十分です。
    """)
    return


@app.cell
def _(Matrix, np, plt):
    # ===== 行列を定義（自由に変更OK）=====
    A = Matrix([
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ])

    # ===== 核と像の基底を計算 =====
    kernel_basis = A.nullspace()      # Ker(T)
    image_basis = A.columnspace()     # Im(T)

    # sympy → numpy
    kernel_basis = [np.array(v, dtype=float).flatten() for v in kernel_basis]
    image_basis = [np.array(v, dtype=float).flatten() for v in image_basis]

    # ===== 図示 =====
    fig = plt.figure(figsize=(10, 5))

    # --- 核 ---
    ax1 = fig.add_subplot(121, projection='3d')
    for v in kernel_basis:
        ax1.quiver(0, 0, 0, v[0], v[1], v[2], color='blue', linewidth=2)
    ax1.set_title("Kernel (Ker T)")
    ax1.set_xlim([-2, 2])
    ax1.set_ylim([-2, 2])
    ax1.set_zlim([-2, 2])

    # --- 像 ---
    ax2 = fig.add_subplot(122, projection='3d')
    for v in image_basis:
        ax2.quiver(0, 0, 0, v[0], v[1], v[2], color='red', linewidth=2)
    ax2.set_title("Image (Im T)")
    ax2.set_xlim([-2, 2])
    ax2.set_ylim([-2, 2])
    ax2.set_zlim([-2, 2])

    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
