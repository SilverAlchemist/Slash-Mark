import nltk
import numpy as np
import string

# NLTK modules for text processing
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Preprocessing for tokenization and lemmatization
lemmatizer = WordNetLemmatizer()

# Function to preprocess text
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in string.punctuation]
    return tokens

# Reading and preprocessing the corpus data
with open('corpus.txt', 'r', errors='ignore') as file:
    corpus = file.read().lower()
sentences = nltk.sent_tokenize(corpus)
word_tokens = [preprocess_text(sentence) for sentence in sentences]

# Function to get bag of words
def get_bag_of_words(sentence, word_tokens):
    bag = np.zeros(len(word_tokens))
    for idx, words in enumerate(word_tokens):
        for word in words:
            if word in sentence:
                bag[idx] = 1
                break
    return bag

# Generating response
def generate_response(user_input):
    user_input_tokens = preprocess_text(user_input)
    user_bag = get_bag_of_words(user_input_tokens, word_tokens)
    similarity_scores = [nltk.jaccard_distance(set(words), set(user_input_tokens)) for words in word_tokens]
    closest_match_idx = np.argmin(similarity_scores)
    return sentences[closest_match_idx]


# Main function to run the chatbot
def chat():
    print("Hello! I'm a chatbot. You can start chatting with me. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            response = generate_response(user_input)
            print("Bot:", response)

if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('wordnet')
    chat()
