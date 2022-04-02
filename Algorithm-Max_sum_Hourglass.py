def hourglass(arr):
    # Iniatialze the result value as 0
    result = 0

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
            if (i == 1 and j == 1):
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
