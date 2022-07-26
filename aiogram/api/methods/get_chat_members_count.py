from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Union

from .base import Request, TelegramMethod

if TYPE_CHECKING:  # pragma: no cover
    from ..client.bot import Bot


class GetChatMembersCount(TelegramMethod[int]):
    """
    Use this method to get the number of members in a chat. Returns Int on success.

    Source: https://core.telegram.org/bots/api#getchatmemberscount
    """

    __returning__ = int

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target supergroup or channel (in
    the format @channelusername)"""

    def build_request(self, bot: Bot) -> Request:
        data: Dict[str, Any] = self.dict()

        return Request(method="getChatMembersCount", data=data)
