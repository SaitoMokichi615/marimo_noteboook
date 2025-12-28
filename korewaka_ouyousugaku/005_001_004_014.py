import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import sympy as sp
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt, sp


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**例5.13**

    次の行列の固有値と固有ベクトルを求めよ。

    $$
    \begin{bmatrix}
    4 & -1 & 1  \\ -1 & 4 & -1 \\ 1 & -1 & 4
    \end{bmatrix}
    $$

    ---

    特性方程式

    $$
    \begin{aligned}
    \begin{vmatrix}
    4-\lambda & -1 & 1 \\
    -1 & 4-\lambda & -1\\
    1 & -1 & 4-\lambda
    \end{vmatrix} &=
    (4-\lambda)^3 + 1 +1 -(4-\lambda) -(4-\lambda) -(4-\lambda)\\
    &= (4-\lambda)^3-3(4-\lambda) + 2 \\
    &= 64 -48\lambda + 12\lambda^2 -\lambda^3 -12 + 3\lambda + 2 = 0
    \end{aligned}
    $$

    $$
    \lambda^3 -12\lambda^2 + 45\lambda -54 = 0
    $$

    $$
    (\lambda-3)^2(\lambda-6) = 0
    $$

    これより、求める固有値は、

    $$
    \lambda_1 = 3, \lambda_2 = 6 \square
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###$\lambda_1=3$に属する固有ベクトル


    $$
    \begin{bmatrix}
    4 & -1 & 1  \\ -1 & 4 & -1 \\ 1 & -1 & 4
    \end{bmatrix}
    \begin{bmatrix}
    x \\ y \\z
    \end{bmatrix} =
    3\begin{bmatrix}
    x \\ y \\z
    \end{bmatrix}
    $$

    $$
    \begin{bmatrix}
    1 & -1 & 1  \\ -1 & 1 & -1 \\ 1 & -1 & 1
    \end{bmatrix}
    \begin{bmatrix}
    x \\ y \\z
    \end{bmatrix} =
    \begin{bmatrix}
    0 \\ 0 \\0
    \end{bmatrix}
    $$

    拡大係数行列で簡略化すると、

    $$
    \begin{aligned}
    & \left[
    \begin{array}{ccc|c}
    1 & -1 & 1  &0\\
    -1 & 1 & -1  &0\\
    1 & -1 & 1  &0\\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第2行} \leftarrow \text{第1行} + \text{第2行}}\;
    & \left[
    \begin{array}{ccc|c}
    1 & -1 & 1  &0\\
    0 & 0 & 0  &0\\
    1 & -1 & 1  &0\\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第3行} \leftarrow \text{第1行} \times (-1)+ \text{第2行}}\;
    & \left[
    \begin{array}{ccc|c}
    1 & -1 & 1  &0\\
    0 & 0 & 0  &0\\
    0 & 0 & 0  &0\\
    \end{array}
    \right]
    \end{aligned}
    $$

    * 自由変数: $y, z$
    * 従属変数: $x = y - z$

    $$
    \begin{aligned}
    W(3:A) &= \left\{\begin{bmatrix} x\\ y \\ z \end{bmatrix}  \in \mathbb{R^3} \; \Big| x = y-z \right\} \\
    W(3:A) &= \left\{\begin{bmatrix} y-z\\ y \\ z \end{bmatrix}  \in \mathbb{R^3} \; \Big| y,z \in \mathbb{R} \right\} \\
    W(3:A) &= \left\{y\begin{bmatrix} 1\\ 1 \\ 0 \end{bmatrix} + z\begin{bmatrix} -1\\ 0 \\ 1 \end{bmatrix} \in \mathbb{R^3} \; \Big| y,z \in \mathbb{R} \right\} \\
    \end{aligned}
    $$

    この固有空間に属するベクトルが、固有値$\lambda_1=2$に属する固有ベクトルである。

    2つのベクトル

    $$
    \boldsymbol{u_1} = \begin{bmatrix}
    1 \\1 \\0
    \end{bmatrix},\;
    \boldsymbol{u_2} = \begin{bmatrix}
    -1 \\0 \\1
    \end{bmatrix}
    $$

    は一次独立であるから、固有空間の基底をなす。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**グラム・シュミットの直交化**

    固有空間$W(3:A)$の 基底は**一次独立だが直交していない**

    $(\boldsymbol{u_1}, \boldsymbol{u_2}) = -1 (\neq 0)$

    ---

    ####**なぜ Gram–Schmidt をするのか（重要）**

    * 対称行列では
      👉 **異なる固有値の固有ベクトルは直交**
    * しかし
      👉 **同じ固有値に属する固有ベクトルは自動では直交しない**

    そこで：

    > **同じ固有空間の中で直交基底を作る**
    >
    > → 直交対角化が可能
    >
    > → $A^n$、指数関数、数値計算が楽になる

    ---

    ### Step 1：1本目はそのまま

    $$
    \boldsymbol{v}_1=\boldsymbol{u}_1=
    \begin{bmatrix}1\\1\\0\end{bmatrix}
    $$

    ---

    ### Step 2：2本目から直交成分を取り出す

    $$
    \boldsymbol{v}_2 = \boldsymbol{u}_2 -
    \frac{\boldsymbol{u}_2\cdot\boldsymbol{v}_1}
    {\boldsymbol{v}_1\cdot\boldsymbol{v}_1}
    \boldsymbol{v}_1
    $$

    内積を計算：

    $$
    \boldsymbol{u}_2\cdot\boldsymbol{v}_1
      = (-1)\cdot1+0\cdot1+1\cdot0=-1
    $$

    $$
    \boldsymbol{v}_1\cdot\boldsymbol{v}_1
      =1^2+1^2=2
    $$

    よって

    $$
    \boldsymbol{v}_2 =
    \begin{bmatrix}-1\\0\\1\end{bmatrix}
    -\left(-\frac12\right)
    \begin{bmatrix}1\\1\\0\end{bmatrix} =
    \begin{bmatrix}
    -\frac{1}{2}\\
    \frac{1}{2}\\
    1
    \end{bmatrix}
    $$

    ### Step 3：直交性の確認

    $$
    \boldsymbol{v}_1\cdot\boldsymbol{v}_2=
    1\cdot\left(-\dfrac{1}{2}\right)
    +1\cdot\left(\dfrac{1}{2}\right)
    +0\cdot1
    =0
    $$

    👉 **確かに直交**

    ---


    ### 正規化（直交正規基底）

    $$
    |\boldsymbol{v}_1|=\sqrt{2}
    \quad\Rightarrow\quad
    \boldsymbol{e}_1= \frac{\boldsymbol{v}_1}{|\boldsymbol{v}_1|}= \frac{1}{\sqrt2}
    \begin{bmatrix}1\\1\\0\end{bmatrix}
    $$


    $$
    |\boldsymbol{v}_2|
    =\sqrt{\frac{1}{4}+\frac{1}{4}+1}
    =\sqrt{\frac{3}{2}}
    $$

    $$
    \boldsymbol{e}_2=\frac{\boldsymbol{v}_2}{|\boldsymbol{v}_2|}=
    \sqrt{\frac{2}{3}}
    \begin{bmatrix}-\frac{1}{2} \\
    \frac{1}{2}\\ 1
    \end{bmatrix}=
    \frac{1}{\sqrt6}
    \begin{bmatrix}
    -1\\
    1\\
    2
    \end{bmatrix}
    $$

    したがって、$\lambda_1=3$に属する固有ベクトルは、

    $$
    \boldsymbol{e}_1=  \frac{1}{\sqrt2}
    \begin{bmatrix}1\\1\\0\end{bmatrix},\;
    \boldsymbol{e}_2 =\frac{1}{\sqrt6}
    \begin{bmatrix}
    -1\\
    1\\
    2
    \end{bmatrix} \;\square
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###$\lambda_1=6$に属する固有ベクトル


    $$
    \begin{bmatrix}
    4 & -1 & 1  \\ -1 & 4 & -1 \\ 1 & -1 & 4
    \end{bmatrix}
    \begin{bmatrix}
    x \\ y \\z
    \end{bmatrix} =
    6\begin{bmatrix}
    x \\ y \\z
    \end{bmatrix}
    $$

    $$
    \begin{bmatrix}
    -2 & -1 & 1  \\ -1 & -2 & -1 \\ 1 & -1 & -2
    \end{bmatrix}
    \begin{bmatrix}
    x \\ y \\z
    \end{bmatrix} =
    \begin{bmatrix}
    0 \\ 0 \\0
    \end{bmatrix}
    $$

    拡大係数行列で簡略化すると、

    $$
    \begin{aligned}
    & \left[
    \begin{array}{ccc|c}
    -2 & -1 & 1 & 0  \\
    -1 & -2 & -1 & 0\\
    1 & -1 & -2 & 0
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第3行} \leftarrow \text{第2行} + \text{第3行}}\;
    & \left[
    \begin{array}{ccc|c}
    -2 & -1 & 1 & 0  \\
    -1 & -2 & -1 & 0\\
    0 & -3 & -3 & 0
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第3行} \leftarrow \text{第3行} \times (-\frac{1}{3})}\;
    & \left[
    \begin{array}{ccc|c}
    -2 & -1 & 1 & 0  \\
    -1 & -2 & -1 & 0\\
    0 & 1 & 1 & 0
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第1行} \leftarrow \text{第3行} + \text{第1行}}\;
    & \left[
    \begin{array}{ccc|c}
    -2 & 0 & 2 & 0  \\
    -1 & -2 & -1 & 0\\
    0 & 1 & 1 & 0
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第1行} \leftarrow \text{第1行} \times (-\frac{1}{2})}\;
    & \left[
    \begin{array}{ccc|c}
    1 & 0 & -1 & 0  \\
    -1 & -2 & -1 & 0\\
    0 & 1 & 1 & 0
    \end{array}
    \right]
    \\ \;\xrightarrow{\text{第2行} \leftarrow \text{第1行} + \text{第2行}}\;
    & \left[
    \begin{array}{ccc|c}
    1 & 0 & -1 & 0  \\
    0 & -2 & -2 & 0\\
    0 & 1 & 1 & 0
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第2行} \leftarrow \text{第3行}\times 2 + \text{第2行}}\;
    & \left[
    \begin{array}{ccc|c}
    1 & 0 & -1 & 0  \\
    0 & 0 & 0 & 0\\
    0 & 1 & 1 & 0
    \end{array}
    \right]
    \\
    \end{aligned}
    $$

    これより、$x=-y=z$であるから、


    $$
    W(6:A) = \left\{y\begin{bmatrix}1 \\ -1 \\1 \end{bmatrix} \; \Big| x \in \mathbb{R} \right\}
    $$

    この固有空間に属するベクトルが、固有値$\lambda_2=6$に属する固有ベクトルである。

    ---
    代表として、固有空間の基底ベクトル

    $$
    \boldsymbol{u_3} = \begin{bmatrix}
    1 \\-1 \\1
    \end{bmatrix}
    $$

    を正規化したものを選ぶと、


    $$
    |\boldsymbol{u_3}| = \sqrt{1^2 + (-1)^2 + 1^2} = \sqrt{3}
    $$

    $$
    \boldsymbol{u'_3} = \frac{\boldsymbol{u_3}}{|\boldsymbol{u_3}|}= \frac{1}{\sqrt{3}}\begin{bmatrix}1 \\ -1 \\1 \end{bmatrix} \square
    $$
    """)
    return


@app.cell(hide_code=True)
def _(sp):
    A = sp.Matrix([[4,-1, 1],[-1,4, -1], [1, -1, 4]])
    A

    # sp.var('r') 
    # L = r*sp.eye(2)
    # D = (A-L).det()
    # sp.solve (D, r)

    # A.eigenvals()

    eig = A.eigenvects()
    eig
    return A, eig


@app.cell
def _(A, sp):
    sp.latex(A.eigenvects())
    return


@app.cell(hide_code=True)
def _(A, eig, sp):

    # 固有値 3 の1つ目の固有ベクトル
    lambda1 = eig[0][0]
    v1 = eig[0][2][0]
    v1_unit = v1 / sp.sqrt(v1.dot(v1))

    # 固有値 3 の2つ目の固有ベクトル
    lambda2 = eig[0][0]
    v2 = eig[0][2][1]
    v2_unit = v2 / sp.sqrt(v2.dot(v2))


    # 固有値 6 の固有ベクトル
    lambda3 = eig[1][0]
    v3 = eig[1][2][0]
    v3_unit = v3 / sp.sqrt(v3.dot(v3))


    A, lambda1, v1_unit, lambda2, v2_unit, lambda3, v3_unit
    return v1, v2, v3


@app.cell
def _(np, plt, v1, v2, v3):
    v1_np = np.array(v1, dtype=float).flatten()
    v2_np = np.array(v2, dtype=float).flatten()
    v3_np = np.array(v3, dtype=float).flatten()

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(projection='3d')

    # 原点
    ax.scatter(0, 0, 0)

    # 固有ベクトル（単位ベクトル）
    ax.quiver(0, 0, 0,
              v1_np[0], v1_np[1], v1_np[2],
              length=1, normalize=True)

    ax.quiver(0, 0, 0,
              v2_np[0], v2_np[1], v2_np[2],
              length=1, normalize=True)

    ax.quiver(0, 0, 0,
              v3_np[0], v3_np[1], v3_np[2],
              length=1, normalize=True)

    # 軸設定
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_zlim([-1.2, 1.2])

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.set_title("Eigenvectors of A (unit vectors)")
    plt.show()
    return fig, v1_np, v2_np


@app.cell
def _(np, sp, v1, v2):
    # 正規化関数
    def normalize(v):
        return v / sp.sqrt(v.dot(v))

    # Gram–Schmidt
    u1 = normalize(v1)
    v2_proj = v2 - (v2.dot(u1)) * u1
    u2 = normalize(v2_proj)


    # 直交化後（正規直交）
    u1_np = np.array(u1, dtype=float).flatten()
    u2_np = np.array(u2, dtype=float).flatten()
    return u1_np, u2_np


@app.cell
def _(fig, plt, u1_np, u2_np, v1_np, v2_np):
    fig_ = plt.figure(figsize=(10, 5))

    # -------- 左：直交化前 --------
    ax1 = fig_.add_subplot(121, projection='3d')
    ax1.set_title("Before orthogonalization")

    ax1.quiver(0, 0, 0, v1_np[0], v1_np[1], v1_np[2],
               length=1, normalize=True)
    ax1.quiver(0, 0, 0, v2_np[0], v2_np[1], v2_np[2],
               length=1, normalize=True)

    ax1.set_xlim([-1.2, 1.2])
    ax1.set_ylim([-1.2, 1.2])
    ax1.set_zlim([-1.2, 1.2])
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_zlabel("z")

    # -------- 右：直交化後 --------
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.set_title("After Gram–Schmidt")

    ax2.quiver(0, 0, 0, u1_np[0], u1_np[1], u1_np[2],
               length=1, normalize=True)
    ax2.quiver(0, 0, 0, u2_np[0], u2_np[1], u2_np[2],
               length=1, normalize=True)

    ax2.set_xlim([-1.2, 1.2])
    ax2.set_ylim([-1.2, 1.2])
    ax2.set_zlim([-1.2, 1.2])
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_zlabel("z")

    plt.tight_layout()
    plt.show()

    return


@app.cell
def _(np):
    def qr_eigen_with_history(A, n_iter=30):
        '''
        QR法で固有値を求める
        '''
        Ak = A.copy()
        offdiag_norms = []
        diagonals = []

        for _ in range(n_iter):
            # 非対角成分のノルム
            offdiag = Ak - np.diag(np.diag(Ak))
            offdiag_norms.append(np.linalg.norm(offdiag))

            diagonals.append(np.diag(Ak).copy())

            Q, R = np.linalg.qr(Ak)
            Ak = R @ Q

        return np.array(offdiag_norms), np.array(diagonals)

    return (qr_eigen_with_history,)


@app.cell
def _(np, qr_eigen_with_history):
    A_ = np.array([[4., -1., 1.],
                  [-1., 4., -1.],
                  [1., -1., 4.],])
    offdiag_norms, diagonals = qr_eigen_with_history(A_, n_iter=25)
    return diagonals, offdiag_norms


@app.cell
def _(offdiag_norms, plt):
    plt.figure()
    plt.plot(offdiag_norms, marker='o')
    plt.yscale("log")
    plt.xlabel("iteration")
    plt.ylabel("off-diagonal norm")
    plt.title("Convergence of QR method")
    plt.grid(True)
    plt.show()

    return


@app.cell
def _(diagonals, plt):
    plt.figure()
    plt.plot(diagonals[:, 0], label="diag(1)")
    plt.plot(diagonals[:, 1], label="diag(2)")
    plt.plot(diagonals[:, 2], label="diag(3)")
    plt.axhline(3, linestyle="--", alpha=0.6)
    plt.axhline(6, linestyle="--", alpha=0.6)


    plt.xlabel("iteration")
    plt.ylabel("diagonal value")
    plt.legend()
    plt.title("Diagonal elements converging to eigenvalues")
    plt.grid(True)
    plt.show()

    return


if __name__ == "__main__":
    app.run()
