def index(text):
    input_list = text.split()
    
    def get_index(target):
        MBTI = ("INFP","ENFP","INFJ","ENFJ","INTJ","ENTJ","INTP","ENTP","ISFP","ESFP","ISTP","ESTP","ISFJ","ESFJ","ISTJ","ESTJ")
        return MBTI.index(target)
    
    def get_compat(x,y):
        compat_chart = (
            (3,3,3,4,3,4,3,3,0,0,0,0,0,0,0,0),
            (3,3,4,3,4,3,3,3,0,0,0,0,0,0,0,0),
            (3,4,3,3,3,3,3,4,0,0,0,0,0,0,0,0),
            (4,3,3,3,3,3,3,3,4,0,0,0,0,0,0,0),
            (3,4,3,3,3,3,3,4,2,2,2,2,1,1,1,1),
            (4,3,3,3,3,3,4,3,2,2,2,2,2,2,2,2),
            (3,3,3,3,3,4,3,3,2,2,2,2,1,1,1,4),
            (3,3,4,3,4,3,3,3,2,2,2,2,1,1,1,1),
            (0,0,0,4,2,2,2,2,1,1,1,1,2,4,2,4),
            (0,0,0,0,2,2,2,2,1,1,1,1,4,2,4,2),
            (0,0,0,0,2,2,2,2,1,1,1,1,2,4,2,4),
            (0,0,0,0,2,2,2,2,1,1,1,1,4,2,4,2),
            (0,0,0,0,1,2,1,1,2,4,2,4,3,3,3,3),
            (0,0,0,0,1,2,1,1,4,2,4,2,3,3,3,3),
            (0,0,0,0,1,2,1,1,2,4,2,4,3,3,3,3),
            (0,0,0,0,1,2,4,1,4,2,4,2,3,3,3,3)
            )
        return compat_chart[x][y]
    
    def get_meaning(index):
        compat_meaning = ("a Disaster","Not Bad","OK","Good","Perfect")
        return compat_meaning[index]
    
    return get_meaning (get_compat(get_index(input_list[0]),get_index(input_list[1])))
    
try:
    print("\nThe compatibility of these two is " + index(input("This program will check for the compatibility of two personalities.\nThe result could either be: Perfect, Good, OK, Not Bad and a Disaster.\nInput two MBTIs, separated by a space (e.g. \"INFP INFJ\").\n"))+ "!")
except:
    print("Invalid input, restart program.")