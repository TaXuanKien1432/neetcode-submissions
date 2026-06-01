class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spe = list(zip(position, speed))
        pos_spe.sort()
        
        def time_to_target(pos_spe_tup):
            return (target - pos_spe_tup[0])/pos_spe_tup[1]
        
        st = [time_to_target(pos_spe[-1])]
        
        for i in range(len(pos_spe) - 2, -1, -1):
            cur_time = time_to_target(pos_spe[i])
            if cur_time > st[-1]:
                st.append(cur_time)
            
        return len(st)
