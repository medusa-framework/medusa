class Printable():
    def __str__(self) -> str:
        return str(f"{self.id}")
    
    def __repr__(self) -> str:
        return str(f"{self.id}")
    
    def __init__(self) -> None:
        super().__init__()