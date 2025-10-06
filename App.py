#import joblib
#model = joblib.load('Save.pkl')
#print('Model loaded successfully')
import streamlit as st
import joblib  # Switch to joblib
import numpy as np

# Load the model with error handling
try:
    model = joblib.load('Save.pkl')
    print('Model loaded successfully!')
except Exception as e:
    print(f'Error loading model: {str(e)}')
    st.stop()

# Dictionary mapping diseases to recommendations
disease_recommendations = {
    'Common Rust': """
    **Recommendations for Common Rust:**
    - **Cultural Practices**: Plant resistant maize varieties. Ensure proper spacing to improve air circulation and reduce humidity around plants.
    - **Chemical Control**: Apply fungicides like triazoles or strobilurins at the early stages of disease development (consult local agricultural extension for approved products).
    - **Crop Management**: Remove and destroy crop debris after harvest to reduce overwintering of the pathogen.
    - **Monitoring**: Regularly scout fields, especially during warm (15-25°C) and humid conditions.
    """,
    'Maize Dwarf Mosaic': """
    **Recommendations for Maize Dwarf Mosaic:**
    - **Cultural Practices**: Use virus-free seeds and plant resistant hybrids. Control aphid vectors by removing weeds that serve as alternate hosts.
    - **Chemical Control**: Apply insecticides to manage aphid populations if necessary (consult local guidelines).
    - **Crop Management**: Avoid late planting to reduce exposure to aphid vectors during vulnerable growth stages.
    - **Monitoring**: Inspect plants for mosaic patterns and stunting, especially in early growth stages.
    """,
    'Northern Corn Leaf Blight': """
    **Recommendations for Northern Corn Leaf Blight:**
    - **Cultural Practices**: Use resistant maize hybrids. Rotate crops with non-hosts like soybeans to reduce pathogen buildup.
    - **Chemical Control**: Apply fungicides (e.g., chlorothalonil or mancozeb) at the onset of symptoms or preventatively in high-risk areas.
    - **Crop Management**: Practice tillage to bury infected residue and reduce inoculum.
    - **Monitoring**: Look for cigar-shaped lesions on leaves, especially in cool, wet conditions.
    """,
    'Anthracnose': """
    **Recommendations for Anthracnose:**
    - **Cultural Practices**: Plant resistant varieties and rotate crops to disrupt the disease cycle.
    - **Chemical Control**: Use fungicides like azoxystrobin during early disease stages if severe.
    - **Crop Management**: Remove crop debris and practice balanced fertilization to avoid excessive nitrogen.
    - **Monitoring**: Check for black lesions on stalks and leaves, particularly in warm, wet conditions.
    """,
    'Southern Rust': """
    **Recommendations for Southern Rust:**
    - **Cultural Practices**: Use resistant hybrids and plant early to avoid peak disease periods.
    - **Chemical Control**: Apply fungicides like triazoles or strobilurins during early disease development.
    - **Crop Management**: Ensure good field drainage and avoid dense planting to reduce humidity.
    - **Monitoring**: Scout for orange pustules on leaves during hot, humid weather.
    """,
    'Fusarium Stalk Rot': """
    **Recommendations for Fusarium Stalk Rot:**
    - **Cultural Practices**: Use resistant hybrids and maintain balanced soil fertility to reduce plant stress.
    - **Crop Management**: Rotate crops and avoid continuous maize planting. Ensure proper irrigation to prevent drought stress.
    - **Chemical Control**: Fungicides are generally not effective; focus on cultural practices.
    - **Monitoring**: Check for pithy, discolored stalks, especially after flowering in stressed plants.
    """,
    'Downy Mildew': """
    **Recommendations for Downy Mildew:**
    - **Cultural Practices**: Plant resistant varieties and ensure well-drained soils.
    - **Chemical Control**: Apply systemic fungicides like metalaxyl at early stages if needed.
    - **Crop Management**: Avoid overhead irrigation and remove infected plants to reduce spread.
    - **Monitoring**: Look for yellowing leaves with white, downy growth on the underside in cool, wet conditions.
    """,
    'Gray Leaf Spot': """
    **Recommendations for Gray Leaf Spot:**
    - **Cultural Practices**: Use resistant maize hybrids and practice crop rotation with non-host crops.
    - **Chemical Control**: Apply fungicides like strobilurins or triazoles during early disease development.
    - **Crop Management**: Reduce residue by tillage and improve air circulation through proper spacing.
    - **Monitoring**: Scout for rectangular, grayish lesions on leaves during warm, humid weather.
    """,
    'Southern Corn Leaf Blight': """
    **Recommendations for Southern Corn Leaf Blight:**
    - **Cultural Practices**: Plant resistant hybrids and rotate crops to reduce pathogen survival.
    - **Chemical Control**: Use fungicides like mancozeb or azoxystrobin if disease pressure is high.
    - **Crop Management**: Remove crop debris and avoid excessive nitrogen fertilization.
    - **Monitoring**: Look for tan, irregularly shaped lesions on leaves in warm, moist conditions.
    """
}

st.title("Maize Disease Prediction")
st.write("Enter inputs below to predict maize diseases and get recommendations.")

# Use float values for min_value, max_value, and step to match the float type of value
Rain = st.number_input("Rainfall (mm)", value=0.0, min_value=0.0, max_value=1000.0, step=0.1)
Temp = st.number_input("Temperature (°C)", value=0.0, min_value=0.0, max_value=50.0, step=0.1)
Hum = st.number_input("Humidity (%)", value=0.0, min_value=0.0, max_value=100.0, step=0.1)

if st.button("Predict"):
    try:
        input_data = np.array([[Rain, Temp, Hum]])
        input_=np.array([[5.45,17.89,50.67]])
        prediction = model.predict(input_data)
        predicted_disease = prediction[0]
        print(f"Predicted Disease: {predicted_disease}")
        st.success(f"Predicted Disease: {predicted_disease}")

        # Display recommendations
        st.subheader("Recommendations")
        if predicted_disease in disease_recommendations:
            st.markdown(disease_recommendations[predicted_disease])
        else:
            st.warning("No recommendations available for this disease.")
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")