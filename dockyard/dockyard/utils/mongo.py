from dockyard.var import GLOBAL
from dockyard.const import MID
from bson.objectid import ObjectId
import pymongo

class Mongo:
    def __init__(self):
        self.__table_name  = self.__class__.__name__
        self.__db          = GLOBAL.mongo()
        self.__table       = self.__db[self.__table_name]
        self.__data        = {}
        self.__list        = []
        self.__index       = 0
        self.__update_data = {}
        self.__update_list = []

    def __del__(self):
        self.flush()

    def __getattr__(self, item):
        return self.__data.get(item, None)

    def __setattr__(self, key, value):
        self.__update_set[key] = value
        self.__data[key]       = value

    def __getitem__(self, item):
        return self.__getattr__(item)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __delattr__(self, item):
        try:
            del self.__data[item]
        except KeyError:
            pass

    def __delitem__(self, key):
        self.__delattr__(key)

    def __next__(self):
        try:
            data = self.__list[self.__index]
        except IndexError:
            raise StopIteration()
        self.__index += 1
        return data

    def __iter__(self):
        return self

    def __len__(self):
        return self.count()

    @property
    def id(self):
        try:
            _id = self.__data[MID]
            if not isinstance(_id, ObjectId):
                return ObjectId(_id)
            else:
                return _id
        except:
            return None

    @property
    def str_id(self):
        try:
            _id = self.__data[MID]
            if not isinstance(_id, str):
                return str(_id)
            else:
                return _id
        except:
            return ""

    def clear(self):
        self.__data.clear()
        self.__list.clear()

    def count(self):
        return len(self.__list)

    def append(self, data):
        self.__list.append(data)
        self.__update_list.append(data)

    def get_raw(self):
        return self.__data or self.__list

    def set_raw(self, data):
        if isinstance(data, list):
            self.__list = data
        elif isinstance(data, dict):
            self.__data = data

    def find(self, query = None, skip = None, limit = None, order = None):
        self.__list = self.__table.find(query)
        if order is not None:
            self.__list.sort(order)
        if skip is not None:
            self.__list.skip(int(skip))
        if limit is not None:
            self.__list.limit(int(limit))
        return self

    def find_one(self, query):
        self.__data   = self.__table.find_one(query)
        return self

    def all(self, skip = None, limit = None, order = None):
        return self.find({}, skip, limit, order)

    def flush(self):
        if self.__update_data:
            if self.id:
                self.__table.update_one({MID: self.id}, self.__update_data)
            else:
                self.__table.insert_one(self.__update_data)

        if self.__update_list:
            self.__table.insert_many(self.__update_list)

    def exists(self, query = None):
        if query:
            self.clear()
            self.find_one(query)

        if self.__data or self.__list:
            return True
        else:
            return False

    @classmethod
    def eq(cls, val):
        return {"$eq": val}

    @classmethod
    def gt(cls, val, eq = True):
        if eq:
            return {"$gte": val}
        else:
            return {"$gt": val}

    @classmethod
    def lt(cls, val, eq = True):
        if eq:
            return {"$lte": val}
        else:
            return {"$lt": val}

    @classmethod
    def q_or(cls, datas):
        return {"$or": datas}

    @classmethod
    def q_in(cls, qrange):
        return {"$in": qrange}

    @classmethod
    def q_nin(cls, qrange):
        return {"$nin": qrange}

    @classmethod
    def q_regex(cls, val):
        return {"$regex": val}

    @classmethod
    def q_exists(cls, val):
        return {"$exists": val}

    @classmethod
    def q_range(cls, start, seq, end, eeq):
        return {"$gte" if seq else "$gt": start,
                "$lte" if eeq else "$lt": end}

    @classmethod
    def desc(cls, fields):
        ret = []
        if not isinstance(fields, list):
            fields = [fields]
        for field in fields:
            ret.append((field, pymongo.DESCENDING))
        return ret

    @classmethod
    def asc(cls, fields):
        ret = []
        if not isinstance(fields, list):
            fields = [fields]
        for field in fields:
            ret.append((field, pymongo.ASCENDING))
        return ret