import check50


@check50.check()
def exists():
    """hello.cpp exists"""
    check50.exists("hello.cpp")


@check50.check(exists)
def compiles():
    """hello.cpp compiles"""
    exitFailed = check50.run("make hello").exit()

    if exitFailed:
        message = "hello.cpp failed to compile"
        raise check50.Failure(message)


@check50.check(compiles)
def test_Hello_World():
    """prints Hello, World!"""
    out = check50.run("./hello").stdout()
    checkOutput(out)


def checkOutput(out):
    correctOutput = "Hello, World!\n"
    if out == correctOutput:
        return

    help = None
    if correctOutput.strip() == out:
        help = "Did you forget a newline?"
    elif correctOutput.lower() == out.lower():
        help = "Is your capitalization right?"

    raise check50.Mismatch(correctOutput, out, help=help)