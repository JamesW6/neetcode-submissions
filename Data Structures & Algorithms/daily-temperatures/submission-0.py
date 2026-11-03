class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=deque()
        ret=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while len(st)>0 and st[-1][0]<temperatures[i]:
                val=st.pop()
                ret[val[1]]=i-val[1]
            st.append((temperatures[i],i))
        return ret
