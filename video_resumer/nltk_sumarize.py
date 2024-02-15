import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

class NLTKSumarize:
    def summarize_text(self, text: str, max_sentences:int = 5):
        # Baixar recursos do NLTK necessários para este exemplo
        nltk.download('punkt')
        nltk.download('stopwords')
        # Tokenização de sentenças
        sentences = sent_tokenize(text)
        
        # Remover stopwords e tokenizar as palavras
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text.lower())
        
        # Calculando a frequência de cada palavra, excluindo as stopwords
        freq_table = {}
        for word in words:
            if word not in stop_words:
                if word not in freq_table:
                    freq_table[word] = 1
                else:
                    freq_table[word] += 1
                    
        # Calculando a pontuação de cada sentença
        sentence_value = {}
        for sentence in sentences:
            for word, freq in freq_table.items():
                if word in sentence.lower():
                    if sentence not in sentence_value:
                        sentence_value[sentence] = freq
                    else:
                        sentence_value[sentence] += freq
                        
        # Identificar as sentenças de maior valor
        summary_sentences = sorted(sentence_value, key=sentence_value.get, reverse=True)[:max_sentences]
        
        # Juntar as sentenças selecionadas para formar o resumo
        summary = ' '.join(summary_sentences)
        return summary
    