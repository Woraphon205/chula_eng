import tkinter as tk
import random

# Thai consonants dictionary
thai_consonants = {
    "ก": "gor gai",
    "ข": "khor khai",
    "ฃ": "khor khuad",
    "ค": "khor khwai",
    "ฅ": "khor khon",
    "ฆ": "khor ra-khang",
    "ง": "ngor ngu",
    "จ": "jor jan",
    "ฉ": "chor ching",
    "ช": "chor chang",
}

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.current_card = None
        self.flipped = False
        
        # Create UI Elements
        self.label = tk.Label(root, text="", font=("Arial", 100), width=5, height=2)
        self.label.pack(pady=50)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card, font=("Arial", 16))
        self.flip_button.pack()
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 16))
        self.next_button.pack()
        
        # Start with first card
        self.next_card()
    
    def next_card(self):
        self.current_card = random.choice(list(thai_consonants.keys()))
        self.label.config(text=self.current_card)
        self.flipped = False
    
    def flip_card(self):
        if self.flipped:
            self.label.config(text=self.current_card)
        else:
            self.label.config(text=thai_consonants[self.current_card])
        self.flipped = not self.flipped

# Run the application
root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()



