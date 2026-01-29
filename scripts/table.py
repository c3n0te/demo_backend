import numpy as np
import pandas as pd

rng = np.random.default_rng()
status = ["Paid", "Unpaid"]
method = ["Credit Card", "Paypal"]
df = pd.DataFrame({"Invoice":[], "Status":[], "Method":[], "Amount":[]})

for i in range(25):
    inv = f"INV{i}"
    stat = rng.choice(status)
    meth = rng.choice(method)
    amount = rng.uniform(low=0., high=1000.)
    #d = {"Invoice":inv, "Status":stat, "Method":meth, "Amount":amount}
    new_row = [inv, stat, meth, amount]
    df.loc[len(df)] = new_row

df.to_csv("table_data.csv")
