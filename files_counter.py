import os
import sys


def count_files(start_dir):
    """
    Stores file extension and count to a Dictionary;
    If `file` is a directory, it will be stored as `FOLDER`,
    if `file` is a file, it will be its extension.
    Otherwise, it will be stored as `OTHER`.

    :param start_dir: The directory to count for files.
    :return: The dictionary of file/folder counts.
    """

    file_dict = {}

    for f_name in os.listdir(start_dir):
        if os.path.isdir(start_dir + '\\' + f_name):
            if 'FOLDER' in file_dict.keys():
                file_dict['FOLDER'] += 1
            else:
                file_dict['FOLDER'] = 1

        elif os.path.isfile(start_dir + '\\' + f_name) and '.' in start_dir + '\\' + f_name:
            if (ext := '.' + f_name.split('.')[-1]) in file_dict.keys():
                file_dict[ext] += 1
            else:
                file_dict[ext] = 1

        else:
            if 'OTHER' in file_dict.keys():
                file_dict['OTHER'] += 1
            else:
                file_dict['OTHER'] = 1

    return file_dict


def dict_to_table(d: dict, left_title: str, right_title: str):
    """
    Converts a 1d Dictionary to a table.

    :param d: The 1d Dictionary.
    :param left_title: The title for the left row.
    :param right_title: The title for the right row.
    :return: The converted table.
    """

    keys_max = max([len(str(key)) for key in d.keys()])
    vals_max = max([len(str(val)) for val in d.values()])
    tl_len = len(left_title)
    tr_len = len(right_title)
    left_max = max([keys_max, tl_len])
    right_max = max([vals_max, tr_len])

    res = '+-' + left_max * '-' + '-+-' + right_max * '-' + '-+\n'

    if tl_len >= keys_max:
        res += '| ' + left_title + ' | '
    else:
        res += '| ' + left_title + (keys_max - tl_len) * ' ' + ' | '
    if tr_len >= vals_max:
        res += right_title + ' |\n'
    else:
        res += right_title + (vals_max - tr_len) * ' ' + ' |\n'

    res += '+-' + left_max * '-' + '-+-' + right_max * '-' + '-+\n'

    for key, val in d.items():
        res += '| ' + str(key) + (left_max - len(str(key))) * ' ' + ' | '
        res += str(val) + (right_max - len(str(val))) * ' ' + ' |\n'

    res += '+-' + left_max * '-' + '-+-' + right_max * '-' + '-+'

    return res


if __name__ == '__main__':
    if len(sys.argv) == 1:
        d = os.getcwd()
    else:
        d = sys.argv[1]

    count_d = count_files(d)
    table = dict_to_table(count_d, 'File Type', '# of File')

    print(table)
