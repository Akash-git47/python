#1 basic callback
def process_data(data, callback):
    result = data * 2
    callback(result)    

def print_result(result):
    print("Processed result:", result)
process_data(5, print_result)

# 2 callback with lambda
def process_data(data, callback):   
    result = data * 2
    callback(result)    
process_data(5, lambda result: print("Processed result:", result))

    # 3 sorting with a callback(key function
    data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]    
    sorted_data = sorted(data, key=lambda x: x[1])
    print(sorted_data)