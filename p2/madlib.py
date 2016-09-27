answer=[['cascading style sheet','bold','paragraph','<h1>'],['tokyo','dhiram','paris','rupee'],
        ['read only memory','random access memory','compact disk','internet protocol'],['assignment','two','instructions','binary language']]
string=["css stands for"+" "+"_1_."+"<b> is use to make the text"+" "+"_2_."+" "+"<p> tag is use for"+" "+"_3_."+" " + "The tag used for largest heading is"+" "+"_4_."+" ",
        "capital of japan is "+" "+"_1_."+"currency of dubai is"+" "+"_2_."+"capital of france is"+" "+"_3_."+"currency of india is"+" "+"_4_.",
        "ROM stands for"+" "+"_1_."+"RAM stands for"+" "+"_2_."+"CD stands for"+" "+"_3_."+"ip stands for"+" "+"_4_.",
        "equal to is an "+" "+"_1_"+" "+" operator.variables are of"+" "+" _2_ "+" "+"types."+"functions are known as set of"+" "+" _3_ ."+ "machine language is "+" "+"_4_ "+"language."]
''' answer and string list refer to the the value of answer and string'''
def level_select():
    ''' level_select() return the index and print the string at index that user selects'''
    level=['beginner','intermediate','expert','professional']
    var=raw_input("enter the level you want to play"+"\n"+"\n"+"beginner"+"\n"+"intermediate"+"\n"+"expert"+"\n"+"professional"+"\n")
    if(var==level[0] or var==level[1] or var==level[2] or var==level[3]):
        level_index=level.index(var)
        print string[level_index]
        input(level_index)
    else:
        print "your answer is wrong please enter the level again"
        level_select()
#behavior:print string which user selects else wrong enter again
#input:level_index saves the value of string at that index
#output:return no value        
        
        
    

def input(index):
    
    quiz_string=string[index]
    iteration=0 # iteration is intialize to zero to run the loop
    while(iteration<4):
        
        var=raw_input("enter the value of "+str(iteration+1)+" blank"+"\n").lower()
        if(var==answer[index][iteration]):
            print "your answer is correct!!!"
            quiz_string=quiz_string.replace("_"+str(iteration+1)+"_", answer[index][iteration])
            print quiz_string
            iteration=iteration+1
        else:
            print "answer is not correct"
#behavior:prompts for guess,compares to answer,print result            
#input:'index' integer representing the current level
#output:return no value            

level_select()
def again(play_again):
    '''if user wants to play again calls the function level_select() else print thanks statment'''
    if(play_again=="y"):
      level_select()
    else:
        print "thankyou for playing"
#behavior:check if user input is y then call function level_select()else print thanks statement
#input:play_again represent user choice
#output:return no value        
                        
def end():
    ''' ask user to play again '''
    choice=raw_input("your game is over you wana play enter y for yes and n for no"+"\n").lower()
    return choice
#behaviour:ask user to play again
#input:choice saves the value y or n
#return:choice

play_again=end()   
again(play_again)
        
        
    



    
    


            
            
            
    

