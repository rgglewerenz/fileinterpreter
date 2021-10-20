"""
    University Honor Code
    Ross Lewerenz
    10-11-2021
    Project
"""
import math
#Math Functions 
#This function adds up all values in the list and outputs the result
dict_mode = {}
def sumList (list1):
    b=0
    SUM =0
    #For each number in list1 it takes the number and adds it to the final sum
    if b< len(list1):
        while True:
            SUM = SUM + float(list1[b])
            b = b+1
            if b > len(list1)-1:
                break
    return SUM
#This function takes the average and outputs the results
def avgLst (list1):
    b=0
    SUM =0
    #Same as sum
    if b< len(list1):
        while True:
            SUM = SUM + float(list1[b])
            b = b+1
            if b > len(list1)-1:
                break
    #Takes the sum and devides by amount of items in list
    result = float(SUM/(len(list1)))
    return("The average of all the data is " + str(result))
#This function takes the standard deviation in a list and outputs the result
def stdDv(list1):
    #Takes the sum and finds the mean
    listOfStandDevia = []
    mean =0.0
    SUM = sumList(list1)
    mean = float(SUM/len(list1))
    newsum= 0.0
    i=0
    #Takes the mean and substacts the mean from the original list, and then sqaures it 
    if i < len(list1):
        while True:
            listOfStandDevia.append(mean-float(list1[i]))
            i= i+1
            if(i>(len(list1)-1)):
                break
    i=0
    #adds all the new numbers up and divides by the ammount of numbers, then takes the square root of it to find standard deviation
    if i < len(list1):
        while True:
            newsum = newsum + (float(listOfStandDevia[i]) *float(listOfStandDevia[i]))
            i= i+1
            if(i>(len(list1)-1)):
                break
    newsum = newsum/len(listOfStandDevia)
    newsum=math.sqrt(abs(newsum))
    return("Standard deviation in this list is " + str(newsum))
#This function multiplies all values in the list and outputs the result
def product(list1):
    PRODUCT =1.0
    i=0
    #Sam as addition function, but instead multiplies each new item in the list 
    if i < len(list1):
        while True:
            PRODUCT= PRODUCT* float(list1[i])
            i= i+1
            if(i>(len(list1)-1)):
                break
    return "Multiplying all numbers together we get an answer of " + str(PRODUCT)
#This function find the middle term/terms and outputs the result
def median(list1):
    medlow=list1[int(len(list1)/2)]
    medhigh= list1[int(len(list1)/2)+1]
    #If ammount of items in list are even
    if len(list1) %2 == 0:
        return("The middle number is "+ str(list1[int(len(list1)/2)]))
    #If amount of items in list are odd, but the median same
    if len(list1) %2 == 1 and medlow == medhigh:
        return("The numbers of numbers are odd, however both the lower limit and the upper limit are the same, so the median is "+ list1[int(len(list1)/2)])
    else:
    #If amount of items in list are odd, but the median different
        return("The numbers of numbers are odd therefore there are 2 medians which are " + str(medlow) +" and " + str(medhigh)+ " respectively")
#This function find the most frequent item and outputs the result
def mode(list1):
    timeRep =0
    l=0
    maxTimeRep = 0
    maxTimeRepVar = ""
    #this goes trough the list and checks to see if there are multiple occurances of a particular i and outputs the most frequent i
    for i in list1:
            l=0
            timeRep = 0
            if l < len(list1):
                testVar = i
                while True:
                    if testVar == list1[l]:
                        timeRep = timeRep +1
                    l=l+1
                    if l > len(list1) -1:
                        #This updates the dictionary with the most recent frequency data
                        dict_mode.update({testVar:timeRep})
                        #This checks if the new var is greater than the pervious var
                        if timeRep > maxTimeRep:
                            maxTimeRepVar = testVar
                            maxTimeRep = timeRep   
                        break 
    return("The mode of this data set is " +str(maxTimeRepVar) + " It was repeated " + str(maxTimeRep) + " times")
#This function finds the frqencies of all items on the list and outputs the result
def FrqLst(list1):
    mode(list1)
    modeString = ""
    list_mode = []
    #This for loop is to turn the dictmode into a list
    for i in dict_mode:
        var = dict_mode[i]
        list_mode.append(i + "," + str(var))
    i=0
    #This for loop takes the list and turns it into a string with curly brackets separating each entry
    for s in list_mode:
        varString = list_mode[i]
        i=i+1
        modeString = modeString + " {" +varString + "}"
    return modeString