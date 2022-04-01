def hourglass(arr):
    # Iniatialze the count i.e., result value as 0
    result = 0

    # We are considering only inner matrix for time efficiency i.e, from arr[1][1] till arr[len(arr[0] - 1)][len(arr[0] - 1)]
    # That is we are neglecting the outer boundary of the array in this for loop.
    # The shape of hourglass is:
    """   
        a b c
          d
        e f g 
    """
    # If arr[i][j] == 1, we have to check all the surrounding values i.e., a,b,c,e,f and j are == 1 or not..
    # If so increment the result value by 1
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[0])-1):
            if arr[i][j] == 1:
                a = arr[i - 1][j - 1]
                b = arr[i - 1][j]
                c = arr[i - 1][j + 1]
                e = arr[i + 1][j - 1]
                f = arr[i + 1][j]
                g = arr[i + 1][j + 1]

                if (a == 1) and (b == 1) and (c == 1) and (e == 1) and (f == 1) and (g == 1):
                    result += 1

    return result
if __name__ == "__main__":
    # Ask for n number of rows to store in the list arr
    n = int(input())

    # 2D arrray
    arr = []

    # It gets a sublist i.e., record(row) from the line of input and stores the sublist in arr
    for i in range(0, n):
        val = list(map(int, input().split()))
        arr.append(val)

    # That's all print the result value
    print(hourglass(arr))
