# just_eval

## Installation 

```bash 
git clone https://github.com/Re-Align/just-eval.git
cd just_eval
pip install .
```

or 
```bash 
pip install git+https://github.com/Re-Align/just-eval.git
```

## Setup OpenAI API Key

```bash 
export OPENAI_API_KEY=<your secret key>
```


## Example Input Format 
Please check [`example_data/example_generation_1.json`](example_data/example_generation_1.json) file for an example. 
```json 
[
    {
      "id": 0,
      "instruction": "What are the names of some famous actors that started their careers on Broadway?",
      "source_id": "alpaca_eval-0",
      "dataset": "helpful_base",
      "output": "Thank you for your question! I'm happy to help. There are many famous actors ...",
      "generator": "Llama-2-7b-chat-hf",
      "datasplit": "just_eval"
    },
    ...
]
```

## Scoring with Multiple Aspects 

```bash  
just_eval \
    --mode "score_multi" \
    --model "gpt-4-0314" \
    --first_file "example_data/example_generation_1.json" \
    --output_file "example_data/eval_outputs/1.score_multi.gpt-4.json"

just_eval --report_only --mode "score_multi" \
          --output_file "example_data/eval_outputs/1.score_multi.gpt4.json" 
             
```


## Scoring with Safety

```bash    

just_eval \
    --mode "score_safety" \
    --model "gpt-3.5-turbo-0613" \
    --first_file "example_data/example_generation_safety.json" \
    --output_file "example_data/eval_outputs/1.safety.score_safety.chatgpt.json"
 

just_eval --report_only --mode "score_safety" \
          --output_file "example_data/eval_outputs/1.safety.score_safety.chatgpt.json" 
             
``` 


## Example Output Format 

