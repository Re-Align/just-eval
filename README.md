# Just-Eval: A simple GPT-based evaluation tool for multi-aspect, interpretable assessment of LLMs.


## Background 


### Suggested dataset

- Check out our data on 🤗 Hugging Face: [**re-align/just-eval-instruct**](https://huggingface.co/datasets/re-align/just-eval-instruct)

- Check here: [https://allenai.github.io/re-align/just_eval.html#leaderboard](https://allenai.github.io/re-align/just_eval.html#leaderboard)

## Multiple Aspects 

![Multiple Aspects](https://allenai.github.io/re-align/images/eval_2.png)
 

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

### Setup OpenAI API Key

```bash 
export OPENAI_API_KEY=<your secret key>
```



## Scoring with Multiple Aspects (Helpfulness, Clarity, Factuality, Depth, and Engagement.)

```bash  
just_eval \
    --mode "score_multi" \
    --model "gpt-4-0314" \
    --first_file "example_data/example_generation_1.json" \
    --output_file "example_data/eval_outputs/1.score_multi.gpt-4.json"

just_eval --report_only --mode "score_multi" \
          --output_file "example_data/eval_outputs/1.score_multi.gpt-4.json" 

cat example_data/eval_outputs/1.score_multi.gpt-4.eval_res.json 
```


## Scoring with the Safety

```bash    

just_eval \
    --mode "score_safety" \
    --model "gpt-3.5-turbo-0613" \
    --first_file "example_data/example_generation_safety.json" \
    --output_file "example_data/eval_outputs/1.safety.score_safety.chatgpt.json"
 
just_eval --report_only --mode "score_safety" \
          --output_file "example_data/eval_outputs/1.safety.score_safety.chatgpt.json" 

cat example_data/eval_outputs/1.safety.score_safety.chatgpt.eval_res.json         
``` 


## Examples 

### Example Input Format 
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

### Example Output Format 
Please check [`example_data/eval_outputs/1.score_multi.gpt-4.json`](example_data/eval_outputs/1.score_multi.gpt-4.json) file for an example.
```json 

[
  {
    "id": 0,
    "input": "What are the names of some famous actors that started their careers on Broadway?",
    "output_cand": "Thank you for your question! I'm happy to help. There are many famous actors who got their start ...",
    "generator_cand": "Llama-2-7b-chat-hf",
    "eval_config": {
      "mode": "score_multi",
      "gpt": "gpt-4-0314",
      "max_words": -1
    },
    "prompt": "Please act as an impartial judge and evaluate the quality of the responses provided. You will rate the quality ....",
    "result": "{\n    \"helpfulness\": {\n ....",
    "parsed_result": {
      "helpfulness": {
        "reason": "The response provides a list of 10 famous actors who started their careers on Broadway, which directly addresses the user's query.",
        "score": "5"
      },
      ...
    }
  },

```


## Case studies

![Case study](https://allenai.github.io/re-align/images/case_1.png)


## Citation 