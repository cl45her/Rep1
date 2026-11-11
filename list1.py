sample_text = (
    "LLM agents require robust tools. A good agent evaluates "
    "tools carefully, but poorly configured tools break the agent!"
)
sample_text = sample_text.lower()
sample_text = sample_text.replace('!',"")
sample_text = sample_text.replace('?',"")
sample_text = sample_text.replace(',',"")
sample_text = sample_text.replace('.',"")
sample_text = sample_text.split()
print(sample_text)
counts = {}
for word in sample_text:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
print(counts)