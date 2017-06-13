# GDCWebApp4Galaxy
This project contains the XML structure of the GDCWebApp asynchronous Data Source tool for Galaxy.
It is also available on the Galaxy ToolShed under the name 'gdcwebapp'.

## What is GDCWebApp
GDCWebApp is a web service to automatically query, filter, extract and convert genomic data and clinical information from the [Genomic Data Commons portal](https://gdc.cancer.gov/) (GDC) to BED format. It is able to operate on all data types for each programs (TCGA and TARGET) available on GDC.

The service is available at [http://bioinf.iasi.cnr.it/gdcwebapp/](http://bioinf.iasi.cnr.it/gdcwebapp/)

## Galaxy Data Sources development documentation
[https://galaxyproject.org/admin/internals/data-sources/](https://galaxyproject.org/admin/internals/data-sources/)

## Notes
This tool requires a patch of the 'async.py' module that is responsible of the management of asynchronous requests.
The patch avoid the system to crash if a collection is defined as a possible output in the tool XML schema in the case of asynchronous data sources. 
It also checks if only one output is defined (required for the async procedure). If more then one outputs are defined (except for collections), it throws an exception.

To apply the patch, just replace the 'async.py' file under the folder '/lib/galaxy/webapps/galaxy/controllers/' starting from the root folder of your Galaxy instance or wait for the integration of this patch into the next Galaxy release.
