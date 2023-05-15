#!/bin/bash

# シェルスクリプトに引数が渡されなかった場合のエラーメッセージ
if [ $# -eq 0 ]; then
  echo "Usage: ./numpy.sh N"
  exit 1
fi

# 実行回数
M=10

# 行列サイズ
N=$1

# 結果ファイルのパス
result_file="result/results.csv"

# 結果ファイルが存在する場合は削除して新規作成
if [ -f "$result_file" ]; then
  rm "$result_file"
fi

# タイトル行の書き込み
echo "Execution Time,3-numpy_dot,4-numpy_matmul,5-numpy_@" >> "$result_file"

# 実行回数ごとに計算時間を計測して結果ファイルに追記
for ((i=1; i<=M; i++))
do
  echo "Calculating $i/$M"

  # 3-numpy_dot.pyの実行時間を計測
  dot_time=$(python3 3-numpy_dot.py $N)

  # 4-numpy_matmul.pyの実行時間を計測
  matmul_time=$(python3 4-numpy_matmul.py $N)

  # 5-numpy_@.pyの実行時間を計測
  at_time=$(python3 5-numpy_@.py $N)

  # 結果ファイルに計算時間を追記
  echo "$i,$dot_time,$matmul_time,$at_time" >> "$result_file"
done

# 平均と標準偏差の計算
avg_dot=$(awk -F, '{ total += $2 } END { printf "%.5f", total/NR }' "$result_file")
avg_matmul=$(awk -F, '{ total += $3 } END { printf "%.5f", total/NR }' "$result_file")
avg_at=$(awk -F, '{ total += $4 } END { printf "%.5f", total/NR }' "$result_file")

std_dot=$(awk -F, -v avg="$avg_dot" '{ diff = $2 - avg; sq_sum += diff^2 } END { printf "%.5f", sqrt(sq_sum/(NR-1)) }' "$result_file")
std_matmul=$(awk -F, -v avg="$avg_matmul" '{ diff = $3 - avg; sq_sum += diff^2 } END { printf "%.5f", sqrt(sq_sum/(NR-1)) }' "$result_file")
std_at=$(awk -F, -v avg="$avg_at" '{ diff = $4 - avg; sq_sum += diff^2 } END { printf "%.5f", sqrt(sq_sum/(NR-1)) }' "$result_file")

# 平均と標準偏差を結果ファイルに追記
echo "Average,$avg_dot,$avg_matmul,$avg_at" >> "$result_file"
echo "Std Deviation,$std_dot,$std_matmul,$std_at" >> "$result_file"

echo "Calculation complete! Results are stored in $result_file"
