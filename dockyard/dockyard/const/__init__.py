MID         = "_id"
MDELETE     = "__deleted__"
MCREATE     = "__create__"
MUPDATE     = "__update__"

LOG_WARN    = "warn"
LOG_FATAL   = "warn"
LOG_SUCCESS = "warn"
LOG_ERROR   = "warn"
LOG_PUTS     = "put"

SYS_ORIGIN  = "system"

LOG_LEVEL   = {LOG_ERROR:      "_error",
               LOG_FATAL:      "_fatal",
               LOG_SUCCESS:    "_success",
               LOG_WARN:       "_warn",
               LOG_PUTS:        "_put"}

from dockyard.const.status import ExpStatus, APIStatus, LogStatus