# Warehouse-management

## Table of Contents

- [Problem Statement](#Problem-Statement)
- [Solution](#solution)
- [ML Solution](#ML-solution)
- [Blockchain Solutions](#Blockchain)
- [Running Instructions](#To-run-on-your-machine)
- [Project Links](#Important-links)

## Problem Statement 
A food delivery service has to deal with a lot of perishable raw materials which makes it all, the most important factor for such a company is to accurately forecast daily and weekly demand. Too much inventory in the warehouse means more risk of wastage, and not enough could lead to out-of-stocks - and push customers to seek solutions from your competitors. Further a lacK of communication between supplier, warehouse and client also leads to a wobbly supply chain, aggravating the situation. For food safety purposes a robust tracing technique is also required.

## Solution
A software prototype web app for demand forecasting, inventory management and food tracking using machine learning and blockchain. 

## ML solutions
With an ensemble of Random Forest Regressor and LSTM on it we acheieved sufficient accuracy.
![Final Prediction](https://github.com/old-school-kid/Warehouse-management/blob/main/Images/Final%20prediction.png)

## Blockchain
Blockchain was used for food-supply management, and finding where food comes from

## To run on your machine 

download the saved models (only few have been provided for testing purpose directly in the repo) from [here](https://drive.google.com/file/d/12tnt5IYw8O-ScwH-dc1JBkSMy3de07Lj/view?usp=sharing).
Run the following commands in the command line:
```
git clone https://github.com/old-school-kid/Warehouse-management.git
cd Warehouse-management
pip install -r requirements 
```

Start two terminal sessions type the following commands:

On terminal 1
```
python app.py
```
Allowed entries for USERNAME are SUPPLIER, RESTAURANT, WAREHOUSE. <br>
Password for all of them are 12345. <br>
Before filling in the data please refer to the dataset. Link provided below.

On terminal 2
```
export FLASK_APP=block_chain.py
flask run --port 8000
```

## Important Links 
  - [Data Set](https://www.kaggle.com/ghoshsaptarshi/av-genpact-hack-dec2018?rvi=1)
  - [Project PPt](https://docs.google.com/presentation/d/1N5q2Oo6VV6-OfUxNbGrZtgSxpJClLpjqZNC8lbzkUbs/edit?usp=sharing)

