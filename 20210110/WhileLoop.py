# count = 0

# while (count < 9) :
#     print ("The Count is: " , count)
#     count = count + 1   #count += 1


status = 1

while (status != 0) :
    print ("Option 01: Check Balance - Enter 1")
    print ("Option 02: Internet - Enter 2")
    print ("Option 03: MMS - Enter 3")
    print ("Option 04: Ringing Tone - Enter 4")
    print ("Option 05: News Alert - Enter 5")
    print ("Option 00: Exit - Enter 0")

    status = int(input("Enter Option Number: "))

    if (status == 1) :
        print ("Your balance is Rs. 1500.00/=")
    elif (status == 2) :
        print ("Your Internet Connection is active")
    elif (status == 3) :
        print ("Your MMS Connection is active")
    elif (status == 4) :
        print ("Your Ringing Tone is active")
    elif (status == 5) :
        print ("Your News Alerts is active")
    elif (status == 0) :
        print ("Thank You for contacting us")
    else :
        print ("Wrong Input")
        
