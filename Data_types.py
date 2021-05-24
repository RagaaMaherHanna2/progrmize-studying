"""
1- Python Numbers
    Integers, floating point numbers and complex numbers


2- Python List:
    ** Lists are mutable, meaning their elements can be changed unlike string or tuple.
    my_list = [1, 2, 3]
    # nested list
        my_list = ["mouse", [8, 4, 6], ['a']]\
    # Access List Elements:
        * various ways:
            1-List Index:
                print(my_list[0])
            2- Negative indexing:
                print(my_list[-1])
            3- slice lists:
                print(my_list[2:5])
            4- changing elements:
                * my_list.append(7) --> ome element
                * my_list.extend([9, 11, 13]) --> several elements
                * use (+) operator to combine two lists
                * use (*) operator repeats a list for the given number of times
                    print(["re"] * 3) --> ['re', 're', 're']
                * my_list.insert(1,3) --> insert 3 at position 1

                * Delete/Remove List Elements
                    - del my_list[2] = my_list.pop(1) --> del elem
                    - del my_list[1:5] --> del slice
                    - del my_list = my_list.clear() --> del list

        # elegant way to create lists
            1- pow2 = [2 ** x for x in range(10)]
            2- [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
                output --> ['Python Language', 'Python Programming', 'C Language', 'C Programming']




"""