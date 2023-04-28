from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, AgentType, load_tools

def weather_agent(city: str) -> str:
    llm = ChatOpenAI(temperature=0)
    template = """
    Given a {city}, I want you to get the current weather for that city, and suggest
    the proper clothing to wear.
    """

    tools = load_tools(["open-meteo-api", "serpapi"], llm = llm)
    prompt_template = PromptTemplate(
        input_variables=["city"],
        template=template,
    )
    agent = initialize_agent(
        tools=tools,
        llm = llm,
        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose = True,
    )
    result = agent.run(prompt_template.format_prompt(city=city))
    return result
