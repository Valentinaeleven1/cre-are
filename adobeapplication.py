# Importing Required Modules & libraries
from tkinter import *
from tkinter.ttk import *
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

text_list = []
project_list = []

def clear_entry():
    idea_text_box.delete(0, END)

def refresh_idea():
    ideas_listbox.delete(0, 'end')

    if os.path.exists("saved_text.txt"):
        with open("saved_text.txt", 'r') as file:
        # iterate through each line in the file
            for line in file:
                idea_ = line.strip()
                ideas_listbox.insert('end',idea_ )
                text_list.append(idea_)

def refresh_project():
    project_listbox.delete(0, 'end')

    if os.path.exists("saved_project.txt"):
        with open("saved_project.txt", 'r') as file:
        # iterate through each line in the file
            for line in file:
                project_ = line.strip()
                project_listbox.insert('end', project_)
                project_list.append(project_)

def add_text_idea():
    text = idea_name_var.get()
    if text:
        send_slack_message('#general', f"New idea created - {text}!")
        ideas_listbox.delete(0, 'end')
        if text:
            text_list.append(text)
            # Entry.delete(0, root.END)

        with open("saved_text.txt", "w") as file:
            for text in text_list:
                file.write(text + "\n")
                ideas_listbox.insert('end', text)

def add_project_idea_p1():
    text = idea_name_var.get()
    if text:
        send_slack_message('#general', f"Now working on project - {text}! with a P1 priority")
        text = text + '--P1'
        project_listbox.delete(0, 'end')
        if text:
            project_list.append(text)
            # Entry.delete(0, root.END)

        with open("saved_project.txt", "w") as file:
            for text in project_list:
                file.write(text + "\n")
                project_listbox.insert('end', text)

def add_project_idea_p2():
    text = idea_name_var.get()
    if text:
        send_slack_message('#general', f"Now working on project - {text}! with a P2 priority")
        text = text + '--P2'
        project_listbox.delete(0, 'end')
        if text:
            project_list.append(text)
            # Entry.delete(0, root.END)

        with open("saved_project.txt", "w") as file:
            for text in project_list:
                file.write(text + "\n")
                project_listbox.insert('end', text)


def add_project_idea_p3():
    text = idea_name_var.get()
    if text:
        send_slack_message('#general', f"Now working on project - {text}! with a P3 priority")
        text = text + '--P3'
        project_listbox.delete(0, 'end')
        if text:
            project_list.append(text)
            # Entry.delete(0, root.END)

        with open("saved_project.txt", "w") as file:
            for text in project_list:
                file.write(text + "\n")
                project_listbox.insert('end', text)

# Sends a message to a Slack channel.
def send_slack_message(channel, text):
    try:
        client.chat_postMessage(channel=channel, text=text)
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")



SLACK_TOKEN = os.environ['SLACK_TOKEN']
client = WebClient(token=SLACK_TOKEN)

root = Tk()

root.configure(bg="orange")
root.title("CRE-ARE")
root.geometry("1100x5000+100+100")

label_font =("Arial", 14, "bold italic")
root.label_frame = Label(root, text="My Recent Ideas",font=label_font)
root.label_frame.place(x=20, y=60, width=200, height=20)
root.label_frame.configure(anchor="center", justify="center")

# Set up the listbox to show existing ideas.
ideas_listbox = Listbox(root)
ideas_listbox.pack(pady=20)
ideas_listbox.place(x=20, y=81, width=200, height=100)



label_font =("Arial", 14, "bold italic")
root.label_frame = Label(root, text="Projects in Process",font=label_font)
root.label_frame.place(x=800, y=60, width=200, height=20)
root.label_frame.configure(anchor="center", justify="center")


# Set up the listbox to show existing ideas.
project_listbox = Listbox(root)
project_listbox.pack(pady=20)
project_listbox.place(x=800, y=81, width=200, height=100)


# root.list_project_frame = LabelFrame(root, text="Projects in Process")
# root.list_project_frame.place(x=800, y=60, width=150, height=300)



# Creating a message label.
# Creating a font.
label_font =("Arial", 18, "bold italic")
root.label_message = Label(root, text="Welcome Creator !\n Begin with your important ideas over here!", font=label_font)
root.label_message.place(x=330, y=30)
# Set the anchor and justify attributes to center the text.
root.label_message.configure(anchor="center", justify="center")
# Creating a text entry widget while creating an object and setting it equal to the Entry keyword.
# Placing the entry box in place by using the method ".pack".
idea_name_var = StringVar()
idea_text_box = Entry(root,textvariable=idea_name_var)
idea_text_box.place(x=370, y=90, width=300, height=60)

# Creating a button for the text entry.
root.add_button = Button(root, text="Add Idea to a List", command=add_text_idea)
root.add_button.place(x=370, y=150)

clear_button = Button(root, text="Clear", command=clear_entry)
clear_button.place(x=370, y=180)

root.save_button = Button(root, text="P1", command=add_project_idea_p1)
root.save_button.place(x=575,y=150)

root.save_button = Button(root, text="P2", command=add_project_idea_p2)
root.save_button.place(x=575,y=180)

root.save_button = Button(root, text="P3", command=add_project_idea_p3)
root.save_button.place(x=575,y=210)

root.text_display= Text(root)


refresh_idea()
refresh_project()
root.mainloop()

