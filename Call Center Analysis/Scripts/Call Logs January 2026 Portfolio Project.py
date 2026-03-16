#Import Pandas module and load the data

import pandas as pd
df = pd.read_csv("C:\\Call Center Analysis\\Data\\synthetic_call_log_january_50.csv")
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

'''Since the top call reason is Hardware, we should make sure that we have a minimum system requirements page
on our website so that clients know whether their devices are compatible with our program. It's likely that the software
crash issue could be related to incompatible hardware so reducing the number of hardware calls should also reduce the number
of Software Crash calls.
'''

