from collections import OrderedDict
ordered_dict = OrderedDict([
    ('b', 2),
    ('c', 3),
    ('d', 4)
])
new_data=OrderedDict([('a',1)])
new_data.update(ordered_dict)
print(new_data)


def check_order(string, reference):
    string_dict = OrderedDict.fromkeys(string)
    reference_dict = OrderedDict.fromkeys(reference)

    return string_dict == reference_dict

input_string = "hello world"
reference_string = "helo wrd"

if check_order(input_string, reference_string):
    print("The order of characters in the input string matches the reference string.")
else:
    print("The order of characters in the input string does not match the reference string.")