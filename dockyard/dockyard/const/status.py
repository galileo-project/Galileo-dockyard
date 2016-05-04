ExpStatus = {
    "STAT_EXP_INIT_MONGO":      "Init mongodb error",
}

APIStatus = {
    #ERROR
    "STAT_API_SUCCESS":             (0,         None),
    "STAT_API_UNKNOWN_ERROR":       (1,         "Unknown error"),
    "STAT_API_DATA_INVALID":        (2,         "Data invalid"),

    "STAT_API_USER_EXIST":          (10001,     "User email already exist"),
    "STAT_API_USER_UNEXIST":        (10002,     "User not exist"),
    "STAT_API_USER_LOGIN":          (10003,     "User not login"),
    "STAT_API_USER_PWD_ERR":        (10004,     "User password error"),
    "STAT_API_PWD_EMPTY":           (10005,     "User password empty"),

    #WARN
}

LogStatus = {

}