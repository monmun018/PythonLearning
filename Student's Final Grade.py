#問題
# https://www.codewars.com/kata/5ad0d8356165e63c140014d4
def final_grade(exam, projects):
    print(exam,projects)
    if(exam > 90 or projects > 10 ): return 100
    if(exam > 75 and projects >= 5 ): return 90
    if(exam > 50 and projects >= 2 ): return 75
    return 0