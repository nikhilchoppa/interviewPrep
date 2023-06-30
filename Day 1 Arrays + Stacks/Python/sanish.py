def req_func(n):
    x = 0
    arr = [1,2.5,5]
    req = []
    while(x < n):
        x = arr[0]
        if(x < n):
            req.append(x)
        x = arr[1]
        if(x < n):
            req.append(x)
        x = arr[2]
        if(x < n):
            req.append(x)
        for i in range(len(arr)):
            x = arr[i]*10
            req.append(x)
        print(req)
    return(req)
req_func(33)
