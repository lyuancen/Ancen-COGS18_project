def check_input(input_text):
    """Check if the input is yes or no.
    
    Parameters
    ----------
    input : ideally string, or any other types
        Input which its type to be checked.
        
    Returns
    -------
    True : boolean 
        The result if the input is the correct "YES" or "NO" string.
        
    Raises
    ------
    ValueError
        If the upper case of the input is not string "YES" or "NO"
    """

    if input_text.upper() in ['YES','NO']:
        return True

    else:
        raise ValueError("Your answer must be 'YES' or 'NO'")   


class Points():
    
    # create a class object which has 4 instance arrtibutes composed
    # of user's input answering 4 screening questions.
    def __init__(self, msg_1, msg_2, msg_3, msg_4):

        self.msg_1 = msg_1
        self.msg_2 = msg_2
        self.msg_3 = msg_3
        self.msg_4 = msg_4

    def calculate(self):
        """Calculate the total points after giving values to users' input values of 4 questions.
        
        Parameters
        ----------
        input : class
            A class with 4 instance attributes which are users' input answering 4 questions.
            
        Returns
        -------
        count : int
            The points a user get based on their answers of 4 questions.
        """

        count = 0
        answer_list = [self.msg_1, self.msg_2, self.msg_3, self.msg_4]

        for answer in answer_list:
            if answer.upper() == 'YES':
                count += 1
            elif answer.upper() == 'NO':
                count += 0

        return count

    def final_screening(self):
        """To give the final screening result of a user depends on their total points.
        
        Parameters
        ----------
        input : class
            A class with 4 instance attriutes which are users' input answering 4 questions.
            
        Returns
        -------
        str
            A string that specifies the user's risk of having MDD.
        """

        if self.calculate() == 4:
            return 'Your risk of MDD is very high. Further inspection highly recommonded.'
        elif self.calculate() == 3:
            return 'Your risk of MDD is relatively high. Further inspection recommonded.'
        elif self.calculate() == 2:
            return 'Your risk of MDD is moderate. You could choose to take further inspection.'
        else:
            return 'Your risk of MDD is low. Further inspection is not necessary.'


def start_chat():
    """To create the chatbot and allow users to answer questions about potential MDD.
    
    Parameters
    ----------
    msg : str
        user's answer to whether they want to start this screening.
    msg_1 : str
        user's answer to the first screening question.
    msg_2 : str
        user's answer to the second screening question.
    msg_3 : str
        user's answer to the third screening question.
    msg_4 : str
        user's answer to the fourth screening question.
    
    Returns
    -------
    result.final_screening() : str
        User's risk of having MDD.
    """

    chat = True

    while chat:

        msg = input("Hi. I'm a chatbot used to screen your potential risk of MDD. \
                                                      Please answer my questions using YES no NO. \
                                                                        Do you want to start now?")

        if check_input(msg):

            if msg.upper() == 'YES':
                
                # the screening process while proceed only if user specifies
                # "YES" when asked about whether or not to start now.
                msg_1 = input('Do you ever spend hours doing nothing but daydreaming?')
                if check_input(msg_1):
                    msg_2 = input ('Does your daydreaming interfere with your studying or social?')
                    if check_input(msg_2):
                        msg_3 = input('Do you somehow believe the characters and events in your daydream are real?')
                        if check_input(msg_3):
                            msg_4 = input('Are your daydreams easily trigerred by music, movies, or other medias?')
                            if check_input(msg_4):
                                result = Points(msg_1, msg_2, msg_3, msg_4)
                                return result.final_screening()
                                break
            else:
                
                # break the screening process if users specifies
                # not to start now.
                break

        else:
            # stop the screening process if the input answering 
            # whether to start now is not "YES" or "NO".
            chat = False



        

