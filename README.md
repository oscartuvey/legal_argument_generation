# Argument Generation from Legal Facts

## Usage

### Training

To train the model on an annotated dataset, use: 

```
!python Train.py
```

Further labels can be assigned to unannotated data utilizing the model:

```
!python Infer.py
```

The method for scraping the [Facts] and [Ratio of the decision] pairs will depend upon the data.

To scrape the appropriate labels on the annotated dataset, use:

```
!python scrape_labelled.py
```

Else, use:

```
!python scrape_unlabelled.py
```



