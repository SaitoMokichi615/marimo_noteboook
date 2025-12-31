import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import itertools
    import string
    import math
    return itertools, math, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **順列の総数**
    $n$個の要素から$k$個選んで並べた順列の総数は

    $$
    {}_nP_{k} = \underbrace{n(n-1)(n-2)\cdots(n-(k-1))}_{k\text{個}} \tag{*}
    $$

    $n$ 個の異なる要素から $k$ 個を選んで並べるとき、
    * 1 番目に置く要素は $n$ 通り、
    * 2 番目に置く要素はすでに 1 個使っているため $n-1$ 通り、
    * 同様に、$i$ 番目には $n-(i-1)$ 通りの選び方がある。

    したがって、各段階の選び方を掛け合わせることで、
    順列の総数は(*)と表すことが出来る。

    また(*)は次のように書くこともできる。

    $$
    \begin{aligned}
    {}_nP_{k} &= \underbrace{n(n-1)(n-2)\cdots (n-(k-1))\Big(\frac{(n-k)(n-(k+1))\cdots 2\cdot 1}{(n-k)(n-(k+1))\cdots 2\cdot 1}\Big)}_{n\text{個}} \\
    &= \frac{n!}{(n-k)!}  \tag{**} \\
    \end{aligned}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **組み合わせの総数（二項係数）**
    異なる$n$から$k$個選んだ組み合わせの総数は、次のように表すことが出来る（**二項係数**）。

    $$
    \dbinom{n}{k} = \frac{{}_nP_k}{k!} = \frac{n!}{k!(n-k)!}
    $$


    * $n!$:全員を順番に並べる方法

    * $k!$:選ばれた側の順番の重複

    * (n-k)!:選ばれなかった側の順番の重複

    順序に意味のない部分を全部割り算で消している。

    「順番を区別して数えたもの」から「順番の違いによる重複」を割り算で取り除いた結果である。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <!-- ###**順列・組み合わせ**
    5つのアルファベットの集合$\{a,b, c, d, e \}$から重複なしで異なる3つを選んで並べることを考える。
    $a$, $b$, $c$ の3つを選んで組み合わせる並べる並べ方は、
    * $a\rightarrow b \rightarrow c$
    * $a\rightarrow c \rightarrow b$
    * $b\rightarrow a \rightarrow c$
    * $b\rightarrow c \rightarrow a$
    * $c\rightarrow a \rightarrow b$
    * $c\rightarrow b \rightarrow a$

    全部で$6$通り($3!$ = $3\cdot 2 \cdot 1$通り)。

    つまり、**$a$, $b$, $c$ の組み合わせは$3!$通りの重複する並び順がある**。 -->
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    letters = "abcde"# string.ascii_lowercase  # 'a' ~ 'z'

    k_input = mo.ui.slider(0, len(letters), value=3, label="取り出す数:k")
    k_input
    return k_input, letters


@app.cell
def _(k_input):
    # パラメータ
    k = k_input.value
    return (k,)


@app.cell(hide_code=True)
def _(itertools, k, letters, math):
    # アルファベットの順列
    perms = list(itertools.permutations(letters, k))

    print("順列の例（最初の10個）:")
    for p in perms[:10]:
        print(p)

    print("順列の総数:", len(perms))

    fact = math.factorial(k)
    print(f"順列内の同一の組み合わせパターンを、重複して{k}!={fact}回カウントしている")
    return fact, perms


@app.cell(hide_code=True)
def _(itertools, k, letters):
    combs = list(itertools.combinations(letters, k))

    print("\n組み合わせの例:")
    for c in combs:
        print(c)

    print("組み合わせの総数:", len(combs))
    return


@app.cell(hide_code=True)
def _(fact, perms):
    # 順列を「並び替えて同一視」する
    # 例：k = 3のとき、
    # ('a','c','b') → ('a','b','c')
    # ('b','a','c') → ('a','b','c')
    # ('b','a','c') → ('a','b','c')
    # 👉 同じ文字集合はすべて同一キーになる
    normalized = {tuple(sorted(p)) for p in perms}

    print("\n順列から重複除去した結果:")
    for n in normalized:
        print(n)

    print("重複除去後の数:", len(normalized))
    print(f"順列の総数を重複の総数で割った数:{len(perms)/fact}")
    return


if __name__ == "__main__":
    app.run()
