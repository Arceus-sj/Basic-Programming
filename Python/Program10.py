year = int(input())

def leap_year(year):
    if year%4==0 and year%100!=0 :
        return True
    elif year%400==0:
        return True
    else :
        return False
    
print(leap_year(year))
