from datetime import datetime 
today = datetime.now()
before = datetime(1970, 1, 1)
ecart = float((today - before).total_seconds())
print("Seconds since", before.strftime("%B %-d, %Y:"), f"{ecart:,.4f}", "or", f"{ecart:.2e}", "in scientific notation")
print(today.strftime("%b %-d %Y"))