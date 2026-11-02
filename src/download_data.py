import arff
import pandas as pd
import re


with open(r"data\raw\Promise+.arff", "r",encoding="utf-8") as f:
    raw_data = f.read()



    repaired_data = re.sub(r"'([A-Za-z0-9_]+)$", r"',\1", raw_data, flags=re.MULTILINE)

    repaired_data = repaired_data.replace('\\', '\\\\')



    dataset = arff.loads(repaired_data)







df = pd.DataFrame(
    dataset["data"],
    columns=[attr[0] for attr in dataset["attributes"]]
)

df.to_csv(r"data\raw\promise_raw.csv", index=False, encoding="utf-8")



print("Data download and conversion to CSV completed successfully.")