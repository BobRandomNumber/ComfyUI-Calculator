class Calculator:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {},
        }

    RETURN_TYPES = ()
    FUNCTION = "Calculator"
    CATEGORY = "Calculator 🧮"

    def Calculator(self):
        return ()

NODE_CLASS_MAPPINGS = {
    "Calculator": Calculator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Calculator": "Calculator 🧮"
}