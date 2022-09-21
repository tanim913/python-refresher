class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(index, current_list, total):
            
            if total == target:
                res.append(current_list.copy())
                return 
            if index >= len(candidates) or total > target:
                return
            
            current_list.append(candidates[index])
            dfs(index, current_list, total + candidates[index])
            current_list.pop()
            dfs(index + 1, current_list, total)
        
        dfs(0, [], 0)
        
        return res
            