# Fast Zero-Shot Image Tagging (in progress)
Implementing algorithm from paper by Zhang , et al

Paper: http://crcv.ucf.edu/papers/cvpr2016/Zhang_CVPR2016.pdf <br>
NUS-WIDE Dataset: http://lms.comp.nus.edu.sg/research/NUS-WIDE.htm

/Dataset contains compressed files for constructing dataframes for the NUS-WIDE dataset. For the raw data, download directly from the link above.

point /Dataset/downloader.py to the appropriate file containing img urls to download images.

**There are a large number of broken links in NUS-WIDE-urls.text if it is crucial to have access to all 260k images, request access from the authors of the dataset at the NUS-WIDE Dataset website.**

## Naming conventions used by authors of NUS-WIDE dataset
  - _Concepts_ are the image classes. There is some overlap in the classes corresponding to fine-grained image classification (for example there exists __animal__ and __bird__ classes).
  - _Groundtruth_ are solutions to both training and test sets for assigning concept to image.
  - _Tags_ are more general categorical assignments with a high degree of overlap between tags.
