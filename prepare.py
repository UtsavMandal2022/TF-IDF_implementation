# Utsav Mandal

with open('Qdata/output_headings.txt','r') as f:
    lines=f.readlines()

# for ind,line in enumerate(lines):
#     print(ind,line)

def preprocess(document_text):
    # remove the leading numbers from the string, remove not alpha numeric characters, make everything lowercase
    terms = [term.lower() for term in document_text.strip().split()[1:]]
    return terms

vocab={}
docs=[]

for line in lines:
    doc = preprocess(line)
    docs.append(doc)
    for term in doc:
        if term not in vocab:
            vocab[term]=1
        else:
            vocab[term]+=1

# print(len(docs))
# print(docs[2156])
# print(len(vocab))
# print(vocab)

vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))

with open ('vocab.txt','w') as f:
    for key in vocab:
        f.write(key+'\n')

with open ('idf-values.txt','w') as f:
    for key in vocab:
        f.write(str(vocab[key])+'\n')

with open ('docs.txt','w') as f:
    for doc in docs:
        for term in doc:
            f.write(term+' ')
        f.write('\n')

inv_index={}

for ind,doc in enumerate(docs):
    for term in doc:
        if term not in inv_index:
            inv_index[term]=[ind]
        else:
            inv_index[term].append(ind)

with open ('inv-index.txt','w') as f:
    for key in inv_index:
        f.write(key+'\n')
        for value in inv_index[key]:
            f.write(str(value)+' ')
        f.write('\n')