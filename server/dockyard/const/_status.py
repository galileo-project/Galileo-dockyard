ExpStatus = {
    "STAT_EXP_INIT_MONGO":      "Init mongodb error",
}

APIStatus = {
    #API SUCCESS code less than 10000
    "STAT_API_SUCCESS":                 (0,         None),
    #API SUCCESS INFO code greater than 0 and less than 10000

    #ERROR code greater than 10000 and less than 30000
    "STAT_API_UNKNOWN_ERROR":           (10001,     "Unknown error"),
    "STAT_API_DATA_INVALID":            (10002,     "Data invalid"),
    "STAT_API_NOT_FOUND":               (10003,     "Api not found"),

    "STAT_API_USER_EXIST":              (10101,     "User already exist"),
    "STAT_API_USER_UNEXIST":            (10102,     "User not exist"),
    "STAT_API_USER_LOGIN":              (10103,     "User not login"),
    "STAT_API_USER_PWD_ERR":            (10104,     "User password error"),
    "STAT_API_USER_PWD_EMPTY":          (10105,     "User password empty"),

    "STAT_API_MANAGER_LOGIN":           (10201,     "Manager not login"),
    "STAT_API_MANAGER_UNEXIST":         (10202,     "Manager not exist"),
    "STAT_API_MANAGER_EXIST":           (10203,     "Manager already exist"),
    "STAT_API_MANAGER_PWD_ERR":         (10204,     "Manager password error"),

    "STAT_API_APP_UNEXIST":             (10303,     "App not exist"),

    "STAT_API_BUILD_UNEXIST":           (10403,     "Build information not exist"),

    "STAT_API_SYS_OBJ_UNEXIST":         (10301,     "System object not exist"),

    "STAT_API_TASK_UNEXIST":            (10401,     "Task not exist"),

    #WARN code greater than 30000 and less than 80000
    "STAT_API_GITHUB_OAUTH_FAILED":     (30101,     "User GitHub Oauth failed"),
    "STAT_API_LOG_UNEXIST":             (30102,     "Log not exist")

    #INFO code greater than 80000 and less than 99999
}

LogStatus = {

}