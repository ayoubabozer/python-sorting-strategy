from bubble_sort import BubbleSort
from selection_sort import SelectionSort
from sort_strategy import SortStrategy



if __name__ == '__main__':

    # the list to sort
    my_list = [1,2,3,4,5,6,7]

    # bubbke sort algo
    b = BubbleSort()

    # Selection sort algo
    s = SelectionSort()

    # choosing the strategy - bubble sort
    print("Bubble sort :")
    strategy = SortStrategy(b)

    sorted_list = strategy.sort(my_list)

    print("result ", sorted_list)

    # changing the strategy to Selection sort
    print("Selection sort :")
    strategy.algo = s

    sorted_list = strategy.sort(my_list)

    print("result ", sorted_list)
