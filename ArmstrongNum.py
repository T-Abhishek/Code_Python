def isArmstrong(x):
    temp=x
    sum1=0

    while(temp!=0):
        digit=temp%10
        sum1+=digit**3
        temp//=10
    if x==sum1:
        print('its an armstrong no',sum1)
    else:
        print('its not an arsmtrong no',x)
isArmstrong(470)
