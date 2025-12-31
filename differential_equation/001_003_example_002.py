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
    ###**人口モデル**

    時刻$t$における人口を$N=N(t)$とする。

    人口は継続しうる限り増加するが、上限$N_{\infty}$があり、

    人口の増加率は、現在の人口$N(t)$と未利用の人口資源に対する比$1-\dfrac{N}{N_{\infty}}$に比例する（ヴェアフルストの人口論）。

    A国における2000年の人口は$1.23\times10^8$、2005年の人口は$1.25\times 10^8$であった。

    このとき、A国の2010年の人口を、ヴェアフルストの人口論に基づいて予測せよ。

    ただし、$N_{\infty}=1.3\times10^8$とし、計算過程で数値を求める場合は、小数点以下第2位まで求めればよいものとする。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ####**(A) 人口は増加する**

    * 増加率は 正
    * 時間変化は微分で以下のように書ける

    $$
    \frac{dN}{dt}
    $$

    ####**(B) 増加率は「現在の人口 $N(t)$ 」に比例**

    * 「人口が多いほど出生数も多い」という仮定。

    $$
    \frac{dN}{dt} \propto N
    $$

    ####**(C) ただし「未利用の人口資源」にも比例**

    $$
    人口資源の残り具合 = (上限)- (現在) = N_{\infty} - N
    $$

    比で表すと、

    $$
    \frac{N_{\infty} - N}{N_{\infty}} = 1-\frac{N}{N_{\infty}}
    $$

    **どれくらい余裕が残っているかを 0〜1 の割合で表したもの**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ###**文章 → 数式への翻訳**

    (A)(B)(C) をすべて掛け合わせると：

    $$
    \boxed{
    \frac{dN}{dt}  = kN\left(1 - \frac{N}{N_{\infty}}\right)
    } \tag{1.}
    $$

    * $k > 0$:比例定数(増加の速さ)
    * $N_{\infty}$:人口の上限

    ---
    ### 数式の再翻訳
    **人口増加率$\dfrac{dN}{dt}$は、「2つの要因の掛け算」**

    (1) $N$：増える主体そのもの(人口)

    人が多いほど→ 子どもを産む人も多い→ 増えやすい

    👉 指数関数的増加の要因（マルサス型人口論）

    (2) $1-\dfrac{N}{N_\infty}$：余力・空き容量

    * $N \ll N_\infty$→ 食料・土地・仕事に余裕→ 増えやすい
    * $N \approx N_\infty$→ 資源が限界→ 増えにくい

    👉 「ブレーキ」の役割

    (3) 掛け算の効果が形を決める

    $$
    \underbrace{\dfrac{dN}{dt}}_{\text{人口増加率}} \;\propto\;
    \underbrace{N}_{\text{アクセル}}
    \times
    \underbrace{\left(1-\frac{N}{N\infty}\right)}_{\text{ブレーキ}}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    (1.)は、

    $$
    \frac{dN}{dt} = f(N)g(N)
    $$

    の形の微分方程式(**変数分離系のパターン**)


    (1.)を変形すると、

    $$
    \frac{N_{\infty}}{N\left({N_{\infty}-N}\right)}\frac{dN}{dt}  = k
    $$

    両辺を$t$で積分すると、


    $$
    \int{\frac{N_{\infty}}{N\left({N_{\infty}-N}\right)}\frac{dN}{dt}dt}  = \int{kdt}
    $$

    $$
    \int{\left(\frac{1}{N} + \frac{1}{N_{\infty}-N}\right)dN}  = \int{kdt}  \tag{2.}
    $$

    (2.) について、

    $$
    \begin{aligned}
    (左辺)  &=\log{|N|} - \log{|N_{\infty} - N|} + c_1 \\
    &= \log{\left|\dfrac{N}{N_{\infty} - N}\right|} + c_1 \quad (c_1は任意定数)
    \end{aligned}
    $$

    $$
    (右辺) = kt + c_2 \quad (c_2は任意定数)
    $$

    これより、

    $$
    \log{\left|\dfrac{N}{N_{\infty} - N}\right|} = kt + c \tag{3.}
    $$

    ただし、$c=c_2-c_1$は任意定数。

    よって、

    $$
    \frac{N}{N_{\infty} - N} = e^{kt + C} = e^{c}e^{kt} \tag{4.}
    $$


    (3.)について、$t=0$とし、$N(t=0) = N_0$とすると、

    $$
    e^c = \frac{N_0}{N_{\infty} - N_0}
    $$

    したがって、

    $$
    \boxed{
    \frac{N}{N_{\infty} - N} = \frac{N_0}{N_{\infty} - N_0}e^{kt}
    } \tag{5.}
    $$
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ここで、

    $$
    A = \frac{N_{\infty} - N_0}{N_0}
    $$

    とおくと、

    $$
    \begin{aligned}
    & \frac{N}{N_{\infty} - N} = \frac{e^{kt}}{A}\\\\
    \rightarrow &\frac{N_{\infty} - N}{N} = \frac{A}{e^{kt}}\\\\
    \rightarrow &\frac{N_{\infty}}{N} - 1 = \frac{A}{e^{kt}}\\\\
    \rightarrow &\frac{N_{\infty}}{N} =  1 + \frac{A}{e^{kt}} = \frac{e^{kt} + A}{e^{kt}}\\\\
    \rightarrow &\frac{N}{N_{\infty}} =   \frac{e^{kt}}{e^{kt} + A}\\\\
    \rightarrow &N = \frac{e^{kt}}{e^{kt} + A}N_{\infty}=  \frac{N_{\infty}}{1 + \dfrac{A}{e^{kt}}}\\
    \end{aligned}
    $$

    よって

    $$
    \boxed{
    N(t) =  \frac{N_{\infty}}{1 + Ae^{-kt}} \quad(ロジスティック関数)
    }　\tag{6.}
    $$


    <!-- N10 = N_inf / (1 + (1/A) * sp.exp(-k_val*10)) -->
    """)
    return


@app.cell
def _(sp):
    # 記号
    k = sp.symbols('k', real=True)
    t = sp.symbols('t', real=True)

    # 定数
    N_inf = 1.3
    N0 = 1.23
    N5 = 1.25

    # 初期条件から係数
    A = N0 / (N_inf - N0)

    # 2005年（t=5）で方程式を立てる
    eq = sp.Eq(
        N5 / (N_inf - N5),
        A * sp.exp(k*5)
    )

    # k を解く
    k_val = sp.solve(eq, k)[0]
    k_val.evalf(3)

    return A, N0, N_inf, k_val


@app.cell
def _(A, N_inf, k_val, sp):
    N10 = N_inf / (1 + (1/A) * sp.exp(-k_val*10))
    N10.evalf(3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    (6.)を横軸$t$,縦軸$N$でプロットする。
    """)
    return


@app.cell
def _(N0, N_inf, k_val, np, plt):
    # パラメータ
    k_ = float(k_val)

    # ロジスティック関数
    def N(t):
        A = (N_inf - N0) / N0
        return N_inf / (1 + A * np.exp(-k_*t))

    # def N_exp(t):
    #     return N0 * np.exp(k_*t)



    t_ = np.linspace(0, 80, 300)

    plt.plot(t_, N(t_))
    plt.axhline(N_inf, linestyle="--", alpha=0.5)
    plt.xlabel("t (year from 2000)")
    plt.ylabel("Population (×10^8)")
    plt.title("Logistic population model")
    plt.show()

    # plt.plot(t_, N(t_), label="Logistic")
    # plt.plot(t_, N_exp(t_), "--", label="Exponential")
    # plt.axhline(N_inf, linestyle=":", label="Carrying capacity")
    # plt.legend()
    # plt.show()

    return N, k_, t_


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ロジスティック曲線

    > 語源：logistic「物流・補給」、logistics（兵站・補給）

    「どれだけ物資を運べるか」「どこまで維持できるか」

    👉 無限には増やせない


    * 初期：指数成長に近い
    * 中期：成長が鈍化
    * 後期：上限で停止

     **「人口が増えるほど、人口抑制が強くなる」**

     <!--
    その結果…
    人口 (N)
    増え方
    小さい
    まだ人が少ない → ゆっくり
    中くらい
    人も多く余力もある → 最も速い
    大きい
    余力がない → ほぼ止まる -->
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    (3.)を横軸$t$、縦軸$\log{\left|\dfrac{N}{N_{\infty}-N}\right|}$でプロットする。
    """)
    return


@app.cell
def _(N, N_inf, np, plt, t_):
    log_ratio = np.log(N(t_) / (N_inf - N(t_)))

    plt.plot(t_, log_ratio)
    plt.xlabel("t")
    plt.ylabel("log(N / (N_inf - N))")
    plt.title("Linearized logistic equation")
    plt.show()

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### 位相線

    (1.)を

    $$
    \frac{dN}{dt} = f(N)
    $$

    として、
    位相線でプロットする


    * 状態空間：1次元

    * $N$軸上に、「増えるか／減るか」を 矢印で表す


    <!-- $y = 0$ の直線
    状態は「点」ではなく 位置 N
    時間方向は 矢印
    👉 **「時間を消して、流れだけを見る」**のが位相線 -->


    * $\dfrac{dN}{dt}$が正 → 右向き矢印

    * $\dfrac{dN}{dt}$が負 → 左向き矢印


    **平衡点（増減が0）**

    $$
    f(N)=0 \Rightarrow
    N=0,\; N=N_\infty
    $$
    """)
    return


@app.cell
def _(N_inf, k_, np, plt):

    # パラメータ
    # k = 0.07
    # N_inf = 1.3

    # N の範囲
    N_ = np.linspace(-0.2, 1.6, 400)

    # 微分方程式
    dNdt = k_ * N_ * (1 - N_ / N_inf)

    # 図の準備
    plt.figure(figsize=(8, 1.8))
    plt.axhline(0)

    # 符号に応じて矢印を描く
    for n, dn in zip(N_[::20], dNdt[::20]):
        if dn > 0:
            plt.arrow(n, 0, 0.03, 0,
                      head_width=0.02, head_length=0.02,
                      fc='black', ec='black')
        elif dn < 0:
            plt.arrow(n, 0, -0.03, 0,
                      head_width=0.02, head_length=0.02,
                      fc='black', ec='black')

    # 平衡点
    plt.plot([0, N_inf], [0, 0], 'o')
    plt.text(0, 0.05, '0', ha='center')
    plt.text(N_inf, 0.05, r'$N_\infty$', ha='center')

    # 装飾
    plt.yticks([])
    plt.xlabel('N')
    plt.title('Phase line of the logistic equation')
    plt.tight_layout()
    plt.show()

    return


if __name__ == "__main__":
    app.run()
