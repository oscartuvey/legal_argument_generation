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
This should create the following file:

```
Preprocessing/Rhetorical_Role_Labelling/categories.txt
```

This will be used for scraping the [Facts] and [Ratio of the decision] pairs onto the unlabelled data.

### Preprocessing

The method for scraping the [Facts] and [Ratio of the decision] pairs will depend upon the data.

To scrape the appropriate labels on the annotated dataset, use:

```
!python Preprocessing/Rhetorical_Role_Labelling/scrape_labelled.py
```

Else, use:

```
!python Preprocessing/Rhetorical_Role_Labelling/scrape_unlabelled.py
```



