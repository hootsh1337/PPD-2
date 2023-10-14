# PPD-2
Product Portfolio Dashboard

This is a mock project using streamlit & pandas in python to generate a Product Portfolio Management Dashboard.

The project is based on an altered set of similar real product data, which was applied and tested in industry.

Summary of project phases:

Phase 1 - 
Product data table import in the form of Excel, csv, or other applicable formats. 
Afterwards, the data was cleaned, unified, and formatted. 
(e.g: Entries with "-" are converted to empty values to facilitate dropping in the python script, entries with "Yes" and "Y" are unified ...etc.) 

Phase 2 - 
Create a directory structure for the different products using the naming system.
The naming system is in the form of: AAAAA/BBB/CCC/DDD/EEE 
Where each part is a subset of the previous part, for example AAAAA is the product type ..etc.
Each of these parts is a directory; so directory AAAAA has several directories BBB, and each directory BBB has several dirs CCC ..etc.
The final directory (EEE) contains all the files of the product, such as images and working drawings ..etc.

Phase 3 -
Using streamlit a dashboard is made presenting all the products and their respective codes.
Each product thumbnail can be expanded to show product details.
The dashboard features a filter, and some charts and statistics on the company's product portfolio.

![Screenshot 2023-10-14 065202](https://github.com/hootsh1337/PPD-2/assets/100040135/32684e84-8227-411a-94c7-de33ed6c1b76)

![Screenshot 2023-10-14 065350](https://github.com/hootsh1337/PPD-2/assets/100040135/7f07f4af-3005-4b16-a9d9-d5e33ff3f1ef)
