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


3- Python tuple:
    ** the difference between the two is that we cannot change the elements of a tuple once it is assigned
    whereas we can change the elements of a list.
    ** 'tuple' object does not support item assignment
    ** Both + and * operations result in a new tuple

    Tuple Methods
        my_tuple.count('p')
        my_tuple.index('l')

NOTE:
    Advantages of Tuple over List Since tuples are quite similar to lists, both of them are used in similar
situations. However, there are certain advantages of implementing a tuple over a list. Below listed are some of the
main advantages:

We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.
Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.


4- Strings:
    ** The + operator does this in Python. Simply writing two string literals together also concatenates them.
    ** The * operator can be used to repeat the string for a given number of times.
    ** string using a for loop.
    ** my_string[5] = 'a'
    ** 'str' object does not support item assignment

    str = 'cold'
    # enumerate()
    list_enumerate = list(enumerate(str)) --> list(enumerate(str) =  [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]


    ** Python String Formatting:
        * Escape Sequence: "https://www.w3schools.com/python/gloss_python_escape_characters.asp"
        # using triple quotes
        print('''He said, "What's there?"''')

        # escaping single quotes
        print('He said, "What\'s there?"')

        # escaping double quotes
        print("He said, \"What's there?\"")

        *The format() Method for Formatting Strings:
            1- Default Order
            2- Positional Order
            3- Keyword Order
            4- mixed arguments

        * There are numerous methods available with the string object. The format() method that we
        mentioned above is one of them. Some of the commonly used methods are lower(), upper(), join(), split(),
        find(), replace() etc. Here is a complete list of all the







"""
