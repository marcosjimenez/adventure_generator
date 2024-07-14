from core.image_generator import ImageGenerator
from core.models.step_model import StepModel
from core.constants import Constants
from core.options import ConversationOptions

class Conversation() :

    INITIAL_TEXT = 'Welcome to the adventure player'
    input_steps: [] # type: ignore
    image: str

    def __init__(self) -> None:
        self.image = Constants.INITIAL_IMAGE
        self.start()

    def start(self) -> StepModel:
        self.input_steps = [self.INITIAL_TEXT]
        return StepModel(self.INITIAL_TEXT, Constants.INITIAL_IMAGE)

    def next_step(self, user_input: str, options: ConversationOptions) -> StepModel:
        self.input_steps.append(user_input)
        self.image = ImageGenerator().generate(input_text=user_input, options=options)
        return StepModel(user_input, self.image)

    @property
    def steps(self):
        return self.input_steps

    @property
    def current_status (self) -> str:
        return self.input_steps[len(self.input_steps) -1]
   
    @property
    def current_image (self) -> str:
        return self.image