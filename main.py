import pandas as pd

df = pd.read_json("Sarcasm_Headlines_Dataset.json", lines=True)


headlines = df['headline'].drop_duplicates().reset_index(drop=True)
headlines=headlines.head(1000)
headlines.to_csv("cleaned_headlines.csv", index=False)
print(headlines)


def get_shingles(text, k=2):
    words = text.lower().split()
    return set([' '.join(words[i:i+k]) for i in range(len(words)-k+1)])

def jaccard_similarity(set1, set2):
    return len(set1 & set2) / len(set1 | set2)

results = []

for i in range(len(headlines)):
    for j in range(i + 1, len(headlines)):
        s1 = get_shingles(headlines[i])
        s2 = get_shingles(headlines[j])
        sim = jaccard_similarity(s1, s2)
        if sim >= 0.15:  
            results.append({
                'Headline 1': headlines[i],
                'Headline 2': headlines[j],
                'Similarity': round(sim, 2)
            })

similar_df = pd.DataFrame(results)

similar_df.to_csv("similar_headlines_output.csv", index=False)

similar_df.head()
print(similar_df.to_string(index=False))
