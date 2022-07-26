from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List

from ..types import BotCommand
from .base import Request, TelegramMethod

if TYPE_CHECKING:  # pragma: no cover
    from ..client.bot import Bot


class SetMyCommands(TelegramMethod[bool]):
    """
    Use this method to change the list of the bot's commands. Returns True on success.

    Source: https://core.telegram.org/bots/api#setmycommands
    """

    __returning__ = bool

    commands: List[BotCommand]
    """A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most
    100 commands can be specified."""

    def build_request(self, bot: Bot) -> Request:
        data: Dict[str, Any] = self.dict()

        return Request(method="setMyCommands", data=data)
