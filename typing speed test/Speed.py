from tkinter import Label, Tk, Entry, Button
from random import choice
import tkinter.messagebox
one = "Engineers as practitioners of engineering\n are people who invent design\n analyze build and test machines\n " \
      "systems structures and materials to fulfill\n objectives and requirements while\n considering the limitations " \
      "imposed by practicality regulation\nsafety and cost. The work of engineers forms the\n link between " \
      "scientific " \
      "discoveries and their subsequent applications \nto human and business needs and quality of life. "

two = "A virtual assistant (typically abbreviated to VA) is generally\n self-employed and provides professional " \
      "administrative\n technical or creative assistance to clients remotely from a home office. "

three = "Closed captions were created for deaf or hard of hearing\n individuals to assist in comprehension." \
        " They can also " \
        "\nbe used as a tool by those learning to read\n learning to speak a non-native language or in an " \
        "environment\n " \
        "where " \
        "the audio is difficult to hear or is intentionally muted "

four = "A teacher's professional duties may extend beyond formal teaching.\n Outside of the classroom teachers may " \
       "accompany students on field trips\n supervise study halls help with the organization of school functions\n " \
       "and serve as supervisors for extracurricular activities.\n In some education systems teachers may have " \
       "\nresponsibility for student discipline. "

five = "Business casual is an ambiguously defined dress code that\n has been " \
       "adopted by many professional and white-collar " \
       "\nworkplaces in Western countries. It entails neat yet casual " \
       "attire and\n is generally more casual than informal " \
       "attire but more formal than casual\n or smart casual attire." \
       " Casual Fridays preceded widespread\n acceptance of " \
       "business casual attire in many offices. "

six = "A paralegal is a person trained in legal matters who performs\n tasks requiring knowledge of the law and legal " \
      "procedures. \nA paralegal is not a lawyer but can be employed by a law" \
      " office\n or work freelance at a company or " \
      "law office.\n Paralegals are not allowed to offer legal services directly to\n the public on their own and must " \
      "perform their\n legal work under an attorney or law firm. "

seven = "Web designers are expected to have an awareness of\n" \
        " usability and if their role involves creating mark up then\n " \
        "they are also expected to be up to date with \n " \
        "web accessibility guidelines. The different areas of\n  web design " \
        "include web graphic design;\n  interface design; " \
        "authoring including standardised\n  code and proprietary software; " \
        "user experience design;\n and search engine optimization. "

eight = "Medical transcription also known as MT\n" \
        " is an allied health profession dealing with the process of transcribing\n " \
        "voice-recorded medical reports that are dictated by physicians\n " \
        "nurses and other healthcare practitioners. " \
        "\n Medical reports can be voice files\n notes taken during a " \
        "lecture or other spoken material.\n These are dictated " \
        "over the phone or uploaded\n digitally via the Internet or through smart phone apps. "

nine = "A late 20th century trend in typing\n primarily used with devices with small keyboards (such as PDAs and " \
       "Smartphones)\n is thumbing or thumb typing." \
       " This can be accomplished using one or\n both thumbs. Similar to desktop " \
       "keyboards and input devices\n if a user overuses keys which need hard " \
       "presses and/or have small and unergonomic\n " \
       "layouts it could cause thumb tendinitis or\n other repetitive strain injury. (Wikipedia) "

teen = "because of the laboriousness of the translation process\n" \
       " since the 1940s efforts have been made\n with varying \n" \
       "degrees of success to automate translation or to mechanically\n " \
       " aid the human translator. More recently\n " \
       "the rise of the Internet has fostered a world-wide market\n " \
       " for translation services and has facilitated 'language\n" \
       "localization'. Ideally the translator must know both languages\n" \
       " as well as the subject that is to be translated. "


class Speed:



    def __init__(self):
        self.texts_list = [one.lower(), two.lower(), three.lower(),
                           four.lower(), five.lower(),
                           six.lower(), seven.lower(),
                           eight.lower(), nine.lower(), teen.lower()]

        self.random = choice(self.texts_list)
        self.window = Tk()
        self.window.config(width=800, height=800)
        self.text = Label(self.window, text="Click start to start the test it will be 60 seconds.", font=("Courier", 20))
        self.text.grid(column=0, row=0)
        self.start_button = Button(self.window, text="Start", font=('Verdana', 20), width=50, command=self.started)
        self.start_button.grid(columnspan=2, column=0, row=1)
        self.time_left = 0
        self.entry = ""
        self.window.mainloop()

    def started(self):
        self.entry = Entry(self.window, font=('Verdana', 35), width=35)
        self.entry.grid(columnspan=2, column=0, row=1)
        self.text.config(text=self.random)
        self.window.after(1000 * 60, func=self.time)

    def time(self):
        users_text = self.entry.get()
        user_text = users_text.split(" ")
        texts_text = self.random.replace("\n", "")
        text_text = texts_text.split(" ")
        lis = [word for word in user_text if word in text_text]
        tkinter.messagebox.showinfo(f"Result", f"Good jop Result is -> {len(lis)} per minute.")
        self.window.quit()
