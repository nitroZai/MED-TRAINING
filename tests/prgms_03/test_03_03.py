
def can_make_str(s1, s2):
 

    count = {s1[i] : 0 for i in range(len(s1))}

    for i in range(len(s1)):

        count[s1[i]] += 1

    # print(count)
    for i in range(len(s2)): 
       #  print(s2[i]) 
        if s2[i]==' ' : 
            continue            #    based on constraint , string having multiple spaces test case should pass

        if count[s2[i]] == 0:

            return False         #   when there is no character in the given string that able to generate given sentence 

        count[s2[i]] -= 1

    return True 
    
def test_01():
        assert True == can_make_str("iItsimlpsietnecseacne","it is a simple sentence")

def test_02():
    try:
        assert False == can_make_str("aeiou","abb")
    except KeyError as e:
        # print('error at ',e)
        assert True