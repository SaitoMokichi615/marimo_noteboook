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
    ###**例5.12**

    次の行列の固有値と固有ベクトルを求めよ。

    $$
    \begin{bmatrix}
    6 & 2 \\ 2 & 3
    \end{bmatrix}
    $$

    ---

    固有方程式は

    $$
    \begin{vmatrix}
    6-\lambda & 2 \\
    2 & 3- \lambda
    \end{vmatrix} = (6-\lambda)(3-\lambda) -4 = 0
    $$

    これより

    $$
    \lambda^2 -9\lambda +14 = 0
    $$

    $$
    (\lambda-7)(\lambda-2) = 0
    $$

    これより、求める固有値は

    $$
    \lambda_1 = 2, \; \lambda_2 = 7 \; \square
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###$\lambda_2=7$に属する固有ベクトル

    $$
    \begin{bmatrix}
    6 & 2 \\ 2 & 3
    \end{bmatrix}
    \begin{bmatrix}
    x \\y
    \end{bmatrix}
    = 7\begin{bmatrix}
    x \\y
    \end{bmatrix}
    $$

    $$
    \begin{bmatrix}
    6x + 2y \\ 2x + 3y
    \end{bmatrix}-
    \begin{bmatrix}
    7x \\7y
    \end{bmatrix}=
    \begin{bmatrix}
    0 \\0
    \end{bmatrix}
    $$

    $$
    \begin{bmatrix}
    -x + 2y \\ 2x - 4y
    \end{bmatrix}=
    \begin{bmatrix}
    0 \\0
    \end{bmatrix}
    $$

    $$
    \begin{bmatrix}
    -1 & 2 \\ 2 & -4
    \end{bmatrix}
    \begin{bmatrix}
    x \\y
    \end{bmatrix}=
    \begin{bmatrix}
    0 \\0
    \end{bmatrix}
    $$

    これより、$x=2y$であるから、固有空間は

    $$
    W(7:A) = \left\{y\begin{bmatrix} 2\\ 1 \end{bmatrix} \; \Big| y \in \mathbb{R} \right\}
    $$

    この固有空間に属するベクトルが、固有値$\lambda_2=7$に属する固有ベクトルである。

    ---
    代表として、固有空間の基底

    $$
    \boldsymbol{u_2} = \begin{bmatrix}
    2 \\1
    \end{bmatrix}
    $$

    を正規化したものを選ぶと、

    $$
    |\boldsymbol{u_2}| = \sqrt{2^2 + 1^2} = \sqrt{5}
    $$

    $$
    \boldsymbol{u'_2} = \frac{\boldsymbol{u_2}}{|\boldsymbol{u_2}|}= \frac{1}{\sqrt{5}}\begin{bmatrix}2 \\ 1 \end{bmatrix} \square
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###$\lambda_1=2$に属する固有ベクトル

    $$
    \begin{bmatrix}
    6 & 2 \\ 2 & 3
    \end{bmatrix}
    \begin{bmatrix}
    x \\y
    \end{bmatrix}
    = 2\begin{bmatrix}
    x \\y
    \end{bmatrix}
    $$

    $$
    \begin{bmatrix}
    6x + 2y \\ 2x + 3y
    \end{bmatrix}-
    \begin{bmatrix}
    2x \\2y
    \end{bmatrix}=
    \begin{bmatrix}
    0 \\0
    \end{bmatrix}
    $$

    $$
    \begin{bmatrix}
    4x + 2y \\ 2x + y
    \end{bmatrix}=
    \begin{bmatrix}
    0 \\0
    \end{bmatrix}
    $$

    $$
    \begin{bmatrix}
    4 & 2 \\ 2 & 1
    \end{bmatrix}
    \begin{bmatrix}
    x \\y
    \end{bmatrix}=
    \begin{bmatrix}
    0 \\0
    \end{bmatrix}
    $$

    これより、$y=-2x$であるから、固有空間は

    $$
    W(2:A) = \left\{x\begin{bmatrix}1 \\ -2 \end{bmatrix} \; \Big| y \in \mathbb{R} \right\}
    $$

    この固有空間に属するベクトルが、固有値$\lambda_1=2$に属する固有ベクトルである。

    ---
    代表として、固有空間の基底ベクトル

    $$
    \boldsymbol{u_1} = \begin{bmatrix}
    1 \\-2
    \end{bmatrix}
    $$

    を正規化したものを選ぶと、

    $$
    |\boldsymbol{u_1}| = \sqrt{1^2 + (-2)^2} = \sqrt{5}
    $$

    $$
    \boldsymbol{u'_1} = \frac{\boldsymbol{u_1}}{|\boldsymbol{u_1}|}= \frac{1}{\sqrt{5}}\begin{bmatrix}1 \\ -2 \end{bmatrix} \square
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 対角化

    $\dim{W(2:A)} + \dim{W(7:A)} = 1+1 = 2$より、2次元正方行列$A$は**対角化可能**である。

    固有空間$W(2:A), W(7:A)$の基底を並べて出来る行列を$P$とすると、

    $$
    P = \begin{bmatrix}
    1 & 2\\ -2 &1
    \end{bmatrix}
    $$

    $$
    P^{-1} = \frac{1}{\det{P}}
    \begin{bmatrix}
    1 & -2\\ 2 &1
    \end{bmatrix} =
    \frac{1}{5}\begin{bmatrix}
    1 & -2\\ 2 &1
    \end{bmatrix}$$

    $$
    \begin{aligned}
    P^{-1}AP &= \frac{1}{5}\begin{bmatrix}
    1 & -2\\ 2 &1
    \end{bmatrix}
    \begin{bmatrix}
    6 & 2 \\ 2 & 3
    \end{bmatrix}
    \begin{bmatrix}
    1 & 2\\ -2 &1
    \end{bmatrix}\\
    &= \frac{1}{5}\begin{bmatrix}
    2 & -4\\ 14 &7
    \end{bmatrix}
    \begin{bmatrix}
    1 & 2\\ -2 &1
    \end{bmatrix}\\
    &= \frac{1}{5}\begin{bmatrix}
    10 & 0\\ 0 &35
    \end{bmatrix} \\
    &= \begin{bmatrix}
    2 & 0\\ 0 &7
    \end{bmatrix}
    \end{aligned}
    $$

    対角成分に固有値$\lambda_1=2, \lambda_2=7$を並べたものに対角化出来る。

    ---

    $$
    \begin{aligned}
    P^{-1}A^nP &= \underbrace{(P^{-1}AP)(P^{-1}AP)\cdot(P^{-1}AP)}_{n個} \\
    &= (P^{-1}AP)^n \\
    &= \left(\begin{bmatrix}
    2 & 0\\ 0 &7
    \end{bmatrix}\right)^{n} \\
    &= \begin{bmatrix}
    2^{n} & 0\\ 0 &7^{n}
    \end{bmatrix}
    \end{aligned}
    $$

    これより、

    $$
    \begin{aligned}
    A^n &= P(P^{-1}A^nP)P^{-1} \\
    &=\begin{bmatrix}
    1 & 2\\ -2 &1
    \end{bmatrix}
    \begin{bmatrix}
    2^{n} & 0\\ 0 &7^{n}
    \end{bmatrix}
    \left(
    \frac{1}{5}\begin{bmatrix}
    1 & -2\\ 2 &1
    \end{bmatrix}
    \right)\\
    &=
    \frac{1}{5}\begin{bmatrix}
    2^{n} & 2\cdot 7^n\\ -2^{n+1} &7^{n}
    \end{bmatrix}
    \begin{bmatrix}
    1 & -2\\ 2 &1
    \end{bmatrix}\\
    &= \frac{1}{5}\begin{bmatrix}
    2^{n} + 4\cdot 7^n & -2^{n+1} +2\cdot 7^n\\ -2^{n+1} + 2\cdot 7^n &2^{n+2} +  7^{n}
    \end{bmatrix}
    \end{aligned}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(sp):

    A = sp.Matrix([[6,2],[2,3]])
    A

    # sp.var('r') 
    # L = r*sp.eye(2)
    # D = (A-L).det()
    # sp.solve (D, r)

    # A.eigenvals()

    eig = A.eigenvects()
    eig

    # sp.latex(A.eigenvects())

    # 固有値 2 の固有ベクトル
    lambda1 = eig[0][0]
    v1 = eig[0][2][0]
    v1_unit = v1 / sp.sqrt(v1.dot(v1))

    # 固有値 7 の固有ベクトル
    lambda2 = eig[1][0]
    v2 = eig[1][2][0]
    v2_unit = v2 / sp.sqrt(v2.dot(v2))


    A, lambda1, v1_unit, lambda2, v2_unit
    return v1_unit, v2_unit


@app.cell(hide_code=True)
def _(np, plt, v1_unit, v2_unit):
    v1_np = np.array(v1_unit, dtype=float).flatten()
    v2_np = np.array(v2_unit, dtype=float).flatten()

    fig, ax = plt.subplots(figsize=(5, 5))

    # 原点
    ax.scatter(0, 0, color='black')

    # 固有ベクトル（単位ベクトル）
    ax.quiver(0, 0, v1_np[0], v1_np[1],
              angles='xy', scale_units='xy', scale=1)

    ax.quiver(0, 0, v2_np[0], v2_np[1],
              angles='xy', scale_units='xy', scale=1)

    # 補助線
    ax.axhline(0)
    ax.axvline(0)

    ax.set_aspect('equal')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    ax.set_title("Eigenvectors (unit vectors)")
    plt.show()
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(np, qr_eigen_with_history):
    A_ = np.array([[6., 2.],
                  [2., 3.]])
    offdiag_norms, diagonals = qr_eigen_with_history(A_, n_iter=25)
    return diagonals, offdiag_norms


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(diagonals, plt):
    plt.figure()
    plt.plot(diagonals[:, 0], label="diag(1)")
    plt.plot(diagonals[:, 1], label="diag(2)")
    plt.axhline(2, linestyle="--", alpha=0.6)
    plt.axhline(7, linestyle="--", alpha=0.6)
    plt.xlabel("iteration")
    plt.ylabel("diagonal value")
    plt.legend()
    plt.title("Diagonal elements converging to eigenvalues")
    plt.grid(True)
    plt.show()

    return


if __name__ == "__main__":
    app.run()
