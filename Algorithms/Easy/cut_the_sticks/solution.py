def main():
    _ = int(input())
    sticks = sorted(map(int, raw_input().split(' ')))
    while sticks[::]:
        cut = sticks[0]
        print len(sticks)
        sticks = [stick - cut for stick in sticks if stick - cut > 0]

if __name__ == "__main__":
    main()