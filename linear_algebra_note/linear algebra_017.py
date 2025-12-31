import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    plt.rcParams["font.family"] = "Meiryo" 
    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **一次結合・一次独立・一次従属**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題 17-1 (1)**
    $\mathbb{R^2}$の次の2つのベクトル

    $$
    \boldsymbol{u1} =
    \begin{bmatrix}
    1 \\ 0
    \end{bmatrix}, \quad
    \boldsymbol{u2} =
    \begin{bmatrix}
    0 \\ 2
    \end{bmatrix}
    $$

    は一次独立であるか?

    <!-- ---
    #### 添削前

    $$
    k_1\boldsymbol{u1} + k_2\boldsymbol{u2} =
    \begin{bmatrix}
    0 \\ 0
    \end{bmatrix}　\tag{*}
    $$

    となる$k_1$と$k_2$が、唯一$k_1=0$と$k_2=0$しか存在しない場合、$\boldsymbol{u1}$と$\boldsymbol{u2}$は一次独立であるといえる。

    (*)より、

    $$
    \begin{aligned}
    k_1\boldsymbol{u1} + k_2\boldsymbol{u2} &=
    \begin{bmatrix}
    k_1 \\ 0
    \end{bmatrix} + \begin{bmatrix}
    0 \\ 2k_2
    \end{bmatrix} \\
    &= \begin{bmatrix}
    k_1 \\ 2k_2
    \end{bmatrix}
    &= \begin{bmatrix}
    0 \\ 0
    \end{bmatrix}
    \end{aligned} \tag{**}
    $$

    (**)を満たすk_1$と$k_2$は、$k_1=0$と$k_2=0$のみであるから、$\boldsymbol{u1}$と$\boldsymbol{u2}$は一時独立である。 -->

    ---
    <!-- #### 添削後 -->
    $$
    \boldsymbol{u}_1 =
    \begin{bmatrix}
    1 \ 0
    \end{bmatrix}, \quad
    \boldsymbol{u}_2 =
    \begin{bmatrix}
    0 \ 2
    \end{bmatrix}
    $$

    が一次独立であるかを調べる。

    $$
    k_1 \boldsymbol{u}_1 + k_2 \boldsymbol{u}_2 =
    \begin{bmatrix}
    0 \\ 0
    \end{bmatrix}
    $$

    とすると，

    $$
    \begin{aligned}
    k_1 \boldsymbol{u}_1 + k_2 \boldsymbol{u}_2 &=
    k_1
    \begin{bmatrix}
    1 \\ 0
    \end{bmatrix}+
    k_2
    \begin{bmatrix}
    0 \\ 2
    \end{bmatrix} \\
    &=
    \begin{bmatrix}
    k_1 \\ 2k_2
    \end{bmatrix} =
    \begin{bmatrix}
    0 \\ 0
    \end{bmatrix}
    \end{aligned}
    $$

    より

    $$
    k_1 = 0,\quad k_2 = 0
    $$

    しか解を持たない。
    したがって，$\boldsymbol{u}_1$ と $\boldsymbol{u}_2$ は一次独立である。$\square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題 17-1 (2)**
    $\mathbb{R^3}$の次の3つのベクトルが一次独立であるか調べよ。

    $$
    \boldsymbol{u}_1 = \begin{bmatrix}
    1 \\
    1 \\
    0
    \end{bmatrix},
    \boldsymbol{u}_2 = \begin{bmatrix}
    1 \\
    2 \\
    3
    \end{bmatrix},
    \boldsymbol{u}_3 = \begin{bmatrix}
    1 \\
    3 \\
    6
    \end{bmatrix}
    $$

    ---

    $$
    k_1 \boldsymbol{u}_2 + k_2 \boldsymbol{u}_2 + k_3 \boldsymbol{u}_3 =
    \begin{bmatrix}
    0 \\ 0 \\ 0
    \end{bmatrix} \tag{*}
    $$

    とすると、

    $$
    \begin{aligned}
    k_1 \boldsymbol{u}_1 + k_2 \boldsymbol{u}_2 + k_3 \boldsymbol{u}_3 &=
    k_1
    \begin{bmatrix}
    1 \\1\\ 0
    \end{bmatrix}+
    k_2
    \begin{bmatrix}
    1 \\ 2 \\3
    \end{bmatrix} +
    k_3
    \begin{bmatrix}
    1 \\ 3 \\6
    \end{bmatrix}\\
    &=
    \begin{bmatrix}
    k_1 + k_2 + k_3 \\ k_1 + 2k_2 + 3k_3 \\ 3k_2 + 6k_3
    \end{bmatrix} =
    \begin{bmatrix}
    0 \\ 0 \\ 0
    \end{bmatrix}
    \end{aligned}
    $$

    上式を拡大係数行列で表すと、

    $$
    \begin{aligned}
    & \left[
    \begin{array}{ccc|c}
    1 & 1 & 1 & 0 \\
    1 & 2 & 3 & 0 \\
    0 & 3 & 6 & 0 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第3行}\times \frac{1}{3}}\;
    & \left[
    \begin{array}{ccc|c}
    1 & 1 & 1 & 0 \\
    1 & 2 & 3 & 0 \\
    0 & 1 & 2 & 0 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第1行}\times(-1) + \text{第2行}}\;
    &\left[
    \begin{array}{ccc|c}
    1 & 1 & 1 & 0 \\
    0 & 1 & 2 & 0 \\
    0 & 1 & 2 & 0 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第2行}\times(-1) + \text{第3行}}\;
    &\left[
    \begin{array}{ccc|c}
    1 & 1 & 1 & 0 \\
    0 & 1 & 2 & 0 \\
    0 & 0 & 0 & 0 \\
    \end{array}
    \right]
    \\
    \end{aligned}
    $$

    これより、

    $$
    \begin{cases}
    k_2  = -2k_3 \\
    k_1  = k_3
    \end{cases}
    $$

    第3行の式より、$k_1 = \alpha \quad(\alpha \neq 0)$
    を解に持つ。

    したがって、

    $$
    k_1 = k_3 = \alpha,\; k_2 = -2\alpha \quad(\alpha \neq 0) \tag{**}
    $$

    (\*), (**)より、$\boldsymbol{u}_1$, $\boldsymbol{u}_2$, $\boldsymbol{u}_3$ は一次従属である。$\square$


    ---
    ### 模範解答
    一次独立かどうかを調べるために

    $$
    k_1\boldsymbol{u}_1+k_2\boldsymbol{u}_2+k_3\boldsymbol{u}_3=\boldsymbol{0}
    $$

    を考える。
    これは

    $$
    \begin{cases}
    k_1+k_2+k_3=0 \\
    k_1+2k_2+3k_3=0 \\
    3k_2+6k_3=0
    \end{cases}
    $$

    に等しい。
    これを拡大係数行列で表すと

    $$
    \left[
    \begin{array}{ccc|c}
    1 & 1 & 1 & 0\\
    1 & 2 & 3 & 0\\
    0 & 3 & 6 & 0
    \end{array}
    \right]
    $$

    である。
    行基本変形を行うと

    $$
    \left[
    \begin{array}{ccc|c}
    1 & 1 & 1 & 0\\
    0 & 1 & 2 & 0\\
    0 & 0 & 0 & 0
    \end{array}
    \right]
    $$

    を得る。
    このとき未知数は3個であるが，独立な方程式は2本しかないため，
    非自明解が存在する。

    実際，第2式より $k_2=-2k_3$，
    これを第1式に代入すると $k_1=k_3$ となる。

    したがって

    $$
    (k_1,k_2,k_3)=(t,-2t,t)\quad(t\neq0)
    $$

    という解が存在する。
    よって

    $k_1=k_2=k_3=0$以外の解が存在するため，

    $$
    \boldsymbol{u}_1,\boldsymbol{u}_2,\boldsymbol{u}_3
    $$

    は 一次独立ではない（一次従属である）。$\square$

    ---
    ### 補足
    * ゼロ行が出た時点で一次独立は崩れる
    * **未知数より独立な方程式が少なければ非自明解が出る**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**問題 17-2**
    $\mathbb{R^2}$ の次の 2つのベクトルが 一次従属のとき, 実数$a$の値を求めよ.


    <!-- $$
    \boldsymbol{u}_1 = \begin{bmatrix}
    1 \\ 1
    \end{bmatrix}, \quad
    \boldsymbol{u}_2 =\begin{bmatrix}
    1 \\ a
    \end{bmatrix}
    $$

    $\boldsymbol{u}_1$と$\boldsymbol{u}_1$は一次従属であるから、

    $$
    \boldsymbol{u}_1 = k\boldsymbol{u}_1
    $$

    と表せる。すなわち、

    $$
    \begin{bmatrix}
    1 \\ 1
    \end{bmatrix} =
    k\begin{bmatrix}
    1 \\ a
    \end{bmatrix}
    $$

    拡大係数行列で表すと、

    $$
    \begin{aligned}
    & \left[
    \begin{array}{cc|c}
    1 & k &  0 \\
    1 & ka & 0 \\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第1行}\times (-1) + \text{第2行}}\;
    & \left[
    \begin{array}{cc|c}
    1 & k &  0 \\
    0 & k(a-1) & 0 \\
    \end{array}
    \right]
    \\
    \end{aligned}
    $$

    これより、$k=-1$であるから、$a=1$ $\square$ -->


    ---
    $\boldsymbol{u}_1$と$\boldsymbol{u}_2$は一次従属であるから、

    $$
    \boldsymbol{u}_2 = k\boldsymbol{u}_1
    $$

    と表せる。すなわち、

    $$
    \begin{bmatrix}
    1 \\ a
    \end{bmatrix} =
    k\begin{bmatrix}
    1 \\ 1
    \end{bmatrix} =
    \begin{bmatrix}
    k \\ k
    \end{bmatrix}
    $$

    上記の成分を比較すると、$k=1$であるから、$a=1$ $\square$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**階数（ランク）**

    定義 (行列の階数(ランク; rank))
    $m\times n$行列$A$に対し、以下の指標を$A$の**階数(ランク)** といい、$\text{rank}(A)$ と書く。

    * $A$を行基本変形で階段行列に変形したときの**0でない行の個数**
    * $A$の列ベクトルのうち、一次独立なベクトルの最大個数
    * $A$の行ベクトルのうち、一次独立なベクトルの最大個数



    <!-- m
    ×￥￥
    n
    m×n 行列
    A
    A に対し，以下の指標を
    A
    A の階数 (ランク; rank)といい，
    rank
    ⁡
    A
    rankA とかく。

    A
    A を行基本変形で階段行列に変形したときの
    0
    0 でない行の個数
    A
    A の列ベクトルのうち，一次独立なベクトルの最大個数
    A
    A の行ベクトルのうち，一次独立なベクトルの最大個数
    A
    A を線形写像
    f
    f の表現行列(行列表示)と思ったときの
    rank
    ⁡
    f
    =
    dim
    ⁡
    Im
    ⁡
    f
    rankf=dimImf，すなわち，
    f
    f の像 (image) の次元 (これを，線形写像の階数(ランク; rank)という)。
    A
    A の
    0
    0 でない特異値の数，すなわち
    A
    A
    ∗
    AA
    ∗
      の
    0
    0 でない固有値の数(重複度込み)。ただし，
    A
    ∗
    A
    ∗
      は随伴行列(共役転置)を表す。 -->
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **問題 17-5 (1)**
    $$
    \begin{bmatrix}
    1 \\ 0
    \end{bmatrix}  \in \mathbb{R^2}
    $$

    を

    $$
    \begin{bmatrix}
    1 \\ 1
    \end{bmatrix}, \quad
    \begin{bmatrix}
    1 \\ 2
    \end{bmatrix}
    $$

    の一次結合で表せ。

    ---

    $k_1, k_2 \in \mathbb{R}$を用いて、一次結合で表すと

    $$
    \begin{aligned}
    \begin{bmatrix}
    1 \\ 0
    \end{bmatrix} &=
    k_1\begin{bmatrix}
    1 \\ 1
    \end{bmatrix} +
    k_2\begin{bmatrix}
    1 \\ 2
    \end{bmatrix} \\
    &=  \begin{bmatrix}
    k_1 \\ k_1
    \end{bmatrix} +
    \begin{bmatrix}
    k_2 \\ k_2
    \end{bmatrix} \\
    &= \begin{bmatrix}
    k_1 + k_2 \\ k_1 + 2k_2
    \end{bmatrix}
    \end{aligned}
    $$

    これより、

    $$
    k_1+k_2 = 1 \tag{1}
    $$

    $$
    k_1 + 2k_2 = 0 \tag{2}
    $$

    (2)より、$k1 = -2k_2$である。この結果を(1)に代入すると、

    $k_1 = 2, k_2 = -1$ であることが分かる。
    よって、一次結合は次のように表すことが出来る。

    $$
    \begin{bmatrix}
    1 \\ 0
    \end{bmatrix} =
    2\begin{bmatrix}
    1 \\ 1
    \end{bmatrix} -\begin{bmatrix}
    1 \\ 2
    \end{bmatrix}
    $$


    ---

    $$
    \begin{aligned}
    \begin{bmatrix}1 & 0\end{bmatrix}
    &= k_1\begin{bmatrix}1 & 1\end{bmatrix}+ k_2\begin{bmatrix}1 & 2\end{bmatrix} \\
    &= \begin{bmatrix}k_1 + k_2 & k_1 + 2k_2\end{bmatrix}
    \end{aligned}
    $$

    より，

    $$
    \begin{cases}
    k_1 + k_2 = 1 \\
    k_1 + 2k_2 = 0
    \end{cases}
    $$

    これを解くと $k_1 = 2, k_2 = -1$ である。

    したがって，

    $$
    \begin{bmatrix}1 & 0\end{bmatrix}
    = 2\begin{bmatrix}1 & 1\end{bmatrix}-\begin{bmatrix}1 & 2\end{bmatrix}
    $$

    <!-- ---
    ### 問題 17-5 (2)

    $$
    \begin{bmatrix}1 & 1\end{bmatrix}, \quad \begin{bmatrix}2 & 1\end{bmatrix},
    \quad \begin{bmatrix}3 & 5\end{bmatrix}  \in \mathbb{R^2}
    $$

    の自明でない一次関係を一つ求めよ。 -->
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    def dashed_arrow(start, vec, color, label=None):
        end = start + vec
        # 点線の軸
        plt.plot([start[0], end[0]], [start[1], end[1]],
                 linestyle='dashed', color=color)
        # 矢印の先端
        plt.annotate(
            '',
            xy=end,
            xytext=start,
            arrowprops=dict(arrowstyle='->', color=color)
        )
        if label:
            plt.text(end[0], end[1], label)

    v1 = np.array([1, 1])
    v2 = np.array([1, 2])
    target = np.array([1, 0])

    k1 = 2
    k2 = -1

    origin = np.array([0, 0])

    plt.figure(figsize=(6, 6))

    # 基底ベクトル（点線矢印）
    dashed_arrow(origin, v1, color='blue', label='基底[1, 1]')
    dashed_arrow(origin, v2, color='green', label='基底[1, 2]')

    # 係数付きベクトル（通常の矢印）
    plt.quiver(*origin, *(k1 * v1), angles='xy', scale_units='xy', scale=1,
               color='cyan', alpha=0.6, label='2·[1, 1]')

    plt.quiver(*(k1 * v1), *(k2 * v2), angles='xy', scale_units='xy', scale=1,
               color='orange', alpha=0.6, label='-1·[1, 2]')

    # 結果ベクトル
    plt.quiver(*origin, *target, angles='xy', scale_units='xy', scale=1,
               color='red', linewidth=2, label='[1, 0]')

    # 補助
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.grid(True)
    plt.axis('equal')
    plt.autoscale()
    plt.xlim(-1, 3)
    plt.ylim(-2, 3)

    plt.legend()
    plt.title("Geometric interpretation of linear combination")
    plt.show()
    return


@app.cell(hide_code=True)
def _(np, plt):
    def arrow3d(ax, start, vec, color, label=None, linestyle='dashed'):
        end = start + vec
        ax.plot(
            [start[0], end[0]],
            [start[1], end[1]],
            [start[2], end[2]],
            linestyle=linestyle,
            color=color
        )
        ax.quiver(
            start[0], start[1], start[2],
            vec[0], vec[1], vec[2],
            color=color,
            arrow_length_ratio=0.1
        )
        if label:
            ax.text(end[0], end[1], end[2], label)

    # ベクトル定義
    u1 = np.array([1, 1, 0])
    u2 = np.array([1, 2, 3])
    u3 = np.array([1, 3, 6])

    origin_ = np.array([0, 0, 0])

    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection='3d')

    # ベクトル描画
    arrow3d(ax, origin_, u1, 'blue',  'u1 = [1,1,0]')
    arrow3d(ax, origin_, u2, 'green', 'u2 = [1,2,3]')
    arrow3d(ax, origin_, u3, 'red',   'u3 = [1,3,6]')

    # 軸設定
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 4)
    ax.set_zlim(0, 7)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_title("u1, u2, u3 in R^3 (linearly dependent)")

    plt.show()
    return


if __name__ == "__main__":
    app.run()
