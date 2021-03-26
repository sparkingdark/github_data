import pandas as pd
from giturlparse import parse

df = pd.read_csv("./awesome_repo.csv")

owner = []
project_name = []

for i in df["links"]:
    data = parse(i)
    owner.append(data.owner)
    project_name.append(data.repo)

print(owner[:5])
print(project_name[:5])

df["owner"] = owner
df["repo"] = project_name

df2 = df.reindex(columns=["repo","owner","stars","links"])

df2["links"] = df["links"]

df2.to_csv("awesome_list.csv")