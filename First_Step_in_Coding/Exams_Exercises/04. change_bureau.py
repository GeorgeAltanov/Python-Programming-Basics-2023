bitcoin = int(input())
chinese_yuan = float(input())
commission = float(input())

bitcoin_to_bgn = bitcoin * 1168
chinese_yuan_to_usd = chinese_yuan * 0.15
usd_to_bgn = chinese_yuan_to_usd * 1.76
bgn_to_euro = (bitcoin_to_bgn + usd_to_bgn) / 1.95

commission_in_euro = bgn_to_euro * commission / 100
result = bgn_to_euro - commission_in_euro

print(f"{result:.2f}")
