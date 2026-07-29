import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
df = pd.read_csv("Customer Churn.csv")

#count customers by churn status
churn_count = df["Churn"].value_counts()
print(churn_count)

#calculate percentage
churn_percentage = df["Churn"].value_counts(normalize=True)*100
print(churn_percentage.round(2))

#visualization 
churn_percentage.plot(
    kind="bar",
    figsize=(6,4),
    color=["steelblue", "tomato"]
)
plt.title("Customer Churn percentage")
plt.xlabel("Churn")
plt.ylabel("Percentage (%)")
plt.xticks(rotation=0)
plt.show()

#Do customers who complain churn more often?
complains_churn = pd.crosstab(
    df["Complains"],
    df["Churn"],
    normalize="index"
)* 100
print(complains_churn.round(2))

#visualization 
complains_churn.plot(
    kind="bar",
    figsize=(7,5)
)
plt.title("Churn Rate by Complaints")
plt.xlabel("Complains")
plt.ylabel("Percentage (%)")
plt.xticks(rotation=0)

plt.show()

#Does subscription length affect churn?

subscription = df.groupby("Churn")["Subscription  Length"].mean()
print(subscription.round(2))

#visualization 

subscription.plot(
    kind="bar",
    figsize=(6,4),
    color=["steelblue", "tomato"]
)
plt.title("Average Subscrition length by Churn")
plt.ylabel("Months")
plt.xticks(rotation=0)

plt.show()

#Do higher charge amounts increase churn?

charge = df.groupby("Churn")["Charge  Amount"].mean()

print(charge.round(2))

#visualization

charge.plot(
    kind="bar",
    figsize=(6,4),
    color=["steelblue","tomato"]
)
plt.title("Average Charge Amount by Churn")
plt.ylabel("Charge  Amount")
plt.xticks(rotation=0)

plt.show()

#Which Age Group has the highest churn?

age_group = pd.crosstab(
    df["Age Group"],
    df["Churn"],
    normalize="index"
)* 100

print(age_group.round(2))

#order by 
age_group = age_group.sort_values(
    by=1,
    ascending=False
)
print(round(2))

#visualization 

age_group.plot(
    kind="bar",
    figsize=(8,5)
)
plt.title("Churn Rate by Age Group")
plt.ylabel("Percentage (%)")

plt.show()

#Does customer value influence churn?

customer_value = df.groupby("Churn")["Customer Value"].mean()

print(customer_value.round(2))

#visualization

customer_value.plot(
    kind="bar",
    figsize=(6,4),
    color=["steelblue","tomato"]
)

plt.title("Average Customer Value by Churn")
plt.ylabel("Customer Value")

plt.xticks(rotation=0)

plt.show()

#Do customers with higher service usage churn less?

usage = df.groupby("Churn")["Seconds of Use"].mean()

print(usage.round(2))

#Visualization

usage.plot(
    kind="bar",
    figsize=(6,4),
    color=["steelblue","tomato"]
)

plt.title("Average Seconds of Use by Churn")
plt.ylabel("Seconds")

plt.xticks(rotation=0)

plt.show()

#Which customer profile is most likely to churn?

customer_profile = pd.crosstab(
    [df["Complains"], df["Tariff Plan"], df["Age Group"]],
    df["Churn"],
    normalize="index"
)* 100

print(customer_profile.round(2))

customer_profile = customer_profile.sort_values(
    by=1,
    ascending=False
)

print(customer_profile.head(10))

#visualization top 10 churn

top_profiles = customer_profile.head(10)

top_profiles[1].plot(
    kind="bar",
    figsize=(12,6),
    color="tomato"
)

plt.title("Top 10 Customer with Highest Churn Rate")
plt.xlabel("Customer Profile")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()