from model import *
room_dict = {
    "start": Room("#write des", ["kitchen" , "HG"], NoMonster()),
    "kitchen": Room("#write des", ["start"], Goblin()),
    "HG": Room("#write des", ["start" , "Lib","Treasure"], Hobgoblin()),
    "Lib": Room("#write des", ["HG"], NoMonster()),
    "Treasure": Room("#write des", ["HG","FB"], NoMonster()),
    "FB": Room("#write des", ["Treasure"], GoblinKing()),
}
