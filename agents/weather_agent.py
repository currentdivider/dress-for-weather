from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain import OpenAI

from langchain.agents import initialize_agent, AgentType, load_tools, Tool
from tools.tools import count_letters
from output_parser import data_parser

def weather_agent(city: str) -> str:
    tools_llm = OpenAI(temperature=0)
    llm = ChatOpenAI(temperature=0)
    template = """
    Given a {city}, get the current weather for that city, I want you to:
    1. Suggest the best outfit for that weather.
    2. Count the letters in the city name.
    \n{format_instructions}
    """

    tools = load_tools(["open-meteo-api", "serpapi"], llm=tools_llm)
    tools.append(
        Tool(
            name="count_letters", func=count_letters, description="Count the letters in the city name."
        )
    )
    prompt_template = PromptTemplate(
        input_variables=["city"],
        template=template,
        partial_variables={"format_instructions": data_parser.get_format_instructions()},
    )
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    result = agent.run(prompt_template.format_prompt(city=city))
    return data_parser.parse(result)
