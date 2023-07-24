import os

from hivemind.utils import logging as hm_logging


def initialize_logs():
    """Initialize Grid logging tweaks. This function is called when you import the `grid` module."""

    # Env var GRID_LOGGING=False prohibits Grid do anything with logs
    if os.getenv("GRID_LOGGING", "True").lower() in ("false", "0"):
        return

    hm_logging.use_hivemind_log_handler("in_root_logger")

    # We suppress asyncio error logs by default since they are mostly not relevant for the end user,
    # unless there is env var GRID_ASYNCIO_LOGLEVEL
    asyncio_loglevel = os.getenv("GRID_ASYNCIO_LOGLEVEL", "FATAL" if hm_logging.loglevel != "DEBUG" else "DEBUG")
    hm_logging.get_logger("asyncio").setLevel(asyncio_loglevel)
