def hourglass(arr):
    # We are considering only inner matrix i.e, from arr[1][1] till arr[len(arr[0] - 1)][len(arr[0] - 1)]
    # That is we are neglecting the outer boundary of the array in this for loop.
    # The shape of hourglass is:
    """   
        a b c
          d
        e f g 
    """
    # val = arr[i][j] , we have to add all the surrounding values i.e., a,b,c,d,e,f and j..
    # Update the result value with val only if the current val is greater than previous result
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[0])-1):
            a = arr[i - 1][j - 1]
            b = arr[i - 1][j]
            c = arr[i - 1][j + 1]
            d = arr[i][j]
            e = arr[i + 1][j - 1]
            f = arr[i + 1][j]
            g = arr[i + 1][j + 1]
            
            val = a + b + c + d + e + f + g

            # Result value initialization. we can't initialize result value as 0 if zero is greater than minus values.
            # That's why we are initializing at 1st iteration i.e., candles[1][1]
            if (i == 1 and j == 1):
                # Iniatialze the result value with the output of 1st hourglass solution i.e., val
                # NOTE: All the hourglass solution will be compared with the previous result value.
                #       Imagine the scenario that all the hourglass solution were in negative values.
                #       If negative solution is compared with zero. The greater value is zero '0'. Everytime it returns 0 in this scenario. 
                #       To avoid this problem, we have to initialize the result value with the output of 1st hourglass solution. 
                result = val
            elif val > result:
                result = val

    return result
if __name__ == "__main__":
    # 2D arrray
    arr = []

    # It gets a sublist i.e., record(row) from the line of input and stores the sublist in arr
    for i in range(0, 6):
        val = list(map(int, input().split()))
        arr.append(val)

    # That's all print the result value
    print(hourglass(arr))
