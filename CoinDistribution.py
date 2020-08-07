number=int(input());
count=0
maxfiverequired=int((number//5))
if(maxfiverequired>=2):
    maxfiverequired=int((number//5) - 1)
remaining=int(number - int(maxfiverequired * 5))
if(number % 2 == 0 ):
    maxtworequired=int((remaining//2))
    remaining=int(remaining - int(maxtworequired * 2))
    maxonerequired=int(remaining//1)
    count=int(maxfiverequired + maxtworequired + maxonerequired)
else:
    maxtworequired=int((remaining//2)-1)
    remaining=int(remaining - int(maxtworequired * 2))
    maxonerequired=int(remaining//1)
    count=int(maxfiverequired + maxtworequired + maxonerequired)
print(count)
print(maxfiverequired)
print(maxtworequired)
print(maxonerequired)
