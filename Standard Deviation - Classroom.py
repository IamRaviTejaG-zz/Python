grades = [];
ind = raw_input("Enter the number of students in the class: ");
print ("\n");
strength = int(ind);
for i in range (0, strength):
	inp = raw_input("Enter score of student " + str(i+1) + ": ");
	z = int(inp);
	grades.append(z);

def print_grades(grades):
    for grade in grades:
        print grade;

def grades_sum(grades):
    total = 0;
    for grade in grades: 
        total += grade;
    return total;
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades);
    average = sum_of_grades / float(len(grades));
    return average;

def grades_variance(scores):
    average = grades_average(scores);
    variance = 0;
    for score in scores:
        variance+=(average-score)**2;
    c = variance/float(len(scores));
    return c;

def grades_std_deviation(variance):
    return variance ** 0.5;

print ("\n");
print_grades(grades);
print ("\nSum of Scores: "), grades_sum(grades);
print ("\nAverage Score: "), grades_average(grades);
print ("\nVariance: "), grades_variance(grades);
print ("\nStandard Deviation: "), grades_std_deviation(grades_variance(grades));
print ("\n\nPress any key to exit.");
x = raw_input("");
