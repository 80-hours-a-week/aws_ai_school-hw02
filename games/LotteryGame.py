"""
추상 게임 클래스
"""
from abc import ABC, abstractmethod
from typing import Optional
from prize.PrizeStructure import PrizeStructure
from prize.DrawingMachine import DrawingMachine
from tickets.Ticket import Ticket

# 모든 복권 게임의 기본 클래스
class LotteryGame(ABC):
    
    def __init__(self, name: str, ticket_price: int):
        self.name = name
        self.ticket_price = ticket_price
        self.prize_structure: Optional[PrizeStructure] = None
        self.drawing_machine: Optional[DrawingMachine] = None
        
    # 티켓 생성하기
    @abstractmethod
    def create_ticket(self, numbers=None) -> Ticket:
        pass
    
    # 추첨 진행하기
    @abstractmethod
    def conduct_draw(self) -> dict:
        pass
    
    # 당첨 확인하기 및 등수 반환
    @abstractmethod
    def check_winning(self, ticket: Ticket, drawn_numbers: dict) -> int:
        pass
    
    # 게임 규칙 설명하기
    def get_game_rules(self) -> str:
        return f"{self.name} - 티켓 가격: {self.ticket_price:,}원"
    
    # 티켓 가격 반환하기
    def get_ticket_price(self) -> int:
        return self.ticket_price
    
    # 인스턴스의 출력 양식
    def __repr__(self):
        return f"{self.name} ({self.ticket_price:,}원)"
