from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from ..types import (
    UNSET,
    ForceReply,
    InlineKeyboardMarkup,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from .base import Request, TelegramMethod, prepare_parse_mode

if TYPE_CHECKING:  # pragma: no cover
    from ..client.bot import Bot


class SendMessage(TelegramMethod[Message]):
    """
    Use this method to send text messages. On success, the sent Message is returned.

    Source: https://core.telegram.org/bots/api#sendmessage
    """

    __returning__ = Message

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target channel (in the format
    @channelusername)"""
    text: str
    """Text of the message to be sent, 1-4096 characters after entities parsing"""
    parse_mode: Optional[str] = UNSET
    """Mode for parsing entities in the message text. See formatting options for more details."""
    disable_web_page_preview: Optional[bool] = None
    """Disables link previews for links in this message"""
    disable_notification: Optional[bool] = None
    """Sends the message silently. Users will receive a notification with no sound."""
    reply_to_message_id: Optional[int] = None
    """If the message is a reply, ID of the original message"""
    reply_markup: Optional[
        Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
    ] = None
    """Additional interface options. A JSON-serialized object for an inline keyboard, custom reply
    keyboard, instructions to remove reply keyboard or to force a reply from the user."""

    def build_request(self, bot: Bot) -> Request:
        data: Dict[str, Any] = self.dict()
        prepare_parse_mode(bot, data)

        return Request(method="sendMessage", data=data)
