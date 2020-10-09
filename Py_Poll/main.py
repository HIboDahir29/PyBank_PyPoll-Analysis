import os
import csv


# navigating and joining the file path
election_data = os.path.join("Resources", "election_data.csv")

# Declaring values
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open(election_data) as csv_file:
    csv_Reader = csv.reader(csv_file, delimiter=",")
    csv_Header = next(csv_Reader)
    print(f'Header : {csv_Header}')

# to add the total votes
    for row in csv_Reader:
        total_votes += 1

        # Checking if the names exist and creating a count of the total votes each candidate has
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1

# creating a dict and using candidates as key, votes as value pair
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]

# adding the list to map into a dict by using the zip function
add_pair = zip(candidates, votes)

#storing the values in dictionary and finding the max value.
Key_value_pair = dict(add_pair)
Max_value = max(Key_value_pair, key=Key_value_pair.get)

# percent values of the votes
khan_percent = round((khan_votes/total_votes) * 100, 2)
correy_percent = round((correy_votes/total_votes)*100, 2)
li_percent = round((li_votes/total_votes) * 100, 2)
otooley_percent = round((otooley_votes/total_votes) * 100, 2)

# Printing the output

print("Election Results")
print("*-*-*-*-*-*-*--**-*-*-**-*-*-*-*")
print(f"Total votes :  {total_votes}")
print("*-*-*-*-*-*-*--**-*-*-**-*-*-*-*")
print(f'Khan:{khan_percent: .3f} ({khan_votes})')
print(f'Correy: {correy_percent: .3f} ({correy_votes})')
print(f'Li: {li_percent: .3f} ({li_votes}) ')
print(f"O'Tooley: {otooley_percent: .3f} ({otooley_votes})")

print("*-*-*-*-*-*-*--**-*-*-**-*-*-*-*")
print(f"Winner : {Max_value}")

# output to a text file


output = open("Analysis/Py_Poll.txt", "w")
output.write("Election Results" + "\n")
output.write(f"Total votes :  {total_votes}  \n")
output.write("*-*-*-*-*-*-*--**-*-*-**-*-*-*-* \n")
output.write(f'Khan:{khan_percent: .3f} ({khan_votes}) \n')
output.write(f'Correy: {correy_percent: .3f} ({correy_votes}) \n')
output.write(f'Li: {li_percent: .3f} ({li_votes}) \n')
output.write(f"O'Tooley: {otooley_percent: .3f} ({otooley_votes}) \n")
output.write("*-*-*-*-*-*-*--**-*-*-**-*-*-*-* \n")
output.write(f"Winner : {Max_value}")


output.close()
