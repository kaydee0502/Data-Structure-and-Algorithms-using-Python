#
# @lc app=leetcode id=1648 lang=python3
#
# [1648] Sell Diminishing-Valued Colored Balls
#

# @lc code=start
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse= True)
        MOD = 10**9+7
        nin = inventory[-1]
        cst =0 
        i = 0
        isSame = True
        while orders:
            #print(inventory,orders,isSame)
            if i == len(inventory)-1:
                if isSame:
                    break
                i = 0
                isSame = True
                
            if inventory[i] != inventory[i+1]:
                isSame = False
            
            if inventory[i] - inventory[i+1] <= orders:
                m = inventory[i]
                n = inventory[i+1]
                
                cst += (m*(m+1))//2 - (n*(n+1))//2 
                
                
                orders -= inventory[i] - inventory[i+1]
                inventory[i] = inventory[i+1]
                
                
                
            else:
                m = inventory[i]
                n = inventory[i]-orders
                
                t = (m*(m+1))//2 - (n*(n+1))//2 
                cst += t
                return cst%MOD
            
            i+=1
            
        ele = inventory[0]
        while orders:
            if orders < len(inventory):
                cst += ele * orders
                return cst%MOD
            else:
                cst+= ele * len(inventory)
                orders -= len(inventory)
            ele -= 1
            
        return cst%MOD
            
        
                
        
            
            
                
                
            
            
            
        
        
# @lc code=end

