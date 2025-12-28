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
    4 & -1 & 0  \\ -2 & 4 & -1 \\ 0 & -2 & 4
    \end{bmatrix}
    $$

    ---

    特性方程式

    $$
    \begin{aligned}
    \begin{vmatrix}
    4-\lambda & -1 & 0 \\
    -2 & 4-\lambda & -1\\
    0 & -2 & 4-\lambda
    \end{vmatrix} &=
    (4-\lambda)^3-2(4-\lambda) -2(4-\lambda) \\
    &= (4-\lambda)((4-\lambda)^2-4) \\
    &= (4-\lambda)(2-\lambda)(6-\lambda) = 0
    \end{aligned}
    $$

    これより、求める固有値は、

    $$
    \lambda_1 = 2, \lambda_2 = 4, \lambda_3 = 6 \square
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###$\lambda_1=2$に属する固有ベクトル


    $$
    \begin{bmatrix}
    4 & -1 & 0  \\ -2 & 4 & -1 \\ 0 & -2 & 4
    \end{bmatrix}
    \begin{bmatrix}
    x \\ y \\z
    \end{bmatrix} =
    2\begin{bmatrix}
    x \\ y \\z
    \end{bmatrix}
    $$

    $$
    \begin{bmatrix}
    2 & -1 & 0  \\ -2 & 2 & -1 \\ 0 & -2 & 2
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
    2 & -1 & 0  &0\\
    -2 & 2 & -1  &0\\
    0 & -2 & 2  &0\\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第2行} \leftarrow \text{第1行} + \text{第2行}}\;
    & \left[
    \begin{array}{ccc|c}
    2 & -1 & 0  &0\\
    0 & 1 & -1  &0\\
    0 & -2 & 2  &0\\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第3行} \leftarrow \text{第2行} \times 2+ \text{第2行}}\;
    & \left[
    \begin{array}{ccc|c}
    2 & -1 & 0  &0\\
    0 & 1 & -1  &0\\
    0 & 0 & 0  &0\\
    \end{array}
    \right]
    \end{aligned}
    $$

    これより、$2x = y = z$であるから、固有空間は、

    $$
    W(2:A) = \left\{x\begin{bmatrix} 1\\ 2 \\ 2 \end{bmatrix} \; \Big| x \in \mathbb{R} \right\}
    $$

    この固有空間に属するベクトルが、固有値$\lambda_1=2$に属する固有ベクトルである。

    ---
    代表として、固有空間の基底ベクトル

    $$
    \boldsymbol{u_1} = \begin{bmatrix}
    1 \\2 \\2
    \end{bmatrix}
    $$

    を正規化したものを選ぶと、

    $$
    |\boldsymbol{u_1}| = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{9} = 3
    $$

    $$
    \boldsymbol{u'_1} = \frac{\boldsymbol{u_1}}{|\boldsymbol{u_1}|}=
    \frac{1}{3}\begin{bmatrix}1\\ 2  \\ 2 \end{bmatrix} \square
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###$\lambda_2=4$に属する固有ベクトル


    $$
    \begin{bmatrix}
    4 & -1 & 0  \\ -2 & 4 & -1 \\ 0 & -2 & 4
    \end{bmatrix}
    \begin{bmatrix}
    x \\ y \\z
    \end{bmatrix} =
    4\begin{bmatrix}
    x \\ y \\z
    \end{bmatrix}
    $$

    $$
    \begin{bmatrix}
    0 & -1 & 0  \\ -2 & 0 & -1 \\ 0 & -2 & 0
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
    0 & -1 & 0  &0\\
    -2 & 0 & -1  &0\\
    0 & -2 & 0  &0\\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第3行} \leftarrow \text{第1行} \times(-2)+ \text{第3行}}\;
    & \left[
    \begin{array}{ccc|c}
    0 & -1 & 0  &0\\
    -2 & 0 & -1  &0\\
    0 & 0 & 0  &0\\
    \end{array}
    \right]
    \end{aligned}
    $$

    これより、$-2x = z, y=0$であるから、固有空間は、

    $$
    W(4:A) = \left\{x\begin{bmatrix} 1\\ 0 \\ -2 \end{bmatrix} \; \Big| x \in \mathbb{R} \right\}
    $$

    この固有空間に属するベクトルが、固有値$\lambda_2=4$に属する固有ベクトルである。

    ---
    代表として、固有空間の基底ベクトル

    $$
    \boldsymbol{u_2} = \begin{bmatrix}
    1 \\0 \\-2
    \end{bmatrix}
    $$

    を正規化したものを選ぶと、

    $$
    |\boldsymbol{u_2}| = \sqrt{1^2 + (-2)^2} = \sqrt{5}
    $$

    $$
    \boldsymbol{u'_2} = \frac{\boldsymbol{u_2}}{|\boldsymbol{u_2}|}=
    \frac{1}{\sqrt{5}}\begin{bmatrix}1\\ 0  \\ -2 \end{bmatrix} \square
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###$\lambda_3=6$に属する固有ベクトル


    $$
    \begin{bmatrix}
    4 & -1 & 0  \\ -2 & 4 & -1 \\ 0 & -2 & 4
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
    -2 & -1 & 0  \\ -2 & -2 & -1 \\ 0 & -2 & -2
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
    -2 & -1 & 0  &0\\
    -2 & -2 & -1  &0\\
    0 & -2 & -2  &0\\
    \end{array}
    \right]
    \\
    \\ \;\xrightarrow{\text{第2行} \leftarrow \text{第1行} \times(-1)+ \text{第2行}}\;
    & \left[
    \begin{array}{ccc|c}
    -2 & -1 & 0  &0\\
    0 & -1 & -1  &0\\
    0 & -2 & -2  &0\\
    \end{array}
    \right]
    \\ \;\xrightarrow{\text{第3行} \leftarrow \text{第2行} \times(-2)+ \text{第-行}}\;
    & \left[
    \begin{array}{ccc|c}
    -2 & -1 & 0  &0\\
    0 & -1 & -1  &0\\
    0 & 0 & 0  &0\\
    \end{array}
    \right]
    \end{aligned}
    $$

    これより、$-2x = y =-z$であるから、固有空間は、

    $$
    W(6:A) = \left\{x\begin{bmatrix} 1\\ -2 \\ 2 \end{bmatrix} \; \Big| x \in \mathbb{R} \right\}
    $$

    この固有空間に属するベクトルが、固有値$\lambda_3=6$に属する固有ベクトルである。

    ---
    代表として、固有空間の基底ベクトル

    $$
    \boldsymbol{u_3} = \begin{bmatrix}
    1 \\-2 \\2
    \end{bmatrix}
    $$

    を正規化したものを選ぶと、

    $$
    |\boldsymbol{u_3}| = \sqrt{1^2 + (-2)^2 + 2^2} = \sqrt{9} = 3
    $$

    $$
    \boldsymbol{u'_3} = \frac{\boldsymbol{u_3}}{|\boldsymbol{u_3}|}=
    \frac{1}{3}\begin{bmatrix}1\\ -2  \\ 2 \end{bmatrix} \square
    $$
    """)
    return


@app.cell(hide_code=True)
def _(sp):
    A = sp.Matrix([[4,-1, 0],[-2,4, -1], [0, -2, 4]])
    A

    # sp.var('r') 
    # L = r*sp.eye(2)
    # D = (A-L).det()
    # sp.solve (D, r)

    # A.eigenvals()

    eig = A.eigenvects()
    eig

    # sp.latex(A.eigenvects())

    return A, eig


@app.cell(hide_code=True)
def _(A, eig, sp):

    # 固有値 2 の固有ベクトル
    lambda1 = eig[0][0]
    v1 = eig[0][2][0]
    v1_unit = v1 / sp.sqrt(v1.dot(v1))

    # 固有値 4 の固有ベクトル
    lambda2 = eig[1][0]
    v2 = eig[1][2][0]
    v2_unit = v2 / sp.sqrt(v2.dot(v2))


    # 固有値 6 の固有ベクトル
    lambda3 = eig[2][0]
    v3 = eig[2][2][0]
    v3_unit = v3 / sp.sqrt(v3.dot(v3))


    A, lambda1, v1_unit, lambda2, v2_unit, lambda3, v3_unit
    return v1_unit, v2_unit, v3_unit


@app.cell(hide_code=True)
def _(np, plt, v1_unit, v2_unit, v3_unit):
    v1_np = np.array(v1_unit, dtype=float).flatten()
    v2_np = np.array(v2_unit, dtype=float).flatten()
    v3_np = np.array(v3_unit, dtype=float).flatten()

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
    A_ = np.array([[4., -1., 0.],
                  [-2., 4., -1.],
                  [0., -2., 4.],])
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
    plt.axhline(2, linestyle="--", alpha=0.6)
    plt.axhline(4, linestyle="--", alpha=0.6)
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
