import os
import csv
import pandas as pd


csvpath = os.path.join("election_data_2.csv")
df = pd.read_csv(csvpath)
results = open("election_results.txt",'w')
voters = len(df["Voter ID"])

candidates = df["Candidate"].unique()

candidate_group = df.groupby(["Candidate"])
grouped = candidate_group.count().head()
new_group = grouped.rename(columns={"Voter ID":"Number of Voters"}).drop(columns=["County"])
percent_vote = new_group["Number of Voters"]/voters*100
new_group["Percentage of Votes"] = percent_vote

new_df = pd.DataFrame(df["Candidate"].value_counts())
winner = new_df["Candidate"].max()
candidate_winner = new_df.loc[new_df["Candidate"]==winner]

print("The total number of votes cast is " + str(voters))
print(candidates)
print(new_group)
print("The winner of the election is "+ str(candidate_winner))

output_file = os.path.join("election_results.txt")
with open(output_file, "a", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Candidate", "Number of Voters", "Percentage of Votes"])

    new_group.to_csv(datafile,sep=' ',mode='a')

results.write("Total Votes: " + str(voters)+"\n")
results.write("Winner: " + str(candidate_winner)+"\n")
