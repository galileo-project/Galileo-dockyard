from dockyard.const import APIStatus

class Driver:
    def _export(self, msg, stat=None):
        if stat is None:
            return False, msg
        else:
            return True, stat

    def succes(self, msg=None):
        return self._export(msg)

    def err(self, stat=None):
        if stat is None:
            stat = APIStatus["STAT_API_UNKNOWN_ERROR"]
        return self._export(None, stat)