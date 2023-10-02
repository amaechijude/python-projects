sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lenght = len(sample_list)
chunk_size = int(lenght/3)
start = 0
end = chunk_size
for i in range(1,4):
    sm = sample_list[start:end]
    print(f"Chunk-{i} = {list(reversed(sm))}")
    start = end
    end += chunk_size