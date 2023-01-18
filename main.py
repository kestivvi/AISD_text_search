import tkinter
from controller import TextController

root = tkinter.Tk()  # Initialize tkinter
app = TextController(root)  # Create an instance of the TextController
root.mainloop()  # Run graphical interface


# Podział obowiązków:
#  -> Szkielet oraz model aplikacji - Krzysztof Kwiatkowski
#  -> Testy jednostkowe wraz z podsumowaniem czasu wykonania - Krzysztof Kwiatkowski
#  -> Interfejs graficzny - Bartosz Malec
#  -> Algorytm Boyer'a i Moore'a - Wspólna implementacja
#  -> Podłączenie algorytmu do interfejsu graficznego - Wspólna implementacja