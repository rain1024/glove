# Huấn luyện Glove

Bước 1: Cài đặt môi trường

Bước 2: Huấn luyện mô hình Glove  

Sửa file `train.sh`

Chạy file `train.sh`
``` 
./train.sh
```

Bước 3: Convert sang định dạng word embeddings của Flair

``` 
python -m gensim.scripts.glove2word2vec --input output/vectors.txt --output output/glove.txt
```