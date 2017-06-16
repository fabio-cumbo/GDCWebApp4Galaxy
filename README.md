# GDCWebApp4Galaxy
This project contains the XML structure of the GDCWebApp asynchronous Data Source tool for Galaxy.
It is also available on the Galaxy ToolShed under the name [gdcwebapp](https://toolshed.g2.bx.psu.edu/view/fabio/gdcwebapp/7f55f83f72da).

## What is GDCWebApp
GDCWebApp is a web service to automatically query, filter, extract and convert genomic data and clinical information from the [Genomic Data Commons portal](https://gdc.cancer.gov/) (GDC) to BED format. It is able to operate on all data types for each tumor and program available on GDC.

GDC hosts genomic experiments about patients affected by different kinds of tumors. These are organized in two main constantly updated programs:
1. TCGA: The Cancer Genome Atlas
2. TARGET: Therapeutically Applicable Research To Generate Effective Treatments

The TCGA program contains data about 33 different tumors listed in the table reported below.

| Disease Abbreviation | Study Name                                                       |
|----------------------|------------------------------------------------------------------|
| BRCA                 | Breast Invasive Carcinoma                                        |
| GBM                  | Glioblastoma Multiforme                                          |
| OV                   | Ovarian Serous Cystadenocarcinoma                                |
| LUAD                 | Lung Adenocarcinoma                                              |
| UCEC                 | Uterine Corpus Endometrial Carcinoma                             |
| KIRC                 | Kidney Renal Clear Cell Carcinoma                                |
| HNSC                 | Head and Neck Squamous Cell Carcinoma                            |
| LGG                  | Brain Lower Grade Glioma                                         |
| THCA                 | Thyroid Carcinoma                                                |
| LUSC                 | Lung Squamous Cell Carcinoma                                     |
| PRAD                 | Prostate Adenocarcinoma                                          |
| SKCM                 | Skin Cutaneous Melanoma                                          |
| COAD                 | Colon Adenocarcinoma                                             |
| STAD                 | Stomach Adenocarcinoma                                           |
| BLCA                 | Bladder Urothelial Carcinoma                                     |
| LIHC                 | Liver Hepatocellular Carcinoma                                   |
| CESC                 | Cervical Squamous Cell Carcinoma and Endocervical Adenocarcinoma |
| KIRP                 | Kidney Renal Papillary Cell Carcinoma                            |
| SARC                 | Sarcoma                                                          |
| LAML                 | Acute Myeloid Leukemia                                           |
| ESCA                 | Esophageal carcinoma                                             |
| PAAD                 | Pancreatic Adenocarcinoma                                        |
| PCPG                 | Pheochromocytoma and Paraganglioma                               |
| READ                 | Rectum Adenocarcinoma                                            |
| TGCT                 | Testicular Germ Cell Tumors                                      |
| THYM                 | Thymoma                                                          |
| KICH                 | Kidney Chromophobe                                               |
| ACC                  | Adrenocortical carcinoma                                         |
| MESO                 | Mesothelioma                                                     |
| UVM                  | Uveal Melanoma                                                   |
| DLBC                 | Lymphoid Neoplasm Diffuse Large B-cell Lymphoma                  |
| UCS                  | Uterine Carcinosarcoma                                           |
| CHOL                 | Cholangiocarcinoma                                               |

Additionally, the following table contains the list of tumors contained in the TARGET program:

| Disease Abbreviation | Study Name                       |
|----------------------|----------------------------------|
| NBL                  | Neuroblastoma                    |
| AML                  | Acute Myeloid Leukemia           |
| WT                   | Wilms Tumor                      |
| OS                   | Osteosarcoma                     |
| RT                   | Rhabdoid Tumors                  |
| CCSK                 | Clear Cell Sarcoma of the Kidney |

For each of the previously listed tumors, at least one of the following data types are available:
- Clinical and Biospecimen Supplements
- Gene Expression Quantification
- Masked Copy Number Segment
- Methylation Beta Value
- Isoform Expression Quantification
- miRNA Expression Quantification
- Masked Somatic Mutation

It is worth noting that all the genomic experiments available on GDC refer to the human genome version 38.

## How to use GDCWebApp in Galaxy

#### [Step 1]: Search and install GDCWebApp from the Galaxy Tool Shed
First of all the user need to install the [gdcwebapp](https://toolshed.g2.bx.psu.edu/view/fabio/gdcwebapp/7f55f83f72da) tool available on the Galaxy Tool Shed.

![alt text](https://github.com/fabio-cumbo/GDCWebApp4Galaxy/raw/master/images/gdcwebapp_step1.1.png "Search GDCWebApp in the Galaxy Tool Shed")

---

![alt text](https://github.com/fabio-cumbo/GDCWebApp4Galaxy/raw/master/images/gdcwebapp_step1.2.png "Overview of GDCWebApp requirements and dependencies")

---

![alt text](https://github.com/fabio-cumbo/GDCWebApp4Galaxy/raw/master/images/gdcwebapp_step1.3.png "Install GDCWebApp")

---

![alt text](https://github.com/fabio-cumbo/GDCWebApp4Galaxy/raw/master/images/gdcwebapp_step1.4.png "Locate GDCWebApp under the Tools menu")

#### [Step 2]: Play with GDCWebApp
Clicking on the GDCWebApp entry under the tools menu, the user will be automatically redirected to the GDCWebApp service page in which he have to select at least one data set starting from the selection of a program, followed by a tumor and a data type, and an optional selection of multiple clinical and biospecimen attributes used to filter out a subset of the experiments corresponding to the previous program, tumor, and data type selection.

![alt text](https://github.com/fabio-cumbo/GDCWebApp4Galaxy/raw/master/images/gdcwebapp_step2.png "Play with GDCWebApp")

In this particular example, the output of this query will consists of two compressed archives contained respectively:
1. the original Masked Somatic Mutation experiments extracted from GDC;
2. a list of BED files corresponding to the original data, one for each experiment.
It is worth noting that, in this particular example, all the experiments contained in these archives are related to MALE patients with BLACK OR AFRICAN AMERICAN race.

Please refer to the following link for a detailed documentation about clinical and biospecimen attributes:
- [https://gdc.cancer.gov/clinical-data-elements](https://gdc.cancer.gov/clinical-data-elements)
- [https://gdc.cancer.gov/about-data/data-harmonization-and-generation/clinical-data-harmonization](https://gdc.cancer.gov/about-data/data-harmonization-and-generation/clinical-data-harmonization)
- [https://gdc.cancer.gov/about-data/data-harmonization-and-generation/biospecimen-data-harmonization](https://gdc.cancer.gov/about-data/data-harmonization-and-generation/biospecimen-data-harmonization)

#### [Step 3]: Return to Galaxy
Clicking on the ```Submit to Galaxy``` button, the user will be redirected to his Galaxy instance in which will be automatically created a job that will continue to rum until GDCWebApp will communicate to Galaxy that the requested data sets are ready to be downloaded.
This job could requires some minutes to complete, it depends on the number of data sets requested on GDCWebApp. These data sets have to to be downloaded from GDC and, optionally, converted to BED. This is the reason why the procedure is asynchronous.

![alt text](https://github.com/fabio-cumbo/GDCWebApp4Galaxy/raw/master/images/gdcwebapp_step3.png "Job running")

#### [Step 4]: GDCWebApp Job Tracker
While the job is running we could monitor its progress using the GDCWebApp Job Tracker bu submitting the Job Key on the official [GDCWebApp page](http://bioinf.iasi.cnr.it/gdcwebapp/). The user will be redirected to the tracking page in which the current status of the job is reported.

![alt text](https://github.com/fabio-cumbo/GDCWebApp4Galaxy/raw/master/images/gdcwebapp_step4.png "GDCWebApp Job Tracking")

#### [Step 5]: Job completed
When the job will be completed, two files will be created in the history. Both of them contain an overview of the GDCWebApp request, one in a human-readable format (TXT) and the other one (XML) is required to resubmit the request on GDCWebApp, for reproducibility purpose (not yet available on Galaxy in the case of data source tools). 

![alt text](https://github.com/fabio-cumbo/GDCWebApp4Galaxy/raw/master/images/gdcwebapp_step5.1.png "GDCWebApp results in Galaxy History")

---

![alt text](https://github.com/fabio-cumbo/GDCWebApp4Galaxy/raw/master/images/gdcwebapp_step5.2.png "Human-readable request overview")

---

It will be also created a list of collections containing the data requested on GDCWebApp (i.e. the output of the [Step 2]). Considering the previous example, ```Data Set 1 [GDC]``` will contains the original Masked Somatic Mutation data as MAF files retrieved from GDC, and ```Data Set 1 [BED] will contains the same data in ```Data Set 1 [GDC]``` converted in BED format.

![alt text](https://github.com/fabio-cumbo/GDCWebApp4Galaxy/raw/master/images/gdcwebapp_step5.3.png "List of Collections")

## GDCWebApp availability
The service is online at [http://bioinf.iasi.cnr.it/gdcwebapp/](http://bioinf.iasi.cnr.it/gdcwebapp/)

## Galaxy Data Sources development documentation
[https://galaxyproject.org/admin/internals/data-sources/#asynchronous-data-depositing](https://galaxyproject.org/admin/internals/data-sources/#asynchronous-data-depositing)

## Notes
This tool requires a patch of the ```async.py``` module that is responsible of the management of asynchronous requests.
The patch avoid the system to crash if a collection is defined as a possible output in the tool XML schema in the case of asynchronous data sources. 
It also checks if only one output is defined (required for the async procedure). If more then one outputs are defined (except for collections), it throws an exception.

This patch has been committed to the official Galaxy repository and will be integrated in the next release.
Please check the status of this pull request to know if it is already available for the version of your Galaxy instance.
[https://github.com/galaxyproject/galaxy/pull/4198](https://github.com/galaxyproject/galaxy/pull/4198)

Alternatively, you can apply the patch replacing the ```async.py``` file under the folder ```/lib/galaxy/webapps/galaxy/controllers/``` starting from the root folder of your Galaxy instance.

