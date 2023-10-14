# Product Portfolio Dashboard

This is a simplified project using streamlit & pandas in python to generate a **Product Portfolio Management Dashboard**.
The project is based on an altered set of similar real product data, which was applied and tested in real industry.


Summary of Project Phases:
-----
**Phase 1 -**

Product data table import in the form of Excel, csv, or other applicable formats. 

Afterwards, the data was cleaned, unified, reduced, and formatted. 

-----
**Phase 2 -**

Create a directory structure for the different products utilizing the product code naming system. Where the product code is essentially a directory path.

The naming system is in the form of: AAAAA/BBB/CCC/DDD/EEE

Where each part is a subset of the previous part, for example AAAAA is the product type, DDD is the product color ..etc.

Each of these parts is a directory; so directory AAAAA has several directories BBB, and each directory BBB has several dirs CCC ..etc.

The final directory (EEE) contains all the files of the product, such as images and working drawings ..etc.

-----
**Phase 3 -**

Using streamlit a dashboard is made presenting all the products and their respective codes.

Each product thumbnail can be expanded to show product details.

The dashboard features a filter, and some charts and statistics on the company's product portfolio.

-----
![Screenshot 2023-10-14 081015](https://github.com/hootsh1337/PPD-2/assets/100040135/74dfbb24-1c9c-4280-b2ed-62a5e4ca3ebf)

-----
![Screenshot 2023-10-14 081150](https://github.com/hootsh1337/PPD-2/assets/100040135/d3adeb58-63a1-4043-b5f7-53b1fc5a5191)
