import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import sympy as sy
    return mo, sy


@app.cell
def _(mo):
    mo.md(r"""
    ## B.818
    次の関数を微分せよ。

    $$
    f(x) = \int_x^{2x+1}\frac{1}{t^2+1}dt
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    $$
    g(t) = \frac{1}{t^2+1}
    $$

    $$
    G(t) = \int g(t)dt
    $$

    とおく。

    $$
    f(x) = \int_{x}^{2x+1}g(t)dt = \Big[ G(t) \Big]_{x}^{2x+1} = G(2x+1) -G(x)
    $$

    よって、$G'(x) = g(x)$に注意すると、

    $$
     f'(x) = 2G'(2x+1) -G'(x)
    $$

    $$
    = 2g(2x+1)-g(x)
    $$

    $$
    = \frac{ 2}{(2x+1)^2+1}-\frac{1}{x^2+1}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 補足
    $G(t)$の正体は**逆三角関数** $\tan^{-1}t$

    $$
    \frac{d}{dt}\tan^{-1}t = \frac{1}{1+t^2},\;
    \tan^{-1}t = \int \frac{1}{1+t^2}\,dt + C
    $$


    積分の定理より、

    $$
    f(x) = \int_x^{2x+1}\frac{1}{1+t^2}d t = \Big[ \tan^{-1}t\Big]_x^{2x+1}
    $$

    $$
    = \tan^{-1}(2x+1) -\tan^{-1}x
    $$

    $f(x)$を$x$で微分すると、

    $$
    f'(x) = \left(\tan^{-1}(2x+1) \right)'(2x+1)' - \left(\tan^{-1}x \right)'
    $$

    $$
    = \frac{2}{(2x+1)^2+1} - \frac{1}{x^2+1}
    $$
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
    x = sy.symbols('x')

    G = sy.atan  # ∫1/(t^2+1)dt = arctan(t)
    G(x)
    return G, x


@app.cell
def _(G, sy, x):
    check = sy.diff(G(2*x+1) - G(x), x)
    check
    return (check,)


@app.cell
def _(check, sy):
    sy.factor(sy.together(check))
    return


@app.cell
def _(x):


    expr = 2/((2*x+1)**2 + 1) - 1/(x**2 + 1)
    expr
    return (expr,)


@app.cell
def _(expr, sy):
    sy.simplify(expr)
    return


@app.cell
def _(expr, sy):
    sy.factor(sy.together(expr))
    return


@app.cell
def _(check, expr, sy):
    sy.simplify(check - expr)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$
    \begin{aligned}
    \frac{d}{dt}\tan^{-1}t &= \frac{1}{1+t^2} \\
    \tan^{-1}t &= \int \frac{1}{1+t^2}\,dt + C
    \end{aligned}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$
    \left\{
    \begin{aligned}
    \frac{d}{dt}\tan^{-1}t &= \frac{1}{1+t^2} \\
    \tan^{-1}t &= \int \frac{1}{1+t^2}\,dt + C
    \end{aligned}
    \right.
    $$
    """)
    return


if __name__ == "__main__":
    app.run()
