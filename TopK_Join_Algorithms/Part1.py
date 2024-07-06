# Chasanis Evangelos 5058

import heapq
import sys
import time

males_file = open('males_sorted', 'r')
females_file = open('females_sorted', 'r')

males_by_age = {}
females_by_age = {}
results_heap = []
p1_max = p2_max = max_score = 0
valid_lines = 0
valid_lines2 = 0

def read_next_male():
    global valid_lines
    line = males_file.readline().strip()
    if line:
        valid_lines += 1
        record = line.split(',')
        try:
            instance_weight = float(record[25])  # instance weight
            age = int(record[1])  # age
            married_status = record[8].strip()  # married status
            if age >= 18 and not married_status.startswith("Married"):  # consider only if age is 18 and above and not married
                record_id = int(record[0])  # record ID
                return {'id': record_id, 'age': age, 'instance_weight': instance_weight}
            else:
                valid_lines -= 1
                return read_next_male()  
        except (ValueError, IndexError):
            valid_lines -= 1
            return read_next_male()  
    else:
        return None

def read_next_female():
    global valid_lines2
    line = females_file.readline().strip()
    if line:
        valid_lines2 += 1
        record = line.split(',')
        try:
            instance_weight = float(record[25])  # instance weight
            age = int(record[1])  # age
            married_status = record[8].strip()  # married status
            if age >= 18 and not married_status.startswith("Married"):  # consider only if age is 18 and above and not married
                record_id = int(record[0])  # record ID
                return {'id': record_id, 'age': age, 'instance_weight': instance_weight}
            else:
                valid_lines2 -= 1
                return read_next_female()  
        except (ValueError, IndexError):
            valid_lines2 -= 1
            return read_next_female()  
    else:
        return None

def join_and_report():
    global males_by_age, females_by_age, results_heap, p1_max, p2_max
    
    male = read_next_male()
    female = read_next_female()
    
    while male and female:
        p1_cur = male['instance_weight']
        p2_cur = female['instance_weight']
        
        if p1_max is None or p1_cur > p1_max:
            p1_max = p1_cur
        if p2_max is None or p2_cur > p2_max:
            p2_max = p2_cur
        
        T = max(p1_max + p2_cur, p1_cur + p2_max)
        
        if male['age'] not in males_by_age:
            males_by_age[male['age']] = []
        if female['age'] not in females_by_age:
            females_by_age[female['age']] = []
        
        males_by_age[male['age']].append(male)
        females_by_age[female['age']].append(female)
        
        # Female probe
        if female['age'] in males_by_age:
            for male_record in males_by_age[female['age']]:
                join_result = male_record['instance_weight'] + female['instance_weight']
                heapq.heappush(results_heap, (-join_result, male_record['id'], female['id']))
                if -results_heap[0][0] >= T:
                    return heapq.heappop(results_heap)

        # Male probe
        if male['age'] in females_by_age:
            for female_record in females_by_age[male['age']]:
                join_result = male['instance_weight'] + female_record['instance_weight']
                heapq.heappush(results_heap, (-join_result, male['id'], female_record['id']))
                if -results_heap[0][0] >= T:
                    return heapq.heappop(results_heap)
        
        male = read_next_male()
        female = read_next_female()
    
    return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\033[91mUsage: python Part1.py <K>\033[0m")
        sys.exit(1)

    K = int(sys.argv[1])

    print("\033[1;35m========================================\033[0m")  
    print("\033[1;32m\t     Top-{} pairs\033[0m".format(K))
    print("\033[1;35m========================================\033[0m") 
    i = 1
    start_time = time.time()  
    for _ in range(K):
        top_result = join_and_report()
        if top_result:
            print("{}. pair: {},{} score: {:.2f}".format(i, top_result[1], top_result[2], -top_result[0]))
        else:
            print("No more results.")
            break
        i += 1
    end_time = time.time()  
    execution_time = end_time - start_time 
    
    males_file.close()
    females_file.close()
    
    print("\033[1;35m========================================\033[0m")  
    print("\033[1;32mExecution time:\033[0m", execution_time)
    print("\033[1;35m========================================\033[0m")
    print("Males: ",valid_lines)
    print("Females: ",valid_lines2)
