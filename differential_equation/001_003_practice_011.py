import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import sympy as sp
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    plt.rcParams["font.family"] = "Meiryo" 
    plt.rcParams["animation.html"] = "jshtml"
    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- ###**ニュートンの万有引力の法則**

    ニュートンの万有引力の法則とは、

    地球の中心から距離$s$の位置にある質量$m$の物体が受ける力$F$」は、

    $$
    F=\dfrac{mk}{s^2} \quad (kは万有引力定数) \tag{1.}
    $$

    である。

    というものである。

    ---

    質量が$m$のロケットの打ち上げについて、以下の条件で考える。

    * 打ち上げ時の初速度は$v_0$
    * 地球中心からロケットまでの距離は$s$
    * 地球の半径は$R$
    * 地球表面における重力加速度は$g$
    * ロケットに地球の向きの働く力は、ニュートンの万有引力の法則に従う。

    (1)
    ロケットの加速度を$a$とすると、ロケットの進行方向に働く力は$ma$である。

    これが、(1.)と釣り合っていると仮定すると、

    $$
    a = -\frac{gR^2}{s^2} \tag{2.}
    $$

    となることが分かる。

    ここで、ロケットの速度を$v$とすると、

    $$
    \begin{cases}
    v = \dfrac{ds}{dt} \\
    a = \dfrac{dv}{dt}
    \end{cases} \tag{3.}
    $$

    となる。

    このとき、次の問いに応えよ。

    (1)微分方程式

    $$
    \frac{dv}{ds}v = -\frac{gR^2}{s^2} \tag{4.}
    $$

    が成立することを示せ。

    (2) (4.)で示した微分方程式を解け。

    (3)$s=R$かつ$v=v_0$とするとき、(4.)で示した微分方程式の特殊解を求めよ。 -->
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**ニュートンの万有引力下での鉛直打ち上げ**

    地球の中心から距離$r$にある質量$m$の物体には、地球中心向きに

    $$
    F(r) = \frac{GMm}{r^2}　\tag{1}
    $$

    の大きさの万有引力が働く。

    地球の半径を$R$、地表における重力加速度を$g$とすると

    $$
    g = \frac{GM}{R^2} \tag{2}
    $$

    が成り立つ（$G$は万有引力定数、$M$は地球の質量）。

    質量 $m$のロケットを、地表$r=R$から初速度$v_0$で鉛直上向きに打ち上げる。

    空気抵抗は無視する。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###  力 → 加速度

    以下、ロケット進行方向外向きを正とする。


    万有引力は内向きなので

    $$
    F = -\frac{GMm}{r^2}　\tag{1'}
    $$

    **運動方程式** $F = ma$と(1')より

    $$
    a(r) = -\frac{GM}{r^2}　\tag{3}
    $$

    (2)より、

    $$
    gR^2 = GM \tag{2'}
    $$

    (2')を(3)に代入

    $$
    a(r) = -\frac{gR^2}{r^2} \tag{3'}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###  微分方程式の導出（チェーンルール）

    $$
    v = \frac{dr}{dt}, \quad a = \frac{dv}{dt}　\tag{4}
    $$

    より

    $$
    \frac{dv}{dt}
    = \frac{dv}{dr}\frac{dr}{dt}
    = v\frac{dv}{dr} \tag{4'}
    $$

    (3')に代入すると、

    $$
    \boxed{
    v\frac{dv}{dr}
    = -\frac{gR^2}{r^2}
    } \tag{5}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 微分方程式を解く（変数分離系）

    (5)の両辺を$r$で積分：

    $$
    \int v\frac{dv}{dr}dr = -gR^2\int r^{-2}dr
    $$


    $$
    \int vdv = -gR^2\int r^{-2}dr
    $$

    $$
    \frac12 v^2 = gR^2r^{-1} + C \quad(Cは積分定数)
    $$

    整理すると

    $$
    \boxed{
    \frac{1}{2} v^2 - \frac{gR^2}{r} = C \tag{6}
    }
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 初期条件を入れる（特殊解）

    初期条件

    $$
    r = R,\quad v = v_0
    $$

    を(6)に代入：

    $$
    C = \frac{1}{2} v_0^2 - gR　\tag{7}
    $$

    (7)を(6)に代入

    $$
    \frac{1}{2} v^2 - \frac{gR^2}{r} = \frac{1}{2} v_0^2 - gR
    $$

    <!--
    $$
    \begin{aligned}
    \frac12 v^2 &= \frac{1}{2} v_0^2 + \frac{gR^2}{r} - gR \\
    &= \frac{1}{2} v_0^2 + \frac{gR^2}{r} - \frac{gR^2}{R} \\
    &= \frac{1}{2} v_0^2 + gR^2\left(\frac{1}{r} - \frac{1}{R}\right)
    \end{aligned}
    $$ -->
    <!--
    $$
    \frac{1}{r} - \frac{1}{R} = \frac{R - r}{rR}
    $$ -->

    よって特殊解は、

    <!-- $$
    \boxed{
    \frac12 v^2
    = \frac12 v_0^2 + gR\left(\frac{1}{r} - \frac{1}{R}\right)
    }
    $$ -->

    $$
    \boxed{
    v^2
    = v_0^2 + 2gR^2\left(\frac{1}{r} - \frac{1}{R}\right)
    }
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### エネルギー保存で「一瞬」で解く

    **力が保存力であることに注目**

    万有引力のポテンシャルエネルギー：

    $$
    U(r) = -\frac{GMm}{r} = -\frac{mgR^2}{r}
    $$

    力学的エネルギー保存：

    $$
    \frac12 mv^2 - \frac{mgR^2}{r} = \text{const}
    $$

    質量$m$を消すと

    $$
    \boxed{
    \frac12 v^2 - \frac{gR^2}{r} = \text{const}
    }
    $$

    → **(6)の積分結果と完全一致**

    👉 微分方程式を解いた正体が**エネルギー保存則**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 脱出速度はどう現れるか

    **「無限遠で速度が 0 になる」条件**

    脱出できるギリギリとは：

    $$
    r \to \infty,\quad v \to 0
    $$

    このとき

    $$
    \frac12 v_0^2 - gR = 0
    $$

    よって

    $$
    \boxed{
    v_0 = \sqrt{2gR}
    }
    $$

    これが **脱出速度**。
    """)
    return


@app.cell(hide_code=True)
def _():

    # # 地球
    # R = 1.0
    # theta = np.linspace(0, 2*np.pi, 400)
    # x_earth = R * np.cos(theta)
    # y_earth = R * np.sin(theta)

    # # ロケット位置
    # r = 1.6
    # rocket_x = 0
    # rocket_y = r

    # plt.figure(figsize=(5, 5))

    # # 地球
    # plt.plot(x_earth, y_earth, label="Earth")
    # plt.fill(x_earth, y_earth, alpha=0.2)

    # # 地球中心
    # plt.plot(0, 0, 'ko')
    # plt.text(0, -0.12, "Earth center", ha='center')

    # # ロケット
    # plt.plot(rocket_x, rocket_y, 'ro')
    # plt.text(rocket_x+0.05, rocket_y, "Rocket")

    # # 万有引力ベクトル
    # plt.arrow(
    #     rocket_x, rocket_y,
    #     0, -0.4,
    #     head_width=0.05,
    #     length_includes_head=True
    # )
    # plt.text(
    #     0.1, rocket_y-0.45,
    #     r"$\vec F = -\dfrac{mgR^2}{r^2}\hat r$",
    #     fontsize=12
    # )

    # # 距離 R
    # plt.plot([0, 0], [0, R], 'k--', alpha=0.6)
    # plt.text(0.02, R/2, r"$R$", fontsize=12)

    # # 距離 r
    # plt.plot([0, 0], [0, rocket_y], 'k:', alpha=0.6)
    # plt.text(0.02, rocket_y/2, r"$r$", fontsize=12)

    # # # 情報ボックス
    # # plt.text(
    # #     -1.4, 1.2,
    # #     r"$\\begin{cases}"
    # #     r"r: \text{distance from center}\\"
    # #     r"R: \text{Earth radius}\\"
    # #     r"g: \text{gravity at } r=R"
    # #     r"\end{cases}$",
    # #     fontsize=11
    # # )

    # # 装飾
    # plt.axhline(0, color='gray', alpha=0.3)
    # plt.axvline(0, color='gray', alpha=0.3)
    # plt.gca().set_aspect('equal')
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.legend()
    # plt.title("Rocket under Newtonian gravity")
    # plt.show()

    return


@app.cell(hide_code=True)
def _():

    # # from IPython.display import HTML  # Notebook表示用（必要なら）

    # # =========================
    # # 物理パラメータ
    # # =========================
    # R_ = 1.0          # 地球半径（規格化）
    # g = 1.0           # 地表重力加速度
    # v0 = 1.3 * np.sqrt(2 * g * R_)   # 初速（脱出速度との比較）
    # dt = 0.01
    # steps = 1500

    # # =========================
    # # 初期条件
    # # =========================
    # r_ = R_           # 初期位置（地表）
    # v = v0            # 初速度

    # # =========================
    # # 履歴保存
    # # =========================
    # r_list = []
    # v_list = []

    # # =========================
    # # 数値積分（オイラー法）
    # # =========================
    # for _ in range(steps):
    #     a = -g * R_**2 / r_**2     # 万有引力加速度
    #     v += a * dt
    #     r_ += v * dt
    #     r_list.append(r_)
    #     v_list.append(v)

    # r_arr = np.array(r_list)
    # v_arr = np.array(v_list)

    # # =========================
    # # 図の準備
    # # =========================
    # fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

    # # ---- 上：位置アニメーション ----
    # ax1.set_xlim(-2, 2)
    # ax1.set_ylim(-0.2, 2.5)
    # ax1.set_aspect('equal')

    # # 地球
    # theta_ = np.linspace(0, 2*np.pi, 300)
    # ax1.fill(
    #     R_ * np.cos(theta_),
    #     R_ * np.sin(theta_),
    #     alpha=0.3,
    #     label="Earth"
    # )

    # # ロケット
    # rocket, = ax1.plot([], [], 'ro')

    # ax1.set_title("Rocket launch under Newtonian gravity")
    # ax1.legend()

    # # 数式注釈
    # ax1.text(
    #     -1.9, 2.1,
    #     r"$a(r) = -\dfrac{g R^2}{r^2}$" "\n"
    #     r"$v_0 = 1.3\sqrt{2gR}$",
    #     fontsize=10
    # )

    # # ---- 下：r(t) ----
    # ax2.set_xlim(0, steps * dt)
    # ax2.set_ylim(R_ * 0.9, np.max(r_arr) * 1.1)
    # line_r, = ax2.plot([], [], lw=2)
    # ax2.set_xlabel("time")
    # ax2.set_ylabel("r(t)")

    # # =========================
    # # アニメーション更新関数
    # # =========================
    # def update(frame):
    #     # ロケット位置（y方向のみ）
    #     rocket.set_data(0, r_arr[frame])

    #     # r(t)
    #     t = np.arange(frame) * dt
    #     line_r.set_data(t, r_arr[:frame])

    #     return rocket, line_r

    # # =========================
    # # アニメーション生成
    # # =========================
    # ani = FuncAnimation(
    #     fig,
    #     update,
    #     frames=len(r_arr),
    #     interval=30,
    #     blit=False      # NotebookではFalseが安定
    # )

    # plt.tight_layout()

    # # Notebookで表示する場合のみ使用
    # # HTML(ani.to_jshtml())

    # ani

    return


@app.cell
def _(np):
    # パラメータ
    R = 1.0
    g = 1.0
    dt = 0.001
    steps = 40000

    v_escape = np.sqrt(2*g*R)
    v0_list = [0.7*v_escape, 0.9*v_escape, 1.0*v_escape, 1.1*v_escape]

    t = np.arange(steps) * dt

    return R, dt, g, steps, v0_list, v_escape


@app.cell
def _(R, dt, g, np, plt, steps):
    def _():
        v_escape = np.sqrt(2*g*R)
        v0_list = [0.7*v_escape, 0.9*v_escape, 1.0*v_escape, 1.1*v_escape]

        t = np.arange(steps) * dt

        plt.figure(figsize=(7,5))

        for v0 in v0_list:
            r = R
            v = v0
            r_hist = []

            for _ in range(steps):
                a = -g * R**2 / r**2
                v += a * dt
                r += v * dt
                r_hist.append(r)

                if r < R*0.9:   # 地表に戻ったら打ち切り
                    break

            plt.plot(t[:len(r_hist)], r_hist, label=fr"$v_0={v0:.2f}$")

        plt.axhline(R, linestyle="--", alpha=0.5)
        plt.xlabel("time")
        plt.ylabel("r(t)")
        plt.legend()
        plt.title("Radial motion under gravity")
        return plt.show()


    _()
    return


@app.cell
def _(R, dt, g, np, plt, steps):
    def _():

        v_escape = np.sqrt(2*g*R)
        v0_list = [0.7*v_escape, 0.9*v_escape, 1.0*v_escape, 1.1*v_escape]

        t = np.arange(steps) * dt

        plt.figure(figsize=(7,5))

        for v0 in v0_list:
            r = R
            v = v0
            E_hist = []

            for _ in range(steps):
                a = -g * R**2 / r**2
                v += a * dt
                r += v * dt

                E = 0.5*v**2 - g*R**2/r
                E_hist.append(E)

                if r < R*0.9:
                    break

            plt.plot(t[:len(E_hist)], E_hist, label=fr"$v_0={v0:.2f}$")

        plt.axhline(0, linestyle="--", color="black")
        plt.xlabel("time")
        plt.ylabel("Energy")
        plt.legend()
        plt.title("Energy conservation check")
        return plt.show()


    _()
    return


@app.cell
def _(R, dt, g, plt, steps, v0_list):
    def _():
        plt.figure(figsize=(6,6))

        for v0 in v0_list:
            r = R
            v = v0
            r_hist = []
            v_hist = []

            for _ in range(steps):
                a = -g * R**2 / r**2
                v += a * dt
                r += v * dt

                r_hist.append(r)
                v_hist.append(v)

                if r < R*0.9:
                    break

            plt.plot(r_hist, v_hist, label=fr"$v_0={v0:.2f}$")

        plt.xlabel("r")
        plt.ylabel("v")
        plt.legend()
        plt.title("Phase plane (r, v)")
        return plt.show()


    _()
    return


@app.cell
def _(R, g, np, plt, v_escape):
    def _():
        # 初期条件
        r = np.array([1.0, 0.0])
        v = np.array([0.0, 0.9*v_escape])  # 横方向速度

        dt = 0.001
        steps = 30000

        traj = []

        for _ in range(steps):
            dist = np.linalg.norm(r)
            a = -g * R**2 * r / dist**3

            v += a * dt
            r += v * dt

            traj.append(r.copy())

        traj = np.array(traj)

        plt.figure(figsize=(5,5))
        plt.plot(traj[:,0], traj[:,1])
        plt.gca().set_aspect("equal")

        # 地球
        theta = np.linspace(0, 2*np.pi, 300)
        plt.fill(R*np.cos(theta), R*np.sin(theta), alpha=0.3)

        plt.title("2D orbit under Newtonian gravity")
        return plt.show()


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 高校物理の公式の正体

    高校物理で習う

    $$
    \boxed{v^2 - v_0^2 = 2ax}
    $$

    は、**暗記公式ではなく**、次の関係から来ています：

    $$
    a = \frac{dv}{dt}, \quad v = \frac{dx}{dt}
    $$

    より

    $$
    a = \frac{dv}{dt}
    = \frac{dv}{dx}\frac{dx}{dt}
    = v\frac{dv}{dx}
    $$

    したがって

    $$
    vdv = adx
    $$

    これを積分すると

    $$
    \int vdv = \int adx
    $$

    ---

    ### 加速度が一定のとき

    $$
    a = \text{const}
    $$

    なので

    $$
    \frac{1}{2}(v^2 - v_0^2) = a(x - 0)
    $$

    $$
    \boxed{v^2 - v_0^2 = 2ax}
    $$

    👉 **「加速度一定」の特別解**が高校公式。

    ---

    ### 今回のロケット問題では？

    今回の加速度は

    $$
    a(r) = -\frac{gR^2}{r^2}
    $$

    つまり **位置依存**。

    同じ手順を使うと：

    $$
    v\frac{dv}{dr} = -\frac{gR^2}{r^2}
    $$

    $$
    vdv = -\frac{gR^2}{r^2}dr
    $$

    積分して：

    $$
    \frac{1}{2}(v^2 - v_0^2)
    = gR^2\left(\frac{1}{r} - \frac{1}{R}\right)
    $$

    $$
    \boxed{
    v^2 - v_0^2
    = 2gR^2\left(\frac{1}{r} - \frac{1}{R}\right)
    }
    $$

    ---

    ### だから結論は？

    > **今回の式は高校公式の完全な一般化**

    です。

    | 高校公式  | 今回       |
    | ----- | -------- |
    | 加速度一定 | 加速度が位置依存 |
    | $a$   | $a(r)$   |
    | $x$   | $r$      |
    | 地表近似  | 万有引力そのもの |

    ---

    ### 直感的に言うと

    高校公式は

    > 「一定の力で引っ張り続けた結果」

    今回の式は

    > 「遠ざかるほど弱くなる力で引っ張られ続けた結果」

    それでも

    $$
    \boxed{
    vdv = a(x)dx
    }
    $$

    という**骨格は全く同じ**。

    ---

    #### さらに一段深い見方（重要）

    実はこの関係は

    $$
    \boxed{
    \text{運動エネルギーの変化} = \text{仕事}
    }
    $$

    そのものです。

    $$
    \frac{1}{2} m(v^2 - v_0^2)
    = \int Fdx
    $$

    * 高校公式 → 一定力の仕事
    * 今回 → 万有引力の仕事

    ---

    ### 🔚 まとめ（暗記を卒業）

    * $v^2 - v_0^2 = 2ax$ は **特殊ケース**
    * 本体は
      $v\frac{dv}{dx} = a(x)$
    * 今回の式はその **完全上位互換**
    * 「公式が違う」のではなく
      **前提条件が違うだけ**
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    <!-- ### 二次元の場合

    質量 $m$ のロケットが、地球中心を原点とする平面内を運動する。
    地球の質量を (M)、万有引力定数を (G) とする。

    ロケットには地球からの万有引力のみが働き、

    [
    \vec F = -\frac{GMm}{r^2}\hat r
    ]

    に従う。

    初期条件として、

    * 初期距離：(r=R)
    * 初期速度：(v_0)
    * 初期速度は地表に対して接線方向

    とする。 -->
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


if __name__ == "__main__":
    app.run()
