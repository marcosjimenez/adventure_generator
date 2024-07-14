class StepModel:
    user_input: str
    image:str

    def __init__(self, user_input, image) -> None:
        self.user_input = user_input
        self.image = image