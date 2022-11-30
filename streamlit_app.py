import streamlit as st
st.write(
  'Division of Two Real Numbers'
)
# x = st.slider('Select a numerator')
# y = st.slider('Select a denominator',min_value=1)
x = st.number_input(label='Enter first Number',step=1.,format="%.2f")
st.write('The X is ', x)
y = st.number_input(label='Enter second Number',step=1.,format="%.2f",min_value=1.0)
st.write('The Y is ', y)
st.write('Answer is', float(x) / float(y))
