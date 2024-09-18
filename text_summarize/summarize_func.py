from transformers import pipeline


# Inicializando o summarizer com o modelo BART
summarizer_bart = pipeline("summarization", model="facebook/bart-large-cnn")

# Função para sumarização usando o modelo BART
def summarize(text, max_length=500, min_length=100):
     
    try:
        
        summary = summarizer_bart(text, max_length=max_length, min_length=min_length)
        
        if isinstance(summary,list):
            
            return summary[0]['summary_text']
    
    except IndexError:
        
        return None
