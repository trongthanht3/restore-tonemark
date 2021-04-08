# Vietnamese Diacritics Restoration

This is a Vietnamese Diacritics Restoration tool based on SVMs.
This is a fork version for python3. It's has a lot of bug but still working.

## Usage

"train" and "predict" directory, you should put LIBLINEAR Libary, "liblinear.so.3" under the "src" directory.

### Train

#### Make corpus
```sh
# make no syllable corpus
% cat corpus.txt | python stdin2delete_tonemark.py > resource/viet_corpus_no_tonemark.txt
```

#### Training
Firstly, you edit config.ini.

```sh
% emacs config.ini
```

```conf
[settings]
path1 = /Users/takahashi/restore-tonemark/train/resource/VNTQcorpus_small.txt
path2 = /Users/takahashi/restore-tonemark/train/resource/VNTQcorpus_small_no_tone_mark.txt
preserve_dir_path = /Users/takahashi/restore-tonemark/train/models
window_size = 2
```

```sh
# training
% cd train
% python train.py
```

### Predict

```sh
% emacs config.ini
```

```conf
[settings]
path1 = /Users/takahashi/restore-tonemark/train/resource/VNTQcorpus_small.txt
path2 = /Users/takahashi/restore-tonemark/train/resource/VNTQcorpus_small_no_tone_mark.txt
preserve_dir_path = /Users/takahashi/restore-tonemark/train/models
model_dir = /Users/takahashi/restore-tonemark/train/models
window_size = 2

```sh
% cd predict
% python predict.py < echo "Toi la sinh vien" # cat input.txt
```
