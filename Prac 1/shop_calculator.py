       n=float(input("Price of item: "))
        list.append(n)
    total= sum(list)
    if total > 100:
        total1= float(total -total*(10/100))
        print("Total price for " +str(item) +" item is: " +str(total1))
    else:
        print("Total price for " + str(item) + " item is: " + str(total))



if __name__ == '__main__':
        main()