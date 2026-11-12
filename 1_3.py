search_results = [
    ("doc_1", 0.92),
    ("doc_2", 0.45),
    ("doc_3", 0.81),
    ("doc_4", 0.30),
    ("doc_5", 0.76),
]
relevant = [name for name, value in search_results if value > 0.7 ]
reg = {name1: value1 for name1, value1 in search_results if value1 >0.7}
print(reg)