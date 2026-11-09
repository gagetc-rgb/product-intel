#!/bin/bash
# Collect all Loox review dates for one product; output: <label>_dates.txt (M/D/YYYY per line)
# Usage: loox_curve.sh <loox_widget_id> <shopify_product_id> <label> <total> [limit]
wid=$1; pid=$2; label=$3; total=$4; lim=${5:-40}
pages=$(( (total + lim - 1) / lim ))
: > "${label}_dates.txt"
for ((p=1; p<=pages; p++)); do
  curl -sL -A "Mozilla/5.0" --max-time 60 --retry 2 "https://loox.io/widget/$wid/reviews/$pid?limit=$lim&page=$p" \
   | grep -oE "\b[0-9]{1,2}/[0-9]{1,2}/20[0-9]{2}\b" >> "${label}_dates.txt"
done
echo "$label done: $(wc -l < ${label}_dates.txt) dates of $total"
