# 0-numpy-size.py
(34*366)のnumpyリストを55回ループを回した結果どうなるかチェック
→8ビットの領域確保
元々32ビットなので、圧縮したら1/4になる計算

# 前提条件
- 行列サイズは任意指定（1000で取った）
- 行列の要素は全てランダムにする
- 余裕が有れば疎行列のパターンでどうなるか

# ファイルの内容
## 1-list_roop.py
for文とlist型で回すようにしている
→遅い

## 2-numpy_roop.py
for文とnumpyで回すようにしている
→遅い

## 3-numpy_dot.py
dot関数を使用して演算
→Pythonだと一番早い


## 4-numpy_matmul.py
matmul関数を使用して演算
→dotや@よりちょい遅い



## 5-numpy_@.py
@を使用して演算（内部的にはmatmulと同じ）
→matmulより早く、dotより遅い


## 6-numpy_ast.py
"*"を使用して演算
→結果がおかしかったので除外

## 7-static.c
C言語で静的に配列を確保した場合を想定
gettimeofday()とclock_gettime()で計測

### gettimeofday()
約1.72[s](dotより早い)

### clock_gettime()
約1.82[s](dot並みかちょい遅いくらい)


