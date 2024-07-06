import heapq
import sys
import time

def read_data(file_path):
    data = []
    valid_lines = 0
    with open(file_path, 'r') as file:
        for line in file:
            valid_lines += 1
            record = line.strip().split(',')
            try:
                instance_weight = float(record[25])  # instance weight
            except ValueError:
                valid_lines -= 1
                continue  # skip records where the instance weight cannot be converted to float
            age = int(record[1])  # age
            married_status = record[8].strip()  # married status
            if age < 18 or married_status.startswith("Married"):  # skip records with age less than 18 or married status starting with "Married"
                valid_lines -= 1                
                continue
            record_id = int(record[0])  # record ID
            data.append((record_id, age, instance_weight))
    print(f"Males: {valid_lines}")
    return data

def alternative_topk_join(males_data, females_data, K):
    results_heap = []
    valid_lines = 0
    
    males_grouped = {}
    for record in males_data:
        age = record[1]
        if age not in males_grouped:
            males_grouped[age] = []
        males_grouped[age].append(record)
    
    with open(females_data, 'r') as file:
        for line in file:
            valid_lines += 1
            record = line.strip().split(',')
            try:
                instance_weight = float(record[25])  
            except ValueError:
                valid_lines -= 1
                continue  
            age = int(record[1])  
            married_status = record[8].strip() 
            if age < 18 or married_status.startswith("Married"):
                valid_lines -= 1 
                continue
            record_id = int(record[0]) 
            
            if age in males_grouped:
                for male in males_grouped[age]:
                    join_result = male[2] + instance_weight  # calculate join result based on instance weights
                    if len(results_heap) < K:
                        heapq.heappush(results_heap, (join_result, male[0], record_id)) 
                    else:
                        if join_result > results_heap[0][0]:  # compare with the smallest element in the heap
                            heapq.heappushpop(results_heap, (join_result, male[0], record_id))  

    print(f"Females: {valid_lines}")
    return results_heap

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\033[91mUsage: python Part2.py <K>\033[0m")
        sys.exit(1)
    K = int(sys.argv[1])
    males_data = read_data('males_sorted')
    females_data = 'females_sorted'
    
    start_time = time.time()
    results_heap = alternative_topk_join(males_data, females_data, K)
    execution_time = time.time() - start_time
    
    top_pairs = sorted([heapq.heappop(results_heap) for _ in range(len(results_heap))], reverse=True)
    
    print("\033[1;35m========================================\033[0m")  
    print("\033[1;32m\t     Top-{} pairs\033[0m".format(K))
    print("\033[1;35m========================================\033[0m")  
    for i, result in enumerate(top_pairs):
        print("{}. pair: {},{} score: {:.2f}".format(i+1, result[1], result[2], result[0]))
    
    print("\033[1;35m========================================\033[0m")  
    print("\033[1;32mExecution time:\033[0m", execution_time)
    print("\033[1;35m========================================\033[0m")
