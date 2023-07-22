class GroupStockDto:
    def __init__(self, group_id, name, code: str):
        self.group_id = group_id
        self.name = name
        self.code = code

    def __init__(self, group_id, code: str):
        self.group_id = group_id
        self.code = code
        self.name = ''
