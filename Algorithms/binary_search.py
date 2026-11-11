arr = [-1, 4, 7, 8, 12, 17, 20, 25, 30]
target = 33
st = 0
end = len(arr) - 1

while st <= end:
    mid = (st + (end-st)) / 2 # To prevent overflow (st int-mx , end int-max)
    mid = int(mid)

    if target > arr[mid]:
        st = mid + 1

    elif target < arr[mid]:
        end = mid - 1

    else:
        print("Target found ", arr[mid])
        print("Index of the number is : ", mid)
        break
else:
    print("Number is not in the array.")
