import time
import argparse
from win10toast import ToastNotifier

SHOW_TOAST_DURATION = 2
DEFAULT_MEMO = "Time ends"

parser = argparse.ArgumentParser(description="Timer")
parser.add_argument(
    "seconds", metavar="seconds", type=int, help="watting seconds", default=0
)

parser.add_argument("-m", "--memo", type=str, nargs="?", default=None)


def remind(wait_duration, memo, show_toast_duration=2):
    for i in range(wait_duration):
        cur = wait_duration - i
        if (i == 0) or (cur < 30) or ((cur % 30) == 0):
            print("Remain: ", cur)
        time.sleep(1)
    toaster = ToastNotifier()
    toaster.show_toast(
        "Timer", memo, threaded=True, icon_path=None, duration=show_toast_duration
    )
    print("End")


def main():
    args = parser.parse_args()
    wait_duration = args.seconds
    memo = args.memo if args.memo is not None else DEFAULT_MEMO
    remind(wait_duration, memo, SHOW_TOAST_DURATION)


if __name__ == "__main__":
    main()
