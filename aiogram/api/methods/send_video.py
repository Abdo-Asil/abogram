from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from ..types import (
    UNSET,
    ForceReply,
    InlineKeyboardMarkup,
    InputFile,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from .base import Request, TelegramMethod, prepare_file

if TYPE_CHECKING:  # pragma: no cover
    from ..client.bot import Bot


class SendVideo(TelegramMethod[Message]):
    """
    Use this method to send video files, Telegram clients support mp4 videos (other formats may be
    sent as Document). On success, the sent Message is returned. Bots can currently send video
    files of up to 50 MB in size, this limit may be changed in the future.

    Source: https://core.telegram.org/bots/api#sendvideo
    """

    __returning__ = Message

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target channel (in the format
    @channelusername)"""
    video: Union[InputFile, str]
    """Video to send. Pass a file_id as String to send a video that exists on the Telegram servers
    (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet,
    or upload a new video using multipart/form-data."""
    duration: Optional[int] = None
    """Duration of sent video in seconds"""
    width: Optional[int] = None
    """Video width"""
    height: Optional[int] = None
    """Video height"""
    thumb: Optional[Union[InputFile, str]] = None
    """Thumbnail of the file sent; can be ignored if thumbnail generation for the file is
    supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size.
    A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded
    using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new
    file, so you can pass 'attach://<file_attach_name>' if the thumbnail was uploaded using
    multipart/form-data under <file_attach_name>."""
    caption: Optional[str] = None
    """Video caption (may also be used when resending videos by file_id), 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = UNSET
    """Mode for parsing entities in the video caption. See formatting options for more details."""
    supports_streaming: Optional[bool] = None
    """Pass True, if the uploaded video is suitable for streaming"""
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
        data: Dict[str, Any] = self.dict(exclude={"video", "thumb"})

        files: Dict[str, InputFile] = {}
        prepare_file(data=data, files=files, name="video", value=self.video)
        prepare_file(data=data, files=files, name="thumb", value=self.thumb)

        return Request(method="sendVideo", data=data, files=files)
