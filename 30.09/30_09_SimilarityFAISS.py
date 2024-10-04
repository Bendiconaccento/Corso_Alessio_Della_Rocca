import numpy as np
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from sklearn.metrics.pairwise import cosine_similarity  # Solo se vuoi calcolare manualmente le similarità

'''
Qui, embeddings è un'istanza della classe OpenAIEmbeddings, che rappresenta un modello di 
embedding pre-addestrato. Questo modello è utilizzato per convertire il testo in rappresentazioni 
vettoriali (embeddings).
'''

#embeddings = OpenAIEmbeddings()


'''
In questa riga, FAISS.from_texts(texts, embeddings) crea un archivio vettoriale
(vector store) utilizzando gli embeddings generati dai testi forniti. 
FAISS è una libreria che consente di gestire efficientemente la ricerca di similarità
tra vettori, particolarmente utile quando si hanno grandi quantità di dati.
'''

#vectorstore = FAISS.from_texts(texts, embeddings)


'''
Sì, puoi utilizzare FAISS per verificare la similarità tra i documenti e una risposta o una query.
FAISS è particolarmente utile quando hai un gran numero di documenti e vuoi eseguire ricerche rapide
e efficienti per trovare i documenti più simili a un embedding fornito (come una risposta o una query).
'''

documents = [
    "Il Giappone ha una lunga tradizione culturale.",
    "Il mondo della tecnologia è in continua evoluzione.",
    "La tradizione dell'Hanami in Giappone celebra i fiori di ciliegio.",
    "L'orso polare vive nelle regioni artiche."
]

# Crea un'istanza del modello di embedding
embedding_model = OpenAIEmbeddings()

# Genera gli embeddings per i documenti
document_embeddings = [embedding_model.embed_text(doc) for doc in documents]

# Converti in un array NumPy
document_embeddings = np.array(document_embeddings)

# Crea l'archivio FAISS
vectorstore = FAISS.from_texts(documents, embedding_model)


# Supponiamo che questa sia la risposta che vogliamo confrontare
response = "In Giappone, la gente celebra i fiori di ciliegio in primavera."

# Genera l'embedding per la risposta
response_embedding = embedding_model.embed_text(response)


# Ricerca dei documenti più simili all'embedding della risposta
k = 2  # Numero di documenti simili che vuoi trovare
distances, indices = vectorstore.search(response_embedding, k)

# Stampa i documenti più simili
print("Documenti più simili alla risposta:")
for i in range(k):
    print(f"Documento {indices[i]}: {documents[indices[i]]} (Distanza: {distances[i]})")


'''
Generazione degli embeddings: Creiamo gli embeddings per i documenti e l'archivio FAISS
 con i documenti e gli embeddings.
Embedding della risposta: Calcoliamo l'embedding per la risposta.
Ricerca in FAISS: Utilizziamo il metodo search di FAISS per trovare i 
k documenti più simili all'embedding della risposta.
FAISS restituisce le distanze e gli indici dei documenti più simili.
'''