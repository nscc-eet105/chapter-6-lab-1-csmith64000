#chris smith
#Chapter 6 Lab 1
#6/23/25

#Tuple
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

#Sales
sales=[]
for day in days:
    ammount = float(input(f"Enter the sales ammount for {day:<9}:"))
    sales.append(ammount)

#Math
total_sales = sum(sales)
average_sales = total_sales / len(sales)
max_sale = max(sales)
min_sale = min(sales)
max_day = days[sales.index(max_sale)]
min_day = days[sales.index(min_sale)]

#output
print(f"\nTotal weekly sales   : ${total_sales:.2f}")
print(f"Average weekly sales  : ${average_sales:.2f} on {max_day}")
print(f"\nThe highest sales were ${max_sale:.2f} on {max_day}")
print(f"The lowest sales were  ${min_sale:.2f} on {min_day}")
