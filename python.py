# بايثون3 كود لحساب العمر
from datetime import date
 
def calculateAge(born):
    today = date.today()
    try:
        birthday = born.replace(year = today.year)
 
    except ValueError:
        birthday = born.replace(year = today.year,
                  month = born.month + 1, day = 1)
 
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year
         
# ادخال سنة الميلاد تبدأ من سنة ثم شهر الى يوم
print(calculateAge(date(2006, 2, 7)), "years")