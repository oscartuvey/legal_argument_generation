# Argument Generation from Legal Facts

## Usage

### Training

To train the model on an annotated dataset, use: 

```
!python Preprocessing/Rhetorical_Role_Labelling/Train.py
```

Further labels can be assigned to unannotated data utilizing the model:

```
!python Preprocessing/Rhetorical_Role_Labelling/Infer.py
```

The method for scraping the [Facts] and [Ratio of the decision] pairs will depend upon the data.

To scrape the appropriate labels on the annotated dataset, use:

```
!python Preprocessing/Rhetorical_Role_Labelling/scrape_labelled.py
```

Else, use:

```
!python Preprocessing/Rhetorical_Role_Labelling/scrape_unlabelled.py
```



