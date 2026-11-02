class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()
        for token in tokens:
            if token == "+":
                st.append(st.pop()+st.pop())
            elif token == "-":
                s=st.pop()
                st.append(st.pop()-s)
            elif token == "*":
                st.append(st.pop()*st.pop())
            elif token == "/":
                div=st.pop()
                num=st.pop()
                if(num//div)<0 and num//div!=num/div:
                    st.append(num//div+1)
                else:
                    st.append(num//div)
            else:
                st.append(int(token))
        return st.pop()