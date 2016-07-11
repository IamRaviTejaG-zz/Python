datas = [];
ind = raw_input("Enter the number data to be evaluated: ");
print ("\n");
strength = int(ind);
for i in range (0, strength):
	inp = raw_input("Enter data " + str(i+1) + ": ");
	z = int(inp);
	datas.append(z);

def print_data(datas):
    for data in datas:
        print data;

def data_sum(datas):
    total = 0;
    for data in datas: 
        total += data;
    return total;
    
def data_average(data):
    sum_of_data = data_sum(datas);
    average = sum_of_data / float(len(datas));
    return average;

def data_variance(scores):
    average = data_average(scores);
    variance = 0;
    for score in scores:
        variance+=(average-score)**2;
    c = variance/float(len(scores));
    return c;

def data_std_deviation(variance):
    return variance ** 0.5;

print ("\n");
print ("\nSum of Data: "), data_sum(datas);
print ("\nAverage Score: "), data_average(datas);
print ("\nVariance: "), data_variance(datas);
print ("\nStandard Deviation: "), data_std_deviation(data_variance(datas));
x = raw_input("\n\nPress any key to exit.");
