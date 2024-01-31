def solution(citations):
    citations.sort(reverse=True) 
    
    left, right = 0, max(citations)
    
    while left <= right:
        mid = (left+right) // 2
        
        if mid <= sum([1 for c in citations if c >= mid]):
            left = mid + 1
        else:
            right = mid - 1
            
    return right