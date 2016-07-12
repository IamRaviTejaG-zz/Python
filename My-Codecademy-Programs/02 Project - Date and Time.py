from datetime import datetime

now = datetime.now();

print ("Date & Time: %s/%s/%s %s:%s:%s" %(now.year, now.month, now.day, now.hour, now.minute, now.second));
x = raw_input("Press any key to exit.");
