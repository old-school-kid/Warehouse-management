# Warehouse-management

## Problem Statemnt 
A food delivery service has to deal with a lot of perishable raw materials which makes it all, the most important factor for such a company is to accurately forecast daily and weekly demand. Too much inventory in the warehouse means more risk of wastage, and not enough could lead to out-of-stocks - and push customers to seek solutions from your competitors. Further a lacK of communication between supplier, warehouse and client also leads to a wobbly supply chain, aggravating the situation. For food safety purposes a robust tracing technique is also required.

## what are we 
A software prototype web app for demand forecasting, inventory management and food tracking using machine learning and blockchain. 

## ML solutions
With an ensemble of Random Forest Regressor and LSTM on it we acheieved sufficient accuracy.

## Blockchain
Blockchain was used for food-supply management, and finding where food comes from

## To run on your machine 
Run the following commands in the command line:
```
pip3 install wheel flask pyrebase numpy joblib 
```

On two terminal sessions type the following commands:

On terminal 1
```
python app.py
```

On terminal 2
```
export FLASK_APP=block_chain.py
flask run --port 8000
```

