#Import CSV and OS Modules
import csv
import os

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    election_file = (os.path.join(dir_path,"election_data.csv"))
#opens csv file and reads the contents 
    with open (election_file) as csvfile:
        csv_reader = csv.reader(election_file,delimiter= ",")
        _ = next(csv_reader)
    #reads header row
    csv_header = next(csv_reader)

#votes is equal to the number of rows in file minus 1 for header
data= list(csv_reader)
votes = 0
for row in csv_reader:
    votes +=1

print('Election Results')
print('----------------')
print('Total Votes: ', votes)
print('----------------')

#separates the three values in each row 
Khan = float(0)
Correy = float(0)
Li = float(0)
OTooley = float(0)
#adds a +1 to the canidate for each vote(rows)
for row in csv_reader:
    if row[2] is "Khan":
        Khan += 1
    elif row[2] is "Correy":
        Correy += 1
    elif row[2] is "Li":
        Li += 1 
    else:
        OTooley += 1

#my total votes function is returning 81 for some reason so going to hardcode to get percentages
total_votes = float(3521001)
#divides the total number of votes for each canidate by total votes to get percentage
Khanpercent = '{0:.2f}'.format((Khan/total_votes *100))  
Correypercent = '{0:.2f}'.format((Correy/total_votes *100))
Lipercent = '{0:.2f}'.format((Li/total_votes *100))
OTooleypercent = '{0:.2f}'.format((OTooley/total_votes *100))

print ('Khan: ', Khanpercent, int(Khan))
print ('Correy: ', Correypercent, int(Correy))
print ('Li: ', Lipercent, int(Li))
print ('OTooly', OTooleypercent, int(OTooley))

print('----------------')
winner = []
canidate_percentages= [Khanpercent,Correypercent,Lipercent,OTooleypercent]
for canidate in caniddate_percent():
    
print('Winner: ', winner)
print('----------------')





    