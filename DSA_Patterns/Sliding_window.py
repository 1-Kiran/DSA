# solve edge case and read question properly and understand the data first and loops

# 1. Maximum sum of K consecutive elements
# def sliding_window(arr,k):
#     window=sum(arr[:k])
#     maximum=window
#     for i in range(0,len(arr)-k):
#         window=window-arr[i]+arr[k+i]
#         if maximum<window:
#             maximum=window
#     return maximum
# arr=[2,1,5,1,3,2]
# k = 3
# print(sliding_window(arr,k))