import pickle
import pickle
import streamlit as Slit

model = pickle.load(open('C:/Users/PRINCESS BALOGUN/Downloads/Assignment6/bestmodel.pkl', 'rb'))

def main():
    Slit.title('Customer Churn Prediction')
    # input variables
    customerID = Slit.number_input('CustomerID')
    TotalCharges = Slit.number_input('TotalCharges')
    MonthlyCharges = Slit.number_input('MonthlyCharges')
    tenure = Slit.number_input('tenure')
    Contract = Slit.number_input('Contract')
    
    

# Prediction
    if Slit.button('Predict'):
        makeprediction= model.predict((['customerID','TotalCharges','MonthlyCharges','tenure','Contract', ]))
        output=round(makeprediction[0],2)
        Slit.success('The Churn rate of this customer  is {}'.format(output))

if __name__=='__main__':
    main()
  







