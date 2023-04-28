from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

class Data(BaseModel):
    weather: str = Field(description="Describes the current weather.")
    dress: str = Field(description="Appropriate dress for the weather.")
    letters: int = Field(description="Number of letters in the city name.")

    def to_dict(self):
        return {
            "weather": self.weather,
            "dress": self.dress,
            "letters": self.letters,
        }
    

data_parser = PydanticOutputParser(pydantic_object=Data)
