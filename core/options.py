from core.models.options_model import OptionsModel
import os
import jsonpickle

class ConversationOptions():

    __options: OptionsModel
    __options_file = "./options.json"

    def __init__(self) -> None:
        self.__options = OptionsModel()
        self.__options.model = "stabilityai/stable-diffusion-2-1"
        self.__options.num_inference_steps = 20
        self.__options.extended_prompt = "film, professional, highly detailed"
        self.__options.guidance_scale = 7.0
        self.__options.cuda = True

    def self_check(self):
        if os.path.exists(self.__options_file):
            self.load()
        else:
            self.save()

    def from_request(self, request):
        self.__options.model = request['selected_model']
        self.__options.num_inference_steps = int(request['selected_inference_steps'])
        self.__options.guidance_scale = float(request['selected_guidance_scale'])
        self.__options.extended_prompt = request['selected_extended_prompt']
        try:
            use_cuda = request['selected_cuda']
            self.__options.cuda = True
        except:
            self.__options.cuda = False
        self.save()

    def load(self):
        file = open(file=self.__options_file, mode="r")
        json = file.read()
        new_config = jsonpickle.decode(json)
        self.__options = new_config

    def save(self):
        json = jsonpickle.encode(self.__options)
        file = open(self.__options_file, mode="w")
        file.write(json)
        file.close()

    def is_model_selected(self, model:str) -> str:
        if model == self.__options.model:
            return "selected"

    @property
    def available_models(self) :
        return {
                "runwayml/stable-diffusion-v1-5",
                "stabilityai/stable-diffusion-xl-base-1.0",
                "dreamlike-art/dreamlike-photoreal-2.0",
                "stabilityai/stable-diffusion-2-1"
         }

    @property
    def options(self) -> OptionsModel:
        return self.__options

    @property
    def model(self) -> str:
        return self.__options.model
    
    @model.setter
    def model(self, new_model):
        self.__options.model = new_model

    @property
    def num_inference_steps(self) -> int:
        return self.__options.num_inference_steps
    
    @num_inference_steps.setter
    def num_inference_steps(self, new_num_inference_steps):
        self.__options.num_inference_steps=new_num_inference_steps

    @property
    def extended_prompt(self) -> str:
        return self.__options.extended_prompt

    @extended_prompt.setter
    def extended_prompt(self, new_extended_prompt:str):
        self.__options.extended_prompt = new_extended_prompt

    @property
    def guidance_scale(self) -> float:
        return self.__options.guidance_scale
    
    @guidance_scale.setter
    def guidance_scale(self, new_guidance_scale:float):
        self.__options.guidance_scale = new_guidance_scale

    @property
    def cuda(self) -> bool:
        return self.__options.cuda
    
    @cuda.setter
    def cuda(self, new_cuda:bool) -> bool:
        self.__options.cuda = new_cuda