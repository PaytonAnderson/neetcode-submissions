class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            if len(st) == 0:
                st.append(a)
            elif a < 0:
                while st and st[-1] > 0 and st[-1] < -1 * a:
                    st.pop()
                if st and st[-1] == a * -1:
                    st.pop() 
                elif not st or st[-1] < 0:
                    st.append(a)
            else:
                st.append(a)
        return st