from kivy.app import App
from kivy.lang import Builder


class CalculatorApp(App):
    def build(self):
        "calculator-app-2"
        return Builder.load_file("calculator.kv")

    def calculate(self):
        print("calculating")


if __name__ == "__main__":
    CalculatorApp().run()
