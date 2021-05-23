def trim(expr, st):
    for k,v in enumerate(expr):
        if k in st:
            expr.pop(k)
    return ''.join(expr)

def removeParenthesis(expr):
    st=[]
    for k,v in enumerate(expr):
        if v == '(':
            st.append(k)
        elif v == ')':
            if st and expr[st[-1]]=='(':
                st.pop()
            else:
                st.append(k)
    return trim(expr,st)

print(removeParenthesis(list("(a(b(c)d)")))