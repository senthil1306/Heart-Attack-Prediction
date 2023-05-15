from sklearn.preprocessing import StandardScaler
import streamlit as st
import numpy as np
import pickle as pkl
from sklearn.preprocessing import MinMaxScaler


scal=MinMaxScaler()

#Load the saved pickle model
with open("RFModel.pkl", 'rb') as file:
    model = pkl.load(file)

st.set_page_config(page_title=" Heart Disease Detection App",page_icon="⚕️",layout="centered",initial_sidebar_state="expanded")

#@st.cache()
 
     
def prediction(age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal ):   

    
    # Pre-processing categorical columnns from user input
    if sex=="male":
         sex=0 
    else: 
        sex= 1

    if cp=="Typical angina":
        cp=0
    elif cp=="Atypical angina":
        cp=1
    elif cp=="Non-anginal pain":
        cp=2
    elif cp=="Asymptomatic":
        cp=3
    
    if exang=="Yes":
        exang=1
    elif exang=="No":
        exang=0
 
    if fbs=="Yes":
        fbs=1
    elif fbs=="No":
        fbs=0
 
    if slope=="Upsloping: better heart rate with excercise(uncommon)":
        slope=0
    elif slope=="Flatsloping: minimal change(typical healthy heart)":
          slope=1
    elif slope=="Downsloping: signs of unhealthy heart":
        slope=2  
 
    if thal=="fixed defect: used to be defect but ok now":
        thal=6
    elif thal=="reversable defect: no proper blood movement when excercising":
        thal=7
    elif thal=="normal":
        thal=2.31

    if restecg=="Nothing to note":
        restecg=0
    elif restecg=="ST-T Wave abnormality":
        restecg=1
    elif restecg=="Possible or definite left ventricular hypertrophy":
        restecg=2
    #preprocessing user  input
    user_input=[[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
    print(user_input)
    #user_input=np.array(user_input)
    #user_input=user_input.reshape(1,-1)
    #user_input=scal.fit_transform(user_input)
    prediction = model.predict(user_input)
    print(user_input)
    if prediction == 0:
        st.write("Warning!!! You have a high risk of getting a heart disease!")
    else:
        st.write("You have a lower risk of getting a heart disease!")
##Creating the main page
def main(): 

    html_temp = """ 
    <div style ="background-color:aliceblue;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Cardiovascular Disease Prediction </h1> 
    </div> 
    """

    #st.title("Heart Prediction App")
        
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

    # following lines create boxes in which user can enter data required to make prediction
    age=st.selectbox ("Age",range(1,121,1))
    sex = st.radio("Select Gender: ",('male', 'female'))
    cp = st.selectbox('Chest Pain Type',("Typical angina","Atypical angina","Non-anginal pain","Asymptomatic")) 
    trestbps=st.selectbox('Resting Blood Sugar',range(1,500,1))
    restecg=st.selectbox('Resting Electrocardiographic Results',("Nothing to note","ST-T Wave abnormality","Possible or definite left ventricular hypertrophy"))
    chol=st.selectbox('Serum Cholesterol in mg/dl',range(1,1000,1))
    fbs=st.radio("Fasting Blood Sugar higher than 120 mg/dl", ['Yes','No'])
    thalach=st.selectbox('Maximum Heart Rate Achieved',range(1,300,1))
    exang=st.selectbox('Exercise Induced Angina',["Yes","No"])
    oldpeak=st.number_input('Oldpeak')
    slope = st.selectbox('Heart Rate Slope',("Upsloping: better heart rate with excercise(uncommon)","Flatsloping: minimal change(typical healthy heart)","Downsloping: signs of unhealthy heart"))
    ca=st.selectbox('Number of Major Vessels Colored by Flourosopy',range(0,5,1))
    thal=st.selectbox('Thalium Stress Result',range(1,8,1))
    result =""
    

    if st.button("Predict"): 

        prediction(age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal)
        
        #if result == 0:
        #    st.write('Warning! You have high risk of getting a heart attack!')
        #else:
        #    st.write("You have a lower risk of getting a heart disease!")

      

st.sidebar.subheader("About App")

st.sidebar.info("This web application can assess your risk of developing cardiovascular disease by evaluating various factors that may contribute to your risk, such as age, gender, family history, lifestyle habits, and medical history.")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check ")
st.sidebar.info("Don't forget to rate this app")



feedback = st.sidebar.slider('How much would you rate this webpage?',min_value=0,max_value=5,step=1)

if feedback:
  st.header("Thank you for rating the app!")
  st.info("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.") 

if __name__=='__main__': 
    main()
