'''Un embedding è una rappresentazione numerica (vettore) di un testo, generato da un modello di linguaggio come quelli offerti da OpenAI. Ogni testo, come una frase o un documento, viene trasformato in un vettore di numeri 
(ad esempio, con 768 dimensioni), dove ogni dimensione cattura un aspetto del significato del testo. 
Testi simili avranno vettori vicini nello spazio vettoriale, mentre testi diversi saranno più distanti.

Come funziona il filtraggio basato su embeddings?
Generazione degli embeddings:

Si generano embeddings per ogni documento e per la query utilizzando un modello come OpenAIEmbeddings.

Calcolo della similarità:

Una volta generati i vettori dei documenti e della query, calcoli la distanza o la similarità tra i vettori. 
Spesso si utilizza la cosine similarity, che misura quanto i due vettori puntano nella stessa direzione. 
Un valore di similarità vicino a 1 indica che i vettori sono molto simili, mentre valori vicini a 0 indicano poca somiglianza.
Filtraggio dei documenti:

Si selezionano i documenti che hanno una similarità elevata con la query. In questo modo, 
si possono trovare documenti rilevanti anche se non contengono esattamente le stesse parole chiave.'''


from langchain_community.embeddings import OpenAIEmbeddings
import numpy as np

documents = [
    "Il Giappone ha una lunga tradizione culturale.",
    "Il mondo della tecnologia è in continua evoluzione.",
    "La tradizione dell'Hanami in Giappone celebra i fiori di ciliegio.",
    "L'orso polare vive nelle regioni artiche."
]

# Crea un'istanza del modello di embedding
embedding_model = OpenAIEmbeddings()

# Genera gli embeddings per ogni documento
document_embeddings = [embedding_model.embed_text(doc) for doc in documents]

# Converti gli embeddings in numpy array per facilitare i calcoli
document_embeddings = np.array(document_embeddings)


# Query per la ricerca
query = "Cosa succede in Giappone durante la primavera?"

# Genera l'embedding per la query
query_embedding = embedding_model.embed_text(query)


from sklearn.metrics.pairwise import cosine_similarity

# Calcola la similarità coseno tra la query e i documenti
similarities = cosine_similarity([query_embedding], document_embeddings)[0]

# Visualizza i risultati di similarità
for i, similarity in enumerate(similarities):
    print(f"Document {i+1}: Similarity = {similarity:.2f}")


# Definisci una soglia di similarità (ad esempio 0.5)
threshold = 0.5

# Filtra i documenti che superano la soglia
filtered_documents = [documents[i] for i in range(len(similarities)) if similarities[i] > threshold]

# Stampa i documenti filtrati
print("Documenti rilevanti:")
for doc in filtered_documents:
    print(doc)


'''
Esempio di output
Document 1: Similarity = 0.45
Document 2: Similarity = 0.12
Document 3: Similarity = 0.89
Document 4: Similarity = 0.10

Documenti rilevanti:
La tradizione dell'Hanami in Giappone celebra i fiori di ciliegio.
'''