from rlbot.agents.base_agent import BaseAgent
from rlbot.utils.structures.game_data_struct import GameTickPacket

class BotlessAgent(BaseAgent):
    def __init__(self):
        pass
    
    # Remove the type hint from get_output (since this agent doesn't control a bot)
    @override
    def get_output(self, game_tick_packet: GameTickPacket):
        pass
    
