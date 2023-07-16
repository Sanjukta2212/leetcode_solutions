def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        one=1
        two=1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        print(one) #it shows 8 number of ways if we have 5 steps
        return one

if __name__=="__main__":
    n=5
    climbStairs(n)
            