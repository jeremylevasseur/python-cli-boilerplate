from typing import Any

from rich.console import Console
from rich.theme import Theme

from config import config
from constants import LogJustifyMethod, LogLevel

log_theme = Theme(
    {
        LogLevel.DEBUG: "bright_magenta",
        LogLevel.INFO: "pale_turquoise1",
        LogLevel.WARNING: "bold yellow",
        LogLevel.ERROR: "bright_red",
        LogLevel.CRITICAL: "bold bright_red",
        LogLevel.TRACE: "bold cyan",
    }
)


class Log:
    def __init__(self) -> None:
        self.console = Console(
            theme=log_theme,
            log_time=False,
            log_path=True if config.DEBUG else False,
        )

    def _log(
        self,
        *objects: Any,
        sep: str = " ",
        end: str = "\n",
        justify: LogJustifyMethod | None = None,
        emoji: bool | None = None,
        markup: bool | None = None,
        highlight: bool | None = None,
        log_locals: bool = False,
        _stack_offset: int = 1,
        level: LogLevel = LogLevel.INFO,
    ) -> None:
        self.console.log(
            *objects,
            sep=sep,
            end=end,
            justify=justify.value if justify else None,
            emoji=emoji,
            markup=markup,
            highlight=highlight,
            log_locals=log_locals,
            _stack_offset=_stack_offset,
            style=level.value,
        )

    def debug(
        self,
        *objects: Any,
        sep: str = " ",
        end: str = "\n",
        justify: LogJustifyMethod | None = None,
        emoji: bool | None = None,
        markup: bool | None = None,
        highlight: bool | None = None,
        log_locals: bool = False,
        _stack_offset: int = 1,
    ) -> None:
        self._log(
            *objects,
            sep=sep,
            end=end,
            justify=justify,
            emoji=emoji,
            markup=markup,
            highlight=highlight,
            log_locals=log_locals,
            _stack_offset=_stack_offset,
            level=LogLevel.DEBUG,
        )

    def info(
        self,
        *objects: Any,
        sep: str = " ",
        end: str = "\n",
        justify: LogJustifyMethod | None = None,
        emoji: bool | None = None,
        markup: bool | None = None,
        highlight: bool | None = None,
        log_locals: bool = False,
        _stack_offset: int = 1,
    ) -> None:
        self._log(
            *objects,
            sep=sep,
            end=end,
            justify=justify,
            emoji=emoji,
            markup=markup,
            highlight=highlight,
            log_locals=log_locals,
            _stack_offset=_stack_offset,
            level=LogLevel.INFO,
        )

    def warning(
        self,
        *objects: Any,
        sep: str = " ",
        end: str = "\n",
        justify: LogJustifyMethod | None = None,
        emoji: bool | None = None,
        markup: bool | None = None,
        highlight: bool | None = None,
        log_locals: bool = False,
        _stack_offset: int = 1,
    ) -> None:
        self._log(
            *objects,
            sep=sep,
            end=end,
            justify=justify,
            emoji=emoji,
            markup=markup,
            highlight=highlight,
            log_locals=log_locals,
            _stack_offset=_stack_offset,
            level=LogLevel.WARNING,
        )

    def error(
        self,
        *objects: Any,
        sep: str = " ",
        end: str = "\n",
        justify: LogJustifyMethod | None = None,
        emoji: bool | None = None,
        markup: bool | None = None,
        highlight: bool | None = None,
        log_locals: bool = False,
        _stack_offset: int = 1,
    ) -> None:
        self._log(
            *objects,
            sep=sep,
            end=end,
            justify=justify,
            emoji=emoji,
            markup=markup,
            highlight=highlight,
            log_locals=log_locals,
            _stack_offset=_stack_offset,
            level=LogLevel.ERROR,
        )

    def critical(
        self,
        *objects: Any,
        sep: str = " ",
        end: str = "\n",
        justify: LogJustifyMethod | None = None,
        emoji: bool | None = None,
        markup: bool | None = None,
        highlight: bool | None = None,
        log_locals: bool = False,
        _stack_offset: int = 1,
    ) -> None:
        self._log(
            *objects,
            sep=sep,
            end=end,
            justify=justify,
            emoji=emoji,
            markup=markup,
            highlight=highlight,
            log_locals=log_locals,
            _stack_offset=_stack_offset,
            level=LogLevel.CRITICAL,
        )

    def trace(
        self,
        *objects: Any,
        sep: str = " ",
        end: str = "\n",
        justify: LogJustifyMethod | None = None,
        emoji: bool | None = None,
        markup: bool | None = None,
        highlight: bool | None = None,
        log_locals: bool = False,
        _stack_offset: int = 1,
    ) -> None:
        self._log(
            *objects,
            sep=sep,
            end=end,
            justify=justify,
            emoji=emoji,
            markup=markup,
            highlight=highlight,
            log_locals=log_locals,
            _stack_offset=_stack_offset,
            level=LogLevel.TRACE,
        )


log = Log()
