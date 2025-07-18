class Widget:
    def render(self):
        raise NotImplementedError("Subclasses must implement this method")

class Button(Widget):
    def render(self):
        print("Rendering a Button")

class TextBox(Widget):
    def render(self):
        print("Rendering a TextBox")

class Label(Widget):
    def render(self):
        print("Rendering a Label")

# Function that uses dynamic polymorphism
def draw_ui(widgets):
    for widget in widgets:
        widget.render()  # Python decides which render() to call at runtime

# Create instances of different widget types
ui_elements = [Button(), TextBox(), Label()]

draw_ui(ui_elements)

