from rlbot.setup_manager import SetupManager
from rlbot.agents.botless_agent import BotlessAgent
from rlbot.utils.python_version_check import check_python_version

botless_agents = []

def add_botless_agent(agent: BotlessAgent):
    agent.index = len(botless_agents)
    botless_agents.append(agent)

def main():

    print("starting")
    check_python_version()
    manager = SetupManager()
    manager.load_config()
    manager.connect_to_game()
    manager.launch_quick_chat_manager()
    manager.start_match()
    manager.launch_bot_processes()
    manager.infinite_loop()  # Runs forever until interrupted


if __name__ == '__main__':
    main()
