def count_chars(str):
    upper_ctr,lower_ctr,number_ctr,
    for i in range(len(str)):
        if str[i]>=A and str[i]<=Z:upper_ctr+=1
        elif str[i]>=a and str[i]<=z:lower_ctr+=1
        elif str[i]>=0 and str[i]<=9:number_ctr+=1
        return upper_ctr,lower_ctr,number_ctr
    str ="saveetha195"
    u,l,n,=count_chars(str)
    print ("upper case :",u)
    print("lower case:",l)
    print("number case:",n)
