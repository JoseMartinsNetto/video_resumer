from transformers import T5Tokenizer, T5ForConditionalGeneration

class TextResumer:
    def __init__(self, text):
        self.text = text

    def resume(self) -> str:
        # Carregar o tokenizer e o modelo
        model_name = "t5-base"
        tokenizer = T5Tokenizer.from_pretrained(model_name)
        model = T5ForConditionalGeneration.from_pretrained(model_name)

        # Preparar o texto para sumarização
        input_ids = tokenizer.encode("summarize: " + self.text, return_tensors="pt", max_length=1024, truncation=True)

        # Gerar o resumo
        summary_ids = model.generate(input_ids, max_length=200, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return summary