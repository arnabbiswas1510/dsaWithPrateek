"""
Validate Parenthesis
Given a sequence of brackets, validate if the sequence is valid
"""

def validateParenthesis(expr):
    st=[]
    for ch in expr:
        if ch in ['(',')','{','}','(',')']:
            if ch in ['(','{','(']:
                st.append(ch)
            else:
                stCh=st.pop()
                if stCh == '(' and not ch==')':
                    return False
                elif stCh == '[' and not ch==']':
                    return False
                elif stCh == '{' and not ch=='}':
                    return False
        else:
            continue
    if st:
        return False #Dont forget this!!
    return True

print(validateParenthesis("{54+(54+29)*[35]}"))