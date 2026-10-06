import os


def ft_tqdm(lst: range) -> None:
    """function that recreate tqdm to see the advancement of a process"""
    if (len(lst) <= 0 or lst.start > lst.stop):
        print("0it [00:00, ?it/s]")
    size = os.get_terminal_size()[0] - 5 - len(str(len(lst))) - 2 - 29
    start_time = os.times().elapsed
    duration = 0
    for x, i in enumerate(lst, 1):
        elapsed = os.times().elapsed - start_time
        if elapsed > 0:
            speed = x / elapsed
        else:
            speed = 0
        if speed != 0:
            duration = (len(lst) - i) // speed
        min_remaining = int(duration // 60)
        s_remaining = int(duration % 60)
        min_passed = int((os.times().elapsed - start_time) // 60)
        s_passed = int((os.times().elapsed - start_time) % 60)
        # print(speed)
        size = (os.get_terminal_size()[0] - 5 - len(str(len(lst)))
                - (len(str(i)) + 1) - 29)
        pourcent = int(x * 100 // len(lst))
        size_dl = int(size * pourcent / 100)
        str_of_dl = '░' * size_dl + ' ' * (size - size_dl)
        print(f"\r{pourcent}%|{str_of_dl}| {x}/{len(lst)} [{min_passed:02d}:"
              f"{s_passed:02d}<{min_remaining:02d}:{s_remaining:02d},"
              f" {speed:.2f}it/s]", end="", flush=True)
        # print(f"\r{speed}it/s]", end="")
        yield x
