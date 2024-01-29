model_name=$1 
target_file="leaderboard/outputs/${model_name}.to_eval.json"
eval_parent_folder="leaderboard/eval_results/gpt-4-turbo/"
eval_folder="${eval_parent_folder}/${model_name}/"
mkdir -p $eval_folder

start_gpu=0 # not useful, just a placeholder

n_shards=8
shard_size=100
for ((start = 0, end = (($shard_size)), gpu = $start_gpu; gpu < $n_shards+$start_gpu; start += $shard_size, end += $shard_size, gpu++)); do
    eval_file="${eval_folder}/${model_name}.general.$start-$end.json"
    just_eval \
        --mode score_multi \
        --gpt_model gpt-4-1106-preview \
        --model_output_file $target_file \
        --eval_output_file $eval_file \
        --start_idx $start --end_idx $end  &
done

n_shards=2
shard_size=100 
for ((start = 800, end = ((800 + $shard_size)), gpu = $start_gpu; gpu < $n_shards+$start_gpu; start += $shard_size, end += $shard_size, gpu++)); do
    eval_file="${eval_folder}/${model_name}.safety.$start-$end.json"
    just_eval \
        --mode score_safety \
        --gpt_model gpt-4-1106-preview \
        --model_output_file $target_file \
        --eval_output_file $eval_file \
        --start_idx $start --end_idx $end  &
done


# Wait for all background processes to finish
wait
echo "All evaluation scripts have completed"
# Run the merge results script after all evaluation scripts have completed
python leaderboard/scripts/merge_results.py $eval_folder $model_name.general
python leaderboard/scripts/merge_results.py $eval_folder $model_name.safety
mv $eval_folder/$model_name.general.json $eval_parent_folder/$model_name.score_multi.json 
mv $eval_folder/$model_name.safety.json $eval_parent_folder/$model_name.score_safety.json