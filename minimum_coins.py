coins = list(map(int,input("Enter the coins : ").strip().split()))
denom = int(input('Enter the denomination : '))
min_coin = min(coins)
INF = 1000000

def DP(dp,denom,coin_dict):
    
    if denom==0:
        dp[denom] = 1
        return dp[denom]
    
    if denom<min_coin:
        dp[denom] = INF
        return dp[denom]

    if dp[denom]!=-1:
        return dp[denom]

    min_val = INF
    coin = -1
    for i in coins:
        x = DP(dp,denom-i,coin_dict)+1
        if x < min_val:
            min_val = x
            coin = i
    
    dp[denom] = min_val
    coin_dict[denom] = coin 
    return dp[denom]

def print_coins(coin_dict,denomination):
    c = []
    denom = denomination
    while denom!=0:
        c.append(str(coin_dict[denom]))
        denom = denom - coin_dict[denom]
    return ' ,'.join(c)

dp = [-1]*(denom+1)
coin_dict = {}
val = DP(dp,denom,coin_dict)

if(val==INF):
    print("Not possible")
else:
    print(print_coins(coin_dict,denom))