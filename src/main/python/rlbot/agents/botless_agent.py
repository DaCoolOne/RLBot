from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot.utils.structures.game_interface import GameInterface

class BotlessAgent():
    index = 0
    
    # Called when the agent connects to a game. Allows the agent access to the game interface that RLBot uses. Also used to initialize the agent.
    def connect(self, game_interface: GameInterface, config_paths = []):
        pass
    
    # @Todo pass this a game tick packet.
    def update():
        pass
    
    # Used to signal end of match
    def retire(self):
        pass
    
