Project proposal:
```
tracing and visualizing diachronic semantic change 
using contextualized embeddings from BERT, with 
historical event contextualization

+ Run experiments on  Multi-senses vs single-averaged sense (WITHOUT testing on different types of semantic change)
+ future semantic change prediction

Tracing: putting in relation of multiple quantified (non-binary) measurements  (of semantic change)
```

Underlying core-core part here is: get quantified measurements of semantic change from bert

For which we need:
- Multiple Bert models (diachronically segmented)
- code to extract measurements from them

histBERT would seem to be most obvious choice for getting multiple diachronic BERT models
https://github.com/2022-2023-M2-NLP-Group-5/diachronicBert

histBERT authors DO provide their trained models for download:
https://drive.google.com/drive/folders/1E4jZPzCatmS73-Mg7iacq4SXROSPsC6b

For re-training/training alternative models...

Full COHA requires purchase ($375 minimum) but it seems a subset can be downloaded free:
https://www.corpusdata.org/formats.asps

Plaintext sample is here (9 mb zip, 25 mb extracted):
https://www.corpusdata.org/coha/samples/text.zip


