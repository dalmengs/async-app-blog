
class BaseResponseDto:
    @staticmethod
    def ok(status_code=200, data=None, msg="Succeed"):
        return {
            "status_code": status_code,
            "data": data,
            "msg": msg
        }