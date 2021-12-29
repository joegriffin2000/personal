homework = []
labs = []
readings = []
attendance = []
quizzes = []
midterm = 0
finalexam = 0

def calculate(hw,lbs,reads,attend,quiz,mid,final):
    if len(hw) > 0:
        Hfinal = sum(hw) / len(hw)
    if len(lbs) > 0:
        Lfinal = sum(lbs) / len(lbs)
    if len(reads) > 0:
        Rfinal = sum(reads) / len(reads)
    if len(attend) > 0:
        Afinal = sum(attend) / len(attend)
    if len(quiz) > 0:
        Qfinal = sum(quiz) / len(quiz)
    
    print('Homework Average:',Hfinal)
    print('Labs Average:',Lfinal)
    print('Readings Average:',Rfinal)
    print('Attendance Average:',Afinal)
    print('Quizzes Average:',Qfinal)
    
    totalGrade = (.2 * Hfinal) + (.2 * Lfinal) + (.1 * Rfinal) + (.05 * Afinal) + (.1 * Qfinal) + (.15 * mid) + (.2 + final)
    return totalGrade

print("Welcome to the CS Grade Calculator")
print("Enter Next to Continue")
user = ''
while user.lower() != 'next':
    user = input('Enter a Homework Grade: ')
    if user.lower() != 'next':
        pas = user
        try:
            pas = int(pas)
            pas < 100
            homework.append(pas)
        except:
            print(user,"is an invalid response")
        
user = ''       
while user.lower() != 'next':
    user = input('Enter a Labs Grade: ')
    if user.lower() != 'next':
        pas = user
        try:
            pas = int(pas)
            pas < 100
            labs.append(pas)
        except:
            print(user,"is an invalid response")
        
user = ''
while user.lower() != 'next':
    user = input('Enter a Readings Grade: ')
    if user.lower() != 'next':
        pas = user
        try:
            pas = int(pas)
            pas < 100
            readings.append(pas)
        except:
            print(user,"is an invalid response")
            
while user.lower() != 'next':
    user = input('Enter a Attendance Grade: ')
    if user.lower() != 'next':
        pas = user
        try:
            pas = int(pas)
            pas < 100
            attendance.append(pas)
        except:
            print(user,"is an invalid response")

while user.lower() != 'next':
    user = input('Enter a Quiz Grade: ')
    if user.lower() != 'next':
        pas = user
        try:
            pas = int(pas)
            pas < 100
            quizzes.append(pas)
        except:
            print(user,"is an invalid response")
        
midterm = input('Enter a Midterm Grade: ')
finalexam = input('Enter a Final Exam Grade: ')

print(calculate(homework,labs,readings,attendance,quizzes,midterm,finalexam))