#!/bin/sh
#SBATCH --partition=GPUQ
#SBATCH --gres=gpu:V100:1
#SBATCH --account=ie-idi
#SBATCH --time=150:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=12000
#SBATCH --job-name="AIR-yolo"
#SBATCH --output=job.out
#SBATCH --mail-user=sebastvi@stud.ntnu.no
#SBATCH --mail-type=END

WORKDIR=${SLURM_SUBMIT_DIR}
cd ${WORKDIR} # /cluser/work/<username>/master-sau/slurm

pip freeze --user | xargs pip uninstall -y
module purge
module load fosscuda/2020b
module load Python/3.8.6-GCCcore-10.2.0
# module load PyTorch/1.7.1-fosscuda-2020b

cd ..
pwd
pip install -r requirements.txt --no-cache-dir

# Train from pretrained weights
python train.py --img 1280 --batch 4 --epochs 300 --data car.yaml --weights yolov5l6.pt --cache --device 0
# Train from scratch
# python train.py --img 1280 --batch 4 --epochs 300 --data car.yaml --weights '' --cfg yolov5l6.yaml --cache --device 0

# python detect.py --weights yolov5s.pt --img 1024 --source ../data/test/

uname -a