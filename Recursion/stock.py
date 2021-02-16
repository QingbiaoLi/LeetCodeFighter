# def selectStock(saving, currentValue, futureValue):
#     # Write your code here
#     num_dates = len(currentValue)
#     list_profit = []
#     for id_date in range(num_dates):
#         current_profit = futureValue[id_date] - currentValue[id_date]
#         if current_profit> 0:
#             list_profit.append((currentValue[id_date], current_profit))
#
#     list_positive_profit = sorted(list_profit, key=lambda x: x[0] - x[1])
#
#     profit = 0
#     for i, currentProfit in list_positive_profit:
#         if i < saving:
#             profit += currentProfit
#             saving -= i
#
#     return profit


def selectStock(saving, currentValue, futureValue):
    # Write your code here
    # Write your code here
    num_dates = len(currentValue)
    list_profict_date = []
    list_profit = []
    for id_date in range(num_dates):
        current_profit = futureValue[id_date] - currentValue[id_date]
        if current_profit > 0:
            list_profit.append((currentValue[id_date], current_profit))

    list_positive_profit = sorted(list_profit, key=lambda x: x[0] - x[1])
    num_positive_profitDates = len(list_positive_profit)
    profit = 0
    # for i, currentProfit in list_positive_profit:
    #     if i < saving:
    #         profit += currentProfit
    #         saving -= i

    return profit



def insertion_sort(array, left=0, right=None):

    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1

        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item
    return array


def timsort(array):

    min_run = 32
    n = len(array)

    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))



    size = min_run

    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1

            end = min((start + size * 2 - 1), (n-1))


            merged_array = merge(left=array[start:midpoint + 1],right=array[midpoint + 1:end + 1])


            array[start:start + len(merged_array)] = merged_array


        size *= 2


    return array

if __name__ == '__main__':

    saving = 250
    currentValue = [175, 133, 109, 210, 97]
    futureValue = [200, 125, 128, 228, 133]

    # saving = 30
    # currentValue = [1, 2, 4, 6]
    # futureValue = [5, 3, 5, 6]

    # saving = 500
    # currentValue = [150, 199, 200, 168, 153]
    # futureValue = [140, 175, 199, 121, 111]

    print(selectStock(saving,currentValue, futureValue))