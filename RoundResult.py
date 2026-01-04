# 라운드 진행 결과 클래스
from typing import List, Tuple, Dict
from tickets.Ticket import Ticket


# 복권 시뮬레이션을 한 라운드 진행한 결과
class RoundResult:
    
    def __init__(self, round_number: int, drawn_numbers: dict):
        self.round_number = round_number
        self.drawn_numbers = drawn_numbers
        self.tickets_purchased = 0
        self.total_spent = 0
        self.winning_tickets: List[Tuple[Ticket, int, int]] = []  # (티켓, 등급, 상금)
        self.total_won = 0
        self.net_profit = 0
        
    # 구매 정보 설정
    def set_purchase_info(self, ticket_count: int, total_cost: int):
        self.tickets_purchased = ticket_count
        self.total_spent = total_cost
    
    # 당첨 티켓 추가
    def add_winning_ticket(self, ticket: Ticket, rank: int, prize: int):
        self.winning_tickets.append((ticket, rank, prize))
        self.total_won += prize
        
    # 순이익 계산하기
    def calculate_net_profit(self):
        self.net_profit = self.total_won - self.total_spent
        
    # 등급별 당첨 횟수 계산하기
    def get_winning_count_by_rank(self) -> Dict[int, int]:
        rank_count = {}
        for _, rank, _ in self.winning_tickets:
            rank_count[rank] = rank_count.get(rank, 0) + 1
        return rank_count
    
    # 인스턴스의 출력 양식
    def __repr__(self):
        return (f"Round {self.round_number}: "
                f"구매 {self.tickets_purchased}장, "
                f"당첨 {len(self.winning_tickets)}장, "
                f"수익 {self.net_profit:+,}원")
