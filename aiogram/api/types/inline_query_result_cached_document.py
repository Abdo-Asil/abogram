from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pydantic import Field

from .base import UNSET
from .inline_query_result import InlineQueryResult

if TYPE_CHECKING:  # pragma: no cover
    from .inline_keyboard_markup import InlineKeyboardMarkup
    from .input_message_content import InputMessageContent


class InlineQueryResultCachedDocument(InlineQueryResult):
    """
    Represents a link to a file stored on the Telegram servers. By default, this file will be sent
    by the user with an optional caption. Alternatively, you can use input_message_content to send
    a message with the specified content instead of the file.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients
    will ignore them.

    Source: https://core.telegram.org/bots/api#inlinequeryresultcacheddocument
    """

    type: str = Field("document", const=True)
    """Type of the result, must be document"""
    id: str
    """Unique identifier for this result, 1-64 bytes"""
    title: str
    """Title for the result"""
    document_file_id: str
    """A valid file identifier for the file"""
    description: Optional[str] = None
    """Short description of the result"""
    caption: Optional[str] = None
    """Caption of the document to be sent, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = UNSET
    """Mode for parsing entities in the document caption. See formatting options for more details."""
    reply_markup: Optional[InlineKeyboardMarkup] = None
    """Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = None
    """Content of the message to be sent instead of the file"""
