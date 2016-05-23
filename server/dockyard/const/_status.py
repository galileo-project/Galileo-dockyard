ExpStatus = {
    "STAT_EXP_INIT_MONGO":      "Init mongodb error",
}

APIStatus = {
    #API SUCCESS code less than 10000 to 0
    "STAT_API_SUCCESS":                 (0,         None),

    #ERROR code greater than 10000 and less than 30000
    "STAT_API_UNKNOWN_ERROR":           (1,         "Unknown error"),
    "STAT_API_DATA_INVALID":            (2,         "Data invalid"),

    "STAT_API_USER_EXIST":              (10001,     "User email already exist"),
    "STAT_API_USER_UNEXIST":            (10002,     "User not exist"),
    "STAT_API_USER_LOGIN":              (10003,     "User not login"),
    "STAT_API_USER_PWD_ERR":            (10004,     "User password error"),
    "STAT_API_PWD_EMPTY":               (10005,     "User password empty"),

    "STAT_API_MANAGER_LOGIN":           (10001,     "Manager not login"),
    "STAT_API_MANAGER_UNEXIST":         (10102,     "Manager not exist"),
    "STAT_API_MANAGER_PWD_ERR":         (10103,     "Manager password error"),

    "STAT_API_SYS_SETTINGS_UNEXIST":    (10201,     "Manager password error"),

    #WARN code greater than 30000 and less than 80000
    "STAT_API_GITHUB_OAUTH_FAILED":     (30006,     "User GitHub Oauth failed"),
    "STAT_API_LOG_UNEXIST":             (30007,     "Log not exist")

    #INFO code greater than 80000
}

LogStatus = {

}