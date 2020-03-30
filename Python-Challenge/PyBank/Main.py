#Import CSV and OS Modules
import csv
import os

#I renamed budget_date.cvs to data.csv
dir_path = os.path.dirname(os.path.realpath(__file__))
file_csv = (os.path.join(dir_path,'data.csv'))

#opens csv file and reads the contents 
with open (file_csv) as csvfile:
    csv_reader = csv.reader(file_csv,delimiter=',')

    #reads header row
    csv_header = next(csv_reader)

#print Title and dashed Line in txt file
print('Financial Analysis')
print('-----------------------------------------------')

#assign a unique integer to month string values 
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
month_to_indicies = {month: index for index, month in enumerate(months)}
   #function to find the the earliest and latest date in the date column
def time_months(csv_reader):
        earliest_timestamp = None 
        latest_timestamp = 0  
    #reads each row in the csv file and splits the first column

    # this will separate the month and year
csv_reader = csv.reader(file_csv,delimiter=',')

for row in csv_reader:
    date, profit = row
    month, year = date.split("-")
#month is an int already because of month_to_indicies so this will convert year to int too

year = int(year)

#Get timestamp for each row in date column to compare 
timestamp = year *12 + month_to_indices[month]
    
    #determine the earliest and latest timestamp
    if earliest_timestamp is None:
        earliest_timestamp = timestamp

        #cahnge the earliest timestamp to the current 
        #timestamp or leave the current 

        earliest_timestamp = min(earliest_timestamp,timestamp)
        latest_timestamp = max(latest_timestamp,timestamp) 
        #once you find earliest and latest subtract latest from earliest 
        #to find month lapse and add 1 to count for the last month of data
        time = latest_timestamp - earliest_timestamp + 1 
    print ('Total Months:' , time)

#find total revenue across time
def total_revenue(csv_reader):
    #sum the profit column to find the total revenue
    revenue = sum(profit for _, profit in csv_reader)
    print ('Total: ', '$',revenue )

def average_revenue(csv_reader):
    #average the profit column and divide by time 
    revenue = []
    for row in csvreader:
        date,profit = row
        revenue.append(profit)
    #average will be revenue divided by 85, number of months with revenue
    average = revenue/ 85 
print ('Average change:', average)

#Find the greatest and smallest profit change
def profit_change(csv_reader):
    greatest_profit, greatest_profit_timestamp = None, None
    smallest_profit, smallest_profit_timestamp = None, None

    #read each row in the csv file to find the total number of rows 
    csv_contents = [row for row in csv_reader]

    #loop though the rows to find difference in profits from month to month
    for index in range(len(csv.contents)-1):
        #compare current row to the one following to find difference in profits
        current_date, current_profit = csv_contents[index]
        next_date, next_profit = csv_contents[index+1]
        
        #find difference in profit between both months
        profit_difference = int(next_profit) - int(current_profit)

    #compare to find greatest and smallest profit
        if greatest_profit is None or greatest_profit < profit_difference:
            greatest_profit, greatest_profit_timestamp = profit_difference, next_date
        if smallest_profit is None or smallest_profit > profit_difference:
            smallest_profit,smallest_profit_timestamp = profit_difference, next_date

print('Greatest Increase in Profits: {} {}'.format(greatest_profit_timestamp, greatest_profit))
print('Greatest Decrease in Profits: {} {}'.format(smallest_profit_timestamp, smallest_profit))


#did not finish and asked for extension


  