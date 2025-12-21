import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import sympy as sy
    return mo, sy


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## B.819
    次の関数を求めよ。

    $$
    f(x) = \int_0^{x}e^t\sin(x-t)dt
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    加法定理より、

    \begin{aligned}
    f(x) &= \int_0^x e^t\Big(\sin x\cos t-\cos x \sin t\Big)dt \\
    &= \sin x\int_0^x e^t\cos t \; dt - \cos x\int_0^x e^t\sin t\;dt \\
    \end{aligned}

    ここで、

    $$
    I_1 = \int_0^x e^t\cos tdt, \quad I_2 =\int_0^x e^t\sin t\;dt
    $$

    とおくと、

    \begin{aligned}
    I_1 &= \Big[e^t \cos t \Big]_0^x -  \int_0^x e^t(-\sin t)dt \\
    &= e^x\cos x-1 + I_2 \tag{$*$}\\
    \end{aligned}

    \begin{aligned}
    I_2 &= \Big[e^t \sin t \Big]_0^x -  \int_0^x e^t(cos t)dt \\
    &= e^x\sin x- I_1 \tag{$**$}\\
    \end{aligned}

     (\*), (\**)より


    \begin{aligned}
    I_1 &= e^x\cos x-1+e^x\sin x - I_1 \\
    I_1 &= \frac{e^x\cos x + e^x\sin x -1}{2} \\
    \end{aligned}

    \begin{aligned}
    I_2 &= e^x\sin x- \Big( e^x\cos x-1 + I_2\Big) \\
    I_2 &= \frac{e^x\sin x - e^x\cos x +1}{2} \\
    \end{aligned}

    よって、

    \begin{aligned}
    f(x ) &= \sin x I_1 -\cos x I_2 \\
    &= \sin x \Big(\frac{e^x\cos x + e^x\sin x -1}{2} \Big)- \cos x \Big(\frac{e^x\sin x - e^x\cos x +1}{2} \Big) \\
    &= \frac{e^x-\sin x - \cos x}{2} \\
    \end{aligned}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 補足
    下記の形の積分を**畳み込み**という。

    $$
    (f * g) (x) = \int _0^xf(t)g(x-t)dt
    $$

    ### 直観的な意味
    * $f(t)$: 過去の影響（ここでは、$e^t$）

    * $g(x-t)$: その影響が時間差でどう現れるか（ここでは、$\sin(x-t)$）

    「過去の入力が、形を変えて現在に重なり合う」イメージ。

    ### 畳み込みが重要な理由

    * 線形微分方程式の特解は、しばしば畳み込みで表される。
    * **ラプラス変換** により、積分が掛け算になる( **畳み込み定理** ) 。

    $$
    \mathcal{L}{f*g} = \mathcal{L}{f}\cdot\mathcal{L}{g}
    $$

    今回の場合

    $$
    e^t * \sin t \quad \Rightarrow \quad \frac{e^x -\sin x - \cos x}{2}
    $$

    ラプラス変換の基本公式は

    $$
    \mathcal{L}{e^x} = \frac{1}{s-1}
    $$

    $$
    \mathcal{L}{\sin x} = \dfrac{1}{s^2+1}
    $$

    $$
    \mathcal{L}{\cos x} = \dfrac{s}{s^2+1}
    $$

    逆ラプラス変換の基本公式は

    $$
    \mathcal{L}^{-1}{\frac{1}{s-1}} = e^x
    $$

    $$
    \mathcal{L}{\sin x} = \dfrac{1}{s^2+1}
    $$

    $$
    \mathcal{L}{\cos x} = \dfrac{s}{s^2+1}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$
    f_1(t) = e^t \quad f_2(t) = \sin t
    $$

    とおくと、

    $$
    f(x) = \int_0^x f_1(t)f_2(x-t) dt = (f_1 * f_2)(x)
    $$


    とする。

    \begin{aligned}
    \mathcal{L}{f(x)} &=  \mathcal{L}{(f_1 * f_2)(x)} \\
    &=  \mathcal{L}{f_1} \cdot \mathcal{L}{f_2}\\
    &=  \mathcal{L}{e^x} \cdot \mathcal{L}{\sin x}\\
    &= \frac{1}{s-1}\cdot \frac{1}{s^2+1} \\
    &= \frac{1}{(s-1)(s^2+1)} \\
    &= \frac{1}{2(s-1)} - \frac{s+1}{2(s^2+1)} \\
    &= \frac{1}{2}\Big(\frac{1}{s-1} + \frac{s}{s^2+1} + \frac{1}{s^2+1}\Big) \\
    \end{aligned}

    ラプラス逆変換をすると、その線形性より、

    \begin{aligned}
    \mathcal{L}^{-1}\Big(\mathcal{L}{f(x)}\Big) &=  \mathcal{L}^{-1}\Big[{\frac{1}{2}\Big(\frac{1}{s-1} - \frac{s}{s^2+1} - \frac{1}{s^2+1}\Big)}\Big] \\
    &=  \frac{1}{2}\Big(\mathcal{L}^{-1}{\frac{1}{s-1}}- \mathcal{L}^{-1}{\frac{s}{s^2+1}} - \mathcal{L}^{-1}{\frac{1}{s^2+1}}\Big)\\
    &= \frac{e^x -\sin x - \cos x}{2} \\
    \end{aligned}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pythonの代数計算ライブラリ、Sympyでも検算する。
    """)
    return


@app.cell
def _(sy):
    x, t = sy.symbols('x t')
    sy.Integral(sy.exp(t) * sy.sin(x - t), (t, 0, x))
    return t, x


@app.cell
def _(sy, t, x):
    f = sy.integrate(sy.exp(t) * sy.sin(x - t), (t, 0, x))
    f
    return


@app.cell
def _(sy):
    s = sy.symbols('s')

    expr = 1 / ((s - 1)*(s**2 + 1))
    sy.apart(expr, s)# 部分分数分解
    return expr, s


@app.cell
def _(expr, s, sy):
    sy.apart(expr, s, full=False)
    return


@app.cell
def _(sy):
    x_, s_, t_ = sy.symbols('x s t', positive=True)

    f1 = sy.exp(t_)
    f2 = sy.sin(t_)

    F1 = sy.laplace_transform(f1, t_, s_, noconds=True)
    F2 = sy.laplace_transform(f2, t_, s_, noconds=True)

    F = sy.simplify(F1 * F2)
    f1, f2, F1, F2, F
    return F, s_


@app.cell
def _(F, s_, sy):
    sy.apart(F, s_)
    return


@app.cell
def _(F, s, sy, x):
    sy.inverse_laplace_transform(F, s, x)
    return


@app.cell
def _(s, sy, x):
    sy.inverse_laplace_transform(
        1/((s - 1)*(s**2 + 1)), s, x
    )

    return


if __name__ == "__main__":
    app.run()
