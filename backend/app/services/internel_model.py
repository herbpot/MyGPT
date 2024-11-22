# TODO
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, StoppingCriteria, StoppingCriteriaList
import torch
import os

# 사용자 정의 StoppingCriteria
class StopOnKeyword(StoppingCriteria):
    def __init__(self, stop_words, tokenizer, max_words=500):
        self.stop_words = stop_words
        self.tokenizer = tokenizer
        self.words = 0
        self.max = max_words

    def __call__(self, input_ids, scores):
        generated_text = self.tokenizer.decode(input_ids[0], skip_special_tokens=True)
        self.words += 1
        if self.words > self.max:
            return any(word in generated_text[-1] for word in self.stop_words)
        return False

class Model:
    def __init__(self) -> None:
        self.isinit = False

    def init(self, BASE_MODEL = "meta-llama/Llama-3.2-3B-Instruct") -> None:
        self.isinit = True
        model = AutoModelForCausalLM.from_pretrained(
                BASE_MODEL,
                device_map="cuda:1",  # 두 번째 GPU로 할당
                # quantization_config=config,
                token=os.environ['HUGGINGFACE_TOKEN']
            )
        self.tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, device_map="cuda:1", token=os.environ['TOKEN_2'])
        self.tokenizer.add_special_tokens({"pad_token": self.tokenizer.eos_token})  # pad_token 설정
        self.loaded_model = PeftModel.from_pretrained(model, "/home/kookmin/chaewon/LLM_document_summary/results/checkpoint-27534", 
                                                is_trainable=False)

    def chat(self, inputs_raw=''):
        if inputs_raw == '':
            return ''
        inputs_raw = f"""<|begin_of_text|><|start_header_id|>user: <|end_header_id|>Please summarize the following text to 20% of its length. There should be no spelling or typos, and the text should not be long or contain repeated similar content.
        {inputs_raw}<|eot_id|><|start_header_id|>assistant: <|end_header_id|>"""
        # del inputs
        torch.cuda.empty_cache()

        # 입력과 종료 조건 설정
        stop_words = ["."]  # 종료를 트리거하는 키워드
        stopping_criteria = StoppingCriteriaList([StopOnKeyword(stop_words, self.tokenizer,len(inputs_raw)//100*25)])

        inputs = self.tokenizer(inputs_raw, return_tensors="pt").to('cuda')

        outputs = self.loaded_model.generate(
            input_ids=inputs["input_ids"], 
            attention_mask=inputs["attention_mask"],
            max_new_tokens=len(inputs_raw)//100*35,
            eos_token_id=128009,
            temperature=0.4,
            no_repeat_ngram_size=10,  # 반복을 방지
            # repetition_penalty = 1.1,
            stopping_criteria=stopping_criteria,  # 사용자 정의 종료 조건
            early_stopping=True,
            do_sample=True
            )



        return tokenizer.batch_decode(outputs, skip_special_tokens=False)[0].replace(inputs_raw, '')