import re 
from flask import *
import random

# Read Txt File
sampleTxt = ""

with open('Az_900_Quest.txt','r',encoding='utf-8') as f:
    
    for line in f:
        
        sampleTxt += line




# Remove unnecessary rows of the text and split by question
NewTxt = ''
for z in (line for line in sampleTxt.splitlines() if "⬆ Back to Top" not in line and line != ''):
    NewTxt += z

NewList = [NewList.strip() for NewList in NewTxt.split('###') if NewList != '']




# Get Question, Option, and Answer of each Question and combine into list
QuestionDict = []

for item in NewList:
    
    Full = re.split(r'~|`',item.replace('- [ ] ','~').replace('- [x] ','`(Ans)').replace('- [-] ','`(Voted)').strip())

    Question = Full[0]
    Option = [Ans.replace('(Ans)','').replace('(Voted)','') for Ans in Full[1:]]
    Ans = [Ans.replace('(Ans)','') for Ans in Full[1:] if "(Ans)" in Ans ]
    Voted = [Ans.replace('(Voted)','') for Ans in Full[1:] if "(Voted)" in Ans ]


    FullQuestion = {
         "question":Question
        ,"options":Option
        ,"answer":Ans
        ,"Voted": Voted
        }
    
    QuestionDict.append(FullQuestion)

# rearrage the order of the question
#random.shuffle(QuestionDict)


print(len(QuestionDict))





app = Flask(__name__)



@app.route('/')
def quiz():
    
    return render_template('quiz.html', questions=QuestionDict)



@app.route('/submit', methods=['POST'])
def submit():

    score = 0
    total_Q = 0 

    Display_submited = ""
    Display_Corr = ""
    Display_Wrong = ""

    for question in QuestionDict:
        

        if ' , '.join(request.form.getlist(question['question'])) !='':

            total_Q += 1

            
            submited_Quest = ""
            submited_yourAns = ""
            submited_CorrAns = ""


            submited_Quest = question['question']
            submited_yourAns = ' , '.join(request.form.getlist(question['question']))           
            
            
            if request.form.getlist(question['question']) == question['answer']:
                
                score += 1


                DisplayStr = f"""
                <br>
                Question: <b>{submited_Quest}</b><br>
                Your Answer: <FONT COLOR="BLUE">{submited_yourAns} </FONT><br>
                -----------------------------------------------------------------------------
                <br>
                """


                Display_Corr += DisplayStr




            else:


                submited_CorrAns = ' , '.join(question['answer'])
                Most_Voted = ' , '.join(question['Voted'])


                if Most_Voted == '':

                    DisplayStr = f"""
                    <br>
                    Question: <b>{submited_Quest}</b><br> 
                    Your Answer: <FONT COLOR="RED">{submited_yourAns} </FONT><br>
                    Correct Answer: <FONT COLOR="BLUE">{submited_CorrAns} </FONT><br>
                    -----------------------------------------------------------------------------
                    <br>
                    """

                else:

                    DisplayStr = f"""
                    <br>
                    Question: <b>{submited_Quest}</b><br> 
                    Your Answer: <FONT COLOR="RED">{submited_yourAns} </FONT><br>
                    Correct Answer: <FONT COLOR="BLUE">{submited_CorrAns} </FONT><br>
                    Most Voted Answer: <FONT COLOR="Orange">{Most_Voted} </FONT><br>
                    -----------------------------------------------------------------------------
                    <br>
                    """



                Display_Wrong += DisplayStr
        
        
        
        
        Display_submited = Display_Wrong + Display_Corr

    
    
    return f" You scored {score} out of {total_Q}      <br><br> " + Display_submited



if __name__ == '__main__':
    app.run(debug=True)





