# just_eval

## Installation 

```bash 
git clone https://github.com/re-align/just_eval.git
cd just_eval
pip install .
```

## Setup OpenAI API Key

```bash 
export OPENAI_API_KEY=<your secret key>
```


## Scoring with Multiple Aspects 

```bash  
just_eval \
    --mode "score_multi" \
    --model "gpt-4-0314" \
    --first_file "example_data/example_generation_0.json" \
    --output_file "example_data/eval_outputs/0.score_multi.gpt-4.json"

# just_eval \
#     --mode "score_multi" \
#     --model "gpt-3.5-turbo-0613" \
#     --first_file "example_data/example_generation_0.json" \
#     --output_file "example_data/eval_outputs/0.score_multi.chatgpt.json"

just_eval --report_only --mode "score_multi" \
          --output_file "example_data/eval_outputs/score_multi.gpt4.json" 
             
```


## Scoring with Safety

```bash   

just_eval \
    --mode "score_safety" \
    --model "gpt-3.5-turbo-0613" \
    --first_file "example_data/example_generation_0.json" \
    --output_file "example_data/eval_outputs/0.score_safety.chatgpt.json"

just_eval \
    --mode "score_safety" \
    --model "gpt-3.5-turbo-0613" \
    --first_file "example_data/example_generation_safety.json" \
    --output_file "example_data/eval_outputs/safety.score_safety.chatgpt.json"

    

just_eval --report_only --mode "score_safety" \
          --output_file "example_data/eval_outputs/score_safety.gpt4.json" 
             
``` 