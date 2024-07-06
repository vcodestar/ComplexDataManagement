import csv
import sys

def merge_join(R_file, S_file, ind1, ind2):

    try:
        with open(R_file, 'r', newline='') as r_file, open(S_file, 'r', newline='') as s_file, open("O3.csv", 'w', newline='') as output:
            r_reader = csv.reader(r_file)
            s_reader = csv.reader(s_file)
            output_writer = csv.writer(output)

            r_row = next(r_reader, None)
            s_row = next(s_reader, None)

            sums = {}

            while r_row is not None and s_row is not None:
                if r_row[ind1] == s_row[ind2] and int(r_row[2]) == 7:
                    key = r_row[ind1]
                    if key not in sums:
                        sums[key] = 0
                    sums[key] += int(s_row[2])
                    s_row = next(s_reader, None)
                elif int(r_row[ind1]) < int(s_row[ind2]):
                    r_row = next(r_reader, None)
                else:
                    s_row = next(s_reader, None)


            for key, value in sums.items():
                output_writer.writerow([key, value])

        print(f"\033[92mResults written to 'O3.csv'.\033[0m")

    except FileNotFoundError:
        print("\033[91mFile not found. Please provide correct file paths.\033[0m")
    except Exception as e:
        print(f"\033[91mAn error occurred: {e}\033[0m")

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("\033[91mUsage: python part3.py <file_1(which has primary key)> <file_2(which has foreign key)> <index_file1> <index_file2>\033[0m")
    else:
        try:
            ind1 = int(sys.argv[3])
            ind2 = int(sys.argv[4])
            merge_join(sys.argv[1], sys.argv[2], ind1, ind2)
        except ValueError:
            print("\033[91mIndices must be integers.\033[0m")
