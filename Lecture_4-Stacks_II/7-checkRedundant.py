def checkRedundant(expr):
    st=[]
    for k,v in enumerate(expr):
        if v == ')':
            flag=False
            while st and st[-1] !='(':
                c = st.pop()
                if c in ['+','-','*','/']:
                    flag=True
            if not flag:
                return "There are redundant brackets"
            st.pop()
        st.append(v)
    return "There are no redundant brackets"

print(checkRedundant(list("(a+b*(c-d))")))