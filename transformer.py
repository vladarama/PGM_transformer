def is_valid_image(PGM_list):
    ''' (list) -> bool
    Returns True if the PGM_list representes a valid non-compressed PGM image matrix
    and False if it does not.

    >>> is_valid_image([["0x5", "200x2"], ["111x7"]])
    False

    >>> is_valid_image([[53,61,70], [3,1,3], [52,52,52]])
    True

    >>> is_valid_image([[257,61,70], [0,1,3], [32,52,52]])
    False
    '''
    len_list = []

    for sublist in PGM_list:

        if len(sublist) not in len_list:
            len_list.append(len(sublist))

        for element in sublist:
            if type(element) != int or element < 0 or element > 255:
                return False

    return len(len_list) == 1


def is_valid_compressed_image(PGM_list):
    ''' (list) -> bool
    Returns True if the PGM_list representes a valid compressed PGM image matrix
    and False if it does not.

    >>> is_valid_compressed_image([["0x5", "200x2"], ["111x7"]])
    True

    >>> is_valid_compressed_image([["1x3", "190x5"], ["107x7"]])
    False

    >>> is_valid_compressed_image([[257,61,70], [0,1,3], [32,52,52]])
    False
    '''

    sum_b_list = []

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for sublist in PGM_list:
        count = 0

        for element in sublist:
            if 'x' not in str(element):
                return False

            splitted_list = str(element).split('x')

            for subelement in splitted_list:
                for char in subelement:
                    if char not in numbers:
                        return False

            A = int(splitted_list[0])
            B = int(splitted_list[1])

            if A < 0 or A > 255 or B < 0:
                return False

            count += B

        if count not in sum_b_list:
            sum_b_list.append(count)

    return len(sum_b_list) == 1


def load_regular_image(file_name):
    ''' (str) -> list<list<int>>
    Returns an image matrix, from the PGM image that was loaded from file_name.
    An AssertionError is raised if the image matrix is not in a proper PGM format.

    >>> load_regular_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    >>> fobj = open("test_two.pgm", "w")
    >>> fobj.write("P2\n5 2\n255\n1 1 1 1 1\n2 2 2 2 2")
    30
    >>> fobj.close()
    >>> load_image("test_two.pgm")
    [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2]]


    >>> fobj = open("invalid_test_two.pgm", "w")
    >>> fobj.write("P2\n5 2\n255\n0 0 0 0 0\n2 2 2 2 2 2")
    36
    >>> fobj.close()
    >>> load_image("invalid_test_two.pgm")
    Traceback (most recent call last):
    AssertionError: The matrix is not a valid PGM image matrix
    '''
    matrix = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    count = 0
    fobj = open(file_name, 'r')

    for line in fobj:
        count += 1
        line = line.strip()

        if count > 3:  # Skipping the information about the image
            sublist = line.split()

            for i in range(0, len(sublist)):
                for element in sublist[i]:
                    if element not in numbers:
                        raise AssertionError(
                            "The matrix is not a valid PGM image matrix")

                sublist[i] = int(sublist[i])

            matrix.append(sublist)

    if not is_valid_image(matrix):
        raise AssertionError("The matrix is not a valid PGM image matrix")

    fobj.close()

    return matrix


def load_compressed_image(file_name):
    ''' (str) => list<list<str>>
    Returns an image matrix, from the compressed PGM image that was loaded from file_name. ]
    An AssertionError is raised when the image matrix is not in a proper PGM compressed format.

    >>> load_compressed_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]

    >>> fobj = open("invalid_test_compressed.pgm", "w")
    >>> fobj.write("P2C\n30 5\n255\n5x25 1x1x3\n")
    28
    >>> fobj.close()
    >>> load_compressed_image("invalid_test_compressed.pgm")
    Traceback (most recent call last):
    AssertionError: The image matrix is not in a proper PGM format

    >>> fobj = open("invalid_test_compressed_two.pgm", "w")
    >>> fobj.write("P2C\n30 5\n255\nasdas5x25 1x1x3\n")
    33
    >>> fobj.close()
    >>> load_compressed_image("invalid_test_compressed_two.pgm")
    Traceback (most recent call last):
    AssertionError: The image matrix is not in a proper PGM format
    '''

    img_matrix = []
    count = 0

    fobj = open(file_name, 'r')

    for line in fobj:
        count += 1
        line = str(line).strip()

        if count > 3:
            sublist = line.split()
            img_matrix.append(sublist)

    if not is_valid_compressed_image(img_matrix):
        raise AssertionError("The image matrix is not in a proper PGM format")

    fobj.close()

    return img_matrix


def load_image(file_name):
    ''' (str) -> list<list<str>>
    Returns either an image matrix if the file_name contains a regular PGM image,
    or it returns a compressed image matrix if the file_name contains a compressed PGM image.

    >>> load_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]

    >>> load_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    >>> fobj = open("invalid_test_compressed_two.pgm", "w")
    >>> fobj.write("P2C\n30 5\n255\nasdas5x25 1x1x3\n")
    33
    >>> fobj.close()
    >>> load_image("invalid_test_compressed_two.pgm")
    Traceback (most recent call last):
    AssertionError: The image matrix is not in a proper PGM format
    '''

    fobj = open(file_name, 'r')
    content = fobj.read()
    loading = 0

    if content[0:3] == 'P2C':
        loading = load_compressed_image(file_name)

    else:
        if content[0:2] == 'P2':
            loading = load_regular_image(file_name)
        else:
            raise AssertionError("The file is not in a PGM format")

    return loading


def save_regular_image(nested_list, file_name):
    ''' (list<list>, str) -> ()
    Saves the nested_list in the PGM format into a file called file_name.
    An Assertion Error is raised when the nested_list is not a valid PGM image matrix.

    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\n10 3\n255\n0 0 0 0 0 0 0 0 0 0\n255 255 255 255 255 255 255 255 255 255\n0 0 0
0 0 0 0 0 0 0\n'
    >>> fobj.close()

    >>> save_regular_image([[3]*5, [255]*3, [0]*2], "test_three.pgm")
    Traceback (most recent call last):
    AssertionError: The nested list is an invalid image matrix

    >>> save_regular_image([[3]*5, [255]*5, [0]*5], "test_four.pgm")
    >>> fobj = open("test_four.pgm", 'r')
    >>> fobj.read()
    'P2\n5 3\n255\n3 3 3 3 3\n255 255 255 255 255\n0 0 0 0 0\n'
    >>> fobj.close() 
    '''

    if not is_valid_image(nested_list):
        raise AssertionError("The nested list is an invalid image matrix")

    fobj = open(file_name, 'w')
    fobj.write('P2\n')
    fobj.write(str(len(nested_list[0])) + ' ' + str(len(nested_list)) + '\n')
    fobj.write('255' + '\n')

    for i in range(0, len(nested_list)):
        for j in range(0, len(nested_list[i])):
            fobj.write(str(nested_list[i][j]))

            if j != len(nested_list[i])-1:
                fobj.write(' ')

        fobj.write('\n')

    fobj.close()


def save_compressed_image(nested_list, file_name):
    ''' (list<list>, str) -> ()
    Saves the nested_list in the compressed PGM format into a file called file_name.
    An Assertion Error is raised when the nested_list is not a valid compressed PGM image matrix.

    >>> save_compressed_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\n7 2\n255\n0x5 200x2\n111x7\n'
    >>> fobj.close()

    >>> save_compressed_image([["1x3", "21x2"], ["32x8"]], "test_2.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: The nested list is an invalid compressed image matrix

    >>> save_compressed_image([[0]*10, [255]*10, [0]*10], "test_3.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: The nested list is an invalid compressed image matrix
    '''

    if not is_valid_compressed_image(nested_list):
        raise AssertionError(
            "The nested list is an invalid compressed image matrix")

    fobj = open(file_name, 'w')
    fobj.write('P2C\n')
    count = 0

    for element in nested_list[0]:
        count += int(element.split('x')[1])

    fobj.write(str(count) + ' ' + str(len(nested_list)) + '\n')
    fobj.write('255' + '\n')

    for i in range(0, len(nested_list)):
        for j in range(0, len(nested_list[i])):
            fobj.write(str(nested_list[i][j]))

            if j != len(nested_list[i])-1:
                fobj.write(' ')

        fobj.write('\n')

    fobj.close()


def save_image(nested_list, file_name):
    ''' (list<list>, str) -> ()
    Saves the nested_list in standard or compressed PGM format depending on the type of the nested_list.
    If the nested_list is made up of integers, the image matrix will be saved into a PGM file with file_name.
    If the nested_list is made up of strings, the image matrix will be saved into a compressed PGM file with file_name.
    An Assertion Error is raised when the nested_list is not a valid PGM image matrix.

    >>> save_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\n7 2\n255\n0x5 200x2\n111x7\n'
    >>> fobj.close()

    >>> save_image([[3]*5, [255]*3, [0]*2], "test_three.pgm")
    Traceback (most recent call last):
    AssertionError: The nested list is an invalid image matrix

    >>> save_image([[3]*5, [255]*5, [0]*5], "test_four.pgm")
    >>> fobj = open("test_four.pgm", 'r')
    >>> fobj.read()
    'P2\n5 3\n255\n3 3 3 3 3\n255 255 255 255 255\n0 0 0 0 0\n'
    >>> fobj.close()
    '''

    type_list = []

    for sublist in nested_list:
        for element in sublist:
            if str(type(element)) not in type_list:
                type_list.append(str(type(element)))

    if type_list == ["<class 'str'>"]:
        save_compressed_image(nested_list, file_name)

    elif type_list == ["<class 'int'>"]:
        save_regular_image(nested_list, file_name)

    else:
        raise AssertionError("The nested list is not of appropriate type")


def invert(PGM_list):
    ''' (list<list<int>>) -> list<list<int>>
    Returns the inverted image of a PGM_list without modifying the input matrix.
    If the PGM_list is not a valid image matrix, an AssertionError is raised.

    >>> image = [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    >>> invert(image)
    [[255, 155, 105], [55, 55, 55], [0, 0, 0]]
    >>> image == [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    True

    >>> image = [[50, 50, 20], [100, 50, 200], [55, 55, 55]]
    >>> invert(image)
    [[205, 205, 235], [155, 205, 55], [200, 200, 200]]
    >>> image == [[50, 50, 20], [100, 50, 200], [55, 55, 55]]
    True

    >>> image = [[0, 0], [1, 1, 1], [255, 255, 255]]
    >>> invert(image)
    Traceback (most recent call last):
    AssertionError: The input list is not a valid PGM image matrix
    '''
    if not is_valid_image(PGM_list):
        raise AssertionError("The input list is not a valid PGM image matrix ")

    img_matrix = []

    for sublist in PGM_list:
        sub_matrix = []

        for element in sublist:
            new_element = 255 - element
            sub_matrix.append(new_element)

        img_matrix.append(sub_matrix)

    return img_matrix


def flip_horizontal(PGM_list):
    ''' (list<list<int>>) -> list<list<int>>
    Returns the image matrix of the PGM_list flipped horizontally without modifying the input matrix.
    An AssertionError is raised if the PGM_list does not represent a valid PGM image matrix.

    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]

    >>> image = [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]

    >>> image = [[5, 5, 3, 3], [1, 1, 1, 9, 9], [1, 2, 3, 4, 4]]
    >>> flip_horizontal(image)
    Traceback (most recent call last):
    AssertionError: The input list is not a valid PGM image matrix
    '''

    if not is_valid_image(PGM_list):
        raise AssertionError("The input list is not a valid PGM image matrix ")

    img_matrix = []
    sub_matrix = []

    for sublist in PGM_list:
        sub_matrix = sublist[::-1]
        img_matrix.append(sub_matrix)

    return img_matrix


def flip_vertical(PGM_list):
    ''' (list<list<int>>) -> list<list<int>>
    Returns the image matrix of the PGM_list flipped vertically without modifying the input matrix.
    An AssertionError is raised if the PGM_list does not represent a valid PGM image matrix.

    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 3, 4, 5]]

    >>> image = [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [10, 10, 5, 0, 0], [5, 4, 3, 2, 1]]

    >>> image = [[5, 5, 3, 3], [1, 1, 9, 9], [1, 2, 3, 4, 4]]
    >>> flip_vertical(image)
    Traceback (most recent call last):
    AssertionError: The input list is not a valid PGM image matrix
    '''

    if not is_valid_image(PGM_list):
        raise AssertionError("The input list is not a valid PGM image matrix ")

    img_matrix = PGM_list[::-1]
    new_img_matrix = []

    for sublist in img_matrix:
        new_img_matrix.append(sublist)

    return new_img_matrix


def crop(PGM_list, top_left_row, top_left_column, n_rows, n_columns):
    ''' (list<list<int>>, int, int, int, int) -> list<list<int>>
    Returns a cropped image matrix of the PGM_list with the shape of a rectangle.
    The rectangle is created with n_rows and n_columns, where the top_left_row and the top_left_column
    represent certain values.

    >>> crop([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]], 1, 2, 2, 1)
    [[6], [10]]

    >>> crop([[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]], 1, 2, 2, 1)
    [[5], [5]]

    >>> crop([[5, 5, 3, 3], [1, 1, 9, 9], [1, 2, 3, 4, 4]]]
    Traceback (most recent call last):
    AssertionError: The input list is not a valid PGM image matrix

    '''

    if not is_valid_image(PGM_list):
        raise AssertionError("The input list is not a valid PGM image matrix ")

    img_matrix = []

    for i in range(top_left_row, top_left_row + n_rows):
        sub_img_matrix = []

        for j in range(top_left_column, top_left_column + n_columns):
            sub_img_matrix.append(PGM_list[i][j])

        img_matrix.append(sub_img_matrix)

    return img_matrix


def find_end_of_repetition(int_list, index, target_num):
    ''' (list<list<int>>, int, int) -> int
    Returns the index of the last consecutive occurent of target_num form an int_list.
    Starts looking in the list starting from index.

    >>> find_end_of_repetition([5, 3, 5, 5, 5, -1, 0], 2, 5)
    4

    >>> find_end_of_repetition([1, 2, 3, 4, 3, 6, 7], 6, 7)
    2

    >>> find_end_of_repetition([3, 3, 3, 3, 2, 5, 7], 0, 3)
    3
    '''
    previous_index = 0
    for i in range(index, len(int_list)):
        if i == len(int_list)-1:
            if int_list[i] == target_num:
                return i

        if int_list[i] == target_num:
            if int_list[i+1] != target_num:
                return i


def compress(PGM_list):
    ''' (list<list<int>>) -> list<list<str>>
    Returns the compressed image matrix of a PGM_list.
    If the PGM_list is not a valid PGM image matrix, an AssertionError is raised.

    >>> compress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    [['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]

    >>> compress([[1, 2, 3, 3, 3], [0, 2, 1, 2, 2], [0, 0, 255, 1, 255]])
    [['1x1', '2x1', '3x3'], ['0x1', '2x1', '1x1', '2x2'], ['0x2', '255x1', '1x1', '255x1']]

    >>> compress([[11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    Traceback (most recent call last):
    AssertionError: The input list is not a valid PGM image matrix
    '''

    if not is_valid_image(PGM_list):
        raise AssertionError("The input list is not a valid PGM image matrix ")

    img_matrix = []

    for sublist in PGM_list:
        sub_img_matrix = []
        previous_index = 0
        index = 0

        while previous_index != len(sublist):
            end_index = find_end_of_repetition(
                sublist, previous_index, sublist[previous_index])
            count = end_index - previous_index + 1
            sub_img_matrix.append(str(sublist[end_index])+'x'+str(count))
            previous_index = end_index + 1

        img_matrix.append(sub_img_matrix)

    return img_matrix


def decompress(PGM_list):
    ''' (list<list<int>>) -> list<list<str>>
    Returns the decompressed image matrix of a compressed PGM_list.
    If the PGM_list is not a valid PGM image matrix, an AssertionError is raised.

    >>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]

    >>> decompress([['1x1', '2x1', '3x3'], ['0x1', '2x1', '1x1', '2x2'], ['0x2', '255x1', '1x1', '255x1']])
    [[1, 2, 3, 3, 3], [0, 2, 1, 2, 2], [0, 0, 255, 1, 255]]

    >>> decompress([['1x1', '2x1', '3x3'], ['0x1', '2x1', '1x1', '2x2'], ['0x2', '255x1', '1x1', '255x1']])
    [[1, 2, 3, 3, 3], [0, 2, 1, 2, 2], [0, 0, 255, 1, 255]]

    '''

    img_matrix = []

    for sublist in PGM_list:
        sub_img_matrix = []

        for element in sublist:
            splitted_list = element.split('x')
            num = int(splitted_list[0])
            num_times = int(splitted_list[1])

            for i in range(0, num_times):
                sub_img_matrix.append(num)

        img_matrix.append(sub_img_matrix)

    return img_matrix


def process_command(input_string):
    '''(str) -> NoneType
    Takes a string called input_string, which contains space-separated commands.
    process_command executes these commands without returning anything.
    Commands might include the load, save, invert, flip horizontal/vertical, crop, compress, decompress.

    >>> process_command("LOAD<comp.pgm> CP DC INV INV SAVE<comp2.pgm>")
    >>> image = load_image("comp.pgm")
    >>> image2 = load_image("comp2.pgm")
    >>> image == image2
    True

    >>> process_command("LOAD<comp.pgm.compressed> DC INV CR<1,2,2,2> CP SAVE<comp_test.pgm.compressed>")
    >>> image1 = load_image("comp.pgm.compressed")
    >>> image2 = load_image("comp_test.pgm.compressed")
    >>> image1_mod = compress(crop(invert(decompress(image1)),1,2,2,2))
    >>> image1_mod == image2
    True

    >>> process_command("LOAD<comp.pgm.compressed> DC FH FV CR<2,3,3,4> INV CP SAVE<comp_test_two.pgm.compressed>")
    >>> image1 = load_image("comp.pgm.compressed")
    >>> image2 = load_image("comp_test_two.pgm.compressed")
    >>> image1_mod = compress(invert(crop(flip_vertical(flip_horizontal(decompress(image1))),2,3,3,4)))
    >>> image1_mod == image2
    True

    >>> process_command("LAOD<comp.pgm.compressed> DC FH CR<1,1,1,1> INV CP SAVE<comp_test_two.pgm.compressed>")
    Traceback (most recent call last):
    AssertionError: The command does not start with the appropriate load function
    '''

    command_list = ['LOAD', 'SAVE', 'INV', 'FH', 'FV', 'CR', 'CP', 'DC']
    splitted_list = input_string.split()
    PGM_list = []

    for i in range(0, len(splitted_list)):
        print(i)
        print(splitted_list[i][0:4])
        if i == 0:
            if splitted_list[i][0:4] != 'LOAD':
                raise AssertionError(
                    "The command does not start with the appropriate load function")

            PGM_list = load_image(splitted_list[i][4:].strip('<>'))

        if i == len(splitted_list)-1:
            if splitted_list[i][0:4] != 'SAVE':
                raise AssertionError(
                    "The command does not end with the appropriate save function")

            save_image(PGM_list, splitted_list[i][4:].strip('<>'))

        if 'CR' in splitted_list[i]:
            string_list = splitted_list[i][2:].strip('<>').split(',')
            PGM_list = crop(PGM_list, int(string_list[0]), int(
                string_list[1]), int(string_list[2]), int(string_list[3]))

        else:
            valid = False
            for element in command_list:
                if element in splitted_list[i]:
                    valid = True

            if not valid:
                raise AssertionError(
                    "The input includes an unrecognized command. Please try again")

            if splitted_list[i] == 'INV':
                PGM_list = invert(PGM_list)

            if splitted_list[i] == 'FH':
                PGM_list = flip_horizontal(PGM_list)

            if splitted_list[i] == 'FV':
                PGM_list = flip_vertical(PGM_list)

            if splitted_list[i] == 'CP':
                PGM_list = compress(PGM_list)

            if splitted_list[i] == 'DC':
                PGM_list = decompress(PGM_list)
