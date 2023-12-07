import random
import difflib
import webbrowser

# Function to perform autocorrection
def autocorrect_sentence(sentence, word_list):
    corrected_words = [get_closest_match(word, word_list) or word for word in sentence.split()]
    return ' '.join(corrected_words)

# Function to get the closest match for a word
def get_closest_match(word, word_list):
    matches = difflib.get_close_matches(word, word_list)
    if matches and difflib.SequenceMatcher(None, word, matches[0]).ratio() > 0.8:
        return matches[0]
    return None

# Function to respond to greetings
def respond_to_greeting(user_input):
    greetings = ['hi', 'hello', 'hru']
    user_input = user_input.lower()
    for greeting in greetings:
        if greeting in user_input:
            if greeting == 'hru':
                return "I'm doing well, thank you!"
            return "Hi! How can I help you today?"

# Function to provide a random quote of the day
def get_quote_of_the_day():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    return random.choice(quotes)

# Function to handle course-related queries
def handle_courses(user_input):
    if 'courses' in user_input:
        return "Sure! Are you interested in undergraduate or graduate courses? Please type 'undergraduate' or 'graduate.'"

    if 'undergraduate' in user_input:
        # Ask for confirmation only if misspelled
        correction_response = input("Wiu Chatbot: Did you mean 'undergraduate'? (yes/no) ").lower()
        if correction_response == 'yes':
            webbrowser.open('https://www.wiu.edu/academics/')
            return "Here are the undergraduate courses. Let me know if you have more questions."
    
    elif 'graduate' in user_input:
        # Ask for confirmation only if misspelled
        correction_response = input("Wiu Chatbot: Did you mean 'graduate'? (yes/no) ").lower()
        if correction_response == 'yes':
            webbrowser.open('https://www.wiu.edu/graduate_studies/programs_of_study/')  
            return "Here are the graduate courses. Let me know if you have more questions."

# Function to handle university-related queries
def handle_university(user_input):
    university_keywords = ['about university', 'tell me about wiu']
    for keyword in university_keywords:
        if keyword in user_input:
            webbrowser.open('https://www.wiu.edu/about/')
            return "Sure! Here is information about Western Illinois University. Let me know if you have more questions."

# Function to handle directions-related queries
def handle_directions(user_input):
    directions_keywords = ['directions', 'driving directions']
    for keyword in directions_keywords:
        if keyword in user_input:
            webbrowser.open('https://www.wiu.edu/about/location.php')
            return "Sure! Here are the directions to Western Illinois University. Let me know if you have more questions."

# Function to handle faculty-related queries for Computer Science
def handle_computer_science_faculty(user_input):
    cs_graduate_keywords = ['cs graduate faculty', 'computer science graduate faculty']
    cs_undergraduate_keywords = ['cs undergraduate faculty', 'computer science undergraduate faculty']
    
    for keyword in cs_graduate_keywords:
        if keyword in user_input:
            webbrowser.open('https://www.wiu.edu/graduate_studies/catalog/computerscience.php')
            return "Sure! Here is information about Computer Science graduate faculty. Let me know if you have more questions."

    for keyword in cs_undergraduate_keywords:
        if keyword in user_input:
            webbrowser.open('https://www.wiu.edu/cbt/computer_science/contact.php')
            return "Sure! Here is information about Computer Science undergraduate faculty. Let me know if you have more questions."

# Function to handle professors-related queries
def handle_professors(user_input):
    professors_keywords = ['professors']
    for keyword in professors_keywords:
        if keyword in user_input:
            print("Wiu Chatbot: Are you interested in CS undergraduate professors or CS graduate professors?")
            user_response = input("Leatherneck: ").lower()
            
            if 'graduate' in user_response:
                webbrowser.open('https://www.wiu.edu/graduate_studies/catalog/computerscience.php')
                return "Sure! Here is information about Computer Science graduate professors. Let me know if you have more questions."

            elif 'undergraduate' in user_response:
                webbrowser.open('https://www.wiu.edu/cbt/computer_science/contact.php')
                return "Sure! Here is information about Computer Science undergraduate professors. Let me know if you have more questions."

# Function to handle other facility-related queries
def handle_other_facilities(user_input):
    other_facilities_keywords = ['other facilities', 'facilities']
    for keyword in other_facilities_keywords:
        if keyword in user_input:
            webbrowser.open('https://www.wiu.edu/graduate_studies/catalog/campus_and_facilities/index.php')
            return "Sure! Here is information about other facilities at Western Illinois University. Let me know if you have more questions."

# Function to handle rec-related queries
def handle_rec(user_input):
    rec_keywords = ['rec', 'campus recreation']
    for keyword in rec_keywords:
        if keyword in user_input:
            webbrowser.open('https://www.wiu.edu/student_success/campus_recreation/index.php')
            return "Sure! Here is information about campus recreation at Western Illinois University. Let me know if you have more questions."

# Function to handle dorms-related queries
def handle_dorms(user_input):
    dorms_keywords = ['dorms', 'residence halls']
    for keyword in dorms_keywords:
        if keyword in user_input:
            webbrowser.open('https://www.wiu.edu/student_success/housing/residence_halls/')
            return "Sure! Here is information about residence halls at Western Illinois University. Let me know if you have more questions."

# Function to handle calendar-related queries
def handle_calendar(user_input):
    calendar_keywords = ['calendar']
    for keyword in calendar_keywords:
        if keyword in user_input:
            webbrowser.open('https://www.wiu.edu/wiucalendar/')
            return "Sure! Here is the academic calendar for Western Illinois University. Let me know if you have more questions."

# Main function for the Wiu Chatbot
def wiu_chatbot():
    while True:
        user_input = input("Leatherneck: ")
        
        # Check for exit condition
        if user_input.lower() == 'bye':
            print("Wiu Chatbot: Goodbye! Thank you!")
            break

        # Autocorrect the user input
        words_to_check = ['hi', 'hello', 'hru', 'undergraduate', 'graduate', 'directions', 'cs', 'computer', 'faculty', 'professors', 'other', 'rec', 'dorms', 'calendar']
        corrected_input = autocorrect_sentence(user_input, words_to_check)

        # Respond to greetings
        greeting_response = respond_to_greeting(corrected_input)

        # Provide a random quote of the day
        if 'quote' in user_input:
            print("Wiu Chatbot:", get_quote_of_the_day())
        else:
            # Handle course-related queries
            courses_response = handle_courses(corrected_input)
            if courses_response:
                print("Wiu Chatbot:", courses_response)
            else:
                # Handle university-related queries
                university_response = handle_university(corrected_input)
                if university_response:
                    print("Wiu Chatbot:", university_response)
                else:
                    # Handle directions-related queries
                    directions_response = handle_directions(corrected_input)
                    if directions_response:
                        print("Wiu Chatbot:", directions_response)
                    else:
                        # Handle faculty-related queries for Computer Science
                        cs_faculty_response = handle_computer_science_faculty(corrected_input)
                        if cs_faculty_response:
                            print("Wiu Chatbot:", cs_faculty_response)
                        else:
                            # Handle professors-related queries
                            professors_response = handle_professors(corrected_input)
                            if professors_response:
                                print("Wiu Chatbot:", professors_response)
                            else:
                                # Handle other facility-related queries
                                other_facilities_response = handle_other_facilities(corrected_input)
                                if other_facilities_response:
                                    print("Wiu Chatbot:", other_facilities_response)
                                else:
                                    # Handle rec-related queries
                                    rec_response = handle_rec(corrected_input)
                                    if rec_response:
                                        print("Wiu Chatbot:", rec_response)
                                    else:
                                        # Handle dorms-related queries
                                        dorms_response = handle_dorms(corrected_input)
                                        if dorms_response:
                                            print("Wiu Chatbot:", dorms_response)
                                        else:
                                            # Handle calendar-related queries
                                            calendar_response = handle_calendar(corrected_input)
                                            if calendar_response:
                                                print("Wiu Chatbot:", calendar_response)
                                            elif greeting_response:
                                                print("Wiu Chatbot:", greeting_response)
                                            else:
                                                # Default response when the chatbot can't understand the input
                                                print("Wiu Chatbot: Sorry, I didn't understand that. How can I help you today?")

wiu_chatbot()
