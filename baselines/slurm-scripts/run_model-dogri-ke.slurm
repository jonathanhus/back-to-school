#!/bin/sh

##  An SBATCH command is "commented out" (ignored) if line begins with 2 "#"
##  Anything in <angle brackets> needs to be modified by you (remove <> too)

## Specify a name for Slurm to use when displaying your job.
#SBATCH --job-name=mtob-dgo

## Select a partition (queue) to submit your job to.
#SBATCH --partition=contrib-gpuq
#SBATCH --qos=cs_dept
#SBATCH --gres=gpu:1g.10gb:1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8

## Deal with output and errors.  Separate into 2 files (not the default).
## May help to put your result files in a directory: e.g. /scratch/%u/logs/...
## NOTE: %u=userID, %x=jobName, %N=nodeID, %j=jobID, %A=arrayID, %a=arrayTaskID
#SBATCH --output=/scratch/%u/%x-%N-%j.out  # Output file
#SBATCH --error=/scratch/%u/%x-%N-%j.err   # Error file
#SBATCH --mail-type=BEGIN,END,FAIL         # ALL,NONE,BEGIN,END,FAIL,REQUEUE,..
#SBATCH --mail-user=jhus@gmu.edu           # Put your GMU email address here

## Load relevant modules needed for the job
module load gnu10
module load python/3.10.1-5r

## Run your program or script
source ~/mtob/venv-upgraded/bin/activate
cd ~/mtob/baselines

set -x;
set -e;

## MTOB
export MODEL_NAME="gpt-4-turbo-preview"
export LANGUAGE='dogri'
export DIRECTION='ke'
export OPENAI_API_KEY="put-key-here"
export AZURE_OPENAI_ENDPOINT="put-endpoint-here"

## Run MTOB on baseline, words, words/sentences, words/sentences/grammar

python main.py --language $LANGUAGE --direction $DIRECTION --model_type azure-openai --model_name $MODEL_NAME > "/scratch/jhus/mtob-${LANGUAGE}-${DIRECTION}-baseline.txt"
python main.py --language $LANGUAGE --direction $DIRECTION --model_type azure-openai --model_name $MODEL_NAME \
  --use_reference_wordlist > "/scratch/jhus/mtob-${LANGUAGE}-${DIRECTION}-W.txt"
python main.py --language $LANGUAGE --direction $DIRECTION --model_type azure-openai --model_name $MODEL_NAME \
  --use_reference_wordlist --use_reference_sentences > "/scratch/jhus/mtob-${LANGUAGE}-${DIRECTION}-WS.txt"
python main.py --language $LANGUAGE --direction $DIRECTION --model_type azure-openai --model_name $MODEL_NAME \
  --use_reference_wordlist --use_reference_sentences --use_reference_book_passages --book_type full_long --num_reference_passages 1 > "/scratch/jhus/mtob-${LANGUAGE}-${DIRECTION}-WSG.txt"
