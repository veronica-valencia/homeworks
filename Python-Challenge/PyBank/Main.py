#Import CSV and OS Modules
import csv
import os

#I renamed budget_date.cvs to data.csv
dir_path = os.path.dirname(os.path.realpath(__file__))
file_csv = (os.path.join(dir_path,'data.csv'))

#opens csv file and reads the contents 
with open (file_csv) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=',')

    #reads header row
    csv_header = next(csv_reader)

    #print Title and dashed Line in txt file
    print('Financial Analysis')
    print('-----------------------------------------------')
    #find total months in data 
    total_months= 0
    revenue = []
    first_row = next(csv_reader)
    revenue.append(first_row[1])
    previous_net = first_row[1] 
    net_changes = {}
    greatest_profit = 0
    smallest_profit = 0
    
    for row in csv_reader:
        date,profit = row
        profit = int(profit)
        total_months +=1
        revenue.append(profit)
        
        #find difference in profit between both months
        profit_difference = profit - int(previous_net)

        #compare to find greatest and smallest profit
        if greatest_profit  < profit_difference:
            greatest_profit = profit_difference 
            net_changes[date] = greatest_profit
        if smallest_profit  > profit_difference:
            smallest_profit = profit_difference
            net_changes[date]= smallest_profit

    revenue_sum = sum(revenue) 
    average= revenue_sum/total_months
    print('Total Months:',total_months)
    print('Total: $ {}'.format(str(revenue_sum)))
    print(f'Average Change:{average} ')
    print('Greatest Increase in Profits: {} {}'.format(greatest_profit_timestamp, greatest_profit))
    print('Greatest Decrease in Profits: {} {}'.format(smallest_profit_timestamp, smallest_profit))


    


  