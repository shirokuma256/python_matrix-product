#!/bin/bash

# �����륹����ץȤ˰������Ϥ���ʤ��ä����Υ��顼��å�����
if [ $# -eq 0 ]; then
  echo "Usage: ./numpy.sh N"
  exit 1
fi

# �¹Բ��
M=10

# ���󥵥���
N=$1

# ��̥ե�����Υѥ�
result_file="result/results.csv"

# ��̥ե����뤬¸�ߤ�����Ϻ�����ƿ�������
if [ -f "$result_file" ]; then
  rm "$result_file"
fi

# �����ȥ�Ԥν񤭹���
echo "Execution Time,3-numpy_dot,4-numpy_matmul,5-numpy_@" >> "$result_file"

# �¹Բ�����Ȥ˷׻����֤��¬���Ʒ�̥ե�������ɵ�
for ((i=1; i<=M; i++))
do
  echo "Calculating $i/$M"

  # 3-numpy_dot.py�μ¹Ի��֤��¬
  dot_time=$(python3 3-numpy_dot.py $N)

  # 4-numpy_matmul.py�μ¹Ի��֤��¬
  matmul_time=$(python3 4-numpy_matmul.py $N)

  # 5-numpy_@.py�μ¹Ի��֤��¬
  at_time=$(python3 5-numpy_@.py $N)

  # ��̥ե�����˷׻����֤��ɵ�
  echo "$i,$dot_time,$matmul_time,$at_time" >> "$result_file"
done

# ʿ�Ѥ�ɸ���к��η׻�
avg_dot=$(awk -F, '{ total += $2 } END { printf "%.5f", total/NR }' "$result_file")
avg_matmul=$(awk -F, '{ total += $3 } END { printf "%.5f", total/NR }' "$result_file")
avg_at=$(awk -F, '{ total += $4 } END { printf "%.5f", total/NR }' "$result_file")

std_dot=$(awk -F, -v avg="$avg_dot" '{ diff = $2 - avg; sq_sum += diff^2 } END { printf "%.5f", sqrt(sq_sum/(NR-1)) }' "$result_file")
std_matmul=$(awk -F, -v avg="$avg_matmul" '{ diff = $3 - avg; sq_sum += diff^2 } END { printf "%.5f", sqrt(sq_sum/(NR-1)) }' "$result_file")
std_at=$(awk -F, -v avg="$avg_at" '{ diff = $4 - avg; sq_sum += diff^2 } END { printf "%.5f", sqrt(sq_sum/(NR-1)) }' "$result_file")

# ʿ�Ѥ�ɸ���к����̥ե�������ɵ�
echo "Average,$avg_dot,$avg_matmul,$avg_at" >> "$result_file"
echo "Std Deviation,$std_dot,$std_matmul,$std_at" >> "$result_file"

echo "Calculation complete! Results are stored in $result_file"
