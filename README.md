# Stock Prophet :moneybag:
### Week 11 MLE Assignment

The goal of this project is to deploy a stock prediction model as a RESTful API using FastAPI to AWS EC2, and make it available (i.e., public) to end users. 

# Connect :electric_plug:

Run this CURL command in your terminal:

```
curl \
--header "Content-Type: application/json" \
--request POST \
--data '{"ticker":"MSFT", "days":7}' \
http://35.93.153.122:8000/predict

```

