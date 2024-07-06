# Evangelos Chasanis
# cs05058

import sys
import csv


def merge(left, right, agg_func):

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        print(left[i])
        left_key, left_value = left[i]
        print(left[i])
        right_key, right_value = right[j]
        if int(left_key) < int(right_key):
            result.append((left_key, left_value))
            i += 1
        elif int(left_key) > int(right_key):
            result.append((right_key, right_value))
            j += 1
        else:  
            if agg_func == 'max':
                result.append((left_key, max(left_value, right_value)))
            elif agg_func == 'min':
                result.append((left_key, min(left_value, right_value)))
            elif agg_func == 'sum':
                result.append((left_key, left_value + right_value))
            i += 1
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort_and_group(arr, group_by_attr, agg_attr, agg_func):

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_and_group(arr[:mid], group_by_attr, agg_attr, agg_func)
    right = merge_sort_and_group(arr[mid:], group_by_attr, agg_attr, agg_func)
    return merge(left, right, agg_func)


if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("\033[91mUsage: python part1.py <file> <grouping_attribute> <aggregation_attribute> <aggregation_function>\033[0m")
        sys.exit(1)

    filename = sys.argv[1]
    group_by_attr = int(sys.argv[2])
    agg_attr = int(sys.argv[3])
    agg_func = sys.argv[4]

    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            table = [row for row in reader]
    except FileNotFoundError:
        print("\033[91mFile not found. Please provide a valid filename.\033[0m")
        sys.exit(1)
    except Exception as e:
        print(f"\033[91mAn error occurred while reading the file: {e}\033[0m")
        sys.exit(1)


    grouped_data = []
    for row in table:
        key = row[group_by_attr]
        value = int(row[agg_attr])
        grouped_data.append((key, value))

    sorted_table = merge_sort_and_group(grouped_data, group_by_attr, agg_attr, agg_func)

    output_filename = "O1.csv"
    try:
        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in sorted_table:
                writer.writerow(row)
    except Exception as e:
        print(f"\033[91mAn error occurred while writing the output file: {e}\033[0m")
        sys.exit(1)

    print(f"\033[92mResults written to {output_filename}\033[0m")
