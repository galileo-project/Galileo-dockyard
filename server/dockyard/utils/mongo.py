import time
import pymongo
from bson.errors import InvalidId
from bson.objectid import ObjectId
from dockyard.var import GLOBAL


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
        self.__query       = {}
        self.__init_kv_model()

    def __init_kv_model(self):
        if self.__key:
            self.find_one({GLOBAL.MKEY: self.__key})
        if not self.exists():
            self[GLOBAL.MKEY] = self.__key

    @property
    def __key(self):
        try:
            key = self.KEY
        except:
            key = None
        return key

    def __del__(self):
        self.flush()

    def __getitem__(self, item):
        return self.__data.get(item, None)

    def __setitem__(self, key, value):
        if not value == self[key] and not value is None:
            self.__update_data[key] = value
            self.__data[key]        = value

    def __delattr__(self, item):
        try:
            del self.__data[item]
            del self.__update_data[item]
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

    def __bool__(self):
        return self.exists()

    def set_query(self, query):
        self.__query.update(query)

    def wrap_query(self, query):
        if query:
            self.__query.update(query)
        self.__query[GLOBAL.MDELETE] = False
        return self.__query

    def add(self, *args, **kwargs):
        raise NotImplemented

    @staticmethod
    def wrapper(data):
        data[GLOBAL.MUPDATE] = time.time()

        if GLOBAL.MDELETE not in data:
            data[GLOBAL.MDELETE] = False

        if GLOBAL.MCREATE not in data:
            data[GLOBAL.MCREATE] = data[GLOBAL.MUPDATE]
        return data

    @staticmethod
    def __unwrapper(data):
        for it in [GLOBAL.MDELETE, GLOBAL.MUPDATE, GLOBAL.MCREATE]:
            try:
                del data[it]
            except:
                pass
            data[GLOBAL.MID] = str(data[GLOBAL.MID])
        return data

    @staticmethod
    def unwrapper(data):
        if isinstance(data, dict):
            return Mongo.__unwrapper(data)
        elif data is None:
            return {}
        else:
            ret = []
            for it in data:
                res = Mongo.__unwrapper(it)
                ret.append(res)
            return ret


    @property
    def id(self):
        try:
            _id = self.__data.get(GLOBAL.MID)
            if _id is None:
                return None
            elif not isinstance(_id, ObjectId):
                return ObjectId(_id)
            else:
                return _id
        except InvalidId:
            return None

    @property
    def str_id(self):
        _id = self.__data.get(GLOBAL.MID)
        if not isinstance(_id, str):
            return str(_id)
        else:
            return _id

    def remove(self):
        self.__update_data[GLOBAL.MDELETE] = True

    def clear(self):
        self.__data.clear()
        self.__list.clear()

    def count(self):
        return len(self.__list)

    def append(self, data):
        self.__list.append(data)
        self.__update_list.append(data)

    @property
    def raw(self):
        if self.__data:
            return self.unwrapper(self.__data)
        elif self.__list:
            return self.unwrapper(self.__list)
        else:
            return {}

    def set_raw(self, data):
        if isinstance(data, list):
            self.__list = data
        elif isinstance(data, dict):
            self.__data = data

    def get_by_id(self, _id):
        if isinstance(_id, ObjectId):
            _id = ObjectId(_id)
        return self.find_one({GLOBAL.MID: _id})

    def find(self, query, skip=None, limit=None, order=None):
        items = self.__table.find(self.wrap_query(query))
        if order is not None:
            items.sort(order)
        if skip is not None:
            items.skip(int(skip))
        if limit is not None:
            items.limit(int(limit))

        self.__list = self.unwrapper(items)
        return self

    def find_one(self, query):
        self.__data = self.unwrapper(self.__table.find_one(self.wrap_query(query)))
        return self

    def all(self, skip=None, limit=None, order=None):
        self.find({}, skip, limit, order)

    def __save_data(self):
        if self.__update_data:
            self.__update_data = self.wrapper(self.__update_data)

            if self.id:
                self.__table.update_one({GLOBAL.MID: self.id}, {"$set": self.__update_data})
            else:
                self.__data[GLOBAL.MID] = self.__table.insert_one(self.__update_data).inserted_id
            self.__update_data = {}

    def __save_list(self):
        if self.__update_data.get(GLOBAL.MDELETE) is True:
            for data in self.__list:
                data = self.wrapper(data)
                data[GLOBAL.MDELETE] = True
                self.__table.update_one({GLOBAL.MID: data[GLOBAL.MID]}, {"$set": data})
            self.__list = []
        else:
            for data in self.__update_list:
                data = self.wrapper(data)
                self.__table.insert_one(data)
                self.__update_list = []

    def flush(self):
        self.__save_data()
        self.__save_list()
        self.clear()

    def exists(self, query=None):
        if query:
            self.find_one(query or self.__update_data)

        if self.__data or self.__list:
            return True
        else:
            return False

    @classmethod
    def eq(cls, val):
        return {"$eq": val}

    @classmethod
    def gt(cls, val, eq=True):
        if eq:
            return {"$gte": val}
        else:
            return {"$gt": val}

    @classmethod
    def lt(cls, val, eq=True):
        if eq:
            return {"$lte": val}
        else:
            return {"$lt": val}

    @classmethod
    def q_or(cls, data):
        if not isinstance(data, list):
            data = [data]
        return {"$or": data}

    @classmethod
    def q_in(cls, data):
        if not isinstance(data, list):
            data = [data]
        return {"$in": data}

    @classmethod
    def q_nin(cls, data):
        if not isinstance(data, list):
            data = [data]
        return {"$nin": data}

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
