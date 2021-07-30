# Python3 program to print
# given matrix in spiral form
def spiralPrint(m, n, a) :
    k = 0; l = 0
    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator '''

    while (k < m and l < n) :
        print("\nBEFORE : m,n,k,l",m,n,k,l)
        print("\nPrint the first row from\n")
        # the remaining rows
        for i in range(l, n) :
            print(a[k][i], end = " ")

        k += 1


        print("\nPrint the last column from\n")
        # the remaining columns
        for i in range(k, m) :
            print(a[i][n - 1], end = " ")

        n -= 1

        print("\nPrint the last row from\n")
        # the remaining rows
        if ( k < m) :
            #print("This is l,m",l,m)
            for i in range(n - 1, (l - 1), -1) :
                print(a[m - 1][i], end = " ")

            m -= 1


        print("\nPrint the first column from\n")
        # the remaining columns
        if (l < n) :
            for i in range(m - 1, k - 1, -1) :
                print(a[i][l], end = " ")

            l += 1
        print("\nAFTER : m,n,k,l",m,n,k,l)
# Driver Code
a = [ [1, 2, 3, 4, 5, 6],
      [7, 8, 9, 10, 11, 12],
      [13, 14, 15, 16, 17, 18],
      [19, 20, 21, 22, 23, 24],
      [25, 26, 27, 28, 29, 30]]

R = 5; C = 6
print(a)
spiralPrint(R, C, a)

# This code is contributed by Nikita Tiwari.
