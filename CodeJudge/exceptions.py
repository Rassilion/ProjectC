class JudgeError(Exception):
    """base class for judge errors"""
    pass


class CompileError(JudgeError):
    """judge compile error"""
    pass
