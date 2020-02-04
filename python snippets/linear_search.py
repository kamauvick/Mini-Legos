def linear_search(collection, value):
    for index, item in enumerate(collection):
        if item == value:
            return index
    return None


coll =  [2,4,6,8,9,36,56,57,64,87,89]
val = 87
_index = linear_search(coll, val) 


if __name__ == "__main__":
    import time
    start = time.process_time()
    print(f'Index {_index} : Value {coll[_index]}')
    print(f"Processing time: {time.process_time() - start}")