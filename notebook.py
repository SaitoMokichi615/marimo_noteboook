import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    import sympy as sy
    return np, plt, sy


@app.cell
def _(sy):
    x, y = sy.symbols("x, y")
    return (x,)


@app.cell
def _(x):
    x**2 - 2*x - 15
    return


@app.cell
def _(sy, x):
    sy.factor(x**2 - 2*x - 15)
    return


@app.cell
def _(sy, x):
    sy.diff(x**2 - 2*x - 15)
    return


@app.cell
def _(sy, x):
    sy.Integral(x**2 - 2*x - 15, x)
    return


@app.cell
def _(sy, x):
    sy.integrate(x**2 - 2*x - 15)
    return


@app.cell
def _(sy, x):
    sy.Integral(x**2 - 2*x - 15, (x, 0, 3))
    return


@app.cell
def _(sy, x):
    sy.integrate(x**2 - 2*x - 15, (x, 0, 3))
    return


@app.cell
def _(sy):
    a, b, c, d = sy.symbols("a, b, c, d")
    A = sy.Matrix([[a, b], [c, d]])
    B = sy.Matrix([[1, 2], [3, -1]])
    A, B
    return A, B


@app.cell
def _(A, sy):
    sy.det(A)
    return


@app.cell
def _(A, B):
    A*B
    return


@app.cell
def _(A):
    A.inv()
    return


@app.cell
def _(sy):
    c_ = sy.Function('c')
    k, t, D = sy.symbols('k, t, D', positive=True)
    eq = sy.Eq(c_(t).diff(t), -k*c_(t))
    ans = sy.dsolve(eq, c_(t))
    eq, ans
    return D, c_, eq, k, t


@app.cell
def _(D, c_, eq, sy, t):
    ans_ic = sy.dsolve(eq, c_(t), ics={c_(0): D})
    ans_ic
    return


@app.cell
def _(c_, k, sy, t):
    eq_2 = sy.Eq(c_(t).diff(t), -k*c_(t)**2)
    ans_2 = sy.dsolve(eq_2, c_(t))
    eq_2, ans_2
    return


@app.cell
def _(np, plt):
    r_vals = np.linspace(2.5, 4.0, 600)
    iterations = 1000
    last = 100

    xs = []
    rs = []

    for r in r_vals:
        x_ = 0.2
        for i in range(iterations):
            x_ = r * x_ * (1 - x_)
            if i > iterations - last:
                xs.append(x_)
                rs.append(r)

    plt.figure()
    plt.plot(rs, xs, '.', markersize=1)
    plt.xlabel("r")
    plt.ylabel("x")
    plt.title("Bifurcation Diagram (Logistic Map)")
    plt.show()

    return (r,)


@app.cell
def _(np, plt, r):
    r_vals_ = np.linspace(-2, 2, 400)
    x_vals = []

    for r_ in r_vals_:
        roots = np.roots([-1, 0, r_, 0])  # -x^3 + r x = 0
        for root in roots:
            if np.isreal(root):
                x_vals.append((r, root.real))

    r_plot, x_plot = zip(*x_vals)

    plt.figure()
    plt.plot(r_plot, x_plot, '.')
    plt.xlabel("r")
    plt.ylabel("Equilibrium x")
    plt.title("Bifurcation Diagram (Pitchfork)")
    plt.show()

    return


@app.cell
def _(np, plt):
    def f(x):
        return x * (1 - x)   # ロジスティック型

    x__ = np.linspace(-0.5, 1.5, 400)
    dx = f(x__)

    plt.figure()
    plt.axhline(0)
    plt.plot(x__, dx)
    plt.xlabel("x")
    plt.ylabel("dx/dt")
    plt.title("Phase Line: x' = x(1 - x)")
    plt.show()

    return


@app.cell
def _(np, plt):

    def field(x, y):
        dx = y
        dy = -x - 0.3*y      # 例：減衰振動
        return dx, dy

    _x = np.linspace(-3, 3, 20)
    _y = np.linspace(-3, 3, 20)
    X, Y = np.meshgrid(_x, _y)

    DX, DY = field(X, Y)

    plt.figure()
    plt.quiver(X, Y, DX, DY)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Phase Plane")
    plt.show()

    return


if __name__ == "__main__":
    app.run()
