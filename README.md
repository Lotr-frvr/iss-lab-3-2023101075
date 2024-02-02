# iss-lab-3-2023101075

 app.py

-> Function to store user registration details in users.txt
store_user_details(user_data):

-> Function to retrieve user registration details based on user ID and mask the password
get_user_details(user_id, mask_password=True):


-> Route to display user details based on user ID
@app.route('/user/<int:user_id>') -> IMPORTANT 
use numbers to access your details 
eg: to access the first user's details use
http://127.0.0.1:5000/user/1




-> Route for success page
@app.route('/success')
