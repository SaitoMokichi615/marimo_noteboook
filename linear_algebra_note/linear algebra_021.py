import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**連立一次方程式の解空間の基底と次元**
    * 解空間は、方程式の解の集合
    * 連立一次方程式の解空間は、ベクトル空間
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **例題21-1**
    次のベクトル空間$W$の1組の基底を求め、次元$\dim{W}$を求めよ。

    $$
    W = \left\{\begin{bmatrix}x \\ y\\ z\end{bmatrix}\in \mathbb{R^3} \;\Big|　x+2y+z=0\right\}
    $$

    ---
    (i)

    $$
    \begin{aligned}
    W &= \left\{\begin{bmatrix}x \\ y\\ z\end{bmatrix}\in \mathbb{R^3} \;\Big|　x+2y+z=0\right\}\\
    &= \left\{\begin{bmatrix}x \\ y\\ z\end{bmatrix}\in \mathbb{R^3} \;\Big|　x=-2y+z\right\}\\
    &= \left\{\begin{bmatrix}-2y+z \\ y\\ z\end{bmatrix}\in \mathbb{R^3} \;\Big|　y,z \in \mathbb{R}\right\}\\
    &= \left\{y\begin{bmatrix}-2 \\ 1\\ 0\end{bmatrix}+z\begin{bmatrix}1\\0\\1 \end{bmatrix}\in \mathbb{R^3} \;\Big|　y,z \in \mathbb{R}\right\}\\
    \end{aligned}
    $$

    よって、$W$の任意のベクトルは、

    $$
    \boldsymbol{u_1} = \begin{bmatrix}-2 \\ 1\\ 0\end{bmatrix},\quad
    \boldsymbol{u_2} = \begin{bmatrix}1\\0\\1 \end{bmatrix}
    $$

    の一次結合で表すことが出来る。

    (ii)
    $c_1\boldsymbol{u_1}+c_2\boldsymbol{u_2}=\mathbb{O}\quad(c_1, c_2 \in \mathbb{R})$とすると、

    $$
    \begin{bmatrix}-2c_1 + c_2 \\ c_1\\ c_2\end{bmatrix} =  \begin{bmatrix}0\\0\\0 \end{bmatrix}
    $$

    より、$c_1=c_2=0$であるから、$\boldsymbol{u_1}, \boldsymbol{u_2}$は一次独立である。

    (i)と(ii)より、$\{\boldsymbol{u_1}, \boldsymbol{u_2}\}$は、$W$の基底である。

    したがって、$\dim{W} = 2 \quad \square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **例題21-2**
    次のベクトル空間$W$の1組の基底を求め、次元$\dim{W}$を求めよ。

    $$
    W = \left\{\begin{bmatrix}x \\ y\\ z\end{bmatrix}\in \mathbb{R^3} \;\Big|　\begin{aligned}&x+y-z=0 \\ &3x+2y-z=0  \end{aligned}\right\}
    $$

    ---
    (i)連立方程式を簡略化すると、

    $$
    \begin{aligned}
    & \left[
    \begin{array}{ccc|c}
    1 & 1 & -1 & 0 \\
    3 & 2 & -1 & 0 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第1行}\times (-3) + \text{第2行}}\;
    & \left[
    \begin{array}{ccc|c}
    1 & 1 & -1 & 0 \\
    0 & -1 & 2 & 0 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第2行}\times (-1)}\;
    & \left[
    \begin{array}{ccc|c}
    1 & 1 & -1 & 0 \\
    0 & 1 & -2 & 0 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第2行}\times (-1) + \text{第1行}}\;
    & \left[
    \begin{array}{ccc|c}
    1 & 0 & 1 & 0 \\
    0 & 1 & -2 & 0 \\
    \end{array}
    \right]
    \\
    \end{aligned}
    $$

    ゆえに、

    $$
    \begin{aligned}
    W &= \left\{\begin{bmatrix}x \\ y\\ z\end{bmatrix}\in \mathbb{R^3} \;\Big|　\begin{aligned}&x+z=0 \\ &y-2z=0  \end{aligned}\right\} \\
    &= \left\{\begin{bmatrix}-z \\ -2z\\ z\end{bmatrix}\in \mathbb{R^3} \;\Big|　z \in \mathbb{R}\right\} \\
    &= \left\{z\begin{bmatrix}-1 \\ -2 \\ 1 \end{bmatrix}\in \mathbb{R^3} \;\Big|　z \in \mathbb{R}\right\} \\
    \end{aligned}
    $$

    よって、$W$の任意のベクトルは、

    $$
    \boldsymbol{u} = \begin{bmatrix}-1 \\ -2\\ 1\end{bmatrix},\quad
    $$

    の一次結合で表すことが出来る。

    (ii)
    $\boldsymbol{u}$だけからなるベクトルは一次独立である。

    (i)と(ii)より、$\{\boldsymbol{u}\}$は、$W$の基底である。

    したがって、$\dim{W} = 1 \quad \square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題21-1**
    $\mathbb{R^3}$の部分空間

    $$
    W = \left\{\begin{bmatrix}x \\ y\\ z\end{bmatrix}\in \mathbb{R^3} \;\Big|　x=y=z  \right\}
    $$

    の1組の基底と次元$\dim{W}$を求めよ。

    ---

    (i)

    $$
    \begin{aligned}
    W &= \left\{\begin{bmatrix}x \\ y\\ z\end{bmatrix}\in \mathbb{R^3} \;\Big|　x=y=z  \right\} \\
    &= \left\{\begin{bmatrix}x \\ x\\ x\end{bmatrix}\in \mathbb{R^3} \;\Big|　x\in \mathbb{R}  \right\} \\
    &= \left\{x\begin{bmatrix}1 \\ 1\\ 1\end{bmatrix}\in \mathbb{R^3} \;\Big|　x\in \mathbb{R}  \right\}
    \end{aligned}
    $$

    ゆえに、$W$の任意の元は、

    $$
    \boldsymbol{u} = \begin{bmatrix}1 \\ 1\\ 1\end{bmatrix}
    $$

    のスカラー倍（一次結合）で表せる。

    (ii)
    $\boldsymbol{u} \neq \boldsymbol{0}$より、$\boldsymbol{u}は$一次独立である。

    (i), (ii)より、$\mathbb{R^3}$の部分空間$W$の基底の1組は、$\{\boldsymbol{u}\}$である。

    よって、$\dim{W} = 1 \square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題21-2**
    $\mathbb{R^4}$の部分空間

    $$
    W = \left\{\begin{bmatrix}x_1 \\ x_2 \\ x_3\\ x_4\end{bmatrix}\in \mathbb{R^4} \;\Bigg|　\begin{aligned}&x_1 + 3x_2 -x_3 +x_4=0 \\ &2x_1 + 6x_2 -5x_3 + 5x_4 = 0\end{aligned}  \right\}
    $$

    の1組の基底と次元$\dim{W}$を求めよ。

    ---
    (i)連立方程式を簡略化すると、

    $$
    \begin{aligned}
    & \left[
    \begin{array}{cccc|c}
    1 & 3 & -1 & 1 & 0 \\
    2 & 6 & -5 & 5 & 0 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第1行}\times (-2) + \text{第2行}}\;
    & \left[
    \begin{array}{cccc|c}
    1 & 3 & -1 & 1 & 0 \\
    0 & 0 & -3 & 3 & 0 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第2行}\times (-\frac{1}{3})}\;
    & \left[
    \begin{array}{cccc|c}
    1 & 3 & -1 & 1 & 0 \\
    0 & 0 & 1 & -1 & 0 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第2行} + \text{第1行}}\;
    & \left[
    \begin{array}{cccc|c}
    1 & 3 & 0 & 0 & 0 \\
    0 & 0 & 1 & -1 & 0 \\
    \end{array}
    \right]
    \\
    \end{aligned}
    $$

    これより、

    $$
    \begin{cases}
    x_1 + 3x_2 = 0
    \\
    x_3 - x_4 = 0
    \end{cases}
    $$

    であるから、$x_1 = -3x_2, x_3 = x_4$を満たす。

    * **自由変数$x_2, x_4$**
    * **従属変数$x_1, x_2$**


    これより、


    $$
    \begin{aligned}
    W &= \left\{\begin{bmatrix}-3x_2 \\ x_2 \\ x_3\\ x_4\end{bmatrix}\in \mathbb{R^4} \;\Bigg|　x_2, x_4 \in \mathbb{R}  \right\}\\
    &= \left\{x_2\begin{bmatrix}-3 \\ 1 \\ 0\\ 0\end{bmatrix} + x_3\begin{bmatrix}0 \\ 0 \\ 1\\ 1\end{bmatrix}\in \mathbb{R^4} \;\Bigg|　x_2, x_4 \in \mathbb{R}  \right\}\\
    \end{aligned}
    $$


    ゆえに、$W$の任意の元は、

    $$
    \boldsymbol{u_1} = \begin{bmatrix}-3 \\ 1\\ 0 \\ 0 \end{bmatrix}, \quad \boldsymbol{u_2} = \begin{bmatrix}0 \\ 0　\\1 \\ 1\end{bmatrix}
    $$

    の一次結合で表せる。

    (ii)
    $c_1\boldsymbol{u_1} + c_2\boldsymbol{u_2} = \mathbb{O} \quad(c_1, c_2 \in \mathbb{R})$とすると、


    $$
    \begin{bmatrix}-3c_1 \\ c_1\\ c_2 \\ c_2\end{bmatrix} = \begin{bmatrix}0\\0\\0 \\0 \end{bmatrix}
    $$

    これより、$c_1=c_2=0$であるから、$\boldsymbol{u_1}, \boldsymbol{u_2}$は一次独立である。

    (i), (ii)より、$\mathbb{R^4}$の部分空間$W$の基底の1組は、$\{\boldsymbol{u_1}, \boldsymbol{u_2}\}$である。

    よって、$\dim{W} = 2 \square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    例題22-1は、

    1. 方程式の変数の個数 = 係数行列の列数 = 入力側の次元 =  $n = 3$
    1. 方程式の本数（見かけ） = 係数行列の行数 = 出力側の次元 $m = 1$
    1. 主成分の数 = 独立な条件の数 = 係数行列の一次独立な行ベクトルの数 = $\text{rank} A = 1\quad(\text{rank} A  \le m)$
    1. 解空間の次元 = 解空間の自由度 = $\dim W = 2$
    1. 関係式 $\dim W = n - \text{rank}A = 3-1 = 2$

    例題22-2は、

    1. 方程式の変数の個数 = 係数行列の列数 = 入力側の次元 =  $n = 3$
    1. 方程式の本数（見かけ） = 係数行列の行数 = 出力側の次元 $m = 2$
    1. 主成分の数 = 独立な条件の数 = 係数行列の一次独立な行ベクトルの数 = $\text{rank} A = 2\quad(\text{rank} A  \le m)$
    1. 解空間の次元 = 解空間の自由度 = $\dim W = 1$
    1. 関係式 $\dim W = n - \text{rank}A = 3-2 = 1$

    <!-- 問題22-1は、

    1. 方程式の変数の個数 = 係数行列の列数 = 入力側の次元 =  $n = 3$
    1. 方程式の本数（見かけ） = 係数行列の行数 = 出力側の次元 $m = 1$？
    1. 主成分の数 = 独立な条件の数 = 係数行列の一次独立な行ベクトルの数 = $\text{rank} A = 2\quad(\text{rank} A  \le m)$?
    1. 解空間の次元 = 解空間の自由度 = $\dim W = 1$
    1. 関係式 $\dim W = n - \text{rank}A = 3-2 = 1$



    問題22-2は、

    1. 方程式の変数の個数 = 係数行列の列数 = 入力側の次元 =  $n = 4$
    1. 方程式の本数（見かけ） = 係数行列の行数 = 出力側の次元 $m = 2$
    1. 主成分の数 = 独立な条件の数 = 係数行列の一次独立な行ベクトルの数 = $\text{rank} A = 2\quad(\text{rank} A  \le m)$
    1. 解空間の次元 = 解空間の自由度 = $\dim W = 2$
    1. 関係式 $\dim W = n - \text{rank}A = 4-2 = 2$ -->

    1.と2.について、
    * 係数行列による**線形写像の値域**は$\mathbb{R^m}$
    * 実際に到達する部分(**像**)の次元は$\text{rank}A$

    > 係数行列$A$を持つ同次連立一次方程式
    > $A \boldsymbol{x} = \boldsymbol{0}$の解空間$W$は
    >
    > $\mathbb{R^n}$の部分空間であり、
    > $\dim{W} = n-\text{rank}A$が成り立つ

    ---
    ### 独立な条件
    連立一次方程式の場合、他の方程式の線形結合では表せない方程式
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    # パラメータ y, z
    y_1 = np.linspace(-5, 5, 30)
    z_1 = np.linspace(-5, 5, 30)

    Y_1, Z_1 = np.meshgrid(y_1, z_1)

    # x + 2y + z = 0 → x = -2y - z
    X_1 = -2 * Y_1 - Z_1

    # プロット
    fig_1 = plt.figure()
    ax_1 = fig_1.add_subplot(projection="3d")

    ax_1.plot_surface(X_1, Y_1, Z_1, alpha=0.6)
    ax_1.scatter([0], [0], [0])  # 零ベクトル
    ax_1.set_xlabel("x")
    ax_1.set_ylabel("y")
    ax_1.set_zlabel("z")
    ax_1.set_title("Example 22-1: Solution Space (Plane)")

    plt.show()
    return


@app.cell(hide_code=True)
def _(np, plt):
    # パラメータ t
    t_2 = np.linspace(-5, 5, 100)

    # 基底ベクトル (-1, -2, 1)
    x_2 = -t_2
    y_2 = -2 * t_2
    z_2 = t_2

    # プロット
    fig_2 = plt.figure()
    ax_2 = fig_2.add_subplot(projection="3d")

    ax_2.plot(x_2, y_2, z_2, linewidth=2)
    ax_2.scatter([0], [0], [0])  # 零ベクトル
    ax_2.set_xlabel("x")
    ax_2.set_ylabel("y")
    ax_2.set_zlabel("z")
    ax_2.set_title("Example 22-2: Solution Space (Line)")

    plt.show()
    return


@app.cell(hide_code=True)
def _(np, plt):
    # パラメータ
    t_3 = np.linspace(-5, 5, 100)

    # 解空間 W : (t, t, t)
    x_3 = t_3
    y_3 = t_3
    z_3 = t_3

    fig_3 = plt.figure()
    ax_3 = fig_3.add_subplot(projection='3d')

    ax_3.plot(x_3, y_3, z_3)
    ax_3.scatter([0], [0], [0])  # 零ベクトル

    ax_3.set_xlabel("x")
    ax_3.set_ylabel("y")
    ax_3.set_zlabel("z")
    ax_3.set_title("Practice 22-1:Solution Space W : x = y = z")

    plt.show()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### **多項式ベクトル空間の基底・次元**
    多項式全体の集合はベクトル空間
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###　**例題21-3**

    $\{1, x, x^2, \dots, x^n\}$は、多項式全体のなすベクトル空間$\mathbb{R}[x]_n$の基底であることを示せ。

    ---

    (i)
    $\mathbb{R}[x]_n$の任意の多項式$a_0 + a_1x + a_2x^2 + \dots + a_nx^n$は、$1, x, x^2, \dots, x^n$の一次結合である。

    (ii)

    $$
    c_0\cdot 1 + c_1x + c_2x^2 + \dots + c_nx^n = \boldsymbol{0} \quad(c_0, c_1, c_2, \dots, c_n \in \mathbb{R}) \tag{*}
    $$

    とする

    **(\*)は「多項式として等しい」**ことを意味する。すなわち、**「両辺の各多項式の係数が等しい」**ことを表す。

    このとき、
    $c_0=c_1=c_2=\dots, =c_n=0$である。

    (i),(ii)より、$\{1, x, x^2, \dots, x^n\}$は$\mathbb{R}[x]_n$の基底である。$\square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題21-3**
    $f(x)=x+1, g(x) = x-1$は、$\mathbb{R}[x]_1$の基底であることを示せ。

    ---

    (i)
    任意の$\alpha, \beta \in \mathbb{R}$について、
    $\alpha f(x) + \beta g(x) = \alpha(x+1) + \beta(x-1) =(\alpha+\beta)x + (\alpha-\beta)$

    任意の一次式$ax+b$が、$f(x)$と$g(x)$の一次結合で表すことが出来るためには、

    $$
    \begin{cases}
    \alpha + \beta = a \\
    \alpha - \beta = b
    \end{cases} \tag{*}
    $$

    を満たす$\alpha, \beta$が必ず存在しなければならない。

    (\*)を解くと、

    $$
    \alpha = \frac{a+b}{2}, \beta = \frac{a-b}{2}
    $$

    であるから、必ず解が存在する。

    よって、任意の一次式$ax+b$が、$f(x)$と$g(x)$の一次結合で表すことが出来る。

    (ii)$c_1f(x) + c_2g(x) = 0 \quad(c_1, c_2 \in \mathbb{R})$

    とすると、

    $$
    c_1f(x) + c_2g(x) = c_1(x+1) + c_2(x-1) = (c_1+c_2)x + (c_1-c_2) = 0 \tag{**}
    $$

    (\**)が**恒等式**であるには、

    $$
    \begin{cases}
    xの係数:c_1 + c_2 = 0 \\
    定数項: c_1 - c_2 = 0
    \end{cases}
    $$

    を満たさなければならない。



    上記連立方程式を計算すると、$c_1=c_2=0$

    よって、$f(x)$と$g(x)$は一次独立である。

    (i),(ii)より、$f(x),g(x)$は、$\mathbb{R}[x]_1$の基底である。$\square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###　**例題21-4**

    $\mathbb{R}[x]_3$の部分空間

    $$
    W = \left\{ f(x) \in \mathbb{R[x]_3}\Big|　f(1)=0,\; f'(1)=0\right\}
    $$

    の1組の基底を求め、次元$\dim{W}$を求めよ。

    ---
    (i)
    $W$の定義より、$a,b,c,d \in \mathbb{R}$とすると、

    $$
    \begin{aligned}
    f(x) &= ax^3 + bx^2 + cx + d \\
    f'(x) &= 3ax^2 + 2bx + c
    \end{aligned}
    $$

    であり、

    $$
    \begin{aligned}
    f(1) &= a + b + c + d = 0 \\
    f'(1) &= 3a + 2b + c = 0
    \end{aligned}
    $$

    となる。
    ゆえに、


    $$
    W = \left\{ ax^3 + bx^2 + cx + d \in \mathbb{R[x]_3}\Big|　\begin{aligned}&a + b+c+d = 0\\ &3a + 2b + c = 0 \end{aligned}\right\}
    $$

    連立方程式の係数行列を簡略化すると

    $$
    \begin{aligned}
    & \left[
    \begin{array}{cccc|c}
    1 & 1 & 1 & 1 & 0 \\
    3 & 2 & 1 & 0 & 0 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第1行}\times (-3) + \text{第2行}}\;
    & \left[
    \begin{array}{cccc|c}
    1 & 1 & 1 & 1 & 0 \\
    0 & -1 & -2 & -3 & 0 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第2行}\times+ \text{第1行}}\;
    & \left[
    \begin{array}{cccc|c}
    1 & 0 & -1 & -2 & 0 \\
    0 & -1 & -2 & -3 & 0 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第1行}\times (-1)}\;
    & \left[
    \begin{array}{cccc|c}
    1 & 0 & -1 & -2 & 0 \\
    0 & 1 & 2 & 3 & 0 \\
    \end{array}
    \right]
    \\
    \end{aligned}
    $$

    * 自由変数: $c, d$
    * 従属変数: $a=c+2d,\; b=-2a-3d$

    $$
    \begin{aligned}
    W &= \left\{ (c+2d)x^3 +(-2c-3d)x^2 + cx + d \in \mathbb{R[x]_3}\Big|　c, d \in R\right\}
    \\
    &= \left\{ c(x^3-2x^2+x) +d(2x^3 -3x^2 + 1) \in \mathbb{R[x]_3}\Big|　c, d \in R\right\}
    \end{aligned}
    $$

    よって$W$の任意の元は、$f_1(x) = x^3-2x^2+x, \; f_2(x) = 2x^3 -3x^2 + 1$の一次結合で表すことが出来る。

    (ii)
    $c_1f_1(x) = c_2f_2(x) = \boldsymbol{0}$ とすると、

    $$
    \begin{aligned}
    &c_1(x^3 -2x^2 + x) + c_2(2x^3-3x^2 + 1) = \boldsymbol{0} \\
    \xrightarrow{} &(c_1 + 2c_2)x^3 +(-2c_1 -3c_2)x^2 +  -2c_1x + c_2= \boldsymbol{0}
    \end{aligned} \tag{*}
    $$

    (\*)が成立するには

    $$
    \begin{cases}
    c_1 + 2c_2 = 0 \\
    -2c_1 -3c_2 = 0 \\
    -2c_1 = 0 \\
    c_2 = 0
    \end{cases} \tag{**}
    $$

    が成り立たなくてはならない。

    (\**)を計算すると、$c_1=c_2=0$となる。

    よって、$f_1(x), f_2(x)$は一次独立である。

    (i),(ii)より、$W$の基底の1組は$\{f_1(x), f_2(x)\}$であり、$\dim{W}=2\square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###　**問題21-4**

    $\mathbb{R}[x]_3$の部分空間

    $$
    W = \left\{ f(x) \in \mathbb{R[x]_3}\Big|　f''(x)-2xf'(x)=\boldsymbol{0}\right\}
    $$

    の1組の基底を求め、次元$\dim{W}$を求めよ。

    ---

    (i)
    $W$の定義より、$a,b,c,d \in \mathbb{R}$とすると、

    $$
    \begin{cases}
    f(x) &= ax^3 + bx^2 + cx + d \\
    f'(x) &= 3ax^2 + 2bx + c \\
    f''(x) &= 6ax + 2b
    \end{cases}
    $$

    であり、

    $$
    \begin{aligned}
    f''(x)-2xf'(x)　&=  (6ax + 2b) -2x(3ax^2 + 2bx + c)\\
    &= -6ax^3 -4bx^2 + (6a - 2c)x + 2b
    &= \boldsymbol{0}
    \end{aligned}
    $$

    であるから、

    $$
    \begin{cases}
    -6a = 0 \\
    -4b = 0 \\
    6a-2c = 0\\
    2b = 0
    \end{cases}
    $$

    これより、$a=b=c=0$

    ゆえに、

    $$
    W = \left\{ d\cdot 1 \in \mathbb{R[x]_3}\Big|　d\in \mathbb{R} \right\}
    $$

    $W$の任意の元は、$1$のスカラー倍（一次結合）で表すことが出来る。

    (ii)
    1個の非零ベクトル1は、一次独立である。

    (i),(ii)より、$\{1\}$は$W$の基底であり、$\dim{W}=1 \; \square$
    """)
    return


@app.cell
def _():
    # s_4 = np.linspace(-5, 5, 50)
    # t_4 = np.linspace(-5, 5, 50)

    # S_4, T_4 = np.meshgrid(s_4, t_4)

    # # 基底
    # u1_4 = np.array([-3, 1, 0, 0])
    # u2_4 = np.array([0, 0, 1, 1])

    # # パラメータ平面
    # X_4 = S_4 * u1_4[0] + T_4 * u2_4[0]
    # Y_4 = S_4 * u1_4[1] + T_4 * u2_4[1]

    # plt.plot(X_4, Y_4)
    # plt.xlabel("x1")
    # plt.ylabel("x2")
    # plt.title("Projection of Solution Space onto (x1, x2)")
    # plt.show()
    return


@app.cell
def _():
    # A_1 = np.array([[1, 2, 1]])

    # # 列空間の基底（列ベクトル）
    # col_basis = A_1.T

    # t_1 = np.linspace(-5, 5, 100)

    # # 像（直線）
    # y_1 = t_1 * col_basis.sum(axis=0)

    # plt.plot(y_1, t_1)
    # plt.xlabel("Image value")
    # plt.ylabel("Parameter")
    # plt.title("Column Space (Image)")
    # plt.grid()
    # plt.show()
    return


@app.cell
def _():
    # A_2 = np.array([
    #     [1, 1, -1],
    #     [3, 2, -1]
    # ])

    # # ---- 核（null space） ----
    # # 手計算で得られた基底 (-1, -2, 1)
    # t_2 = np.linspace(-5, 5, 100)
    # x_2 = -t_2
    # y_2 = -2 * t_2
    # z_2 = t_2

    # fig_2 = plt.figure()
    # ax_2 = fig_2.add_subplot(111, projection="3d")

    # ax_2.plot(x_2, y_2, z_2, label="Kernel (Null Space)", linewidth=2)

    # # ---- 像（column space） ----
    # col1_2 = A_2[:, 0]
    # col2_2 = A_2[:, 1]

    # s_2, r_2 = np.meshgrid(np.linspace(-3, 3, 10),
    #                    np.linspace(-3, 3, 10))

    # U_2 = s_2 * col1_2[0] + r_2 * col2_2[0]
    # V_2 = s_2 * col1_2[1] + r_2 * col2_2[1]
    # W_2 = np.zeros_like(U_2)

    # ax_2.plot_surface(U_2, V_2, W_2, alpha=0.4, label="Image")

    # ax_2.set_xlabel("x")
    # ax_2.set_ylabel("y")
    # ax_2.set_zlabel("z")
    # ax_2.legend()
    # plt.show()
    return


@app.cell
def _(mo):
    mo.md(r"""
    <!-- * 「解空間」は 方程式側の言葉（方程式の解の集合）

    【例題22-1】の$W$は、「一次方程式 $x+2y+z=0$の解をすべて集めた集合」

    ➡一次方程式 $x+2y+z=0$の解空間


    【例題22-2】の$W$は、「与えられた連立一次方程式を満たすベクトル全体の集合」

    ➡

    $W$ は、ある連立一次方程式（または線形写像）の解空間として定義されたベクトル空間。 -->
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- > **「主成分に対応しない変数（自由変数）の個数＝解空間（部分空間）の次元」**

    ###**解空間**
    連立方程式の解の集合


    ###**主成分（ピボット）**
    **各行で最初に現れる0でない成分** を**「主成分（pivot）」**と呼ぶ。

    例題22-1の係数行列の最終形

    $$
    \left[
    \begin{array}{ccc|c}
    1 & 0 & 1 & 0 \\
    0 & 1 & -2 & 0 \\
    \end{array} \tag{*}
    \right]
    $$

    を、連立方程式で書き直すと、

    $$
    \begin{cases}
    x + z = 0 \\
    y - 2z = 0
    \end{cases} \tag{**}
    $$

    では：

    * 第1行：列1の $x$

    * 第2行：列2の $y$

    これらが、主成分に対応する変数である。

    今回の$z$は、主成分に対応しない変数であり、

    別名で：
    * **自由変数**
    * パラメータ

    という。


    式(\**)を解くと、

    $x=-z, y=2z$であり、$z$の値は任意である(自由に値を決めることが出来る)。


    つまり、**$x, y$ は$z$が決まれば自動的に決まる。**



    * **解空間の「自由度」は 1である**

    * **ベクトル空間$W$の「次元」は1である** -->
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


if __name__ == "__main__":
    app.run()
