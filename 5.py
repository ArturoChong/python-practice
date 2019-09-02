import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def determine_bigger_list(list1, list2):
    lists = {
        'bigger_list': [],
        'smaller_list': [],
    }

    if len(list1) > len(list2):
        lists['bigger_list'] = list1
        lists['smaller_list'] = list2
    else:
        lists['bigger_list'] = list2
        lists['smaller_list'] = list1

    return lists 

def obtain_common_items(lists):
    common_items = []

    for item in lists['bigger_list']:
        if item in lists['smaller_list']:
            common_items.append(item)

    return common_items

def generate_list(length):
    generated_list = []

    for i in range(length):
        generated_list.append(random.randint(0, 9999))

    return generated_list

a = generate_list(10)
b = generate_list(12)

lists = determine_bigger_list(a, b)
common_items = obtain_common_items(lists)

print('Bigger list: {}'.format(lists['bigger_list']))
print('Small list {}'.format(lists['smaller_list']))

print('Common items: {}'.format(common_items))
