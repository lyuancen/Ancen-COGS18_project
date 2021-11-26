import pytest
from functions import check_input
from functions import Points
from functions import start_chat

def test_check_input():
    
    assert check_input('yes') is True
    
    assert check_input('No') is True
    
    with pytest.raises(ValueError): check_input('random') 
        
        
def test_Points():
    
    assert type(Points('yes', 'yes', 'no', 'no').calculate()) == int
    
    assert Points('yes', 'yes', 'no', 'no').calculate() == 2
    
    assert Points('yes', 'yes', 'yes', 'yes').final_screening() == 'Your risk of MDD is very high. Further inspection highly recommonded.'
    
    
def test_start_chat():

    assert callable(start_chat)

    with pytest.raises(ValueError): check_input('random')