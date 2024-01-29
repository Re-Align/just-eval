import json 
from datasets import load_dataset
from tabulate import tabulate


show_key = "aspect"
lite = False

test_data = load_dataset("re-align/just-eval-instruct", split="test")

id_types = {} 
for d in list(test_data)[:800]: 
    source = "alpaca_eval"
    if d["dataset"] == "mt":
        source = "mt-1"
    elif d["dataset"] == "lima":
        source = "lima"
    if d["category"] == "safety":
        source = "safety"
    id_types[d["id"]] = dict(task=d["task"], topic=d["topic"], source=[source]) 

config_file = "leaderboard/configs_gpt4t.json"
with open(config_file) as f:
    # print(f.name)
    configs = json.load(f)
if lite:
    filter_file = "leaderboard/filters.json"
    with open(filter_file) as f:
        filter_data = json.load(f)
    lite_regular_ids = filter_data["lite_regular_ids"]
    lite_safety_ids = filter_data["lite_safety_ids"]
else:
    lite_regular_ids, lite_safety_ids = [], []

# Constants 
aspects = ["helpfulness", "factuality", "depth",  "clarity", "engagement", "safety" ]
task_types = ['info-seek', 'reasoning', 'procedure', 'writing',  'role-play',  'coding', 'math' ] 
topic_types = ['ethics', 'nature', 'stem', 'medical', 'finance', 'humanities', 'lifestyle']
sources = ["alpaca_eval", "lima", "mt-1", "safety"]


# Define the dimensions to show
dims = []
if show_key == "task":
    dims = task_types 
elif show_key == "topic":
    dims = topic_types
elif show_key == "source":
    dims = sources
elif show_key == "aspect":
    dims = aspects
    
    
headers = ["name"] + dims + ["avg", "len"]  
# headers = headers[:-1]
table = []
for item in configs:    
    with open(item["eval_result_general"]) as f:
        eval_data = json.load(f)    
    dim_scores = {}
    lens = []
    for dim in dims:
        dim_scores[dim] = []
    for eval_item in eval_data:
        _id = eval_item["id"]
        if len(lite_regular_ids) > 0 and _id not in lite_regular_ids:
            continue  
        lens.append(len(eval_item["output_cand"].split()))
        if show_key in ["task", "topic", "source"]:
            # Option 1: use the average score 
            # scores = [float(str(r["score"]).replace("N/A", "5")) for _, r in eval_item["parsed_result"].items()]
            # item_score = sum(scores) / len(scores)
            # Option 2: only use the helpfulness score
            item_score = float(str(eval_item["parsed_result"]["helpfulness"]["score"]).replace("N/A", "5"))                        
            for _t in id_types[_id][show_key]:
                if _t not in dims:
                    continue
            dim_scores[_t].append(item_score)
        elif show_key == "aspect":
            for dim in dims:
                if dim != "safety":
                    item_score = float(str(eval_item["parsed_result"][dim]["score"]).replace("N/A", "5"))
                    dim_scores[dim].append(item_score)
    
    # for the safety aspect 
    if show_key in ["aspect", "source"]:
        with open(item["eval_result_safety"]) as f:
            eval_data_safety = json.load(f)
        for eval_item in eval_data_safety:
            _id = eval_item["id"] 
            if len(lite_safety_ids) > 0 and _id not in lite_safety_ids:
                continue 
            item_score = float(str(eval_item["parsed_result"]["safety"]["score"]).replace("N/A", "5"))
            dim_scores["safety"].append(item_score) 
            # lens.append(len(eval_item["output_cand"].split()))
    dim_score_avg = {} 
    for dim, scores in dim_scores.items(): 
        dim_score_avg[dim] = sum(scores)/len(scores)
    avg = sum([score for _, score in dim_score_avg.items()])/len(dim_score_avg)
    row = [item["nickname"]] + [f"{dim_score_avg[dim]:.2f}" for dim in dims] + [f"{avg:.2f}"] + [sum(lens)/len(lens)]
    # # ignore avg 
    # row = row[:-1]
    table.append(row)
    
 
# print(headers)
# print(table)

# sort the table
if show_key == "aspect":
    # table = sorted(table, key=lambda x: x[-2], reverse=True)
    table = sorted(table, key=lambda x: x[1], reverse=True)
elif show_key == "task":
    table = sorted(table, key=lambda x: x[-2], reverse=True) 
elif show_key == "source":
    table = sorted(table, key=lambda x: x[-2], reverse=True)
    
print(tabulate(table, headers=headers, tablefmt="tsv", floatfmt=".2f"))
# def html_gen(table):
print(tabulate(table, headers=headers, tablefmt="html", floatfmt=".2f").replace(' style="text-align: right;"', ""))
