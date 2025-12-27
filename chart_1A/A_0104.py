import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import random
    import matplotlib.pyplot as plt
    return mo, np, plt, random


@app.cell
def _(mo):
    mo.md(r"""
    ###**問題104**

    当たりと外れのくじが5本ずつ、計10本入った箱がある。この箱から1本ずつくじを引き、当たりくじを引いた人は持ち去るが、はずれくじを引いた人は、そのくじを箱に戻してしまうものとする。

    (1)二人目の人が当たる確率を求めよ。

    (2)二人目と三人目の二人が共に当たる確率を求めよ。

    ---

    (1)
    「一人目の人が10本のくじの中から1本くじを選び、5本のあたりのうち1本を引き当てる」という事象を$A$とすると、

    $$
    \begin{aligned}
    P(A) &= \frac{\dbinom{5}{1}}{\dbinom{10}{1}} = \frac{1}{2}\\
    P(\overline{A}) &= 1 = P(A) = \frac{1}{2}
    \end{aligned}
    $$

    「二人目の人が当たりを引く事象」を$B$とする。

    * 一人目の人が当たった場合、

    $P_A(B)$は、「二人目の人が、9本のくじの中から1本くじを選び、4本のあたりのうち1本を引き当てる」確率であるから、

    $$
    P_A(B) = \frac{\dbinom{4}{1}}{\dbinom{9}{1}} = \frac{4}{9}
    $$

    * 一人目の人が外した場合、

    $P_{\overline{A}}(B)$は、「二人目の人が、10本のくじの中から1本くじを選び、5本のあたりのうち1本を引き当てる」確率であるから、


    $$
    P_{\overline{A}}(B) = \frac{\dbinom{5}{1}}{\dbinom{10}{1}} = \frac{1}{2}
    $$

    $A \cap B$と$\overline{A} \cap B$は排反であるから、
    求める確率は

    $$
    \begin{aligned}
    P(B) &= P(A \cap B) + P(\overline{A} \cap B) \\ &= P(A)P_A(B) +  P(\overline{A})P_{\overline{A}}(B) \\
    &= \frac{1}{2}\cdot\frac{4}{9} + \frac{1}{2}\cdot\frac{1}{2} \\
    &= \frac{2}{9} + \frac{1}{4} \\
    &= \frac{8 + 9}{36} = \frac{17}{36} \; \square
    \end{aligned}
    $$

    ---

    (2)

    「三人目の人が当たりを引く事象」を$C$とする。


    * 「一人目が当たって、二人目が当たった」場合、

    「三人目の人が、8本のくじの中から1本くじを選び、3本のあたりのうち1本を引き当てる」確率は、

    $$
    P_{A\cap B}(C)  = \frac{\dbinom{3}{1}}{\dbinom{8}{1}} = \frac{3}{8}
    $$

    *「一人目が外れて、二人目が当たった」場合

    「三人目の人が、9本のくじの中から1本くじを選び、4本のあたりのうち1本を引き当てる」確率は、


    $$
    P_{\overline{A}\cap B}(C)  = \frac{\dbinom{4}{1}}{\dbinom{9}{1}} = \frac{4}{9}
    $$

    $A\cap B \cap C$と　$\overline{A}\cap B \cap C$は排反であるから、求める確率は

    $$
    \begin{aligned}
    P(B\cap C) &= P(A\cap B \cap C) + P(\overline{A}\cap B \cap C) \\
    &= P(A\cap B)P_{A\cap B}(C) + P(\overline{A}\cap B)P_{\overline{A}\cap B}(C) \\
    &= P(A)P_A(B)P_{A\cap B}(C) + P(\overline{A})P_{\overline{A}}(B)P_{\overline{A}\cap B}(C) \\
    &= \frac{1}{2}\cdot\frac{4}{9}\cdot\frac{3}{8} + \frac{1}{2}\cdot\frac{1}{2}\cdot \frac{4}{9} \\
    &= \frac{3 + 4}{36} = \frac{7}{36} \;\square
    \end{aligned}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**確率過程・確率方程式・マルコフ過程**



    今回の問題は、

    * 初期状態：

    $$
    \boxed{\text{当たり }5\text{本、外れ }5\text{本}}
    $$

    * 外れを引く→「状態が戻る」
    * 当たりを引く→「状態が少しずつ減る」

    そして
    > **当たりの本数だけが状態を決める**


    ここで

    $$
    p_k = \text{「当たりが }k\text{本残っている状態で、次の人が当たる確率」}
    $$

    と定義する。

    ---

    ### 状態遷移の考察

    状態が「当たり $k$本、外れ5本」のとき、

    * 当たる確率は、$\dfrac{k}{k+5}$
    * 当たりは1本減る → 状態 $k-1$

    * 外れる確率は、$\dfrac{5}{k+5}$
    * くじを戻す → 状態は **変わらない（ここが重要）**

    ---

    ### 確率方程式を立てる

    次の人が当たる確率 $p_k$ は、


    $$
    \boxed{p_k= \frac{k}{k+5}\cdot 1+ \frac{5}{k+5}\cdot p_k}
    $$

    - 当たったら確率1で成功
    - 外れたら **同じ状態に戻るので再び$p_k$**


    ---

    ### 方程式を解く

    $$
    p_k - \frac{5}{k+5}p_k = \frac{k}{k+5}
    $$

    $$
    p_k\left(1-\frac{5}{k+5}\right) = \frac{k}{k+5}
    $$

    $$
    p_k \cdot \frac{k}{k+5} = \frac{k}{k+5}
    $$

    $$
    \boxed{p_k = 1}
    $$

    ❗ **これは「いずれ当たる確率」** 。

    > 何人でも引き続ければ、必ず当たりが出る

    という意味。

    ---

    ### 「n人目が当たる確率」は？

    一方で、**n人目が当たる確率**は別で、

    * 「外れが続く」確率が影響する
    * ここで **マルコフ過程的な視点**が効いてくる
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###  マルコフ過程としての見方

    ### 状態空間

    状態を

    $$
    \boxed{S_k = \text{当たりが }k\text{本残っている}}
    \quad (k=0,1,\dots,5)
    $$

    とする。

    ---

    ### 遷移確率

    状態 $S_k$ から：

    * $S_{k-1}$ へ：$\dfrac{k}{k+5}$
    * $S_k$ へ：$\dfrac{5}{k+5}$

    （$S_0$ は吸収状態）

    これは **離散時間マルコフ連鎖** 。

    ---

    ### 遷移図（イメージ）

    ```
    S5 → S4 → S3 → S2 → S1 → S0
     ↑    ↑    ↑    ↑    ↑
     └────┴────┴────┴────┴──
          (外れを引くと戻る)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ### 「二人目が当たる確率」の再解釈

    二人目が当たるとは：

    * 1人目：外れ → 状態 $S_5$
    * 2人目：当たり

    または

    * 1人目：当たり → 状態 $S_4$
    * 2人目：当たり

    という **経路の和**。

    (1)でやった分解と完全一致。

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###**「当たり a 本、外れ b 本」の一般化**

    ### 状態の定義（最重要）

    この種の問題では

    > **状態は「当たりの残り本数」だけで十分**


    $$
    S_k := \text{当たりが }k\text{本残っている状態}
    \quad (k=0,1,\dots,a)
    $$

    外れは常に $b$ 本ある（戻るから）。

    ---

    ## 状態遷移

    状態 $S_k$ にいるとき：

    * 当たりを引く確率

    $$
    \frac{k}{k+b}
    \quad\Rightarrow\quad S_{k-1}
    $$

    * 外れを引く確率

    $$
    \frac{b}{k+b}
    \quad\Rightarrow\quad S_k
    $$

    👉 **同じ状態に戻る自己ループ** があるのが特徴。


    ---

    ### マルコフ連鎖としての性質

    * 状態数：$a+1$
    * 吸収状態：$S_0$
    * 単方向（左）＋自己ループ
    * 必ず最終的に $S_0$ に到達（確率1）


    ---

    ### 確率方程式（復習）

    「状態 $S_k$ から、次の人が当たる確率」を $p_k$ とすると：

    $$
    p_k
    = \frac{k}{k+b} \cdot 1+ \frac{b}{k+b} \cdot p_k
    $$

    $$
    \Rightarrow
    p_k\left(1-\frac{b}{k+b}\right)=\frac{k}{k+b}
    \Rightarrow
    \boxed{p_k=1}
    $$

    👉 **「いずれ当たる確率」は必ず1**
    （外れが戻る限り、無限に試行できる）
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 遷移行列の定義

    状態順を

    $$
    (S_0, S_1, \dots, S_a)
    $$

    とすると、遷移行列 $P$ は

    * $P_{k,k} = \dfrac{b}{k+b}$
    * $P_{k,k-1} = \dfrac{k}{k+b}$
    * その他 $0$

    ---

    ## 遷移行列で何ができる？

    * $P^n$：$n$人後の状態分布
    * 初期分布 $\pi_0=(0,0,0,0,0,1)$
    * $\pi_n=\pi_0P^n$

    👉 **$n$人目が当たる確率**

    👉 **何人で全部なくなるかの分布**

    がすべて行列計算で扱える。
    """)
    return


@app.cell
def _(np):
    def transition_matrix(a, b):
        """
        当たり a 本、外れ b 本の遷移行列
        状態 S_k = 当たりが k 本残っている
        """
        n = a + 1
        P = np.zeros((n, n))

        for k in range(1, n):
            # 外れ → 状態維持
            P[k, k]   = b / (k + b)

            # 当たり → 1本減る
            P[k, k-1] = k / (k + b)      

        P[0, 0] = 1.0  # 吸収状態
        return P

    #     import numpy as np

    # # def transition_matrix(a, b):
    # #     n = a + 1
    # #     P = np.zeros((n, n))

    # #     for k in range(1, n):
    # #         P[k, k]   = b / (k + b)
    # #         P[k, k-1] = k / (k + b)

    # #     P[0, 0] = 1
    # #     return P

    return (transition_matrix,)


@app.cell
def _():
    # a, b = 5, 5
    # P = transition_matrix(a, b)

    # # 行＝「今の状態」
    # # 列＝「次の状態」

    # # → **下三角＋対角成分** の行列になる。
    # print(P)

    # pi = np.zeros(a+1)
    # pi[a] = 1   # 初期状態 S_a

    # print(pi)
    # print(pi[a])


    return


@app.cell
def _(random):
    def simulate_returning(a, b, trials=100000):
        """
        外れが戻るモデル
        何人目で当たりが出たかを記録
        """
        results = []

        for _ in range(trials):
            k = a
            count = 0
            while True:
                count += 1
                if random.random() < k / (k + b):
                    k -= 1
                    results.append(count)
                    break
        return results

    return


@app.cell
def _(random):
    def simulate_non_returning(a, b, trials=100000):
        """
        外れが戻らないモデル
        当たりが出たか／何人目か
        """
        results = []

        for _ in range(trials):
            k, l = a, b
            count = 0
            hit = False

            while k + l > 0:
                count += 1
                if random.random() < k / (k + l):
                    results.append(count)
                    hit = True
                    break
                else:
                    l -= 1

            if not hit:
                results.append(None)  # 最後まで当たらない
        return results

    return


@app.cell
def _(np):
    def prob_hit_at_n(P, a, b, n):
        pi = np.zeros(a+1)
        pi[a] = 1

        for _ in range(n-1):
            pi = pi @ P

        probs = [k/(k+b) for k in range(a+1)]
        return np.dot(pi, probs)

    return (prob_hit_at_n,)


@app.cell
def _(P, a, b, prob_hit_at_n):
    for n in range(1, 10):
        print(n, prob_hit_at_n(P, a, b, n))

    print(f"(1)の結果:{17/36}")
    return


@app.cell
def _(np):
    def state_distributions(P, a, steps):
        pi = np.zeros(a+1)
        pi[a] = 1  # 初期状態 S_a

        history = [pi.copy()]
        for _ in range(steps):
            pi = pi @ P
            history.append(pi.copy())

        return np.array(history)
    return (state_distributions,)


@app.cell
def _(plt, state_distributions, transition_matrix):
    a, b = 5, 5
    P = transition_matrix(a, b)

    history = state_distributions(P, a, steps=30)

    for k in range(a+1):
        plt.plot(history[:, k], label=f"S_{k}")

    plt.xtick = 1
    plt.xlabel("number of people")
    plt.ylabel("probability")
    plt.legend()
    plt.show()

    return P, a, b


@app.function
def geometric(p, n):
    return (1 - p)**(n-1) * p


@app.cell
def _():
    # p0 = a / (a + b)

    # for n_ in range(1, 10):
    #     print(
    #         n,
    #         prob_hit_at_n(P, a, b, n),
    #         geometric(p0, n)
    #     )

    return


@app.cell
def _(np):
    def state_index(k, l, b):
        return k * (b + 1) + l

    def transition_matrix_non_returning(a, b):
        n = (a+1)*(b+1)
        P = np.zeros((n, n))

        for k in range(a+1):
            for l in range(b+1):
                idx = state_index(k, l, b)

                if k + l == 0:
                    P[idx, idx] = 1
                    continue

                if k > 0:
                    P[idx, state_index(k-1, l, b)] = k / (k + l)
                if l > 0:
                    P[idx, state_index(k, l-1, b)] = l / (k + l)

        return P

    return


if __name__ == "__main__":
    app.run()
