#Import Pandas module and load the data

import pandas as pd
df = pd.read_csv("C:\\Users\\logan.b\\Downloads\\Call Log - 2026 - January.csv")
df.head()
list(df.columns)


#Which issue types appear most often?

top_issues = df["Reason"].value_counts().head(5) # Returns top 5 values and the amount of times they appear


#Make a chart

import matplotlib.pyplot as plt

top_issues.plot(kind="bar",
                color=["teal","gold"],
                title="Top 5 Call Reasons",
                ylabel="Count",
                figsize=(10,6))

plt.show()



#Findings/insights:

#A lot of time is being spent assisting clinics with their 3rd party billing.
#Additionally, installation assistance is a very basic process that we are still getting lots of calls about.
#We should find a way to incorporate short tutorials on 3rd party billing when assisting users with installation.
