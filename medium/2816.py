# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Преобразуем связанный список в список цифр в обратном порядке
        digits = []
        cur = head
        while cur:
            digits.append(cur.val)
            cur = cur.next
        digits.reverse()

        # Умножаем каждую цифру на 2 и учитываем перенос
        carry = 0
        for i in range(len(digits)):
            total = digits[i] * 2 + carry
            digits[i] = total % 10
            carry = total // 10

        # Если остался перенос, добавляем его в начало списка
        if carry:
            digits.append(carry)

        # Преобразуем список цифр обратно в связанный список
        digits.reverse()
        dummy_head = ListNode(0)  # Вспомогательный узел
        cur = dummy_head
        for digit in digits:
            cur.next = ListNode(digit)
            cur = cur.next

        return dummy_head.next
