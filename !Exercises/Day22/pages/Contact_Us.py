import streamlit as st, time
from send_email import send_email

with open("topics.csv") as file:
    topics = file.readlines()[1:]
    topics = [topic.strip() for topic in topics]

with st.form(key="contact_form"):
    email = st.text_input("Your Email Address")
    topic_dropdown = st.selectbox("Topic", options=topics, placeholder="Select a topic")
    message = st.text_area("Text")
    submit = st.form_submit_button("Submit")

    final_message = f"""\
Subject: Sent from The Best Company \"Contact Us\" page

Topic: {topic_dropdown}
From: {email}
{message}
"""
    if submit:
        send_email(final_message)
        success = st.success("Email has been successfuly sent!") # Display the alert
        time.sleep(3) # Wait for 3 seconds
        success.empty() # Clear the alert