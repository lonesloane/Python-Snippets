the_grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades):
    for grade in grades:
        print(grade)


def grades_sum(grades):
    _sum = 0
    for grade in grades:
        _sum += grade
    return _sum


def grades_average(grades):
    _sum = grades_sum(grades)
    average = float(_sum)/len(grades)
    return average


def grades_variance(grades, average):
    variance = 0
    for grade in grades:
        variance += (average-grade)**2
    return variance/len(grades)


def grades_std_deviation(variance):
    return variance**(1/2)

print_grades(the_grades)
gradesSum = grades_sum(the_grades)
print(gradesSum)
gradesAverage = grades_average(the_grades)
print(gradesAverage)
gradesVariance = grades_variance(the_grades, grades_average(the_grades))
print(gradesVariance)
print(grades_std_deviation(gradesVariance))
