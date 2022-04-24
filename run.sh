 cd classifier
 python textcnn.py --mode train
 echo "classifier!!!!!!!!!!!"

cd nmt
python nmt.py --mode train --nmt_direction 0-1 
python nmt.py --mode train --nmt_direction 1-0
echo "bilstm nmt done"

cd ..
python dual_training.py --n_epoch 10
echo "Rl done!!!!!!!!!!!"