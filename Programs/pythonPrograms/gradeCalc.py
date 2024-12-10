import functools

HW_GRADES = 0.6
FP_PROTOTYPE_GRADE = 0.1
FP_IMPLEMENTATION_GRADE = 0.15
FP_PRESENTATION_GRADE = 0.05
ATTENDANCE_GRADE = 0.1

def calcMobileProgramming(hw=None,attendance=None,fp_protoype=None,fp_implementation=None,fp_presentation=None):
    if isinstance(hw,list) and len(hw) in [5,6]:
        max = len(hw)
        hw = functools.reduce(lambda a, b: a+b, hw)
        hw /= max #averaging 

    total = (hw*HW_GRADES) + (fp_protoype*FP_PROTOTYPE_GRADE) + (fp_implementation*FP_IMPLEMENTATION_GRADE) + (fp_presentation*FP_PRESENTATION_GRADE) + (attendance*ATTENDANCE_GRADE)

    return total


if __name__ == "__main__":
    Homework = [100,100,100,70,100]
    Attendance = 100
    FP_Protoype = 100
    FP_Implementation = 80
    FP_Presentation = 80
    
    print(calcMobileProgramming(Homework,Attendance,FP_Protoype,FP_Implementation,FP_Presentation))